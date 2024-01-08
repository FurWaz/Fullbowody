# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/visibility_smoothing_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/visibility_smoothing_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n@mediapipe/calculators/util/visibility_smoothing_calculator.proto\x12\tmediapipe\x1a,mediapipe/framework/calculator_options.proto\"\xf2\x02\n$VisibilitySmoothingCalculatorOptions\x12M\n\tno_filter\x18\x01 \x01(\x0b\x32\x38.mediapipe.VisibilitySmoothingCalculatorOptions.NoFilterH\x00\x12X\n\x0flow_pass_filter\x18\x02 \x01(\x0b\x32=.mediapipe.VisibilitySmoothingCalculatorOptions.LowPassFilterH\x00\x1a\n\n\x08NoFilter\x1a#\n\rLowPassFilter\x12\x12\n\x05\x61lpha\x18\x01 \x01(\x02:\x03\x30.12^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf6\xa7\xe1\xab\x01 \x01(\x0b\x32/.mediapipe.VisibilitySmoothingCalculatorOptionsB\x10\n\x0e\x66ilter_options')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER = _descriptor.Descriptor(
  name='NoFilter',
  full_name='mediapipe.VisibilitySmoothingCalculatorOptions.NoFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=335,
  serialized_end=345,
)

_VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER = _descriptor.Descriptor(
  name='LowPassFilter',
  full_name='mediapipe.VisibilitySmoothingCalculatorOptions.LowPassFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha', full_name='mediapipe.VisibilitySmoothingCalculatorOptions.LowPassFilter.alpha', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
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
  serialized_start=347,
  serialized_end=382,
)

_VISIBILITYSMOOTHINGCALCULATOROPTIONS = _descriptor.Descriptor(
  name='VisibilitySmoothingCalculatorOptions',
  full_name='mediapipe.VisibilitySmoothingCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no_filter', full_name='mediapipe.VisibilitySmoothingCalculatorOptions.no_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low_pass_filter', full_name='mediapipe.VisibilitySmoothingCalculatorOptions.low_pass_filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.VisibilitySmoothingCalculatorOptions.ext', index=0,
      number=360207350, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[_VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER, _VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='filter_options', full_name='mediapipe.VisibilitySmoothingCalculatorOptions.filter_options',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=126,
  serialized_end=496,
)

_VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER.containing_type = _VISIBILITYSMOOTHINGCALCULATOROPTIONS
_VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER.containing_type = _VISIBILITYSMOOTHINGCALCULATOROPTIONS
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['no_filter'].message_type = _VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['low_pass_filter'].message_type = _VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.oneofs_by_name['filter_options'].fields.append(
  _VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['no_filter'])
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['no_filter'].containing_oneof = _VISIBILITYSMOOTHINGCALCULATOROPTIONS.oneofs_by_name['filter_options']
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.oneofs_by_name['filter_options'].fields.append(
  _VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['low_pass_filter'])
_VISIBILITYSMOOTHINGCALCULATOROPTIONS.fields_by_name['low_pass_filter'].containing_oneof = _VISIBILITYSMOOTHINGCALCULATOROPTIONS.oneofs_by_name['filter_options']
DESCRIPTOR.message_types_by_name['VisibilitySmoothingCalculatorOptions'] = _VISIBILITYSMOOTHINGCALCULATOROPTIONS

VisibilitySmoothingCalculatorOptions = _reflection.GeneratedProtocolMessageType('VisibilitySmoothingCalculatorOptions', (_message.Message,), dict(

  NoFilter = _reflection.GeneratedProtocolMessageType('NoFilter', (_message.Message,), dict(
    DESCRIPTOR = _VISIBILITYSMOOTHINGCALCULATOROPTIONS_NOFILTER,
    __module__ = 'mediapipe.calculators.util.visibility_smoothing_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.VisibilitySmoothingCalculatorOptions.NoFilter)
    ))
  ,

  LowPassFilter = _reflection.GeneratedProtocolMessageType('LowPassFilter', (_message.Message,), dict(
    DESCRIPTOR = _VISIBILITYSMOOTHINGCALCULATOROPTIONS_LOWPASSFILTER,
    __module__ = 'mediapipe.calculators.util.visibility_smoothing_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.VisibilitySmoothingCalculatorOptions.LowPassFilter)
    ))
  ,
  DESCRIPTOR = _VISIBILITYSMOOTHINGCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.visibility_smoothing_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.VisibilitySmoothingCalculatorOptions)
  ))
_sym_db.RegisterMessage(VisibilitySmoothingCalculatorOptions)
_sym_db.RegisterMessage(VisibilitySmoothingCalculatorOptions.NoFilter)
_sym_db.RegisterMessage(VisibilitySmoothingCalculatorOptions.LowPassFilter)

_VISIBILITYSMOOTHINGCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _VISIBILITYSMOOTHINGCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_VISIBILITYSMOOTHINGCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
