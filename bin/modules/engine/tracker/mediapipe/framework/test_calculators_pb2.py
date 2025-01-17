# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/test_calculators.proto

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
  name='mediapipe/framework/test_calculators.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n*mediapipe/framework/test_calculators.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xdd\x01\n\x1dRandomMatrixCalculatorOptions\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ols\x18\x02 \x01(\x05\x12\x17\n\x0fstart_timestamp\x18\x03 \x01(\x03\x12\x17\n\x0flimit_timestamp\x18\x04 \x01(\x03\x12\x16\n\x0etimestamp_step\x18\x05 \x01(\x03\x32V\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc8\xa0\xe9\x18 \x01(\x0b\x32(.mediapipe.RandomMatrixCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RANDOMMATRIXCALCULATOROPTIONS = _descriptor.Descriptor(
  name='RandomMatrixCalculatorOptions',
  full_name='mediapipe.RandomMatrixCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='mediapipe.RandomMatrixCalculatorOptions.rows', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cols', full_name='mediapipe.RandomMatrixCalculatorOptions.cols', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='mediapipe.RandomMatrixCalculatorOptions.start_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit_timestamp', full_name='mediapipe.RandomMatrixCalculatorOptions.limit_timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_step', full_name='mediapipe.RandomMatrixCalculatorOptions.timestamp_step', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.RandomMatrixCalculatorOptions.ext', index=0,
      number=52056136, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
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
  serialized_start=96,
  serialized_end=317,
)

DESCRIPTOR.message_types_by_name['RandomMatrixCalculatorOptions'] = _RANDOMMATRIXCALCULATOROPTIONS

RandomMatrixCalculatorOptions = _reflection.GeneratedProtocolMessageType('RandomMatrixCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _RANDOMMATRIXCALCULATOROPTIONS,
  __module__ = 'mediapipe.framework.test_calculators_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.RandomMatrixCalculatorOptions)
  ))
_sym_db.RegisterMessage(RandomMatrixCalculatorOptions)

_RANDOMMATRIXCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _RANDOMMATRIXCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_RANDOMMATRIXCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
