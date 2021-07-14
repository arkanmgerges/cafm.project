# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/city_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from identity import city_pb2 as identity_dot_city__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/city_app_service.proto',
  package='cafm.identity.country',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fidentity/city_app_service.proto\x12\x15\x63\x61\x66m.identity.country\x1a\x13identity/city.proto\x1a\x0border.proto\",\n\x1e\x43ityAppService_cityByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"L\n\x1f\x43ityAppService_cityByIdResponse\x12)\n\x04\x63ity\x18\x01 \x01(\x0b\x32\x1b.cafm.identity.country.City\"r\n\x1c\x43ityAppService_citiesRequest\x12\x13\n\x0bresult_from\x18\x01 \x01(\x05\x12\x13\n\x0bresult_size\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"f\n\x1d\x43ityAppService_citiesResponse\x12+\n\x06\x63ities\x18\x01 \x03(\x0b\x32\x1b.cafm.identity.country.City\x12\x18\n\x10total_item_count\x18\x02 \x01(\x05\x32\x86\x02\n\x0e\x43ityAppService\x12}\n\ncity_by_id\x12\x35.cafm.identity.country.CityAppService_cityByIdRequest\x1a\x36.cafm.identity.country.CityAppService_cityByIdResponse\"\x00\x12u\n\x06\x63ities\x12\x33.cafm.identity.country.CityAppService_citiesRequest\x1a\x34.cafm.identity.country.CityAppService_citiesResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[identity_dot_city__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_CITYAPPSERVICE_CITYBYIDREQUEST = _descriptor.Descriptor(
  name='CityAppService_cityByIdRequest',
  full_name='cafm.identity.country.CityAppService_cityByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.identity.country.CityAppService_cityByIdRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=92,
  serialized_end=136,
)


_CITYAPPSERVICE_CITYBYIDRESPONSE = _descriptor.Descriptor(
  name='CityAppService_cityByIdResponse',
  full_name='cafm.identity.country.CityAppService_cityByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='cafm.identity.country.CityAppService_cityByIdResponse.city', index=0,
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
  serialized_end=214,
)


_CITYAPPSERVICE_CITIESREQUEST = _descriptor.Descriptor(
  name='CityAppService_citiesRequest',
  full_name='cafm.identity.country.CityAppService_citiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_from', full_name='cafm.identity.country.CityAppService_citiesRequest.result_from', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_size', full_name='cafm.identity.country.CityAppService_citiesRequest.result_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.identity.country.CityAppService_citiesRequest.orders', index=2,
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
  serialized_start=216,
  serialized_end=330,
)


_CITYAPPSERVICE_CITIESRESPONSE = _descriptor.Descriptor(
  name='CityAppService_citiesResponse',
  full_name='cafm.identity.country.CityAppService_citiesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cities', full_name='cafm.identity.country.CityAppService_citiesResponse.cities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_item_count', full_name='cafm.identity.country.CityAppService_citiesResponse.total_item_count', index=1,
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
  serialized_start=332,
  serialized_end=434,
)

_CITYAPPSERVICE_CITYBYIDRESPONSE.fields_by_name['city'].message_type = identity_dot_city__pb2._CITY
_CITYAPPSERVICE_CITIESREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_CITYAPPSERVICE_CITIESRESPONSE.fields_by_name['cities'].message_type = identity_dot_city__pb2._CITY
DESCRIPTOR.message_types_by_name['CityAppService_cityByIdRequest'] = _CITYAPPSERVICE_CITYBYIDREQUEST
DESCRIPTOR.message_types_by_name['CityAppService_cityByIdResponse'] = _CITYAPPSERVICE_CITYBYIDRESPONSE
DESCRIPTOR.message_types_by_name['CityAppService_citiesRequest'] = _CITYAPPSERVICE_CITIESREQUEST
DESCRIPTOR.message_types_by_name['CityAppService_citiesResponse'] = _CITYAPPSERVICE_CITIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CityAppService_cityByIdRequest = _reflection.GeneratedProtocolMessageType('CityAppService_cityByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _CITYAPPSERVICE_CITYBYIDREQUEST,
  '__module__' : 'identity.city_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.country.CityAppService_cityByIdRequest)
  })
_sym_db.RegisterMessage(CityAppService_cityByIdRequest)

CityAppService_cityByIdResponse = _reflection.GeneratedProtocolMessageType('CityAppService_cityByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _CITYAPPSERVICE_CITYBYIDRESPONSE,
  '__module__' : 'identity.city_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.country.CityAppService_cityByIdResponse)
  })
_sym_db.RegisterMessage(CityAppService_cityByIdResponse)

CityAppService_citiesRequest = _reflection.GeneratedProtocolMessageType('CityAppService_citiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _CITYAPPSERVICE_CITIESREQUEST,
  '__module__' : 'identity.city_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.country.CityAppService_citiesRequest)
  })
_sym_db.RegisterMessage(CityAppService_citiesRequest)

CityAppService_citiesResponse = _reflection.GeneratedProtocolMessageType('CityAppService_citiesResponse', (_message.Message,), {
  'DESCRIPTOR' : _CITYAPPSERVICE_CITIESRESPONSE,
  '__module__' : 'identity.city_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.identity.country.CityAppService_citiesResponse)
  })
_sym_db.RegisterMessage(CityAppService_citiesResponse)



_CITYAPPSERVICE = _descriptor.ServiceDescriptor(
  name='CityAppService',
  full_name='cafm.identity.country.CityAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=437,
  serialized_end=699,
  methods=[
  _descriptor.MethodDescriptor(
    name='city_by_id',
    full_name='cafm.identity.country.CityAppService.city_by_id',
    index=0,
    containing_service=None,
    input_type=_CITYAPPSERVICE_CITYBYIDREQUEST,
    output_type=_CITYAPPSERVICE_CITYBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='cities',
    full_name='cafm.identity.country.CityAppService.cities',
    index=1,
    containing_service=None,
    input_type=_CITYAPPSERVICE_CITIESREQUEST,
    output_type=_CITYAPPSERVICE_CITIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CITYAPPSERVICE)

DESCRIPTOR.services_by_name['CityAppService'] = _CITYAPPSERVICE

# @@protoc_insertion_point(module_scope)