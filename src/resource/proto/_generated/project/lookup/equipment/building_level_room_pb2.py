# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/equipment/building_level_room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/equipment/building_level_room.proto',
  package='cafm.project.lookup.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2project/lookup/equipment/building_level_room.proto\x12\x1d\x63\x61\x66m.project.lookup.equipment\"B\n\x11\x42uildingLevelRoom\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tb\x06proto3'
)




_BUILDINGLEVELROOM = _descriptor.Descriptor(
  name='BuildingLevelRoom',
  full_name='cafm.project.lookup.equipment.BuildingLevelRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.equipment.BuildingLevelRoom.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.equipment.BuildingLevelRoom.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.lookup.equipment.BuildingLevelRoom.description', index=2,
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
  serialized_start=85,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['BuildingLevelRoom'] = _BUILDINGLEVELROOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildingLevelRoom = _reflection.GeneratedProtocolMessageType('BuildingLevelRoom', (_message.Message,), {
  'DESCRIPTOR' : _BUILDINGLEVELROOM,
  '__module__' : 'project.lookup.equipment.building_level_room_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.BuildingLevelRoom)
  })
_sym_db.RegisterMessage(BuildingLevelRoom)


# @@protoc_insertion_point(module_scope)