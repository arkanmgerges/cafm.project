# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_pb2 as user__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_app_service.proto',
  package='cafm.project.user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16user_app_service.proto\x12\x11\x63\x61\x66m.project.user\x1a\nuser.proto\x1a\x0border.proto\"2\n!UserAppService_userByEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"K\n\"UserAppService_userByEmailResponse\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.cafm.project.user.User\",\n\x1eUserAppService_userByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x1fUserAppService_userByIdResponse\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.cafm.project.user.User\"n\n\x1bUserAppService_usersRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"^\n\x1cUserAppService_usersResponse\x12&\n\x05users\x18\x01 \x03(\x0b\x32\x17.cafm.project.user.User\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\"\x1d\n\x1bUserAppService_newIdRequest\"*\n\x1cUserAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xdb\x03\n\x0eUserAppService\x12|\n\x0buserByEmail\x12\x34.cafm.project.user.UserAppService_userByEmailRequest\x1a\x35.cafm.project.user.UserAppService_userByEmailResponse\"\x00\x12s\n\x08userById\x12\x31.cafm.project.user.UserAppService_userByIdRequest\x1a\x32.cafm.project.user.UserAppService_userByIdResponse\"\x00\x12j\n\x05users\x12..cafm.project.user.UserAppService_usersRequest\x1a/.cafm.project.user.UserAppService_usersResponse\"\x00\x12j\n\x05newId\x12..cafm.project.user.UserAppService_newIdRequest\x1a/.cafm.project.user.UserAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[user__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




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
  serialized_start=70,
  serialized_end=120,
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
  serialized_start=122,
  serialized_end=197,
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
  serialized_start=199,
  serialized_end=243,
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
  serialized_start=245,
  serialized_end=317,
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
      name='resultFrom', full_name='cafm.project.user.UserAppService_usersRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.user.UserAppService_usersRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.user.UserAppService_usersRequest.order', index=2,
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
  serialized_start=319,
  serialized_end=429,
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
      name='totalItemCount', full_name='cafm.project.user.UserAppService_usersResponse.totalItemCount', index=1,
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
  serialized_start=431,
  serialized_end=525,
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
  serialized_start=527,
  serialized_end=556,
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
  serialized_start=558,
  serialized_end=600,
)

_USERAPPSERVICE_USERBYEMAILRESPONSE.fields_by_name['user'].message_type = user__pb2._USER
_USERAPPSERVICE_USERBYIDRESPONSE.fields_by_name['user'].message_type = user__pb2._USER
_USERAPPSERVICE_USERSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_USERAPPSERVICE_USERSRESPONSE.fields_by_name['users'].message_type = user__pb2._USER
DESCRIPTOR.message_types_by_name['UserAppService_userByEmailRequest'] = _USERAPPSERVICE_USERBYEMAILREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByEmailResponse'] = _USERAPPSERVICE_USERBYEMAILRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_userByIdRequest'] = _USERAPPSERVICE_USERBYIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_userByIdResponse'] = _USERAPPSERVICE_USERBYIDRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_usersRequest'] = _USERAPPSERVICE_USERSREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_usersResponse'] = _USERAPPSERVICE_USERSRESPONSE
DESCRIPTOR.message_types_by_name['UserAppService_newIdRequest'] = _USERAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['UserAppService_newIdResponse'] = _USERAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAppService_userByEmailRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYEMAILREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByEmailRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByEmailRequest)

UserAppService_userByEmailResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYEMAILRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByEmailResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByEmailResponse)

UserAppService_userByIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_userByIdRequest)

UserAppService_userByIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_userByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERBYIDRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_userByIdResponse)
  })
_sym_db.RegisterMessage(UserAppService_userByIdResponse)

UserAppService_usersRequest = _reflection.GeneratedProtocolMessageType('UserAppService_usersRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersRequest)
  })
_sym_db.RegisterMessage(UserAppService_usersRequest)

UserAppService_usersResponse = _reflection.GeneratedProtocolMessageType('UserAppService_usersResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_USERSRESPONSE,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_usersResponse)
  })
_sym_db.RegisterMessage(UserAppService_usersResponse)

UserAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('UserAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'user_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user.UserAppService_newIdRequest)
  })
_sym_db.RegisterMessage(UserAppService_newIdRequest)

UserAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('UserAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'user_app_service_pb2'
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
  serialized_start=603,
  serialized_end=1078,
  methods=[
  _descriptor.MethodDescriptor(
    name='userByEmail',
    full_name='cafm.project.user.UserAppService.userByEmail',
    index=0,
    containing_service=None,
    input_type=_USERAPPSERVICE_USERBYEMAILREQUEST,
    output_type=_USERAPPSERVICE_USERBYEMAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userById',
    full_name='cafm.project.user.UserAppService.userById',
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
    name='newId',
    full_name='cafm.project.user.UserAppService.newId',
    index=3,
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
