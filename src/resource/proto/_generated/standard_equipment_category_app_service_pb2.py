# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: standard_equipment_category_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import standard_equipment_category_pb2 as standard__equipment__category__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="standard_equipment_category_app_service.proto",
    package="cafm.project.standard_equipment_category",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-standard_equipment_category_app_service.proto\x12(cafm.project.standard_equipment_category\x1a!standard_equipment_category.proto\x1a\x0border.proto"V\nHStandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t"\xb3\x01\nIStandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse\x12\x66\n\x19standardEquipmentCategory\x18\x01 \x01(\x0b\x32\x43.cafm.project.standard_equipment_category.StandardEquipmentCategory"\x99\x01\nFStandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order"\xc6\x01\nGStandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse\x12h\n\x1bstandardEquipmentCategories\x18\x01 \x03(\x0b\x32\x43.cafm.project.standard_equipment_category.StandardEquipmentCategory\x12\x11\n\titemCount\x18\x02 \x01(\x05"2\n0StandardEquipmentCategoryAppService_newIdRequest"?\n1StandardEquipmentCategoryAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xfe\x05\n#StandardEquipmentCategoryAppService\x12\x8a\x02\n\x1dstandardEquipmentCategoryById\x12r.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest\x1as.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse"\x00\x12\x84\x02\n\x1bstandardEquipmentCategories\x12p.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest\x1aq.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse"\x00\x12\xc2\x01\n\x05newId\x12Z.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdRequest\x1a[.cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdResponse"\x00\x62\x06proto3',
    dependencies=[
        standard__equipment__category__pb2.DESCRIPTOR,
        order__pb2.DESCRIPTOR,
    ],
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDREQUEST = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=139,
    serialized_end=225,
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDRESPONSE = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="standardEquipmentCategory",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse.standardEquipmentCategory",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=407,
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESREQUEST = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resultFrom",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest.resultFrom",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="resultSize",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest.resultSize",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="order",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest.order",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=410,
    serialized_end=563,
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESRESPONSE = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="standardEquipmentCategories",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse.standardEquipmentCategories",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="itemCount",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse.itemCount",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=566,
    serialized_end=764,
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_newIdRequest",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=766,
    serialized_end=816,
)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
    name="StandardEquipmentCategoryAppService_newIdResponse",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdResponse.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=818,
    serialized_end=881,
)

_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDRESPONSE.fields_by_name[
    "standardEquipmentCategory"
].message_type = standard__equipment__category__pb2._STANDARDEQUIPMENTCATEGORY
_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESREQUEST.fields_by_name[
    "order"
].message_type = order__pb2._ORDER
_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESRESPONSE.fields_by_name[
    "standardEquipmentCategories"
].message_type = standard__equipment__category__pb2._STANDARDEQUIPMENTCATEGORY
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDRESPONSE
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESRESPONSE
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_newIdRequest"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name[
    "StandardEquipmentCategoryAppService_newIdResponse"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDREQUEST,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest)
    },
)
_sym_db.RegisterMessage(
    StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest
)

StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDRESPONSE,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse)
    },
)
_sym_db.RegisterMessage(
    StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse
)

StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESREQUEST,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest)
    },
)
_sym_db.RegisterMessage(
    StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest
)

StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESRESPONSE,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse)
    },
)
_sym_db.RegisterMessage(
    StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse
)

StandardEquipmentCategoryAppService_newIdRequest = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_newIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdRequest)
    },
)
_sym_db.RegisterMessage(StandardEquipmentCategoryAppService_newIdRequest)

StandardEquipmentCategoryAppService_newIdResponse = _reflection.GeneratedProtocolMessageType(
    "StandardEquipmentCategoryAppService_newIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE,
        "__module__": "standard_equipment_category_app_service_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService_newIdResponse)
    },
)
_sym_db.RegisterMessage(StandardEquipmentCategoryAppService_newIdResponse)


_STANDARDEQUIPMENTCATEGORYAPPSERVICE = _descriptor.ServiceDescriptor(
    name="StandardEquipmentCategoryAppService",
    full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=884,
    serialized_end=1650,
    methods=[
        _descriptor.MethodDescriptor(
            name="standardEquipmentCategoryById",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService.standardEquipmentCategoryById",
            index=0,
            containing_service=None,
            input_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDREQUEST,
            output_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORYBYIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="standardEquipmentCategories",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService.standardEquipmentCategories",
            index=1,
            containing_service=None,
            input_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESREQUEST,
            output_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_STANDARDEQUIPMENTCATEGORIESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="newId",
            full_name="cafm.project.standard_equipment_category.StandardEquipmentCategoryAppService.newId",
            index=2,
            containing_service=None,
            input_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST,
            output_type=_STANDARDEQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_STANDARDEQUIPMENTCATEGORYAPPSERVICE)

DESCRIPTOR.services_by_name[
    "StandardEquipmentCategoryAppService"
] = _STANDARDEQUIPMENTCATEGORYAPPSERVICE

# @@protoc_insertion_point(module_scope)
