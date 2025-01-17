# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/audio/rational_factor_resample_calculator.proto

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
  name='mediapipe/calculators/audio/rational_factor_resample_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\nEmediapipe/calculators/audio/rational_factor_resample_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xac\x03\n\'RationalFactorResampleCalculatorOptions\x12\x1a\n\x12target_sample_rate\x18\x01 \x01(\x01\x12|\n!resampler_rational_factor_options\x18\x02 \x01(\x0b\x32Q.mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions\x12+\n\x1d\x63heck_inconsistent_timestamps\x18\x03 \x01(\x08:\x04true\x1aX\n\x1eResamplerRationalFactorOptions\x12\x0e\n\x06radius\x18\x01 \x01(\x01\x12\x0e\n\x06\x63utoff\x18\x02 \x01(\x01\x12\x16\n\x0bkaiser_beta\x18\x03 \x01(\x01:\x01\x36\x32`\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xca\xbf\xee{ \x01(\x0b\x32\x32.mediapipe.RationalFactorResampleCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS = _descriptor.Descriptor(
  name='ResamplerRationalFactorOptions',
  full_name='mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius', full_name='mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions.radius', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cutoff', full_name='mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions.cutoff', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kaiser_beta', full_name='mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions.kaiser_beta', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(6),
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
  serialized_start=365,
  serialized_end=453,
)

_RATIONALFACTORRESAMPLECALCULATOROPTIONS = _descriptor.Descriptor(
  name='RationalFactorResampleCalculatorOptions',
  full_name='mediapipe.RationalFactorResampleCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_sample_rate', full_name='mediapipe.RationalFactorResampleCalculatorOptions.target_sample_rate', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resampler_rational_factor_options', full_name='mediapipe.RationalFactorResampleCalculatorOptions.resampler_rational_factor_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_inconsistent_timestamps', full_name='mediapipe.RationalFactorResampleCalculatorOptions.check_inconsistent_timestamps', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.RationalFactorResampleCalculatorOptions.ext', index=0,
      number=259760074, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[_RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=551,
)

_RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS.containing_type = _RATIONALFACTORRESAMPLECALCULATOROPTIONS
_RATIONALFACTORRESAMPLECALCULATOROPTIONS.fields_by_name['resampler_rational_factor_options'].message_type = _RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS
DESCRIPTOR.message_types_by_name['RationalFactorResampleCalculatorOptions'] = _RATIONALFACTORRESAMPLECALCULATOROPTIONS

RationalFactorResampleCalculatorOptions = _reflection.GeneratedProtocolMessageType('RationalFactorResampleCalculatorOptions', (_message.Message,), dict(

  ResamplerRationalFactorOptions = _reflection.GeneratedProtocolMessageType('ResamplerRationalFactorOptions', (_message.Message,), dict(
    DESCRIPTOR = _RATIONALFACTORRESAMPLECALCULATOROPTIONS_RESAMPLERRATIONALFACTOROPTIONS,
    __module__ = 'mediapipe.calculators.audio.rational_factor_resample_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions)
    ))
  ,
  DESCRIPTOR = _RATIONALFACTORRESAMPLECALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.audio.rational_factor_resample_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RationalFactorResampleCalculatorOptions)
  ))
_sym_db.RegisterMessage(RationalFactorResampleCalculatorOptions)
_sym_db.RegisterMessage(RationalFactorResampleCalculatorOptions.ResamplerRationalFactorOptions)

_RATIONALFACTORRESAMPLECALCULATOROPTIONS.extensions_by_name['ext'].message_type = _RATIONALFACTORRESAMPLECALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_RATIONALFACTORRESAMPLECALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
