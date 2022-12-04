# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/openmetrics_data_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,streamlit/proto/openmetrics_data_model.proto\x12\x0bopenmetrics\x1a\x1fgoogle/protobuf/timestamp.proto\"?\n\tMetricSet\x12\x32\n\x0fmetric_families\x18\x01 \x03(\x0b\x32\x19.openmetrics.MetricFamily\"\x85\x01\n\x0cMetricFamily\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x17.openmetrics.MetricType\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x0c\n\x04help\x18\x04 \x01(\t\x12$\n\x07metrics\x18\x05 \x03(\x0b\x32\x13.openmetrics.Metric\"]\n\x06Metric\x12\"\n\x06labels\x18\x01 \x03(\x0b\x32\x12.openmetrics.Label\x12/\n\rmetric_points\x18\x02 \x03(\x0b\x32\x18.openmetrics.MetricPoint\"$\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xae\x03\n\x0bMetricPoint\x12\x32\n\runknown_value\x18\x01 \x01(\x0b\x32\x19.openmetrics.UnknownValueH\x00\x12.\n\x0bgauge_value\x18\x02 \x01(\x0b\x32\x17.openmetrics.GaugeValueH\x00\x12\x32\n\rcounter_value\x18\x03 \x01(\x0b\x32\x19.openmetrics.CounterValueH\x00\x12\x36\n\x0fhistogram_value\x18\x04 \x01(\x0b\x32\x1b.openmetrics.HistogramValueH\x00\x12\x35\n\x0fstate_set_value\x18\x05 \x01(\x0b\x32\x1a.openmetrics.StateSetValueH\x00\x12,\n\ninfo_value\x18\x06 \x01(\x0b\x32\x16.openmetrics.InfoValueH\x00\x12\x32\n\rsummary_value\x18\x07 \x01(\x0b\x32\x19.openmetrics.SummaryValueH\x00\x12-\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x07\n\x05value\"D\n\x0cUnknownValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x42\x07\n\x05value\"B\n\nGaugeValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x42\x07\n\x05value\"\x9a\x01\n\x0c\x43ounterValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x04H\x00\x12+\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x08\x65xemplar\x18\x04 \x01(\x0b\x32\x15.openmetrics.ExemplarB\x07\n\x05total\"\x8c\x02\n\x0eHistogramValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\x12+\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x07\x62uckets\x18\x05 \x03(\x0b\x32\".openmetrics.HistogramValue.Bucket\x1aU\n\x06\x42ucket\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x01\x12\'\n\x08\x65xemplar\x18\x03 \x01(\x0b\x32\x15.openmetrics.ExemplarB\x05\n\x03sum\"k\n\x08\x45xemplar\x12\r\n\x05value\x18\x01 \x01(\x01\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x05label\x18\x03 \x03(\x0b\x32\x12.openmetrics.Label\"i\n\rStateSetValue\x12\x30\n\x06states\x18\x01 \x03(\x0b\x32 .openmetrics.StateSetValue.State\x1a&\n\x05State\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0c\n\x04name\x18\x02 \x01(\t\"-\n\tInfoValue\x12 \n\x04info\x18\x01 \x03(\x0b\x32\x12.openmetrics.Label\"\xe1\x01\n\x0cSummaryValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\x12+\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x08quantile\x18\x05 \x03(\x0b\x32\".openmetrics.SummaryValue.Quantile\x1a+\n\x08Quantile\x12\x10\n\x08quantile\x18\x01 \x01(\x01\x12\r\n\x05value\x18\x02 \x01(\x01\x42\x05\n\x03sum*{\n\nMetricType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\x0b\n\x07\x43OUNTER\x10\x02\x12\r\n\tSTATE_SET\x10\x03\x12\x08\n\x04INFO\x10\x04\x12\r\n\tHISTOGRAM\x10\x05\x12\x13\n\x0fGAUGE_HISTOGRAM\x10\x06\x12\x0b\n\x07SUMMARY\x10\x07\x62\x06proto3')

_METRICTYPE = DESCRIPTOR.enum_types_by_name['MetricType']
MetricType = enum_type_wrapper.EnumTypeWrapper(_METRICTYPE)
UNKNOWN = 0
GAUGE = 1
COUNTER = 2
STATE_SET = 3
INFO = 4
HISTOGRAM = 5
GAUGE_HISTOGRAM = 6
SUMMARY = 7


_METRICSET = DESCRIPTOR.message_types_by_name['MetricSet']
_METRICFAMILY = DESCRIPTOR.message_types_by_name['MetricFamily']
_METRIC = DESCRIPTOR.message_types_by_name['Metric']
_LABEL = DESCRIPTOR.message_types_by_name['Label']
_METRICPOINT = DESCRIPTOR.message_types_by_name['MetricPoint']
_UNKNOWNVALUE = DESCRIPTOR.message_types_by_name['UnknownValue']
_GAUGEVALUE = DESCRIPTOR.message_types_by_name['GaugeValue']
_COUNTERVALUE = DESCRIPTOR.message_types_by_name['CounterValue']
_HISTOGRAMVALUE = DESCRIPTOR.message_types_by_name['HistogramValue']
_HISTOGRAMVALUE_BUCKET = _HISTOGRAMVALUE.nested_types_by_name['Bucket']
_EXEMPLAR = DESCRIPTOR.message_types_by_name['Exemplar']
_STATESETVALUE = DESCRIPTOR.message_types_by_name['StateSetValue']
_STATESETVALUE_STATE = _STATESETVALUE.nested_types_by_name['State']
_INFOVALUE = DESCRIPTOR.message_types_by_name['InfoValue']
_SUMMARYVALUE = DESCRIPTOR.message_types_by_name['SummaryValue']
_SUMMARYVALUE_QUANTILE = _SUMMARYVALUE.nested_types_by_name['Quantile']
MetricSet = _reflection.GeneratedProtocolMessageType('MetricSet', (_message.Message,), {
  'DESCRIPTOR' : _METRICSET,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.MetricSet)
  })
