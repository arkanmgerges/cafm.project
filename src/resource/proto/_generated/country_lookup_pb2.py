# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: country_lookup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='country_lookup.proto',
  package='cafm.project.lookup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x63ountry_lookup.proto\x12\x13\x63\x61\x66m.project.lookup\")\n\rCountryLookup\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3'
)




_COUNTRYLOOKUP = _descriptor.Descriptor(
  name='CountryLookup',
  full_name='cafm.project.lookup.CountryLookup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.CountryLookup.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.CountryLookup.name', index=1,
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
  serialized_start=45,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['CountryLookup'] = _COUNTRYLOOKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountryLookup = _reflection.GeneratedProtocolMessageType('CountryLookup', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRYLOOKUP,
  '__module__' : 'country_lookup_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.CountryLookup)
  })
_sym_db.RegisterMessage(CountryLookup)


# @@protoc_insertion_point(module_scope)