# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/daily_check_procedure/equipment_category_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/daily_check_procedure/equipment_category_group.proto',
  package='cafm.project.lookup.daily_check_procedure',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCproject/lookup/daily_check_procedure/equipment_category_group.proto\x12)cafm.project.lookup.daily_check_procedure\"2\n\x16\x45quipmentCategoryGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3'
)




_EQUIPMENTCATEGORYGROUP = _descriptor.Descriptor(
  name='EquipmentCategoryGroup',
  full_name='cafm.project.lookup.daily_check_procedure.EquipmentCategoryGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.daily_check_procedure.EquipmentCategoryGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.daily_check_procedure.EquipmentCategoryGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=114,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['EquipmentCategoryGroup'] = _EQUIPMENTCATEGORYGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentCategoryGroup = _reflection.GeneratedProtocolMessageType('EquipmentCategoryGroup', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENTCATEGORYGROUP,
  '__module__' : 'project.lookup.daily_check_procedure.equipment_category_group_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.daily_check_procedure.EquipmentCategoryGroup)
  })
_sym_db.RegisterMessage(EquipmentCategoryGroup)


# @@protoc_insertion_point(module_scope)
