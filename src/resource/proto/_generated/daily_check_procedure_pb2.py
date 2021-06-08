# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daily_check_procedure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='daily_check_procedure.proto',
  package='cafm.project.daily_check_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x64\x61ily_check_procedure.proto\x12\"cafm.project.daily_check_procedure\"\x7f\n\x13\x44\x61ilyCheckProcedure\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x65quipment_id\x18\x04 \x01(\t\x12#\n\x1b\x65quipment_category_group_id\x18\x05 \x01(\tb\x06proto3'
)




_DAILYCHECKPROCEDURE = _descriptor.Descriptor(
  name='DailyCheckProcedure',
  full_name='cafm.project.daily_check_procedure.DailyCheckProcedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.daily_check_procedure.DailyCheckProcedure.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.daily_check_procedure.DailyCheckProcedure.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.daily_check_procedure.DailyCheckProcedure.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equipment_id', full_name='cafm.project.daily_check_procedure.DailyCheckProcedure.equipment_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equipment_category_group_id', full_name='cafm.project.daily_check_procedure.DailyCheckProcedure.equipment_category_group_id', index=4,
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
  serialized_start=67,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['DailyCheckProcedure'] = _DAILYCHECKPROCEDURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyCheckProcedure = _reflection.GeneratedProtocolMessageType('DailyCheckProcedure', (_message.Message,), {
  'DESCRIPTOR' : _DAILYCHECKPROCEDURE,
  '__module__' : 'daily_check_procedure_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.daily_check_procedure.DailyCheckProcedure)
  })
_sym_db.RegisterMessage(DailyCheckProcedure)


# @@protoc_insertion_point(module_scope)
