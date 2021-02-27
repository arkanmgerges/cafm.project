# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daily_check_procedure_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import daily_check_procedure_pb2 as daily__check__procedure__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='daily_check_procedure_app_service.proto',
  package='cafm.project.daily_check_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'daily_check_procedure_app_service.proto\x12\"cafm.project.daily_check_procedure\x1a\x1b\x64\x61ily_check_procedure.proto\x1a\x0border.proto\"J\n<DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x95\x01\n=DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse\x12T\n\x13\x64\x61ilyCheckProcedure\x18\x01 \x01(\x0b\x32\x37.cafm.project.daily_check_procedure.DailyCheckProcedure\"\x8c\x01\n9DailyCheckProcedureAppService_dailyCheckProceduresRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xa6\x01\n:DailyCheckProcedureAppService_dailyCheckProceduresResponse\x12U\n\x14\x64\x61ilyCheckProcedures\x18\x01 \x03(\x0b\x32\x37.cafm.project.daily_check_procedure.DailyCheckProcedure\x12\x11\n\titemCount\x18\x02 \x01(\x05\x32\xdc\x03\n\x1d\x44\x61ilyCheckProcedureAppService\x12\xe0\x01\n\x17\x64\x61ilyCheckProcedureById\x12`.cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest\x1a\x61.cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse\"\x00\x12\xd7\x01\n\x14\x64\x61ilyCheckProcedures\x12].cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest\x1a^.cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[daily__check__procedure__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest.id', index=0,
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
  serialized_start=121,
  serialized_end=195,
)


_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dailyCheckProcedure', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse.dailyCheckProcedure', index=0,
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
  serialized_start=198,
  serialized_end=347,
)


_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESREQUEST = _descriptor.Descriptor(
  name='DailyCheckProcedureAppService_dailyCheckProceduresRequest',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest.order', index=2,
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
  serialized_start=350,
  serialized_end=490,
)


_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESRESPONSE = _descriptor.Descriptor(
  name='DailyCheckProcedureAppService_dailyCheckProceduresResponse',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dailyCheckProcedures', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresResponse.dailyCheckProcedures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresResponse.itemCount', index=1,
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
  serialized_start=493,
  serialized_end=659,
)

_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDRESPONSE.fields_by_name['dailyCheckProcedure'].message_type = daily__check__procedure__pb2._DAILYCHECKPROCEDURE
_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESRESPONSE.fields_by_name['dailyCheckProcedures'].message_type = daily__check__procedure__pb2._DAILYCHECKPROCEDURE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest'] = _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse'] = _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDRESPONSE
DESCRIPTOR.message_types_by_name['DailyCheckProcedureAppService_dailyCheckProceduresRequest'] = _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESREQUEST
DESCRIPTOR.message_types_by_name['DailyCheckProcedureAppService_dailyCheckProceduresResponse'] = _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDREQUEST,
  '__module__' : 'daily_check_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest)

DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDRESPONSE,
  '__module__' : 'daily_check_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse)

DailyCheckProcedureAppService_dailyCheckProceduresRequest = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureAppService_dailyCheckProceduresRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESREQUEST,
  '__module__' : 'daily_check_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresRequest)
  })
_sym_db.RegisterMessage(DailyCheckProcedureAppService_dailyCheckProceduresRequest)

DailyCheckProcedureAppService_dailyCheckProceduresResponse = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureAppService_dailyCheckProceduresResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESRESPONSE,
  '__module__' : 'daily_check_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure.DailyCheckProcedureAppService_dailyCheckProceduresResponse)
  })
_sym_db.RegisterMessage(DailyCheckProcedureAppService_dailyCheckProceduresResponse)



_DAILYCHECKPROCEDUREAPPSERVICE = _descriptor.ServiceDescriptor(
  name='DailyCheckProcedureAppService',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=662,
  serialized_end=1138,
  methods=[
  _descriptor.MethodDescriptor(
    name='dailyCheckProcedureById',
    full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService.dailyCheckProcedureById',
    index=0,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDREQUEST,
    output_type=_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDUREBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='dailyCheckProcedures',
    full_name='cafm.project.daily_check_procedure.DailyCheckProcedureAppService.dailyCheckProcedures',
    index=1,
    containing_service=None,
    input_type=_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESREQUEST,
    output_type=_DAILYCHECKPROCEDUREAPPSERVICE_DAILYCHECKPROCEDURESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYCHECKPROCEDUREAPPSERVICE)

DESCRIPTOR.services_by_name['DailyCheckProcedureAppService'] = _DAILYCHECKPROCEDUREAPPSERVICE

# @@protoc_insertion_point(module_scope)
