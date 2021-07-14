# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/user_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project import user_pb2 as project_dot_user__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/user_app_service.proto',
  package='cafm.project.user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eproject/user_app_service.proto\x12\x11\x63\x61\x66m.project.user\x1a\x12project/user.proto\x1a\x0border.proto\"2\n!UserAppService_userByEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"K\n\"UserAppService_userByEmailResponse\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.cafm.project.user.User\",\n\x1eUserAppService_userByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x1fUserAppService_userByIdResponse\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.cafm.project.user.User\"q\n\x1bUserAppService_usersRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"`\n\x1cUserAppService_usersResponse\x12&\n\x05users\x18\x01 \x03(\x0b\x32\x17.cafm.project.user.User\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\x9a\x01\n+UserAppService_usersByOrganizationIdRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\x13\n\x0bresult_from\x18\x02 \x01(\x05\x12\x13\n\x0bresult_size\x18\x03 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"p\n,UserAppService_usersByOrganizationIdResponse\x12&\n\x05users\x18\x01 \x03(\x0b\x32\x17.cafm.project.user.User\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\"\x1d\n\x1bUserAppService_newIdRequest\"*\n\x1cUserAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\x80\x05\n\x0eUserAppService\x12~\n\ruser_by_email\x12\x34.cafm.project.user.UserAppService_userByEmailRequest\x1a\x35.cafm.project.user.UserAppService_userByEmailResponse\"\x00\x12u\n\nuser_by_id\x12\x31.cafm.project.user.UserAppService_userByIdRequest\x1a\x32.cafm.project.user.UserAppService_userByIdResponse\"\x00\x12j\n\x05users\x12..cafm.project.user.UserAppService_usersRequest\x1a/.cafm.project.user.UserAppService_usersResponse\"\x00\x12\x9d\x01\n\x18users_by_organization_id\x12>.cafm.project.user.UserAppService_usersByOrganizationIdRequest\x1a?.cafm.project.user.UserAppService_usersByOrganizationIdResponse\"\x00\x12k\n\x06new_id\x12..cafm.project.user.UserAppService_newIdRequest\x1a/.cafm.project.user.UserAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[project_dot_user__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_USERAPPSERVICE_USERBYEMAILREQUEST = _descriptor.Descriptor(
  name='UserAppService_userByEmailRequest',
  full_name='cafm.project.user.UserAppService_userByEmailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.user.UserAppService_userByEmailRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=86,
  serialized_end=136,
)


_USERAPPSERVICE_USERBYEMAILRESPONSE = _descriptor.Descriptor(
  name='UserAppService_userByEmailResponse',
  full_name='cafm.project.user.UserAppService_userByEmailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='cafm.project.user.UserAppService_userByEmailResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=138,
  serialized_end=213,
)


_USERAPPSERVICE_USERBYIDREQUEST = _descriptor.Descriptor(
  name='UserAppService_userByIdRequest',
  full_name='cafm.project.user.UserAppService_userByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.user.UserAppService_userByIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=215,
  serialized_end=259,
)


_USERAPPSERVICE_USERBYIDRESPONSE = _descriptor.Descriptor(
  name='UserAppService_userByIdResponse',
  full_name='cafm.project.user.UserAppService_userByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='cafm.project.user.UserAppService_userByIdResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=261,
  serialized_end=333,
)


_USERAPPSERVICE_USERSREQUEST = _descriptor.Descriptor(
  name='UserAppService_usersRequest',
  full_name='cafm.project.user.UserAppService_usersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.user.UserAppService_usersRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.user.UserAppService_usersRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.user.UserAppService_usersRequest.orders', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=335,
  serialized_end=448,
)


_USERAPPSERVICE_USERSRESPONSE = _descriptor.Descriptor(
  name='UserAppService_usersResponse',
  full_name='cafm.project.user.UserAppService_usersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='cafm.project.user.UserAppService_usersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.user.UserAppService_usersResponse.total_item_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=450,
  serialized_end=546,
)


_USERAPPSERVICE_USERSBYORGANIZATIONIDREQUEST = _descriptor.Descriptor(
  name='UserAppService_usersByOrganizationIdRequest',
  full_name='cafm.project.user.UserAppService_usersByOrganizationIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='cafm.project.user.UserAppService_usersByOrganizationIdRequest.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.project.user.UserAppService_usersByOrganizationIdRequest.result_from', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.project.user.UserAppService_usersByOrganizationIdRequest.result_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.user.UserAppService_usersByOrganizationIdRequest.orders', index=3,
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
  serialized_start=549,
  serialized_end=703,
)


_USERAPPSERVICE_USERSBYORGANIZATIONIDRESPONSE = _descriptor.Descriptor(
  name='UserAppService_usersByOrganizationIdResponse',
  full_name='cafm.project.user.UserAppService_usersByOrganizationIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='cafm.project.user.UserAppService_usersByOrganizationIdResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.project.user.UserAppService_usersByOrganizationIdResponse.total_item_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=705,
  serialized_end=817,
)


_USERAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='UserAppService_newIdRequest',
  full_name='cafm.project.user.UserAppService_newIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=819,
  serialized_end=848,
)


_USERAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='UserAppService_newIdResponse',
  full_name='cafm.project.user.UserAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.user.UserAppService_newIdResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=850,
  serialized_end=892,
)

_USERAPPSERVICE_USERBYEMAILRESPONSE.fields_by_name['user'].message_type = project_dot_user__pb2._USER
_USERAPPSERVICE_USERBYIDRESPONSE.fields_by_name['user'].message_type = project_dot_user__pb2._USER
_USERAPPSERVICE_USERSREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_USERAPPSERVICE_USERSRESPONSE.fields_by_name['users'].message_type = project_dot_user__pb2._USER
_USERAPPSERVICE_USERSBYORGANIZATIONIDREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_USERAPPSERVICE_USERSBYORGANIZATIONIDRESPONSE.fields_by_name['users'].message_type = project_dot_user__pb2._USER
DESCRIPTOR.message_types_by_name['UserAppService_userByEmailRequest'] = _USERAPPSERVICE_USERBYEMAILREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByEmailResponse'] = _USERAPPSERVICE_USERBYEMAILRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_userByIdRequest'] = _USERAPPSERVICE_USERBYIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByIdResponse'] = _USERAPPSERVICE_USERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_usersRequest'] = _USERAPPSERVICE_USERSREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_usersResponse'] = _USERAPPSERVICE_USERSRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_usersByOrganizationIdRequest'] = _USERAPPSERVICE_USERSBYORGANIZATIONIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_usersByOrganizationIdResponse'] = _USERAPPSERVICE_USERSBYORGANIZATIONIDRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_newIdRequest'] = _USERAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_newIdResponse'] = _USERAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAppService_userByEmailRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYEMAILREQUEST,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByEmailRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByEmailRequest)

UserAppService_userByEmailResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYEMAILRESPONSE,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByEmailResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByEmailResponse)

UserAppService_userByIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDREQUEST,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByIdRequest)

UserAppService_userByIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDRESPONSE,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByIdResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByIdResponse)

UserAppService_usersRequest = _reflection.GeneratedProtocolMessageType('UserAppService_usersRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSREQUEST,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersRequest)
  })
_sym_db.RegisterMessage(UserAppService_usersRequest)

UserAppService_usersResponse = _reflection.GeneratedProtocolMessageType('UserAppService_usersResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSRESPONSE,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersResponse)
  })
_sym_db.RegisterMessage(UserAppService_usersResponse)

UserAppService_usersByOrganizationIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_usersByOrganizationIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSBYORGANIZATIONIDREQUEST,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersByOrganizationIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_usersByOrganizationIdRequest)

UserAppService_usersByOrganizationIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_usersByOrganizationIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSBYORGANIZATIONIDRESPONSE,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersByOrganizationIdResponse)
  })
_sym_db.RegisterMessage(UserAppService_usersByOrganizationIdResponse)

UserAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_newIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_newIdRequest)

UserAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'project.user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_newIdResponse)
  })
_sym_db.RegisterMessage(UserAppService_newIdResponse)



_USERAPPSERVICE = _descriptor.ServiceDescriptor(
  name='UserAppService',
  full_name='cafm.project.user.UserAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=895,
  serialized_end=1535,
  methods=[
  _descriptor.MethodDescriptor(
    name='user_by_email',
    full_name='cafm.project.user.UserAppService.user_by_email',
    index=0,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERBYEMAILREQUEST,
    output_type=_USERAPPSERVICE_USERBYEMAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='user_by_id',
    full_name='cafm.project.user.UserAppService.user_by_id',
    index=1,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERBYIDREQUEST,
    output_type=_USERAPPSERVICE_USERBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='users',
    full_name='cafm.project.user.UserAppService.users',
    index=2,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERSREQUEST,
    output_type=_USERAPPSERVICE_USERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='users_by_organization_id',
    full_name='cafm.project.user.UserAppService.users_by_organization_id',
    index=3,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERSBYORGANIZATIONIDREQUEST,
    output_type=_USERAPPSERVICE_USERSBYORGANIZATIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='new_id',
    full_name='cafm.project.user.UserAppService.new_id',
    index=4,
    containing_service=None,
    input_type=_USERAPPSERVICE_NEWIDREQUEST,
    output_type=_USERAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERAPPSERVICE)

DESCRIPTOR.services_by_name['UserAppService'] = _USERAPPSERVICE

# @@protoc_insertion_point(module_scope)