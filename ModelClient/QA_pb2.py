# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QA.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08QA.proto\"+\n\tQARequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08question\x18\x02 \x01(\t\"\x1c\n\nQAResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2+\n\tQAService\x12\x1e\n\x03\x41sk\x12\n.QARequest\x1a\x0b.QAResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QA_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QAREQUEST._serialized_start=12
  _QAREQUEST._serialized_end=55
  _QARESPONSE._serialized_start=57
  _QARESPONSE._serialized_end=85
  _QASERVICE._serialized_start=87
  _QASERVICE._serialized_end=130
# @@protoc_insertion_point(module_scope)
