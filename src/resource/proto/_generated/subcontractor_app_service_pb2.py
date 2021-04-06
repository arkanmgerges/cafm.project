# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subcontractor_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import subcontractor_pb2 as subcontractor__pb2
import order_pb2 as order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='subcontractor_app_service.proto',
  package='cafm.project.subcontractor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fsubcontractor_app_service.proto\x12\x1a\x63\x61\x66m.project.subcontractor\x1a\x13subcontractor.proto\x1a\x0border.proto\"=\n/SubcontractorppService_subcontractorByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"t\n0SubcontractorppService_subcontractorByIdResponse\x12@\n\rsubcontractor\x18\x01 \x01(\x0b\x32).cafm.project.subcontractor.Subcontractor\"\x80\x01\n-SubcontractorAppService_subcontractorsRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12\'\n\x05order\x18\x03 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x86\x01\n.SubcontractorAppService_subcontractorsResponse\x12\x41\n\x0esubcontractors\x18\x01 \x03(\x0b\x32).cafm.project.subcontractor.Subcontractor\x12\x11\n\titemCount\x18\x02 \x01(\x05\"\xa8\x01\n=SubcontractorAppService_subcontractorsByOrganizationIdRequest\x12\x16\n\x0eorganizationId\x18\x01 \x01(\t\x12\x12\n\nresultFrom\x18\x02 \x01(\x05\x12\x12\n\nresultSize\x18\x03 \x01(\x05\x12\'\n\x05order\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\"\x96\x01\n>SubcontractorAppService_subcontractorsByOrganizationIdResponse\x12\x41\n\x0esubcontractors\x18\x01 \x03(\x0b\x32).cafm.project.subcontractor.Subcontractor\x12\x11\n\titemCount\x18\x02 \x01(\x05\"&\n$SubcontractorAppService_newIdRequest\"3\n%SubcontractorAppService_newIdResponse\x12\n\n\x02id\x18\x01 \x01(\t2\xe5\x05\n\x17SubcontractorAppService\x12\xd9\x01\n\x1esubcontractorsByOrganizationId\x12Y.cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest\x1aZ.cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdResponse\"\x00\x12\xb0\x01\n\x11subcontractorById\x12K.cafm.project.subcontractor.SubcontractorppService_subcontractorByIdRequest\x1aL.cafm.project.subcontractor.SubcontractorppService_subcontractorByIdResponse\"\x00\x12\xa9\x01\n\x0esubcontractors\x12I.cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest\x1aJ.cafm.project.subcontractor.SubcontractorAppService_subcontractorsResponse\"\x00\x12\x8e\x01\n\x05newId\x12@.cafm.project.subcontractor.SubcontractorAppService_newIdRequest\x1a\x41.cafm.project.subcontractor.SubcontractorAppService_newIdResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[subcontractor__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,])




_SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDREQUEST = _descriptor.Descriptor(
  name='SubcontractorppService_subcontractorByIdRequest',
  full_name='cafm.project.subcontractor.SubcontractorppService_subcontractorByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.subcontractor.SubcontractorppService_subcontractorByIdRequest.id', index=0,
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
  serialized_start=97,
  serialized_end=158,
)


_SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDRESPONSE = _descriptor.Descriptor(
  name='SubcontractorppService_subcontractorByIdResponse',
  full_name='cafm.project.subcontractor.SubcontractorppService_subcontractorByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcontractor', full_name='cafm.project.subcontractor.SubcontractorppService_subcontractorByIdResponse.subcontractor', index=0,
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
  serialized_start=160,
  serialized_end=276,
)


_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSREQUEST = _descriptor.Descriptor(
  name='SubcontractorAppService_subcontractorsRequest',
  full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest.order', index=2,
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
  serialized_start=279,
  serialized_end=407,
)


_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSRESPONSE = _descriptor.Descriptor(
  name='SubcontractorAppService_subcontractorsResponse',
  full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcontractors', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsResponse.subcontractors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsResponse.itemCount', index=1,
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
  serialized_start=410,
  serialized_end=544,
)


_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDREQUEST = _descriptor.Descriptor(
  name='SubcontractorAppService_subcontractorsByOrganizationIdRequest',
  full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizationId', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest.organizationId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest.resultFrom', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest.resultSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest.order', index=3,
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
  serialized_start=547,
  serialized_end=715,
)


_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDRESPONSE = _descriptor.Descriptor(
  name='SubcontractorAppService_subcontractorsByOrganizationIdResponse',
  full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcontractors', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdResponse.subcontractors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemCount', full_name='cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdResponse.itemCount', index=1,
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
  serialized_start=718,
  serialized_end=868,
)


_SUBCONTRACTORAPPSERVICE_NEWIDREQUEST = _descriptor.Descriptor(
  name='SubcontractorAppService_newIdRequest',
  full_name='cafm.project.subcontractor.SubcontractorAppService_newIdRequest',
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
  serialized_start=870,
  serialized_end=908,
)


_SUBCONTRACTORAPPSERVICE_NEWIDRESPONSE = _descriptor.Descriptor(
  name='SubcontractorAppService_newIdResponse',
  full_name='cafm.project.subcontractor.SubcontractorAppService_newIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.subcontractor.SubcontractorAppService_newIdResponse.id', index=0,
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
  serialized_start=910,
  serialized_end=961,
)

_SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDRESPONSE.fields_by_name['subcontractor'].message_type = subcontractor__pb2._SUBCONTRACTOR
_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSRESPONSE.fields_by_name['subcontractors'].message_type = subcontractor__pb2._SUBCONTRACTOR
_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDREQUEST.fields_by_name['order'].message_type = order__pb2._ORDER
_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDRESPONSE.fields_by_name['subcontractors'].message_type = subcontractor__pb2._SUBCONTRACTOR
DESCRIPTOR.message_types_by_name['SubcontractorppService_subcontractorByIdRequest'] = _SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDREQUEST
DESCRIPTOR.message_types_by_name['SubcontractorppService_subcontractorByIdResponse'] = _SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDRESPONSE
DESCRIPTOR.message_types_by_name['SubcontractorAppService_subcontractorsRequest'] = _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSREQUEST
DESCRIPTOR.message_types_by_name['SubcontractorAppService_subcontractorsResponse'] = _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSRESPONSE
DESCRIPTOR.message_types_by_name['SubcontractorAppService_subcontractorsByOrganizationIdRequest'] = _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDREQUEST
DESCRIPTOR.message_types_by_name['SubcontractorAppService_subcontractorsByOrganizationIdResponse'] = _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDRESPONSE
DESCRIPTOR.message_types_by_name['SubcontractorAppService_newIdRequest'] = _SUBCONTRACTORAPPSERVICE_NEWIDREQUEST
DESCRIPTOR.message_types_by_name['SubcontractorAppService_newIdResponse'] = _SUBCONTRACTORAPPSERVICE_NEWIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubcontractorppService_subcontractorByIdRequest = _reflection.GeneratedProtocolMessageType('SubcontractorppService_subcontractorByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDREQUEST,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorppService_subcontractorByIdRequest)
  })
_sym_db.RegisterMessage(SubcontractorppService_subcontractorByIdRequest)

SubcontractorppService_subcontractorByIdResponse = _reflection.GeneratedProtocolMessageType('SubcontractorppService_subcontractorByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDRESPONSE,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorppService_subcontractorByIdResponse)
  })
_sym_db.RegisterMessage(SubcontractorppService_subcontractorByIdResponse)

SubcontractorAppService_subcontractorsRequest = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_subcontractorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSREQUEST,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_subcontractorsRequest)
  })
_sym_db.RegisterMessage(SubcontractorAppService_subcontractorsRequest)

SubcontractorAppService_subcontractorsResponse = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_subcontractorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSRESPONSE,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_subcontractorsResponse)
  })
_sym_db.RegisterMessage(SubcontractorAppService_subcontractorsResponse)

SubcontractorAppService_subcontractorsByOrganizationIdRequest = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_subcontractorsByOrganizationIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDREQUEST,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdRequest)
  })
_sym_db.RegisterMessage(SubcontractorAppService_subcontractorsByOrganizationIdRequest)

SubcontractorAppService_subcontractorsByOrganizationIdResponse = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_subcontractorsByOrganizationIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDRESPONSE,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_subcontractorsByOrganizationIdResponse)
  })
_sym_db.RegisterMessage(SubcontractorAppService_subcontractorsByOrganizationIdResponse)

SubcontractorAppService_newIdRequest = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_newIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_NEWIDREQUEST,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_newIdRequest)
  })
_sym_db.RegisterMessage(SubcontractorAppService_newIdRequest)

SubcontractorAppService_newIdResponse = _reflection.GeneratedProtocolMessageType('SubcontractorAppService_newIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORAPPSERVICE_NEWIDRESPONSE,
  '__module__' : 'subcontractor_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.subcontractor.SubcontractorAppService_newIdResponse)
  })
_sym_db.RegisterMessage(SubcontractorAppService_newIdResponse)



_SUBCONTRACTORAPPSERVICE = _descriptor.ServiceDescriptor(
  name='SubcontractorAppService',
  full_name='cafm.project.subcontractor.SubcontractorAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=964,
  serialized_end=1705,
  methods=[
  _descriptor.MethodDescriptor(
    name='subcontractorsByOrganizationId',
    full_name='cafm.project.subcontractor.SubcontractorAppService.subcontractorsByOrganizationId',
    index=0,
    containing_service=None,
    input_type=_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDREQUEST,
    output_type=_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSBYORGANIZATIONIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='subcontractorById',
    full_name='cafm.project.subcontractor.SubcontractorAppService.subcontractorById',
    index=1,
    containing_service=None,
    input_type=_SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDREQUEST,
    output_type=_SUBCONTRACTORPPSERVICE_SUBCONTRACTORBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='subcontractors',
    full_name='cafm.project.subcontractor.SubcontractorAppService.subcontractors',
    index=2,
    containing_service=None,
    input_type=_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSREQUEST,
    output_type=_SUBCONTRACTORAPPSERVICE_SUBCONTRACTORSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='newId',
    full_name='cafm.project.subcontractor.SubcontractorAppService.newId',
    index=3,
    containing_service=None,
    input_type=_SUBCONTRACTORAPPSERVICE_NEWIDREQUEST,
    output_type=_SUBCONTRACTORAPPSERVICE_NEWIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUBCONTRACTORAPPSERVICE)

DESCRIPTOR.services_by_name['SubcontractorAppService'] = _SUBCONTRACTORAPPSERVICE

# @@protoc_insertion_point(module_scope)
