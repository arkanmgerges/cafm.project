# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_model_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import equipment_model_pb2 as equipment__model__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment_model_app_service.proto',
  package='cafm.project.equipment_model',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!equipment_model_app_service.proto\x12\x1c\x63\x61\x66m.project.equipment_model\x1a\x15\x65quipment_model.proto\x1a\x0border.proto\"@\n2EquipmentModelAppService_equipmentModelByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"{\n3EquipmentModelAppService_equipmentModelByIdResponse\x12\x44\n\x0e\x65quipmentModel\x18\x01 \x01(\x0b\x32,.cafm.project.equipment_model.EquipmentModel\"\x82\x01\n/EquipmentModelAppService_equipmentModelsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x91\x01\n0EquipmentModelAppService_equipmentModelsResponse\x12\x45\n\x0f\x65quipmentModels\x18\x01 \x03(\x0b\x32,.cafm.project.equipment_model.EquipmentModel\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"\'\n%EquipmentModelAppService_newIdRequest\"4\n&EquipmentModelAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xa4\x04\n\x18\x45quipmentModelAppService\x12\xbb\x01\n\x12\x65quipmentModelById\x12P.cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdRequest\x1aQ.cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdResponse\"\x00\x12\xb2\x01\n\x0f\x65quipmentModels\x12M.cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest\x1aN.cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsResponse\"\x00\x12\x94\x01\n\x05newId\x12\x43.cafm.project.equipment_model.EquipmentModelAppService_newIdRequest\x1a\x44.cafm.project.equipment_model.EquipmentModelAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[equipment__model__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDREQUEST = _descriptor.Descriptor(
  name='EquipmentModelAppService_equipmentModelByIdRequest',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdRequest.id', index=0,
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
  serialized_start=103,
  serialized_end=167,
)


_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentModelAppService_equipmentModelByIdResponse',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentModel', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdResponse.equipmentModel', index=0,
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
  serialized_start=169,
  serialized_end=292,
)


_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSREQUEST = _descriptor.Descriptor(
  name='EquipmentModelAppService_equipmentModelsRequest',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest.order', index=2,
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
  serialized_start=295,
  serialized_end=425,
)


_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSRESPONSE = _descriptor.Descriptor(
  name='EquipmentModelAppService_equipmentModelsResponse',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipmentModels', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsResponse.equipmentModels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsResponse.totalItemCount', index=1,
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
  serialized_start=428,
  serialized_end=573,
)


_EQUIPMENTMODELAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='EquipmentModelAppService_newIdRequest',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_newIdRequest',
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
  serialized_start=575,
  serialized_end=614,
)


_EQUIPMENTMODELAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='EquipmentModelAppService_newIdResponse',
  full_name='cafm.project.equipment_model.EquipmentModelAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_model.EquipmentModelAppService_newIdResponse.id', index=0,
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
  serialized_start=616,
  serialized_end=668,
)

_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDRESPONSE.fields_by_name['equipmentModel'].message_type = equipment__model__pb2._EQUIPMENTMODEL
_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSRESPONSE.fields_by_name['equipmentModels'].message_type = equipment__model__pb2._EQUIPMENTMODEL
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_equipmentModelByIdRequest'] = _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_equipmentModelByIdResponse'] = _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_equipmentModelsRequest'] = _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSREQUEST
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_equipmentModelsResponse'] = _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSRESPONSE
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_newIdRequest'] = _EQUIPMENTMODELAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['EquipmentModelAppService_newIdResponse'] = _EQUIPMENTMODELAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentModelAppService_equipmentModelByIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_equipmentModelByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDREQUEST,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdRequest)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_equipmentModelByIdRequest)

EquipmentModelAppService_equipmentModelByIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_equipmentModelByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDRESPONSE,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_equipmentModelByIdResponse)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_equipmentModelByIdResponse)

EquipmentModelAppService_equipmentModelsRequest = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_equipmentModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSREQUEST,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsRequest)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_equipmentModelsRequest)

EquipmentModelAppService_equipmentModelsResponse = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_equipmentModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSRESPONSE,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_equipmentModelsResponse)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_equipmentModelsResponse)

EquipmentModelAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_newIdRequest)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_newIdRequest)

EquipmentModelAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('EquipmentModelAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTMODELAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'equipment_model_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_model.EquipmentModelAppService_newIdResponse)
  })
_sym_db.RegisterMessage(EquipmentModelAppService_newIdResponse)



_EQUIPMENTMODELAPPSERVICE = _descriptor.ServiceDescriptor(
  name='EquipmentModelAppService',
  full_name='cafm.project.equipment_model.EquipmentModelAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=671,
  serialized_end=1219,
  methods=[
  _descriptor.MethodDescriptor(
    name='equipmentModelById',
    full_name='cafm.project.equipment_model.EquipmentModelAppService.equipmentModelById',
    index=0,
    containing_service=None,
    input_type=_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDREQUEST,
    output_type=_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='equipmentModels',
    full_name='cafm.project.equipment_model.EquipmentModelAppService.equipmentModels',
    index=1,
    containing_service=None,
    input_type=_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSREQUEST,
    output_type=_EQUIPMENTMODELAPPSERVICE_EQUIPMENTMODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.equipment_model.EquipmentModelAppService.newId',
    index=2,
    containing_service=None,
    input_type=_EQUIPMENTMODELAPPSERVICE_NEWIDREQUEST,
    output_type=_EQUIPMENTMODELAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EQUIPMENTMODELAPPSERVICE)

DESCRIPTOR.services_by_name['EquipmentModelAppService'] = _EQUIPMENTMODELAPPSERVICE

# @@protoc_insertion_point(module_scope)
