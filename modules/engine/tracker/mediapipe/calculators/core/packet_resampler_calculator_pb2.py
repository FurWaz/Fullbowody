# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/packet_resampler_calculator.proto

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
  name='mediapipe/calculators/core/packet_resampler_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n<mediapipe/calculators/core/packet_resampler_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x89\x04\n PacketResamplerCalculatorOptions\x12\x16\n\nframe_rate\x18\x01 \x01(\x01:\x02-1\x12U\n\routput_header\x18\x02 \x01(\x0e\x32\x38.mediapipe.PacketResamplerCalculatorOptions.OutputHeader:\x04NONE\x12\x1f\n\x11\x66lush_last_packet\x18\x03 \x01(\x08:\x04true\x12\x0e\n\x06jitter\x18\x04 \x01(\x01\x12%\n\x16jitter_with_reflection\x18\t \x01(\x08:\x05\x66\x61lse\x12$\n\x15reproducible_sampling\x18\n \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0e\x62\x61se_timestamp\x18\x05 \x01(\x03\x12\x12\n\nstart_time\x18\x06 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x03\x12\x1b\n\x0cround_limits\x18\x08 \x01(\x08:\x05\x66\x61lse\"B\n\x0cOutputHeader\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bPASS_HEADER\x10\x01\x12\x17\n\x13UPDATE_VIDEO_HEADER\x10\x02\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe4\xde\xd3- \x01(\x0b\x32+.mediapipe.PacketResamplerCalculatorOptionsB\x0c\xa2\x02\tMediaPipe')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER = _descriptor.EnumDescriptor(
  name='OutputHeader',
  full_name='mediapipe.PacketResamplerCalculatorOptions.OutputHeader',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASS_HEADER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_VIDEO_HEADER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=478,
  serialized_end=544,
)
_sym_db.RegisterEnumDescriptor(_PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER)


_PACKETRESAMPLERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='PacketResamplerCalculatorOptions',
  full_name='mediapipe.PacketResamplerCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_rate', full_name='mediapipe.PacketResamplerCalculatorOptions.frame_rate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_header', full_name='mediapipe.PacketResamplerCalculatorOptions.output_header', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flush_last_packet', full_name='mediapipe.PacketResamplerCalculatorOptions.flush_last_packet', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jitter', full_name='mediapipe.PacketResamplerCalculatorOptions.jitter', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jitter_with_reflection', full_name='mediapipe.PacketResamplerCalculatorOptions.jitter_with_reflection', index=4,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reproducible_sampling', full_name='mediapipe.PacketResamplerCalculatorOptions.reproducible_sampling', index=5,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_timestamp', full_name='mediapipe.PacketResamplerCalculatorOptions.base_timestamp', index=6,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='mediapipe.PacketResamplerCalculatorOptions.start_time', index=7,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='mediapipe.PacketResamplerCalculatorOptions.end_time', index=8,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='round_limits', full_name='mediapipe.PacketResamplerCalculatorOptions.round_limits', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.PacketResamplerCalculatorOptions.ext', index=0,
      number=95743844, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=635,
)

_PACKETRESAMPLERCALCULATOROPTIONS.fields_by_name['output_header'].enum_type = _PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER
_PACKETRESAMPLERCALCULATOROPTIONS_OUTPUTHEADER.containing_type = _PACKETRESAMPLERCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['PacketResamplerCalculatorOptions'] = _PACKETRESAMPLERCALCULATOROPTIONS

PacketResamplerCalculatorOptions = _reflection.GeneratedProtocolMessageType('PacketResamplerCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _PACKETRESAMPLERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.packet_resampler_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketResamplerCalculatorOptions)
  ))
_sym_db.RegisterMessage(PacketResamplerCalculatorOptions)

_PACKETRESAMPLERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _PACKETRESAMPLERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_PACKETRESAMPLERCALCULATOROPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\242\002\tMediaPipe'))
# @@protoc_insertion_point(module_scope)
