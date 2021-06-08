# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maintenance_procedure_operation_parameter_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import maintenance_procedure_operation_parameter_pb2 as maintenance__procedure__operation__parameter__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='maintenance_procedure_operation_parameter_app_service.proto',
  package='cafm.project.maintenance_procedure_operation_parameter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;maintenance_procedure_operation_parameter_app_service.proto\x12\x36\x63\x61\x66m.project.maintenance_procedure_operation_parameter\x1a/maintenance_procedure_operation_parameter.proto\x1a\x0border.proto\"p\nbMaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xf9\x01\ncMaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse\x12\x91\x01\n)maintenance_procedure_operation_parameter\x18\x01 \x01(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\"\xb4\x01\n_MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x91\x02\n`MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse\x12\x92\x01\n*maintenance_procedure_operation_parameters\x18\x01 \x03(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\x82\x02\n\x80\x01MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest\x12*\n\"maintenance_procedure_operation_id\x18\x01 \x01(\t\x12\x13\n\x0bresult_from\x18\x02 \x01(\x05\x12\x13\n\x0bresult_size\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xb0\x02\n\x81\x01MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse\x12\x8f\x01\n\'maintenanceProcedureOperationParameters\x18\x01 \x03(\x0b\x32^.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameter\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"?\n=MaintenanceProcedureOperationParameterAppService_newIdRequest\"L\n>MaintenanceProcedureOperationParameterAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xd3\x0b\n0MaintenanceProcedureOperationParameterAppService\x12\xee\x02\n/maintenance_procedure_operation_parameter_by_id\x12\x9a\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest\x1a\x9b\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse\"\x00\x12\xe3\x02\n*maintenance_procedure_operation_parameters\x12\x97\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest\x1a\x98\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse\"\x00\x12\xcb\x03\nPmaintenance_procedure_operation_parameters_by_maintenance_procedure_operation_id\x12\xb8\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest\x1a\xb9\x01.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse\"\x00\x12\xf9\x01\n\x06new_id\x12u.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdRequest\x1av.cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[maintenance__procedure__operation__parameter__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest.id', index=0,
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
  serialized_start=181,
  serialized_end=293,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_parameter', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse.maintenance_procedure_operation_parameter', index=0,
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
  serialized_start=296,
  serialized_end=545,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest.order', index=2,
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
  serialized_start=548,
  serialized_end=728,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_parameters', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse.maintenance_procedure_operation_parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse.total_item_count', index=1,
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
  serialized_start=731,
  serialized_end=1004,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operation_id', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.maintenance_procedure_operation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.result_from', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.result_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest.order', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1007,
  serialized_end=1265,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='maintenanceProcedureOperationParameters', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse.maintenanceProcedureOperationParameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse.total_item_count', index=1,
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
  serialized_start=1268,
  serialized_end=1572,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_newIdRequest',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdRequest',
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
  serialized_start=1574,
  serialized_end=1637,
)


_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='MaintenanceProcedureOperationParameterAppService_newIdResponse',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdResponse.id', index=0,
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
  serialized_start=1639,
  serialized_end=1715,
)

_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE.fields_by_name['maintenance_procedure_operation_parameter'].message_type = maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE.fields_by_name['maintenance_procedure_operation_parameters'].message_type = maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE.fields_by_name['maintenanceProcedureOperationParameters'].message_type = maintenance__procedure__operation__parameter__pb2._MAINTENANCEPROCEDUREOPERATIONPARAMETER
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_newIdRequest'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['MaintenanceProcedureOperationParameterAppService_newIdResponse'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest)

MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse)

MaintenanceProcedureOperationParameterAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdRequest)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_newIdRequest)

MaintenanceProcedureOperationParameterAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('MaintenanceProcedureOperationParameterAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'maintenance_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService_newIdResponse)
  })
_sym_db.RegisterMessage(MaintenanceProcedureOperationParameterAppService_newIdResponse)



_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceProcedureOperationParameterAppService',
  full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1718,
  serialized_end=3209,
  methods=[
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_parameter_by_id',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenance_procedure_operation_parameter_by_id',
    index=0,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_parameters',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenance_procedure_operation_parameters',
    index=1,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='maintenance_procedure_operation_parameters_by_maintenance_procedure_operation_id',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.maintenance_procedure_operation_parameters_by_maintenance_procedure_operation_id',
    index=2,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_MAINTENANCEPROCEDUREOPERATIONPARAMETERSBYMAINTENANCEPROCEDUREOPERATIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.maintenance_procedure_operation_parameter.MaintenanceProcedureOperationParameterAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST,
    output_type=_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE)

DESCRIPTOR.services_by_name['MaintenanceProcedureOperationParameterAppService'] = _MAINTENANCEPROCEDUREOPERATIONPARAMETERAPPSERVICE

# @@protoc_insertion_point(module_scope)
