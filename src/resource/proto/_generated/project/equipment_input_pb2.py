# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/equipment_input.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/equipment_input.proto',
  package='cafm.project.equipment_input',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dproject/equipment_input.proto\x12\x1c\x63\x61\x66m.project.equipment_input\"`\n\x0e\x45quipmentInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0f\n\x07unit_id\x18\x04 \x01(\t\x12\x14\n\x0c\x65quipment_id\x18\x05 \x01(\tb\x06proto3'
)




_EQUIPMENTINPUT = _descriptor.Descriptor(
  name='EquipmentInput',
  full_name='cafm.project.equipment_input.EquipmentInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_input.EquipmentInput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.equipment_input.EquipmentInput.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cafm.project.equipment_input.EquipmentInput.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='cafm.project.equipment_input.EquipmentInput.unit_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equipment_id', full_name='cafm.project.equipment_input.EquipmentInput.equipment_id', index=4,
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
  serialized_start=63,
  serialized_end=159,
)

DESCRIPTOR.message_types_by_name['EquipmentInput'] = _EQUIPMENTINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentInput = _reflection.GeneratedProtocolMessageType('EquipmentInput', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTINPUT,
  '__module__' : 'project.equipment_input_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_input.EquipmentInput)
  })
_sym_db.RegisterMessage(EquipmentInput)


# @@protoc_insertion_point(module_scope)