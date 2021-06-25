# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: standard_maintenance_procedure_operation_parameter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='standard_maintenance_procedure_operation_parameter.proto',
  package='cafm.project.standard_maintenance_procedure_operation_parameter',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8standard_maintenance_procedure_operation_parameter.proto\x12?cafm.project.standard_maintenance_procedure_operation_parameter\"\xb6\x01\n.StandardMaintenanceProcedureOperationParameter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07unit_id\x18\x03 \x01(\t\x12\x33\n+standard_maintenance_procedure_operation_id\x18\x04 \x01(\t\x12\x11\n\tmin_value\x18\x05 \x01(\t\x12\x11\n\tmax_value\x18\x06 \x01(\tb\x06proto3'
)




_STANDARDMAINTENANCEPROCEDUREOPERATIONPARAMETER = _descriptor.Descriptor(
  name='StandardMaintenanceProcedureOperationParameter',
  full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.unit_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='standard_maintenance_procedure_operation_id', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.standard_maintenance_procedure_operation_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.min_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter.max_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=126,
  serialized_end=308,
)

DESCRIPTOR.message_types_by_name['StandardMaintenanceProcedureOperationParameter'] = _STANDARDMAINTENANCEPROCEDUREOPERATIONPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StandardMaintenanceProcedureOperationParameter = _reflection.GeneratedProtocolMessageType('StandardMaintenanceProcedureOperationParameter', (_message.Message,), {
  'DESCRIPTOR' : _STANDARDMAINTENANCEPROCEDUREOPERATIONPARAMETER,
  '__module__' : 'standard_maintenance_procedure_operation_parameter_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameter)
  })
_sym_db.RegisterMessage(StandardMaintenanceProcedureOperationParameter)


# @@protoc_insertion_point(module_scope)
