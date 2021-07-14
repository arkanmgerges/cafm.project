# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/daily_check_procedure_operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/daily_check_procedure_operation.proto',
  package='cafm.project.daily_check_procedure_operation',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-project/daily_check_procedure_operation.proto\x12,cafm.project.daily_check_procedure_operation\"}\n\x1c\x44\x61ilyCheckProcedureOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12 \n\x18\x64\x61ily_check_procedure_id\x18\x05 \x01(\tb\x06proto3'
)




_DAILYCHECKPROCEDUREOPERATION = _descriptor.Descriptor(
  name='DailyCheckProcedureOperation',
  full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='daily_check_procedure_id', full_name='cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation.daily_check_procedure_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=95,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['DailyCheckProcedureOperation'] = _DAILYCHECKPROCEDUREOPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedureOperation = _reflection.GeneratedProtocolMessageType('DailyCheckProcedureOperation', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDUREOPERATION,
  '__module__' : 'project.daily_check_procedure_operation_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure_operation.DailyCheckProcedureOperation)
  })
_sym_db.RegisterMessage(DailyCheckProcedureOperation)


# @@protoc_insertion_point(module_scope)