_sym_db.RegisterMessage(MetricSet)

MetricFamily = _reflection.GeneratedProtocolMessageType('MetricFamily', (_message.Message,), {
  'DESCRIPTOR' : _METRICFAMILY,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.MetricFamily)
  })
_sym_db.RegisterMessage(MetricFamily)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.Metric)
  })
_sym_db.RegisterMessage(Metric)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.Label)
  })
_sym_db.RegisterMessage(Label)

MetricPoint = _reflection.GeneratedProtocolMessageType('MetricPoint', (_message.Message,), {
  'DESCRIPTOR' : _METRICPOINT,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.MetricPoint)
  })
_sym_db.RegisterMessage(MetricPoint)

UnknownValue = _reflection.GeneratedProtocolMessageType('UnknownValue', (_message.Message,), {
  'DESCRIPTOR' : _UNKNOWNVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.UnknownValue)
  })
_sym_db.RegisterMessage(UnknownValue)

GaugeValue = _reflection.GeneratedProtocolMessageType('GaugeValue', (_message.Message,), {
  'DESCRIPTOR' : _GAUGEVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.GaugeValue)
  })
_sym_db.RegisterMessage(GaugeValue)

CounterValue = _reflection.GeneratedProtocolMessageType('CounterValue', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.CounterValue)
  })
_sym_db.RegisterMessage(CounterValue)

HistogramValue = _reflection.GeneratedProtocolMessageType('HistogramValue', (_message.Message,), {

  'Bucket' : _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), {
    'DESCRIPTOR' : _HISTOGRAMVALUE_BUCKET,
    '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
    # @@protoc_insertion_point(class_scope:openmetrics.HistogramValue.Bucket)
    })
  ,
  'DESCRIPTOR' : _HISTOGRAMVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.HistogramValue)
  })
_sym_db.RegisterMessage(HistogramValue)
_sym_db.RegisterMessage(HistogramValue.Bucket)

Exemplar = _reflection.GeneratedProtocolMessageType('Exemplar', (_message.Message,), {
  'DESCRIPTOR' : _EXEMPLAR,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.Exemplar)
  })
_sym_db.RegisterMessage(Exemplar)

StateSetValue = _reflection.GeneratedProtocolMessageType('StateSetValue', (_message.Message,), {

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR' : _STATESETVALUE_STATE,
    '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
    # @@protoc_insertion_point(class_scope:openmetrics.StateSetValue.State)
    })
  ,
  'DESCRIPTOR' : _STATESETVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.StateSetValue)
  })
_sym_db.RegisterMessage(StateSetValue)
_sym_db.RegisterMessage(StateSetValue.State)

InfoValue = _reflection.GeneratedProtocolMessageType('InfoValue', (_message.Message,), {
  'DESCRIPTOR' : _INFOVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.InfoValue)
  })
_sym_db.RegisterMessage(InfoValue)

SummaryValue = _reflection.GeneratedProtocolMessageType('SummaryValue', (_message.Message,), {

  'Quantile' : _reflection.GeneratedProtocolMessageType('Quantile', (_message.Message,), {
    'DESCRIPTOR' : _SUMMARYVALUE_QUANTILE,
    '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
    # @@protoc_insertion_point(class_scope:openmetrics.SummaryValue.Quantile)
    })
  ,
  'DESCRIPTOR' : _SUMMARYVALUE,
  '__module__' : 'streamlit.proto.openmetrics_data_model_pb2'
  # @@protoc_insertion_point(class_scope:openmetrics.SummaryValue)
  })
_sym_db.RegisterMessage(SummaryValue)
_sym_db.RegisterMessage(SummaryValue.Quantile)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _METRICTYPE._serialized_start=1918
  _METRICTYPE._serialized_end=2041
  _METRICSET._serialized_start=94
  _METRICSET._serialized_end=157
  _METRICFAMILY._serialized_start=160
  _METRICFAMILY._serialized_end=293
  _METRIC._serialized_start=295
  _METRIC._serialized_end=388
  _LABEL._serialized_start=390
  _LABEL._serialized_end=426
  _METRICPOINT._serialized_start=429
  _METRICPOINT._serialized_end=859
  _UNKNOWNVALUE._serialized_start=861
  _UNKNOWNVALUE._serialized_end=929
  _GAUGEVALUE._serialized_start=931
  _GAUGEVALUE._serialized_end=997
  _COUNTERVALUE._serialized_start=1000
  _COUNTERVALUE._serialized_end=1154
  _HISTOGRAMVALUE._serialized_start=1157
  _HISTOGRAMVALUE._serialized_end=1425
  _HISTOGRAMVALUE_BUCKET._serialized_start=1333
  _HISTOGRAMVALUE_BUCKET._serialized_end=1418
  _EXEMPLAR._serialized_start=1427
  _EXEMPLAR._serialized_end=1534
  _STATESETVALUE._serialized_start=1536
  _STATESETVALUE._serialized_end=1641
  _STATESETVALUE_STATE._serialized_start=1603
  _STATESETVALUE_STATE._serialized_end=1641
  _INFOVALUE._serialized_start=1643
  _INFOVALUE._serialized_end=1688
  _SUMMARYVALUE._serialized_start=1691
  _SUMMARYVALUE._serialized_end=1916
  _SUMMARYVALUE_QUANTILE._serialized_start=1866
  _SUMMARYVALUE_QUANTILE._serialized_end=1909
# @@protoc_insertion_point(module_scope)
