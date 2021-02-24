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
  serialized_pb=b'\n*equipment_category_group_app_service.proto\x12%cafm.project.equipment_category_group\x1a\x1e\x65quipment_category_group.proto\x1a\x0border.proto\"P\nBEquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xa4\x01\nCEquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse\x12]\n\x16\x65quipmentCategoryGroup\x18\x01 \x01(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\"\x92\x01\n?EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xb5\x01\n@EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse\x12^\n\x17\x65quipmentCategoryGroups\x18\x01 \x03(\x0b\x32=.cafm.project.equipment_category_group.EquipmentCategoryGroup\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\x89\x04\n EquipmentCategoryGroupAppService\x12\xf5\x01\n\x1a\x65quipmentCategoryGroupById\x12i.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest\x1aj.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse\"\x00\x12\xec\x01\n\x17\x65quipmentCategoryGroups\x12\x66.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest\x1ag.cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse\"\x00\x62\x06proto3'
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
      name='equipmentCategoryGroup', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse.equipmentCategoryGroup', index=0,
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
  serialized_end=377,
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
      name='resultFrom', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest.order', index=2,
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
  serialized_start=380,
  serialized_end=526,
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
      name='equipmentCategoryGroups', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.equipmentCategoryGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse.itemCount', index=1,
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
  serialized_start=529,
  serialized_end=710,
)

_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE.fields_by_name['equipmentCategoryGroup'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE.fields_by_name['equipmentCategoryGroups'].message_type = equipment__category__group__pb2._EQUIPMENTCATEGORYGROUP
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE
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



_EQUIPMENTCATEGORYGROUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentCategoryGroupAppService',
  full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=713,
  serialized_end=1234,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipmentCategoryGroupById',
    full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService.equipmentCategoryGroupById',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDREQUEST,
    output_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentCategoryGroups',
    full_name='cafm.project.equipment_category_group.EquipmentCategoryGroupAppService.equipmentCategoryGroups',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSREQUEST,
    output_type=_EQUIPMENTCATEGORYGROUPAPPSERVICE_EQUIPMENTCATEGORYGROUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTCATEGORYGROUPAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentCategoryGroupAppService'] = _EQUIPMENTCATEGORYGROUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
