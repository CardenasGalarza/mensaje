# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Slider.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import LabelVisibilityMessage_pb2 as streamlit_dot_proto_dot_LabelVisibilityMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cstreamlit/proto/Slider.proto\x1a,streamlit/proto/LabelVisibilityMessage.proto\"\xea\x02\n\x06Slider\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x04 \x01(\t\x12#\n\tdata_type\x18\x05 \x01(\x0e\x32\x10.Slider.DataType\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x03(\x01\x12\x0b\n\x03min\x18\x07 \x01(\x01\x12\x0b\n\x03max\x18\x08 \x01(\x01\x12\x0c\n\x04step\x18\t \x01(\x01\x12\r\n\x05value\x18\n \x03(\x01\x12\x11\n\tset_value\x18\x0b \x01(\x08\x12\x0f\n\x07options\x18\r \x03(\t\x12\x0c\n\x04help\x18\x0e \x01(\t\x12\x10\n\x08\x64isabled\x18\x0f \x01(\x08\x12\x31\n\x10label_visibility\x18\x10 \x01(\x0b\x32\x17.LabelVisibilityMessage\"@\n\x08\x44\x61taType\x12\x07\n\x03INT\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\x0c\n\x08\x44\x41TETIME\x10\x02\x12\x08\n\x04\x44\x41TE\x10\x03\x12\x08\n\x04TIME\x10\x04\x62\x06proto3')



_SLIDER = DESCRIPTOR.message_types_by_name['Slider']
_SLIDER_DATATYPE = _SLIDER.enum_types_by_name['DataType']
Slider = _reflection.GeneratedProtocolMessageType('Slider', (_message.Message,), {
  'DESCRIPTOR' : _SLIDER,
  '__module__' : 'streamlit.proto.Slider_pb2'
  # @@protoc_insertion_point(class_scope:Slider)
  })
_sym_db.RegisterMessage(Slider)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SLIDER._serialized_start=79
  _SLIDER._serialized_end=441
  _SLIDER_DATATYPE._serialized_start=377
  _SLIDER_DATATYPE._serialized_end=441
# @@protoc_insertion_point(module_scope)
