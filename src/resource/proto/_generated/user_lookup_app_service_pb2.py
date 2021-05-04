# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_lookup_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import user_lookup_pb2 as user__lookup__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_lookup_app_service.proto',
  package='cafm.project.user_lookup',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1duser_lookup_app_service.proto\x12\x18\x63\x61\x66m.project.user_lookup\x1a\x11user_lookup.proto\x1a\x0border.proto\"B\n1UserLookupAppService_userLookupByUserEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"n\n2UserLookupAppService_userLookupByUserEmailResponse\x12\x38\n\nuserLookup\x18\x01 \x01(\x0b\x32$.cafm.project.user_lookup.UserLookup\"<\n.UserLookupAppService_userLookupByUserIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"k\n/UserLookupAppService_userLookupByUserIdResponse\x12\x38\n\nuserLookup\x18\x01 \x01(\x0b\x32$.cafm.project.user_lookup.UserLookup\"z\n\'UserLookupAppService_userLookupsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"}\n(UserLookupAppService_userLookupsResponse\x12\x39\n\x0buserLookups\x18\x01 \x03(\x0b\x32$.cafm.project.user_lookup.UserLookup\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\x32\x94\x04\n\x14UserLookupAppService\x12\xb4\x01\n\x15userLookupByUserEmail\x12K.cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailRequest\x1aL.cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailResponse\"\x00\x12\xab\x01\n\x12userLookupByUserId\x12H.cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdRequest\x1aI.cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdResponse\"\x00\x12\x96\x01\n\x0buserLookups\x12\x41.cafm.project.user_lookup.UserLookupAppService_userLookupsRequest\x1a\x42.cafm.project.user_lookup.UserLookupAppService_userLookupsResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[user__lookup__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILREQUEST = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupByUserEmailRequest',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailRequest.email', index=0,
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
  serialized_start=91,
  serialized_end=157,
)


_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILRESPONSE = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupByUserEmailResponse',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userLookup', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailResponse.userLookup', index=0,
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
  serialized_start=159,
  serialized_end=269,
)


_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDREQUEST = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupByUserIdRequest',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdRequest.id', index=0,
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
  serialized_start=271,
  serialized_end=331,
)


_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDRESPONSE = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupByUserIdResponse',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userLookup', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdResponse.userLookup', index=0,
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
  serialized_start=333,
  serialized_end=440,
)


_USERLOOKUPAPPSERVICE_USERLOOKUPSREQUEST = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupsRequest',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsRequest.order', index=2,
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
  serialized_start=442,
  serialized_end=564,
)


_USERLOOKUPAPPSERVICE_USERLOOKUPSRESPONSE = _descriptor.Descriptor(
  name='UserLookupAppService_userLookupsResponse',
  full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userLookups', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsResponse.userLookups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.user_lookup.UserLookupAppService_userLookupsResponse.totalItemCount', index=1,
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
  serialized_start=566,
  serialized_end=691,
)

_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILRESPONSE.fields_by_name['userLookup'].message_type = user__lookup__pb2._USERLOOKUP
_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDRESPONSE.fields_by_name['userLookup'].message_type = user__lookup__pb2._USERLOOKUP
_USERLOOKUPAPPSERVICE_USERLOOKUPSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_USERLOOKUPAPPSERVICE_USERLOOKUPSRESPONSE.fields_by_name['userLookups'].message_type = user__lookup__pb2._USERLOOKUP
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupByUserEmailRequest'] = _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILREQUEST
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupByUserEmailResponse'] = _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILRESPONSE
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupByUserIdRequest'] = _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDREQUEST
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupByUserIdResponse'] = _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDRESPONSE
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupsRequest'] = _USERLOOKUPAPPSERVICE_USERLOOKUPSREQUEST
DESCRIPTOR.message_types_by_name['UserLookupAppService_userLookupsResponse'] = _USERLOOKUPAPPSERVICE_USERLOOKUPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserLookupAppService_userLookupByUserEmailRequest = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupByUserEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILREQUEST,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailRequest)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupByUserEmailRequest)

UserLookupAppService_userLookupByUserEmailResponse = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupByUserEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILRESPONSE,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupByUserEmailResponse)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupByUserEmailResponse)

UserLookupAppService_userLookupByUserIdRequest = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupByUserIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDREQUEST,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdRequest)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupByUserIdRequest)

UserLookupAppService_userLookupByUserIdResponse = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupByUserIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDRESPONSE,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupByUserIdResponse)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupByUserIdResponse)

UserLookupAppService_userLookupsRequest = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPSREQUEST,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupsRequest)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupsRequest)

UserLookupAppService_userLookupsResponse = _reflection.GeneratedProtocolMessageType('UserLookupAppService_userLookupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLOOKUPAPPSERVICE_USERLOOKUPSRESPONSE,
  '__module__' : 'user_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.user_lookup.UserLookupAppService_userLookupsResponse)
  })
_sym_db.RegisterMessage(UserLookupAppService_userLookupsResponse)



_USERLOOKUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='UserLookupAppService',
  full_name='cafm.project.user_lookup.UserLookupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=694,
  serialized_end=1226,
  methods=[
  _descriptor.MethodDescriptor(
    name='userLookupByUserEmail',
    full_name='cafm.project.user_lookup.UserLookupAppService.userLookupByUserEmail',
    index=0,
    containing_service=None,
    input_type=_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILREQUEST,
    output_type=_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSEREMAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userLookupByUserId',
    full_name='cafm.project.user_lookup.UserLookupAppService.userLookupByUserId',
    index=1,
    containing_service=None,
    input_type=_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDREQUEST,
    output_type=_USERLOOKUPAPPSERVICE_USERLOOKUPBYUSERIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='userLookups',
    full_name='cafm.project.user_lookup.UserLookupAppService.userLookups',
    index=2,
    containing_service=None,
    input_type=_USERLOOKUPAPPSERVICE_USERLOOKUPSREQUEST,
    output_type=_USERLOOKUPAPPSERVICE_USERLOOKUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERLOOKUPAPPSERVICE)

DESCRIPTOR.services_by_name['UserLookupAppService'] = _USERLOOKUPAPPSERVICE

# @@protoc_insertion_point(module_scope)
