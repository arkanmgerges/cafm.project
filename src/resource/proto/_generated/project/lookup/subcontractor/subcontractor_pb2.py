# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/subcontractor/subcontractor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.subcontractor import country_pb2 as project_dot_lookup_dot_subcontractor_dot_country__pb2
from project.lookup.subcontractor import city_pb2 as project_dot_lookup_dot_subcontractor_dot_city__pb2
from project.lookup.subcontractor import state_pb2 as project_dot_lookup_dot_subcontractor_dot_state__pb2
from project.lookup.subcontractor import subcontractor_category_pb2 as project_dot_lookup_dot_subcontractor_dot_subcontractor__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/subcontractor/subcontractor.proto',
  package='cafm.project.lookup.subcontractor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0project/lookup/subcontractor/subcontractor.proto\x12!cafm.project.lookup.subcontractor\x1a*project/lookup/subcontractor/country.proto\x1a\'project/lookup/subcontractor/city.proto\x1a(project/lookup/subcontractor/state.proto\x1a\x39project/lookup/subcontractor/subcontractor_category.proto\"\xde\x03\n\rSubcontractor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x02 \x01(\t\x12\x13\n\x0bwebsite_url\x18\x03 \x01(\t\x12\x16\n\x0e\x63ontact_person\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\x12\x13\n\x0b\x61\x64\x64ress_one\x18\x07 \x01(\t\x12\x13\n\x0b\x61\x64\x64ress_two\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x13\n\x0bpostal_code\x18\n \x01(\t\x12X\n\x16subcontractor_category\x18\x0b \x01(\x0b\x32\x38.cafm.project.lookup.subcontractor.SubcontractorCategory\x12;\n\x07\x63ountry\x18\x0c \x01(\x0b\x32*.cafm.project.lookup.subcontractor.Country\x12\x37\n\x05state\x18\r \x01(\x0b\x32(.cafm.project.lookup.subcontractor.State\x12\x35\n\x04\x63ity\x18\x0e \x01(\x0b\x32\'.cafm.project.lookup.subcontractor.Cityb\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_subcontractor_dot_country__pb2.DESCRIPTOR,project_dot_lookup_dot_subcontractor_dot_city__pb2.DESCRIPTOR,project_dot_lookup_dot_subcontractor_dot_state__pb2.DESCRIPTOR,project_dot_lookup_dot_subcontractor_dot_subcontractor__category__pb2.DESCRIPTOR,])




_SUBCONTRACTOR = _descriptor.Descriptor(
  name='Subcontractor',
  full_name='cafm.project.lookup.subcontractor.Subcontractor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.subcontractor.Subcontractor.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='cafm.project.lookup.subcontractor.Subcontractor.company_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='website_url', full_name='cafm.project.lookup.subcontractor.Subcontractor.website_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contact_person', full_name='cafm.project.lookup.subcontractor.Subcontractor.contact_person', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.lookup.subcontractor.Subcontractor.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='cafm.project.lookup.subcontractor.Subcontractor.phone_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_one', full_name='cafm.project.lookup.subcontractor.Subcontractor.address_one', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_two', full_name='cafm.project.lookup.subcontractor.Subcontractor.address_two', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cafm.project.lookup.subcontractor.Subcontractor.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postal_code', full_name='cafm.project.lookup.subcontractor.Subcontractor.postal_code', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractor_category', full_name='cafm.project.lookup.subcontractor.Subcontractor.subcontractor_category', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='cafm.project.lookup.subcontractor.Subcontractor.country', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='cafm.project.lookup.subcontractor.Subcontractor.state', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='cafm.project.lookup.subcontractor.Subcontractor.city', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=274,
  serialized_end=752,
)

_SUBCONTRACTOR.fields_by_name['subcontractor_category'].message_type = project_dot_lookup_dot_subcontractor_dot_subcontractor__category__pb2._SUBCONTRACTORCATEGORY
_SUBCONTRACTOR.fields_by_name['country'].message_type = project_dot_lookup_dot_subcontractor_dot_country__pb2._COUNTRY
_SUBCONTRACTOR.fields_by_name['state'].message_type = project_dot_lookup_dot_subcontractor_dot_state__pb2._STATE
_SUBCONTRACTOR.fields_by_name['city'].message_type = project_dot_lookup_dot_subcontractor_dot_city__pb2._CITY
DESCRIPTOR.message_types_by_name['Subcontractor'] = _SUBCONTRACTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subcontractor = _reflection.GeneratedProtocolMessageType('Subcontractor', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTOR,
  '__module__' : 'project.lookup.subcontractor.subcontractor_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.subcontractor.Subcontractor)
  })
_sym_db.RegisterMessage(Subcontractor)


# @@protoc_insertion_point(module_scope)
