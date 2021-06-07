# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lookup/daily_check_procedure/daily_check_procedure_operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lookup.daily_check_procedure import daily_check_procedure_operation_parameter_pb2 as lookup_dot_daily__check__procedure_dot_daily__check__procedure__operation__parameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lookup/daily_check_procedure/daily_check_procedure_operation.proto',
  package='cafm.project.lookup.daily_check_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBlookup/daily_check_procedure/daily_check_procedure_operation.proto\x12)cafm.project.lookup.daily_check_procedure\x1aLlookup/daily_check_procedure/daily_check_procedure_operation_parameter.proto\"\xe2\x01\n\x1c\x44\x61ilyCheckProcedureOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x84\x01\n*daily_check_procedure_operation_parameters\x18\x05 \x03(\x0b\x32P.cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterb\x06proto3'
  ,
  dependencies=[lookup_dot_daily__check__procedure_dot_daily__check__procedure__operation__parameter__pb2.DESCRIPTOR,])




_DAILYCHECKPROCEDUREOPERATION = _descriptor.Descriptor(
  name='DailyCheckProcedureOperation',
  full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_operation_parameters', full_name='cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation.daily_check_procedure_operation_parameters', index=4,
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
  serialized_start=192,
  serialized_end=418,
)

_DAILYCHECKPROCEDUREOPERATION.fields_by_name['daily_check_procedure_operation_parameters'].message_type = lookup_dot_daily__check__procedure_dot_daily__check__procedure__operation__parameter__pb2._DAILYCHECKPROCEDUREOPERATIONPARAMETER
DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperation'] = _DAILYCHECKPROCEDUREOPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureOperation = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperation', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATION,
  '__module__' : 'lookup.daily_check_procedure.daily_check_procedure_operation_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.daily_check_procedure.DailyCheckProcedureOperation)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperation)


# @@protoc_insertion_point(module_scope)
