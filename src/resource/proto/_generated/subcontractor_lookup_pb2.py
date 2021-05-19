# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subcontractor_lookup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='subcontractor_lookup.proto',
  package='cafm.project.subcontractor_lookup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1asubcontractor_lookup.proto\x12!cafm.project.subcontractor_lookup\"\x88\x03\n\x13SubcontractorLookup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x02 \x01(\t\x12\x12\n\nwebsiteUrl\x18\x03 \x01(\t\x12\x15\n\rcontactPerson\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x06 \x01(\t\x12\x12\n\naddressOne\x18\x07 \x01(\t\x12\x12\n\naddressTwo\x18\x08 \x01(\t\x12\x1f\n\x17subcontractorCategoryId\x18\t \x01(\t\x12!\n\x19subcontractorCategoryName\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x0e\n\x06\x63ityId\x18\x0c \x01(\x05\x12\x10\n\x08\x63ityName\x18\r \x01(\t\x12\x11\n\tcountryId\x18\x0e \x01(\x05\x12\x13\n\x0b\x63ountryName\x18\x0f \x01(\t\x12\x0f\n\x07stateId\x18\x10 \x01(\t\x12\x11\n\tstateName\x18\x11 \x01(\t\x12\x12\n\npostalCode\x18\x12 \x01(\tb\x06proto3'
)




_SUBCONTRACTORLOOKUP = _descriptor.Descriptor(
  name='SubcontractorLookup',
  full_name='cafm.project.subcontractor_lookup.SubcontractorLookup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.companyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='websiteUrl', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.websiteUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contactPerson', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.contactPerson', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.phoneNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressOne', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.addressOne', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addressTwo', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.addressTwo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractorCategoryId', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.subcontractorCategoryId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractorCategoryName', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.subcontractorCategoryName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cityId', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.cityId', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cityName', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.cityName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='countryId', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.countryId', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='countryName', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.countryName', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stateId', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.stateId', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stateName', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.stateName', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postalCode', full_name='cafm.project.subcontractor_lookup.SubcontractorLookup.postalCode', index=17,
      number=18, type=9, cpp_type=9, label=1,
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
  serialized_start=66,
  serialized_end=458,
)

DESCRIPTOR.message_types_by_name['SubcontractorLookup'] = _SUBCONTRACTORLOOKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubcontractorLookup = _reflection.GeneratedProtocolMessageType('SubcontractorLookup', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORLOOKUP,
  '__module__' : 'subcontractor_lookup_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor_lookup.SubcontractorLookup)
  })
_sym_db.RegisterMessage(SubcontractorLookup)


# @@protoc_insertion_point(module_scope)