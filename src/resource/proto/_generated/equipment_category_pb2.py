# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment_category.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="equipment_category.proto",
    package="cafm.project.equipment_category",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x18\x65quipment_category.proto\x12\x1f\x63\x61\x66m.project.equipment_category"-\n\x11\x45quipmentCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3',
)


_EQUIPMENTCATEGORY = _descriptor.Descriptor(
    name="EquipmentCategory",
    full_name="cafm.project.equipment_category.EquipmentCategory",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="cafm.project.equipment_category.EquipmentCategory.id",
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
            full_name="cafm.project.equipment_category.EquipmentCategory.name",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=61,
    serialized_end=106,
)

DESCRIPTOR.message_types_by_name["EquipmentCategory"] = _EQUIPMENTCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquipmentCategory = _reflection.GeneratedProtocolMessageType(
    "EquipmentCategory",
    (_message.Message,),
    {
        "DESCRIPTOR": _EQUIPMENTCATEGORY,
        "__module__": "equipment_category_pb2"
        # @@protoc_insertion_point(class_scope:cafm.project.equipment_category.EquipmentCategory)
    },
)
_sym_db.RegisterMessage(EquipmentCategory)


# @@protoc_insertion_point(module_scope)
