# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Alert.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreamlit/proto/Alert.proto\"\x87\x01\n\x05\x41lert\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x1d\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\r.Alert.Format\x12\x0c\n\x04icon\x18\x03 \x01(\t\"C\n\x06\x46ormat\x12\n\n\x06UNUSED\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x62\x06proto3')



_ALERT = DESCRIPTOR.message_types_by_name['Alert']
_ALERT_FORMAT = _ALERT.enum_types_by_name['Format']
Alert = _reflection.GeneratedProtocolMessageType('Alert', (_message.Message,), {
  'DESCRIPTOR' : _ALERT,
  '__module__' : 'streamlit.proto.Alert_pb2'
  # @@protoc_insertion_point(class_scope:Alert)
  })
_sym_db.RegisterMessage(Alert)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALERT._serialized_start=32
  _ALERT._serialized_end=167
  _ALERT_FORMAT._serialized_start=100
  _ALERT_FORMAT._serialized_end=167
# @@protoc_insertion_point(module_scope)
