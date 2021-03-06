# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/standard_maintenance_procedure_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import standard_maintenance_procedure_pb2 as project_dot_standard__maintenance__procedure__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/standard_maintenance_procedure_app_service.proto',
  package='cafm.project.standard_maintenance_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8project/standard_maintenance_procedure_app_service.proto\x12+cafm.project.standard_maintenance_procedure\x1a,project/standard_maintenance_procedure.proto\x1a\x0border.proto\"\\\nNStandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc4\x01\nOStandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse\x12q\n\x1estandard_maintenance_procedure\x18\x01 \x01(\x0b\x32I.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure\"\xa1\x01\nKStandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xdc\x01\nLStandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse\x12r\n\x1fstandard_maintenance_procedures\x18\x01 \x03(\x0b\x32I.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedure\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"5\n3StandardMaintenanceProcedureAppService_newIdRequest\"B\n4StandardMaintenanceProcedureAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xbb\x06\n&StandardMaintenanceProcedureAppService\x12\xa3\x02\n$standard_maintenance_procedure_by_id\x12{.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest\x1a|.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse\"\x00\x12\x98\x02\n\x1fstandard_maintenance_procedures\x12x.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest\x1ay.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse\"\x00\x12\xcf\x01\n\x06new_id\x12`.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest\x1a\x61.cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_standard__maintenance__procedure__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest.id', index=0,
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
  serialized_start=164,
  serialized_end=256,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse.standard_maintenance_procedure', index=0,
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
  serialized_start=259,
  serialized_end=455,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest.orders', index=2,
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
  serialized_start=458,
  serialized_end=619,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedures', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse.standard_maintenance_procedures', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse.total_item_count', index=1,
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
  serialized_start=622,
  serialized_end=842,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_newIdRequest',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest',
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
  serialized_start=844,
  serialized_end=897,
)


_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureAppService_newIdResponse',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse.id', index=0,
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
  serialized_start=899,
  serialized_end=965,
)

_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE.fields_by_name['standard_maintenance_procedure'].message_type = project_dot_standard__maintenance__procedure__pb2._STANDARDMAINTENANCEPROCEDURE
_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE.fields_by_name['standard_maintenance_procedures'].message_type = project_dot_standard__maintenance__procedure__pb2._STANDARDMAINTENANCEPROCEDURE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_newIdRequest'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureAppService_newIdResponse'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest)

StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse)

StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest)

StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse)

StandardMaintenanceProcedureAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_newIdRequest)

StandardMaintenanceProcedureAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.standard_maintenance_procedure_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService_newIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureAppService_newIdResponse)



_STANDARDMAINTENANCEPROCEDUREAPPSERVICE = _descriptor.ServiceDescriptor(
  name='StandardMaintenanceProcedureAppService',
  full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=968,
  serialized_end=1795,
  methods=[
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_by_id',
    full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.standard_maintenance_procedure_by_id',
    index=0,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDUREBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedures',
    full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.standard_maintenance_procedures',
    index=1,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_STANDARDMAINTENANCEPROCEDURESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.standard_maintenance_procedure.StandardMaintenanceProcedureAppService.new_id',
    index=2,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STANDARDMAINTENANCEPROCEDUREAPPSERVICE)

DESCRIPTOR.services_by_name['StandardMaintenanceProcedureAppService'] = _STANDARDMAINTENANCEPROCEDUREAPPSERVICE

# @@protoc_insertion_point(module_scope)
