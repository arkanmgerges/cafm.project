# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/daily_check_procedure_operation_parameter_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import daily_check_procedure_operation_parameter_pb2 as project_dot_daily__check__procedure__operation__parameter__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/daily_check_procedure_operation_parameter_app_service.proto',
  package='cafm.project.daily_check_procedure_operation_parameter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCproject/daily_check_procedure_operation_parameter_app_service.proto\x12\x36\x63\x61\x66m.project.daily_check_procedure_operation_parameter\x1a\x37project/daily_check_procedure_operation_parameter.proto\x1a\x0border.proto\"n\n`DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xf6\x01\naDailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse\x12\x90\x01\n)daily_check_procedure_operation_parameter\x18\x01 \x01(\x0b\x32].cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameter\"\xb3\x01\n]DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x8e\x02\n^DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse\x12\x91\x01\n*daily_check_procedure_operation_parameters\x18\x01 \x03(\x0b\x32].cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameter\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\">\n<DailyCheckProcedureOperationParameterAppService_newIdRequest\"K\n=DailyCheckProcedureOperationParameterAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\xff\x01\n}DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest\x12*\n\"daily_check_procedure_operation_id\x18\x01 \x01(\t\x12\x13\n\x0bresult_from\x18\x02 \x01(\x05\x12\x13\n\x0bresult_size\x18\x03 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xae\x02\n~DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse\x12\x91\x01\n*daily_check_procedure_operation_parameters\x18\x01 \x03(\x0b\x32].cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameter\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\x32\xc2\x0b\n/DailyCheckProcedureOperationParameterAppService\x12\xea\x02\n/daily_check_procedure_operation_parameter_by_id\x12\x98\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest\x1a\x99\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse\"\x00\x12\xdf\x02\n*daily_check_procedure_operation_parameters\x12\x95\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest\x1a\x96\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse\"\x00\x12\xc5\x03\nPdaily_check_procedure_operation_parameters_by_daily_check_procedure_operation_id\x12\xb5\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest\x1a\xb6\x01.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse\"\x00\x12\xf7\x01\n\x06new_id\x12t.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdRequest\x1au.cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_daily__check__procedure__operation__parameter__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest.id', index=0,
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
  serialized_start=197,
  serialized_end=307,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_parameter', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse.daily_check_procedure_operation_parameter', index=0,
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
  serialized_start=310,
  serialized_end=556,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.orders', index=2,
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
  serialized_start=559,
  serialized_end=738,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_parameters', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse.daily_check_procedure_operation_parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse.total_item_count', index=1,
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
  serialized_start=741,
  serialized_end=1011,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_newIdRequest',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdRequest',
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
  serialized_start=1013,
  serialized_end=1075,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_newIdResponse',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdResponse.id', index=0,
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
  serialized_start=1077,
  serialized_end=1152,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_id', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest.daily_check_procedure_operation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest.result_from', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest.result_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest.orders', index=3,
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
  serialized_start=1155,
  serialized_end=1410,
)


_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_parameters', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse.daily_check_procedure_operation_parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse.total_item_count', index=1,
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
  serialized_start=1413,
  serialized_end=1715,
)

_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDRESPONSE.fields_by_name['daily_check_procedure_operation_parameter'].message_type = project_dot_daily__check__procedure__operation__parameter__pb2._DAILYCHECKPROCEDUREOPERATIONPARAMETER
_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSRESPONSE.fields_by_name['daily_check_procedure_operation_parameters'].message_type = project_dot_daily__check__procedure__operation__parameter__pb2._DAILYCHECKPROCEDUREOPERATIONPARAMETER
_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDRESPONSE.fields_by_name['daily_check_procedure_operation_parameters'].message_type = project_dot_daily__check__procedure__operation__parameter__pb2._DAILYCHECKPROCEDUREOPERATIONPARAMETER
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSRESPONSE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_newIdRequest'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_newIdResponse'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSREQUEST,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSRESPONSE,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse)

DailyCheckProcedureOperationParameterAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_newIdRequest)

DailyCheckProcedureOperationParameterAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_newIdResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_newIdResponse)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDREQUEST,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest)

DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDRESPONSE,
  '__module__' : 'project.daily_check_procedure_operation_parameter_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse)



_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE = _descriptor.ServiceDescriptor(
  name='DailyCheckProcedureOperationParameterAppService',
  full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1718,
  serialized_end=3192,
  methods=[
  _descriptor.MethodDescriptor(
    name='daily_check_procedure_operation_parameter_by_id',
    full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService.daily_check_procedure_operation_parameter_by_id',
    index=0,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDREQUEST,
    output_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='daily_check_procedure_operation_parameters',
    full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService.daily_check_procedure_operation_parameters',
    index=1,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSREQUEST,
    output_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='daily_check_procedure_operation_parameters_by_daily_check_procedure_operation_id',
    full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService.daily_check_procedure_operation_parameters_by_daily_check_procedure_operation_id',
    index=2,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDREQUEST,
    output_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_DAILYCHECKPROCEDUREOPERATIONPARAMETERSBYDAILYCHECKPROCEDUREOPERATIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDREQUEST,
    output_type=_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE)

DESCRIPTOR.services_by_name['DailyCheckProcedureOperationParameterAppService'] = _DAILYCHECKPROCEDUREOPERATIONPARAMETERAPPSERVICE

# @@protoc_insertion_point(module_scope)
