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
    def models(self, *_args, **kwargs):
        request = kwargs['request'] if 'request' in kwargs else None
        context = kwargs['context'] if 'context' in kwargs else None
        response = kwargs['response'] if 'response' in kwargs else None
        appServiceMethod = kwargs['appServiceMethod'] if 'appServiceMethod' in kwargs else None
        responseAttribute = kwargs['responseAttribute'] if 'responseAttribute' in kwargs else None
        params = kwargs['appServiceParams'] if 'appServiceParams' in kwargs else {}

        token = self._token(context)

        resultFrom = request.result_from if request.result_from >= 0 else 0
        resultSize = request.result_size if request.result_size >= 0 else 10
        claims = (
            self._tokenService.claimsFromToken(token=token)
            if "token" != ""
            else None
        )
        logger.debug(
            f"[{CommonBaseListener.models.__qualname__}] - claims: {claims}\n\t \
            result_from: {request.result_from}, result_size: {request.result_size}, token: {token}"
        )

        orderData = [
            {"orderBy": o.order_by, "direction": o.direction} for o in request.orders if request.orders is not None
        ]

        result: dict = appServiceMethod(
            resultFrom=resultFrom,
            resultSize=resultSize,
            token=token,
            order=orderData,
            **params,
        )
        logger.debug(f'[{CommonBaseListener.models.__qualname__}] - result: {result}')
        response = response()
        responseAttributeObject = getattr(response, responseAttribute, responseAttribute)
        for item in result["items"]:
            self._addObjectToGrpcResponse(obj=item, grpcResponseObject=responseAttributeObject.add())
        response.total_item_count = result["totalItemCount"]
        return response


    @debugLogger
    def oneModel(self, *_args, **kwargs):
        request = kwargs['request'] if 'request' in kwargs else None
        context = kwargs['context'] if 'context' in kwargs else None
        response = kwargs['response'] if 'response' in kwargs else None
        appServiceMethod = kwargs['appServiceMethod'] if 'appServiceMethod' in kwargs else None
        responseAttribute = kwargs['responseAttribute'] if 'responseAttribute' in kwargs else None
        ignoreToken = kwargs['ignoreToken'] if 'ignoreToken' in kwargs else False
        params = kwargs['appServiceParams'] if 'appServiceParams' in kwargs else {}

        if not ignoreToken:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{CommonBaseListener.oneModel.__qualname__}] - claims: {claims}\n\t token: {token}"
            )
            params['token'] = token
        response = response()
        responseAttributeObject = getattr(response, responseAttribute, None)
        obj = appServiceMethod(**params)
        logger.debug(
            f"[{CommonBaseListener.oneModel.__qualname__}] - response: {obj}"
        )
        self._addObjectToGrpcResponse(obj=obj, grpcResponseObject=responseAttributeObject)
        return response
