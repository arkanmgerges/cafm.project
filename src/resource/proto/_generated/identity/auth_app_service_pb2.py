# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/auth_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/auth_app_service.proto',
  package='cafm.identity.auth',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fidentity/auth_app_service.proto\x12\x12\x63\x61\x66m.identity.auth\"[\n8AuthAppService_authenticateUserByEmailAndPasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"J\n9AuthAppService_authenticateUserByEmailAndPasswordResponse\x12\r\n\x05token\x18\x01 \x01(\t\"6\n%AuthAppService_isAuthenticatedRequest\x12\r\n\x05token\x18\x01 \x01(\t\":\n&AuthAppService_isAuthenticatedResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"-\n\x1c\x41uthAppService_logoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1f\n\x1d\x41uthAppService_logoutResponse2\xda\x03\n\x0e\x41uthAppService\x12\xc8\x01\n\'authenticate_user_by_email_and_password\x12L.cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordRequest\x1aM.cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordResponse\"\x00\x12\x8b\x01\n\x10is_authenticated\x12\x39.cafm.identity.auth.AuthAppService_isAuthenticatedRequest\x1a:.cafm.identity.auth.AuthAppService_isAuthenticatedResponse\"\x00\x12o\n\x06logout\x12\x30.cafm.identity.auth.AuthAppService_logoutRequest\x1a\x31.cafm.identity.auth.AuthAppService_logoutResponse\"\x00\x62\x06proto3'
)




_AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDREQUEST = _descriptor.Descriptor(
  name='AuthAppService_authenticateUserByEmailAndPasswordRequest',
  full_name='cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordRequest.password', index=1,
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
  serialized_start=55,
  serialized_end=146,
)


_AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_authenticateUserByEmailAndPasswordResponse',
  full_name='cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordResponse.token', index=0,
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
  serialized_start=148,
  serialized_end=222,
)


_AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST = _descriptor.Descriptor(
  name='AuthAppService_isAuthenticatedRequest',
  full_name='cafm.identity.auth.AuthAppService_isAuthenticatedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_isAuthenticatedRequest.token', index=0,
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
  serialized_start=224,
  serialized_end=278,
)


_AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_isAuthenticatedResponse',
  full_name='cafm.identity.auth.AuthAppService_isAuthenticatedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='cafm.identity.auth.AuthAppService_isAuthenticatedResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=280,
  serialized_end=338,
)


_AUTHAPPSERVICE_LOGOUTREQUEST = _descriptor.Descriptor(
  name='AuthAppService_logoutRequest',
  full_name='cafm.identity.auth.AuthAppService_logoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cafm.identity.auth.AuthAppService_logoutRequest.token', index=0,
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
  serialized_start=340,
  serialized_end=385,
)


_AUTHAPPSERVICE_LOGOUTRESPONSE = _descriptor.Descriptor(
  name='AuthAppService_logoutResponse',
  full_name='cafm.identity.auth.AuthAppService_logoutResponse',
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
  serialized_start=387,
  serialized_end=418,
)

DESCRIPTOR.message_types_by_name['AuthAppService_authenticateUserByEmailAndPasswordRequest'] = _AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_authenticateUserByEmailAndPasswordResponse'] = _AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['AuthAppService_isAuthenticatedRequest'] = _AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_isAuthenticatedResponse'] = _AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE
DESCRIPTOR.message_types_by_name['AuthAppService_logoutRequest'] = _AUTHAPPSERVICE_LOGOUTREQUEST
DESCRIPTOR.message_types_by_name['AuthAppService_logoutResponse'] = _AUTHAPPSERVICE_LOGOUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthAppService_authenticateUserByEmailAndPasswordRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_authenticateUserByEmailAndPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDREQUEST,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordRequest)
  })
_sym_db.RegisterMessage(AuthAppService_authenticateUserByEmailAndPasswordRequest)

AuthAppService_authenticateUserByEmailAndPasswordResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_authenticateUserByEmailAndPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDRESPONSE,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_authenticateUserByEmailAndPasswordResponse)
  })
_sym_db.RegisterMessage(AuthAppService_authenticateUserByEmailAndPasswordResponse)

AuthAppService_isAuthenticatedRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_isAuthenticatedRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_isAuthenticatedRequest)
  })
_sym_db.RegisterMessage(AuthAppService_isAuthenticatedRequest)

AuthAppService_isAuthenticatedResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_isAuthenticatedResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_isAuthenticatedResponse)
  })
_sym_db.RegisterMessage(AuthAppService_isAuthenticatedResponse)

AuthAppService_logoutRequest = _reflection.GeneratedProtocolMessageType('AuthAppService_logoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_LOGOUTREQUEST,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_logoutRequest)
  })
_sym_db.RegisterMessage(AuthAppService_logoutRequest)

AuthAppService_logoutResponse = _reflection.GeneratedProtocolMessageType('AuthAppService_logoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHAPPSERVICE_LOGOUTRESPONSE,
  '__module__' : 'identity.auth_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.auth.AuthAppService_logoutResponse)
  })
_sym_db.RegisterMessage(AuthAppService_logoutResponse)



_AUTHAPPSERVICE = _descriptor.ServiceDescriptor(
  name='AuthAppService',
  full_name='cafm.identity.auth.AuthAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=421,
  serialized_end=895,
  methods=[
  _descriptor.MethodDescriptor(
    name='authenticate_user_by_email_and_password',
    full_name='cafm.identity.auth.AuthAppService.authenticate_user_by_email_and_password',
    index=0,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDREQUEST,
    output_type=_AUTHAPPSERVICE_AUTHENTICATEUSERBYEMAILANDPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='is_authenticated',
    full_name='cafm.identity.auth.AuthAppService.is_authenticated',
    index=1,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_ISAUTHENTICATEDREQUEST,
    output_type=_AUTHAPPSERVICE_ISAUTHENTICATEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='logout',
    full_name='cafm.identity.auth.AuthAppService.logout',
    index=2,
    containing_service=None,
    input_type=_AUTHAPPSERVICE_LOGOUTREQUEST,
    output_type=_AUTHAPPSERVICE_LOGOUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHAPPSERVICE)

DESCRIPTOR.services_by_name['AuthAppService'] = _AUTHAPPSERVICE

# @@protoc_insertion_point(module_scope)
