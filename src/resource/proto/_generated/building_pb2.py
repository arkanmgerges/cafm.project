# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: building.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import building_level_pb2 as building__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='building.proto',
  package='cafm.project.project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x62uilding.proto\x12\x14\x63\x61\x66m.project.project\x1a\x14\x62uilding_level.proto\"t\n\x08\x42uilding\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprojectId\x18\x03 \x01(\t\x12;\n\x0e\x62uildingLevels\x18\x04 \x03(\x0b\x32#.cafm.project.project.BuildingLevelb\x06proto3'
  ,
  dependencies=[building__level__pb2.DESCRIPTOR,])




_BUILDING = _descriptor.Descriptor(
  name='Building',
  full_name='cafm.project.project.Building',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.project.Building.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.project.Building.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='projectId', full_name='cafm.project.project.Building.projectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buildingLevels', full_name='cafm.project.project.Building.buildingLevels', index=3,
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
  serialized_start=62,
  serialized_end=178,
)

_BUILDING.fields_by_name['buildingLevels'].message_type = building__level__pb2._BUILDINGLEVEL
DESCRIPTOR.message_types_by_name['Building'] = _BUILDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Building = _reflection.GeneratedProtocolMessageType('Building', (_message.Message,), {
  'DESCRIPTOR' : _BUILDING,
  '__module__' : 'building_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.project.Building)
  })
_sym_db.RegisterMessage(Building)


# @@protoc_insertion_point(module_scope)