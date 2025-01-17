# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/audio/time_series_framer_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/audio/time_series_framer_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n?mediapipe/calculators/audio/time_series_framer_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xc5\x03\n!TimeSeriesFramerCalculatorOptions\x12\x1e\n\x16\x66rame_duration_seconds\x18\x01 \x01(\x01\x12 \n\x15\x66rame_overlap_seconds\x18\x02 \x01(\x01:\x01\x30\x12/\n emulate_fractional_frame_overlap\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x10pad_final_packet\x18\x03 \x01(\x08:\x04true\x12Z\n\x0fwindow_function\x18\x04 \x01(\x0e\x32;.mediapipe.TimeSeriesFramerCalculatorOptions.WindowFunction:\x04NONE\x12\"\n\x13use_local_timestamp\x18\x06 \x01(\x08:\x05\x66\x61lse\"1\n\x0eWindowFunction\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07HAMMING\x10\x01\x12\x08\n\x04HANN\x10\x02\x32Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc5\xa7\x92\x18 \x01(\x0b\x32,.mediapipe.TimeSeriesFramerCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TIMESERIESFRAMERCALCULATOROPTIONS_WINDOWFUNCTION = _descriptor.EnumDescriptor(
  name='WindowFunction',
  full_name='mediapipe.TimeSeriesFramerCalculatorOptions.WindowFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAMMING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HANN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=429,
  serialized_end=478,
)
_sym_db.RegisterEnumDescriptor(_TIMESERIESFRAMERCALCULATOROPTIONS_WINDOWFUNCTION)


_TIMESERIESFRAMERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TimeSeriesFramerCalculatorOptions',
  full_name='mediapipe.TimeSeriesFramerCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_duration_seconds', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.frame_duration_seconds', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_overlap_seconds', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.frame_overlap_seconds', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emulate_fractional_frame_overlap', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.emulate_fractional_frame_overlap', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pad_final_packet', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.pad_final_packet', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='window_function', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.window_function', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_local_timestamp', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.use_local_timestamp', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TimeSeriesFramerCalculatorOptions.ext', index=0,
      number=50631621, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _TIMESERIESFRAMERCALCULATOROPTIONS_WINDOWFUNCTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=570,
)

_TIMESERIESFRAMERCALCULATOROPTIONS.fields_by_name['window_function'].enum_type = _TIMESERIESFRAMERCALCULATOROPTIONS_WINDOWFUNCTION
_TIMESERIESFRAMERCALCULATOROPTIONS_WINDOWFUNCTION.containing_type = _TIMESERIESFRAMERCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['TimeSeriesFramerCalculatorOptions'] = _TIMESERIESFRAMERCALCULATOROPTIONS

TimeSeriesFramerCalculatorOptions = _reflection.GeneratedProtocolMessageType('TimeSeriesFramerCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _TIMESERIESFRAMERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.audio.time_series_framer_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TimeSeriesFramerCalculatorOptions)
  ))
_sym_db.RegisterMessage(TimeSeriesFramerCalculatorOptions)

_TIMESERIESFRAMERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TIMESERIESFRAMERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TIMESERIESFRAMERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
