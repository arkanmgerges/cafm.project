# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_project_category_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import equipment_category_group_pb2 as equipment__category__group__pb2
import equipment_project_category_pb2 as equipment__project__category__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment_project_category_app_service.proto',
  package='cafm.project.equipment_project_category',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,equipment_project_category_app_service.proto\x12\'cafm.project.equipment_project_category\x1a\x1e\x65quipment_category_group.proto\x1a equipment_project_category.proto\x1a\x0border.proto\"T\nFEquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xb0\x01\nGEquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse\x12\x65\n\x1a\x65quipment_project_category\x18\x01 \x01(\x0b\x32\x41.cafm.project.equipment_project_category.EquipmentProjectCategory\"\x99\x01\nDEquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xca\x01\nEEquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse\x12g\n\x1c\x65quipment_project_categories\x18\x01 \x03(\x0b\x32\x41.cafm.project.equipment_project_category.EquipmentProjectCategory\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\xbe\x01\n]EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\x12\n\n\x02id\x18\x04 \x01(\t\"\xdc\x01\n^EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse\x12`\n\x19\x65quipment_category_groups\x18\x01 \x03(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"1\n/EquipmentProjectCategoryAppService_newIdRequest\">\n0EquipmentProjectCategoryAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xc6\x08\n\"EquipmentProjectCategoryAppService\x12\x87\x02\n equipment_project_category_by_id\x12o.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest\x1ap.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse\"\x00\x12\xff\x01\n\x1c\x65quipment_project_categories\x12m.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest\x1an.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse\"\x00\x12\xd1\x02\n:equipment_category_groups_by_equipment_project_category_id\x12\x86\x01.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest\x1a\x87\x01.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse\"\x00\x12\xbf\x01\n\x06new_id\x12X.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdRequest\x1aY.cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[equipment__category__group__pb2.DESCRIPTOR,equipment__project__category__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest.id', index=0,
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
  serialized_start=168,
  serialized_end=252,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment_project_category', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse.equipment_project_category', index=0,
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
  serialized_start=255,
  serialized_end=431,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESREQUEST = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest.order', index=2,
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
  serialized_start=434,
  serialized_end=587,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESRESPONSE = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment_project_categories', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse.equipment_project_categories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse.total_item_count', index=1,
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
  serialized_start=590,
  serialized_end=792,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.order', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest.id', index=3,
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
  serialized_start=795,
  serialized_end=985,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment_category_groups', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse.equipment_category_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse.total_item_count', index=1,
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
  serialized_start=988,
  serialized_end=1208,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_newIdRequest',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdRequest',
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
  serialized_start=1210,
  serialized_end=1259,
)


_EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentProjectCategoryAppService_newIdResponse',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdResponse.id', index=0,
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
  serialized_start=1261,
  serialized_end=1323,
)

_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDRESPONSE.fields_by_name['equipment_project_category'].message_type = equipment__project__category__pb2._EQUIPMENTPROJECTCATEGORY
_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESRESPONSE.fields_by_name['equipment_project_categories'].message_type = equipment__project__category__pb2._EQUIPMENTPROJECTCATEGORY
_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDRESPONSE.fields_by_name['equipment_category_groups'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESREQUEST
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_newIdRequest'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentProjectCategoryAppService_newIdResponse'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDREQUEST,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdRequest)

EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDRESPONSE,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse)

EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESREQUEST,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentProjectCategoriesRequest)

EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESRESPONSE,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse)

EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDREQUEST,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest)

EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDRESPONSE,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse)

EquipmentProjectCategoryAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_newIdRequest)

EquipmentProjectCategoryAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategoryAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'equipment_project_category_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategoryAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentProjectCategoryAppService_newIdResponse)



_EQUIPMENTPROJECTCATEGORYAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentProjectCategoryAppService',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1326,
  serialized_end=2420,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipment_project_category_by_id',
    full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService.equipment_project_category_by_id',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDREQUEST,
    output_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORYBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipment_project_categories',
    full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService.equipment_project_categories',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESREQUEST,
    output_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTPROJECTCATEGORIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipment_category_groups_by_equipment_project_category_id',
    full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService.equipment_category_groups_by_equipment_project_category_id',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDREQUEST,
    output_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_EQUIPMENTCATEGORYGROUPSBYEQUIPMENTPROJECTCATEGORYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.equipment_project_category.EquipmentProjectCategoryAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTPROJECTCATEGORYAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTPROJECTCATEGORYAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentProjectCategoryAppService'] = _EQUIPMENTPROJECTCATEGORYAPPSERVICE

# @@protoc_insertion_point(module_scope)
