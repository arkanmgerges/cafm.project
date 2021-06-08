"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import grpc

from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class CommonBaseListener(BaseListener):
    @debugLogger
    def __init__(self):
        from src.domain_model.token.TokenService import TokenService
        self._tokenService = TokenService()
        super().__init__()

    @debugLogger
    def newId(self, request, context, response):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{CommonBaseListener.newId.__qualname__}] - claims: {claims}\n\t \
                        token: {token}"
            )

            return response(id=self._appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    def allModels(self, request, context, response, appServiceMethod, responseAttribute):
        token = self._token(context)

        resultFrom = request.result_from if request.result_from >= 0 else 0
        resultSize = request.result_size if request.result_size >= 0 else 10
        claims = (
            self._tokenService.claimsFromToken(token=token)
            if "token" != ""
            else None
        )
        logger.debug(
            f"[{CommonBaseListener.__qualname__}] - claims: {claims}\n\t \
            result_from: {request.result_from}, result_size: {request.result_size}, orders: {request.orders}, filters: {request.filters}, token: {token}"
        )

        orderData = [
            {"orderBy": o.orderBy, "direction": o.direction} for o in request.orders if request.orders is not None
        ]

        result: dict = appServiceMethod(
            resultFrom=resultFrom,
            resultSize=resultSize,
            token=token,
            order=orderData,
        )
        response = response()
        responseAttributeObject = getattr(response, responseAttribute, None)
        for item in result["items"]:
            responseAttributeObject.add(
                id=item.id(),
                name=item.name(),
                description=item.description(),
                equipment_id=item.equipmentId(),
                equipment_category_group_id=item.equipmentCategoryGroupId(),
            )
        response.total_item_count = result["totalItemCount"]
        logger.debug(
            f"[{CommonBaseListener.allModels.__qualname__}] - response: {response}"
        )
        return response