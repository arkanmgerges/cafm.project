# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_project_category.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='equipment_project_category.proto',
  package='cafm.project.equipment_project_category',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n equipment_project_category.proto\x12\'cafm.project.equipment_project_category\"H\n\x18\x45quipmentProjectCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\tb\x06proto3'
)




_EQUIPMENTPROJECTCATEGORY = _descriptor.Descriptor(
  name='EquipmentProjectCategory',
  full_name='cafm.project.equipment_project_category.EquipmentProjectCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.equipment_project_category.EquipmentProjectCategory.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.equipment_project_category.EquipmentProjectCategory.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='cafm.project.equipment_project_category.EquipmentProjectCategory.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=77,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['EquipmentProjectCategory'] = _EQUIPMENTPROJECTCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentProjectCategory = _reflection.GeneratedProtocolMessageType('EquipmentProjectCategory', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTPROJECTCATEGORY,
  '__module__' : 'equipment_project_category_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.equipment_project_category.EquipmentProjectCategory)
  })
_sym_db.RegisterMessage(EquipmentProjectCategory)


# @@protoc_insertion_point(module_scope)
