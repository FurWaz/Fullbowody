# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/video_pre_stream_calculator.proto

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
  name='mediapipe/calculators/video/video_pre_stream_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n=mediapipe/calculators/video/video_pre_stream_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xcf\x02\n\x1fVideoPreStreamCalculatorOptions\x12;\n\x03\x66ps\x18\x01 \x01(\x0b\x32..mediapipe.VideoPreStreamCalculatorOptions.Fps\x1a\x94\x01\n\x03\x46ps\x12\r\n\x05value\x18\x01 \x01(\x01\x12H\n\x05ratio\x18\x02 \x01(\x0b\x32\x39.mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32\x1a\x34\n\nRational32\x12\x11\n\tnumerator\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x05\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8b\xf0\x97H \x01(\x0b\x32*.mediapipe.VideoPreStreamCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32 = _descriptor.Descriptor(
  name='Rational32',
  full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numerator', full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32.numerator', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='denominator', full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32.denominator', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=360,
)

_VIDEOPRESTREAMCALCULATOROPTIONS_FPS = _descriptor.Descriptor(
  name='Fps',
  full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='mediapipe.VideoPreStreamCalculatorOptions.Fps.ratio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=360,
)

_VIDEOPRESTREAMCALCULATOROPTIONS = _descriptor.Descriptor(
  name='VideoPreStreamCalculatorOptions',
  full_name='mediapipe.VideoPreStreamCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fps', full_name='mediapipe.VideoPreStreamCalculatorOptions.fps', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.VideoPreStreamCalculatorOptions.ext', index=0,
      number=151386123, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[_VIDEOPRESTREAMCALCULATOROPTIONS_FPS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=450,
)

_VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32.containing_type = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS
_VIDEOPRESTREAMCALCULATOROPTIONS_FPS.fields_by_name['ratio'].message_type = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32
_VIDEOPRESTREAMCALCULATOROPTIONS_FPS.containing_type = _VIDEOPRESTREAMCALCULATOROPTIONS
_VIDEOPRESTREAMCALCULATOROPTIONS.fields_by_name['fps'].message_type = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS
DESCRIPTOR.message_types_by_name['VideoPreStreamCalculatorOptions'] = _VIDEOPRESTREAMCALCULATOROPTIONS

VideoPreStreamCalculatorOptions = _reflection.GeneratedProtocolMessageType('VideoPreStreamCalculatorOptions', (_message.Message,), dict(

  Fps = _reflection.GeneratedProtocolMessageType('Fps', (_message.Message,), dict(

    Rational32 = _reflection.GeneratedProtocolMessageType('Rational32', (_message.Message,), dict(
      DESCRIPTOR = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS_RATIONAL32,
      __module__ = 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
      # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions.Fps.Rational32)
      ))
    ,
    DESCRIPTOR = _VIDEOPRESTREAMCALCULATOROPTIONS_FPS,
    __module__ = 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions.Fps)
    ))
  ,
  DESCRIPTOR = _VIDEOPRESTREAMCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.video.video_pre_stream_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.VideoPreStreamCalculatorOptions)
  ))
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions)
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions.Fps)
_sym_db.RegisterMessage(VideoPreStreamCalculatorOptions.Fps.Rational32)

_VIDEOPRESTREAMCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _VIDEOPRESTREAMCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_VIDEOPRESTREAMCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
