# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lookup/subcontractor/subcontractor_lookup_app_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lookup.subcontractor import subcontractor_pb2 as lookup_dot_subcontractor_dot_subcontractor__pb2
import order_pb2 as order__pb2
import filter_pb2 as filter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lookup/subcontractor/subcontractor_lookup_app_service.proto',
  package='cafm.project.lookup.subcontractor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;lookup/subcontractor/subcontractor_lookup_app_service.proto\x12!cafm.project.lookup.subcontractor\x1a(lookup/subcontractor/subcontractor.proto\x1a\x0border.proto\x1a\x0c\x66ilter.proto\"\xac\x01\n+SubcontractorLookupAppService_lookupRequest\x12\x12\n\nresultFrom\x18\x01 \x01(\x05\x12\x12\n\nresultSize\x18\x02 \x01(\x05\x12(\n\x06orders\x18\x04 \x03(\x0b\x32\x18.cafm.common.order.Order\x12+\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x1a.cafm.common.filter.Filter\"\x96\x01\n,SubcontractorLookupAppService_lookupResponse\x12N\n\x14subcontractorLookups\x18\x01 \x03(\x0b\x32\x30.cafm.project.lookup.subcontractor.Subcontractor\x12\x16\n\x0etotalItemCount\x18\x02 \x01(\x05\x32\xcd\x01\n\x1dSubcontractorLookupAppService\x12\xab\x01\n\x06lookup\x12N.cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest\x1aO.cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[lookup_dot_subcontractor_dot_subcontractor__pb2.DESCRIPTOR,order__pb2.DESCRIPTOR,filter__pb2.DESCRIPTOR,])




_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST = _descriptor.Descriptor(
  name='SubcontractorLookupAppService_lookupRequest',
  full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultFrom', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest.resultFrom', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultSize', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest.resultSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orders', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest.orders', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest.filters', index=3,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=168,
  serialized_end=340,
)


_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPRESPONSE = _descriptor.Descriptor(
  name='SubcontractorLookupAppService_lookupResponse',
  full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subcontractorLookups', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupResponse.subcontractorLookups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalItemCount', full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupResponse.totalItemCount', index=1,
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
  serialized_start=343,
  serialized_end=493,
)

_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['orders'].message_type = order__pb2._ORDER
_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST.fields_by_name['filters'].message_type = filter__pb2._FILTER
_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPRESPONSE.fields_by_name['subcontractorLookups'].message_type = lookup_dot_subcontractor_dot_subcontractor__pb2._SUBCONTRACTOR
DESCRIPTOR.message_types_by_name['SubcontractorLookupAppService_lookupRequest'] = _SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['SubcontractorLookupAppService_lookupResponse'] = _SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubcontractorLookupAppService_lookupRequest = _reflection.GeneratedProtocolMessageType('SubcontractorLookupAppService_lookupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST,
  '__module__' : 'lookup.subcontractor.subcontractor_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupRequest)
  })
_sym_db.RegisterMessage(SubcontractorLookupAppService_lookupRequest)

SubcontractorLookupAppService_lookupResponse = _reflection.GeneratedProtocolMessageType('SubcontractorLookupAppService_lookupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPRESPONSE,
  '__module__' : 'lookup.subcontractor.subcontractor_lookup_app_service_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.subcontractor.SubcontractorLookupAppService_lookupResponse)
  })
_sym_db.RegisterMessage(SubcontractorLookupAppService_lookupResponse)



_SUBCONTRACTORLOOKUPAPPSERVICE = _descriptor.ServiceDescriptor(
  name='SubcontractorLookupAppService',
  full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=496,
  serialized_end=701,
  methods=[
  _descriptor.MethodDescriptor(
    name='lookup',
    full_name='cafm.project.lookup.subcontractor.SubcontractorLookupAppService.lookup',
    index=0,
    containing_service=None,
    input_type=_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPREQUEST,
    output_type=_SUBCONTRACTORLOOKUPAPPSERVICE_LOOKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUBCONTRACTORLOOKUPAPPSERVICE)

DESCRIPTOR.services_by_name['SubcontractorLookupAppService'] = _SUBCONTRACTORLOOKUPAPPSERVICE

# @@protoc_insertion_point(module_scope)