# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/string_int_label_map.proto
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
    'object_detection/protos/string_int_label_map.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2object_detection/protos/string_int_label_map.proto\x12\x17object_detection.protos\"\xc1\x02\n\x15StringIntLabelMapItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12M\n\tkeypoints\x18\x04 \x03(\x0b\x32:.object_detection.protos.StringIntLabelMapItem.KeypointMap\x12\x14\n\x0c\x61ncestor_ids\x18\x05 \x03(\x05\x12\x16\n\x0e\x64\x65scendant_ids\x18\x06 \x03(\x05\x12\x39\n\tfrequency\x18\x07 \x01(\x0e\x32&.object_detection.protos.LVISFrequency\x12\x16\n\x0einstance_count\x18\x08 \x01(\x05\x1a(\n\x0bKeypointMap\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05label\x18\x02 \x01(\t\"Q\n\x11StringIntLabelMap\x12<\n\x04item\x18\x01 \x03(\x0b\x32..object_detection.protos.StringIntLabelMapItem*D\n\rLVISFrequency\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08\x46REQUENT\x10\x01\x12\n\n\x06\x43OMMON\x10\x02\x12\x08\n\x04RARE\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.string_int_label_map_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LVISFREQUENCY']._serialized_start=486
  _globals['_LVISFREQUENCY']._serialized_end=554
  _globals['_STRINGINTLABELMAPITEM']._serialized_start=80
  _globals['_STRINGINTLABELMAPITEM']._serialized_end=401
  _globals['_STRINGINTLABELMAPITEM_KEYPOINTMAP']._serialized_start=361
  _globals['_STRINGINTLABELMAPITEM_KEYPOINTMAP']._serialized_end=401
  _globals['_STRINGINTLABELMAP']._serialized_start=403
  _globals['_STRINGINTLABELMAP']._serialized_end=484
# @@protoc_insertion_point(module_scope)
