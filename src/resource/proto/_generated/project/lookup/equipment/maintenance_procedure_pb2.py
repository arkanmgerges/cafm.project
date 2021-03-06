# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project/lookup/equipment/maintenance_procedure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from project.lookup.equipment import maintenance_procedure_operation_pb2 as project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__pb2
from project.lookup.equipment import subcontractor_pb2 as project_dot_lookup_dot_equipment_dot_subcontractor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='project/lookup/equipment/maintenance_procedure.proto',
  package='cafm.project.lookup.equipment',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4project/lookup/equipment/maintenance_procedure.proto\x12\x1d\x63\x61\x66m.project.lookup.equipment\x1a>project/lookup/equipment/maintenance_procedure_operation.proto\x1a,project/lookup/equipment/subcontractor.proto\"\xa4\x02\n\x14MaintenanceProcedure\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\tfrequency\x18\x04 \x01(\t\x12\x12\n\nstart_date\x18\x05 \x01(\x05\x12\x10\n\x08sub_type\x18\x06 \x01(\t\x12\x66\n maintenance_procedure_operations\x18\x07 \x03(\x0b\x32<.cafm.project.lookup.equipment.MaintenanceProcedureOperation\x12\x43\n\rsubcontractor\x18\x08 \x01(\x0b\x32,.cafm.project.lookup.equipment.Subcontractorb\x06proto3'
  ,
  dependencies=[project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__pb2.DESCRIPTOR,project_dot_lookup_dot_equipment_dot_subcontractor__pb2.DESCRIPTOR,])




_MAINTENANCEPROCEDURE = _descriptor.Descriptor(
  name='MaintenanceProcedure',
  full_name='cafm.project.lookup.equipment.MaintenanceProcedure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.frequency', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.start_date', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_type', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.sub_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maintenance_procedure_operations', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.maintenance_procedure_operations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subcontractor', full_name='cafm.project.lookup.equipment.MaintenanceProcedure.subcontractor', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=198,
  serialized_end=490,
)

_MAINTENANCEPROCEDURE.fields_by_name['maintenance_procedure_operations'].message_type = project_dot_lookup_dot_equipment_dot_maintenance__procedure__operation__pb2._MAINTENANCEPROCEDUREOPERATION
_MAINTENANCEPROCEDURE.fields_by_name['subcontractor'].message_type = project_dot_lookup_dot_equipment_dot_subcontractor__pb2._SUBCONTRACTOR
DESCRIPTOR.message_types_by_name['MaintenanceProcedure'] = _MAINTENANCEPROCEDURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedure = _reflection.GeneratedProtocolMessageType('MaintenanceProcedure', (_message.Message,), {
  'DESCRIPTOR' : _MAINTENANCEPROCEDURE,
  '__module__' : 'project.lookup.equipment.maintenance_procedure_pb2'
  # @@protoc_insertion_point(class_scope:cafm.project.lookup.equipment.MaintenanceProcedure)
  })
_sym_db.RegisterMessage(MaintenanceProcedure)


# @@protoc_insertion_point(module_scope)
