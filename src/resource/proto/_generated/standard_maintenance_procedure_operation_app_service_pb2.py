# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: standard_maintenance_procedure_operation_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import standard_maintenance_procedure_operation_pb2 as standard__maintenance__procedure__operation__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='standard_maintenance_procedure_operation_app_service.proto',
  package='cafm.project.standard_maintenance_procedure_operation',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:standard_maintenance_procedure_operation_app_service.proto\x12\x35\x63\x61\x66m.project.standard_maintenance_procedure_operation\x1a.standard_maintenance_procedure_operation.proto\x1a\x0border.proto\"n\n`StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xf4\x01\naStandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse\x12\x8e\x01\n(standard_maintenance_procedure_operation\x18\x01 \x01(\x0b\x32\\.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperation\"\xb3\x01\n]StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x8c\x02\n^StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse\x12\x8f\x01\n)standard_maintenance_procedure_operations\x18\x01 \x03(\x0b\x32\\.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperation\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\xfe\x01\n}StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest\x12)\n!standard_maintenance_procedure_id\x18\x01 \x01(\t\x12\x13\n\x0bresult_from\x18\x02 \x01(\x05\x12\x13\n\x0bresult_size\x18\x03 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\xac\x02\n~StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse\x12\x8f\x01\n)standard_maintenance_procedure_operations\x18\x01 \x03(\x0b\x32\\.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperation\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\">\n<StandardMaintenanceProcedureOperationAppService_newIdRequest\"K\n=StandardMaintenanceProcedureOperationAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xb6\x0b\n/StandardMaintenanceProcedureOperationAppService\x12\xe7\x02\n.standard_maintenance_procedure_operation_by_id\x12\x97\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest\x1a\x98\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse\"\x00\x12\xdc\x02\n)standard_maintenance_procedure_operations\x12\x94\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest\x1a\x95\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse\"\x00\x12\xc1\x03\nNstandard_maintenance_procedure_operations_by_standard_maintenance_procedure_id\x12\xb4\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest\x1a\xb5\x01.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse\"\x00\x12\xf5\x01\n\x06new_id\x12s.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdRequest\x1at.cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[standard__maintenance__procedure__operation__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest.id', index=0,
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
  serialized_start=178,
  serialized_end=288,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operation', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse.standard_maintenance_procedure_operation', index=0,
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
  serialized_start=291,
  serialized_end=535,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest.orders', index=2,
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
  serialized_start=538,
  serialized_end=717,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operations', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse.standard_maintenance_procedure_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse.total_item_count', index=1,
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
  serialized_start=720,
  serialized_end=988,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_id', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest.standard_maintenance_procedure_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest.result_from', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest.result_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest.orders', index=3,
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
  serialized_start=991,
  serialized_end=1245,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operations', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse.standard_maintenance_procedure_operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse.total_item_count', index=1,
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
  serialized_start=1248,
  serialized_end=1548,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_newIdRequest',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdRequest',
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
  serialized_start=1550,
  serialized_end=1612,
)


_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationAppService_newIdResponse',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdResponse.id', index=0,
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
  serialized_start=1614,
  serialized_end=1689,
)

_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE.fields_by_name['standard_maintenance_procedure_operation'].message_type = standard__maintenance__procedure__operation__pb2._STANDARDMAINTENANCEPROCEDUREOPERATION
_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSRESPONSE.fields_by_name['standard_maintenance_procedure_operations'].message_type = standard__maintenance__procedure__operation__pb2._STANDARDMAINTENANCEPROCEDUREOPERATION
_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDRESPONSE.fields_by_name['standard_maintenance_procedure_operations'].message_type = standard__maintenance__procedure__operation__pb2._STANDARDMAINTENANCEPROCEDUREOPERATION
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDRESPONSE
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_newIdRequest'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationAppService_newIdResponse'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDREQUEST,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdRequest)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSREQUEST,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsRequest)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSRESPONSE,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDREQUEST,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdRequest)

StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDRESPONSE,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse)

StandardMaintenanceProcedureOperationAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdRequest)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_newIdRequest)

StandardMaintenanceProcedureOperationAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'standard_maintenance_procedure_operation_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService_newIdResponse)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationAppService_newIdResponse)



_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE = _descriptor.ServiceDescriptor(
  name='StandardMaintenanceProcedureOperationAppService',
  full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1692,
  serialized_end=3154,
  methods=[
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_operation_by_id',
    full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService.standard_maintenance_procedure_operation_by_id',
    index=0,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_operations',
    full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService.standard_maintenance_procedure_operations',
    index=1,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='standard_maintenance_procedure_operations_by_standard_maintenance_procedure_id',
    full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService.standard_maintenance_procedure_operations_by_standard_maintenance_procedure_id',
    index=2,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_STANDARDMAINTENANCEPROCEDUREOPERATIONSBYSTANDARDMAINTENANCEPROCEDUREIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.standard_maintenance_procedure_operation.StandardMaintenanceProcedureOperationAppService.new_id',
    index=3,
    containing_service=None,
    input_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDREQUEST,
    output_type=_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE)

DESCRIPTOR.services_by_name['StandardMaintenanceProcedureOperationAppService'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONAPPSERVICE

# @@protoc_insertion_point(module_scope)
