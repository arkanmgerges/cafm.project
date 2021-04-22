# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maintenance_procedure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="maintenance_procedure.proto",
    package="cafm.project.maintenance_procedure",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bmaintenance_procedure.proto\x12"cafm.project.maintenance_procedure"\xa3\x01\n\x14MaintenanceProcedure\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\tfrequency\x18\x04 \x01(\t\x12\x11\n\tstartDate\x18\x05 \x01(\x05\x12\x17\n\x0fsubcontractorId\x18\x06 \x01(\t\x12\x13\n\x0b\x65quipmentId\x18\x07 \x01(\t\x12\x0f\n\x07subType\x18\x08 \x01(\tb\x06proto3',
)


_MAINTENANCEPROCEDURE = _descriptor.Descriptor(
    name="MaintenanceProcedure",
    full_name="cafm.project.maintenance_procedure.MaintenanceProcedure",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.type",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="frequency",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.frequency",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="startDate",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.startDate",
            index=4,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subcontractorId",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.subcontractorId",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="equipmentId",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.equipmentId",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subType",
            full_name="cafm.project.maintenance_procedure.MaintenanceProcedure.subType",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=68,
    serialized_end=231,
)

DESCRIPTOR.message_types_by_name["MaintenanceProcedure"] = _MAINTENANCEPROCEDURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaintenanceProcedure = _reflection.GeneratedProtocolMessageType(
    "MaintenanceProcedure",
    (_message.Message,),
    {
        "DESCRIPTOR": _MAINTENANCEPROCEDURE,
        "__module__": "maintenance_procedure_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.maintenance_procedure.MaintenanceProcedure)
    },
)
_sym_db.RegisterMessage(MaintenanceProcedure)


# @@protoc_insertion_point(module_scope)
