# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lookup/equipment/equipment_lookup_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lookup.equipment import equipment_pb2 as lookup_dot_equipment_dot_equipment__pb2
import order_pb2 as order__pb2
import filter_pb2 as filter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lookup/equipment/equipment_lookup_app_service.proto',
  package='cafm.project.lookup.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3lookup/equipment/equipment_lookup_app_service.proto\x12\x1d\x63\x61\x66m.project.lookup.equipment\x1a lookup/equipment/equipment.proto\x1a\x0border.proto\x1a\x0c\x66ilter.proto\"\xa8\x01\n\'EquipmentLookupAppService_lookupRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\x12+\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x1a.cafm.common.filter.Filter\"\x80\x01\n(EquipmentLookupAppService_lookupResponse\x12<\n\nequipments\x18\x01 \x03(\x0b\x32(.cafm.project.lookup.equipment.Equipment\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\x32\xb9\x01\n\x19\x45quipmentLookupAppService\x12\x9b\x01\n\x06lookup\x12\x46.cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest\x1aG.cafm.project.lookup.equipment.EquipmentLookupAppService_lookupResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[lookup_dot_equipment_dot_equipment__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,filter__pb2.DESCRIPTOR,])




_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST = _descriptor.Descriptor(
  name='EquipmentLookupAppService_lookupRequest',
  full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest.orders', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest.filters', index=3,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=148,
  serialized_end=316,
)


_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPRESPONSE = _descriptor.Descriptor(
  name='EquipmentLookupAppService_lookupResponse',
  full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipments', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupResponse.equipments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.lookup.equipment.EquipmentLookupAppService_lookupResponse.totalItemCount', index=1,
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
  serialized_start=319,
  serialized_end=447,
)

_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['filters'].message_type = filter__pb2._FILTER
_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPRESPONSE.fields_by_name['equipments'].message_type = lookup_dot_equipment_dot_equipment__pb2._EQUIPMENT
DESCRIPTOR.message_types_by_name['EquipmentLookupAppService_lookupRequest'] = _EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['EquipmentLookupAppService_lookupResponse'] = _EQUIPMENTLOOKUPAPPSERVICE_LOOKUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentLookupAppService_lookupRequest = _reflection.GeneratedProtocolMessageType('EquipmentLookupAppService_lookupRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST,
  '__module__' : 'lookup.equipment.equipment_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.EquipmentLookupAppService_lookupRequest)
  })
_sym_db.RegisterMessage(EquipmentLookupAppService_lookupRequest)

EquipmentLookupAppService_lookupResponse = _reflection.GeneratedProtocolMessageType('EquipmentLookupAppService_lookupResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTLOOKUPAPPSERVICE_LOOKUPRESPONSE,
  '__module__' : 'lookup.equipment.equipment_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.EquipmentLookupAppService_lookupResponse)
  })
_sym_db.RegisterMessage(EquipmentLookupAppService_lookupResponse)



_EQUIPMENTLOOKUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentLookupAppService',
  full_name='cafm.project.lookup.equipment.EquipmentLookupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=450,
  serialized_end=635,
  methods=[
  _descriptor.MethodDescriptor(
    name='lookup',
    full_name='cafm.project.lookup.equipment.EquipmentLookupAppService.lookup',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPREQUEST,
    output_type=_EQUIPMENTLOOKUPAPPSERVICE_LOOKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTLOOKUPAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentLookupAppService'] = _EQUIPMENTLOOKUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
