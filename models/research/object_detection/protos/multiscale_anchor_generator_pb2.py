# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/multiscale_anchor_generator.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'object_detection/protos/multiscale_anchor_generator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9object_detection/protos/multiscale_anchor_generator.proto\x12\x17object_detection.protos\"\xba\x01\n\x19MultiscaleAnchorGenerator\x12\x14\n\tmin_level\x18\x01 \x01(\x05:\x01\x33\x12\x14\n\tmax_level\x18\x02 \x01(\x05:\x01\x37\x12\x17\n\x0c\x61nchor_scale\x18\x03 \x01(\x02:\x01\x34\x12\x15\n\raspect_ratios\x18\x04 \x03(\x02\x12\x1c\n\x11scales_per_octave\x18\x05 \x01(\x05:\x01\x32\x12#\n\x15normalize_coordinates\x18\x06 \x01(\x08:\x04true')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.multiscale_anchor_generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MULTISCALEANCHORGENERATOR']._serialized_start=87
  _globals['_MULTISCALEANCHORGENERATOR']._serialized_end=273
# @@protoc_insertion_point(module_scope)
