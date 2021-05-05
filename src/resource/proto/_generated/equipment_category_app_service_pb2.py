# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_category_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import equipment_category_pb2 as equipment__category__pb2
import equipment_category_group_pb2 as equipment__category__group__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment_category_app_service.proto',
  package='cafm.project.equipment_category',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$equipment_category_app_service.proto\x12\x1f\x63\x61\x66m.project.equipment_category\x1a\x18\x65quipment_category.proto\x1a\x1e\x65quipment_category_group.proto\x1a\x0border.proto\"F\n8EquipmentCategoryAppService_equipmentCategoryByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x8a\x01\n9EquipmentCategoryAppService_equipmentCategoryByIdResponse\x12M\n\x11\x65quipmentCategory\x18\x01 \x01(\x0b\x32\x32.cafm.project.equipment_category.EquipmentCategory\"\x89\x01\n6EquipmentCategoryAppService_equipmentCategoriesRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xa2\x01\n7EquipmentCategoryAppService_equipmentCategoriesResponse\x12O\n\x13\x65quipmentCategories\x18\x01 \x03(\x0b\x32\x32.cafm.project.equipment_category.EquipmentCategory\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"\xa5\x01\nFEquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\x12\n\n\x02id\x18\x04 \x01(\t\"\xc1\x01\nGEquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse\x12^\n\x17\x65quipmentCategoryGroups\x18\x01 \x03(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"*\n(EquipmentCategoryAppService_newIdRequest\"7\n)EquipmentCategoryAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xdd\x06\n\x1b\x45quipmentCategoryAppService\x12\xd0\x01\n\x15\x65quipmentCategoryById\x12Y.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdRequest\x1aZ.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdResponse\"\x00\x12\xca\x01\n\x13\x65quipmentCategories\x12W.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest\x1aX.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesResponse\"\x00\x12\xa0\x01\n\x05newId\x12I.cafm.project.equipment_category.EquipmentCategoryAppService_newIdRequest\x1aJ.cafm.project.equipment_category.EquipmentCategoryAppService_newIdResponse\"\x00\x12\xfa\x01\n#equipmentCategoryGroupsByCategoryId\x12g.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest\x1ah.cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[equipment__category__pb2.DESCRIPTOR,equipment__category__group__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoryByIdRequest',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=214,
)


_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoryByIdResponse',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentCategory', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdResponse.equipmentCategory', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=355,
)


_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoriesRequest',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest.order', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=495,
)


_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoriesResponse',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentCategories', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesResponse.equipmentCategories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesResponse.totalItemCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=660,
)


_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest.order', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=828,
)


_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentCategoryGroups', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse.equipmentCategoryGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse.totalItemCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=1024,
)


_EQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_newIdRequest',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_newIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1026,
  serialized_end=1068,
)


_EQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryAppService_newIdResponse',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_category.EquipmentCategoryAppService_newIdResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1070,
  serialized_end=1125,
)

_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDRESPONSE.fields_by_name['equipmentCategory'].message_type = equipment__category__pb2._EQUIPMENTCATEGORY
_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESRESPONSE.fields_by_name['equipmentCategories'].message_type = equipment__category__pb2._EQUIPMENTCATEGORY
_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDRESPONSE.fields_by_name['equipmentCategoryGroups'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoryByIdRequest'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoryByIdResponse'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoriesRequest'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoriesResponse'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse'] = _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_newIdRequest'] = _EQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryAppService_newIdResponse'] = _EQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentCategoryAppService_equipmentCategoryByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoryByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDREQUEST,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoryByIdRequest)

EquipmentCategoryAppService_equipmentCategoryByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoryByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDRESPONSE,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoryByIdResponse)

EquipmentCategoryAppService_equipmentCategoriesRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESREQUEST,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoriesRequest)

EquipmentCategoryAppService_equipmentCategoriesResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESRESPONSE,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoriesResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoriesResponse)

EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDREQUEST,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest)

EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDRESPONSE,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse)

EquipmentCategoryAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_newIdRequest)

EquipmentCategoryAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'equipment_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategoryAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryAppService_newIdResponse)



_EQUIPMENTCATEGORYAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentCategoryAppService',
  full_name='cafm.project.equipment_category.EquipmentCategoryAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1128,
  serialized_end=1989,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipmentCategoryById',
    full_name='cafm.project.equipment_category.EquipmentCategoryAppService.equipmentCategoryById',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDREQUEST,
    output_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentCategories',
    full_name='cafm.project.equipment_category.EquipmentCategoryAppService.equipmentCategories',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESREQUEST,
    output_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.equipment_category.EquipmentCategoryAppService.newId',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTCATEGORYAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentCategoryGroupsByCategoryId',
    full_name='cafm.project.equipment_category.EquipmentCategoryAppService.equipmentCategoryGroupsByCategoryId',
    index=3,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDREQUEST,
    output_type=_EQUIPMENTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYCATEGORYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTCATEGORYAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentCategoryAppService'] = _EQUIPMENTCATEGORYAPPSERVICE

# @@protoc_insertion_point(module_scope)
