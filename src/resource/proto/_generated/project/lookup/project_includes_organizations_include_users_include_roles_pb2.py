# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/project_includes_organizations_include_users_include_roles.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup import organization_includes_users_include_roles_pb2 as project_dot_lookup_dot_organization__includes__users__include__roles__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/project_includes_organizations_include_users_include_roles.proto',
  package='cafm.project.lookup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nOproject/lookup/project_includes_organizations_include_users_include_roles.proto\x12\x13\x63\x61\x66m.project.lookup\x1a>project/lookup/organization_includes_users_include_roles.proto\"\x98\x06\n4ProjectIncludesOrganizationsIncludeUsersIncludeRoles\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ity_id\x18\x03 \x01(\x05\x12\x12\n\ncountry_id\x18\x04 \x01(\x05\x12\x12\n\nstart_date\x18\x05 \x01(\x05\x12\x16\n\x0e\x62\x65neficiary_id\x18\x06 \x01(\t\x12\x14\n\x0c\x61\x64\x64ress_line\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\x12\x18\n\x10\x61\x64\x64ress_line_two\x18\t \x01(\t\x12\x16\n\x0e\x64\x65veloper_name\x18\n \x01(\t\x12\x19\n\x11\x64\x65veloper_city_id\x18\x0b \x01(\x05\x12\x1c\n\x14\x64\x65veloper_country_id\x18\x0c \x01(\x05\x12\"\n\x1a\x64\x65veloper_address_line_one\x18\r \x01(\t\x12\"\n\x1a\x64\x65veloper_address_line_two\x18\x0e \x01(\t\x12\x19\n\x11\x64\x65veloper_contact\x18\x0f \x01(\t\x12\x17\n\x0f\x64\x65veloper_email\x18\x10 \x01(\t\x12\x1e\n\x16\x64\x65veloper_phone_number\x18\x11 \x01(\t\x12\x1a\n\x12\x64\x65veloper_warranty\x18\x12 \x01(\t\x12\x13\n\x0bpostal_code\x18\x13 \x01(\t\x12\x1d\n\x15\x64\x65veloper_postal_code\x18\x14 \x01(\t\x12\x1a\n\x12\x63ountry_state_name\x18\x15 \x01(\t\x12\x1e\n\x16\x63ountry_state_iso_code\x18\x16 \x01(\t\x12$\n\x1c\x64\x65veloper_country_state_name\x18\x17 \x01(\t\x12(\n developer_country_state_iso_code\x18\x18 \x01(\t\x12m\n)organizations_include_users_include_roles\x18\x19 \x03(\x0b\x32:.cafm.project.lookup.OrganizationIncludesUsersIncludeRolesb\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_organization__includes__users__include__roles__pb2.DESCRIPTOR,])




_PROJECTINCLUDESORGANIZATIONSINCLUDEUSERSINCLUDEROLES = _descriptor.Descriptor(
  name='ProjectIncludesOrganizationsIncludeUsersIncludeRoles',
  full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city_id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.city_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.country_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.start_date', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='beneficiary_id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.beneficiary_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.address_line', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.state', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_line_two', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.address_line_two', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_name', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_city_id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_city_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_country_id', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_country_id', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_address_line_one', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_address_line_one', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_address_line_two', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_address_line_two', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_contact', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_contact', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_email', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_email', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_phone_number', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_phone_number', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_warranty', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_warranty', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postal_code', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.postal_code', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_postal_code', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_postal_code', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_state_name', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.country_state_name', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_state_iso_code', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.country_state_iso_code', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_country_state_name', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_country_state_name', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='developer_country_state_iso_code', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.developer_country_state_iso_code', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organizations_include_users_include_roles', full_name='cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles.organizations_include_users_include_roles', index=24,
      number=25, type=11, cpp_type=10, label=3,
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
  serialized_start=169,
  serialized_end=961,
)

_PROJECTINCLUDESORGANIZATIONSINCLUDEUSERSINCLUDEROLES.fields_by_name['organizations_include_users_include_roles'].message_type = project_dot_lookup_dot_organization__includes__users__include__roles__pb2._ORGANIZATIONINCLUDESUSERSINCLUDEROLES
DESCRIPTOR.message_types_by_name['ProjectIncludesOrganizationsIncludeUsersIncludeRoles'] = _PROJECTINCLUDESORGANIZATIONSINCLUDEUSERSINCLUDEROLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProjectIncludesOrganizationsIncludeUsersIncludeRoles = _reflection.GeneratedProtocolMessageType('ProjectIncludesOrganizationsIncludeUsersIncludeRoles', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTINCLUDESORGANIZATIONSINCLUDEUSERSINCLUDEROLES,
  '__module__' : 'project.lookup.project_includes_organizations_include_users_include_roles_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.ProjectIncludesOrganizationsIncludeUsersIncludeRoles)
  })
_sym_db.RegisterMessage(ProjectIncludesOrganizationsIncludeUsersIncludeRoles)


# @@protoc_insertion_point(module_scope)
