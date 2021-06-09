# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_category_group_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import equipment_category_group_pb2 as equipment__category__group__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment_category_group_app_service.proto',
  package='cafm.project.equipment_category_group',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*equipment_category_group_app_service.proto\x12%cafm.project.equipment_category_group\x1a\x1e\x65quipment_category_group.proto\x1a\x0border.proto\"P\nBEquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa6\x01\nCEquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse\x12_\n\x18\x65quipment_category_group\x18\x01 \x01(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\"\x95\x01\n?EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xbe\x01\n@EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse\x12`\n\x19\x65quipment_category_groups\x18\x01 \x03(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"/\n-EquipmentCategoryGroupAppService_newIdRequest\"<\n.EquipmentCategoryGroupAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xc9\x05\n EquipmentCategoryGroupAppService\x12\xf9\x01\n\x1e\x65quipment_category_group_by_id\x12i.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest\x1aj.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse\"\x00\x12\xee\x01\n\x19\x65quipment_category_groups\x12\x66.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest\x1ag.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse\"\x00\x12\xb7\x01\n\x06new_id\x12T.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdRequest\x1aU.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[equipment__category__group__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest.id', index=0,
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
  serialized_start=130,
  serialized_end=210,
)


_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment_category_group', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse.equipment_category_group', index=0,
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
  serialized_start=213,
  serialized_end=379,
)


_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.orders', index=2,
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
  serialized_start=382,
  serialized_end=531,
)


_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment_category_groups', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.equipment_category_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.total_item_count', index=1,
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
  serialized_start=534,
  serialized_end=724,
)


_EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_newIdRequest',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdRequest',
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
  serialized_start=726,
  serialized_end=773,
)


_EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentCategoryGroupAppService_newIdResponse',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdResponse.id', index=0,
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
  serialized_start=775,
  serialized_end=835,
)

_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE.fields_by_name['equipment_category_group'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE.fields_by_name['equipment_category_groups'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_newIdRequest'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_newIdResponse'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest)

EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse)

EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest)

EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse)

EquipmentCategoryGroupAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_newIdRequest)

EquipmentCategoryGroupAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroupAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'equipment_category_group_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroupAppService_newIdResponse)



_EQUIPMENTCATEGORYGROUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentCategoryGroupAppService',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=838,
  serialized_end=1551,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipment_category_group_by_id',
    full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService.equipment_category_group_by_id',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST,
    output_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipment_category_groups',
    full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService.equipment_category_groups',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST,
    output_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService.new_id',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTCATEGORYGROUPAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentCategoryGroupAppService'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
