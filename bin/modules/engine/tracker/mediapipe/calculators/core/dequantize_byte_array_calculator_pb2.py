# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/dequantize_byte_array_calculator.proto

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
  name='mediapipe/calculators/core/dequantize_byte_array_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\nAmediapipe/calculators/core/dequantize_byte_array_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xc0\x01\n$DequantizeByteArrayCalculatorOptions\x12\x1b\n\x13max_quantized_value\x18\x01 \x01(\x02\x12\x1b\n\x13min_quantized_value\x18\x02 \x01(\x02\x32^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb7\xef\xec\x81\x01 \x01(\x0b\x32/.mediapipe.DequantizeByteArrayCalculatorOptionsB\x0c\xa2\x02\tMediaPipe')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEQUANTIZEBYTEARRAYCALCULATOROPTIONS = _descriptor.Descriptor(
  name='DequantizeByteArrayCalculatorOptions',
  full_name='mediapipe.DequantizeByteArrayCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_quantized_value', full_name='mediapipe.DequantizeByteArrayCalculatorOptions.max_quantized_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_quantized_value', full_name='mediapipe.DequantizeByteArrayCalculatorOptions.min_quantized_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.DequantizeByteArrayCalculatorOptions.ext', index=0,
      number=272316343, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=311,
)

DESCRIPTOR.message_types_by_name['DequantizeByteArrayCalculatorOptions'] = _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS

DequantizeByteArrayCalculatorOptions = _reflection.GeneratedProtocolMessageType('DequantizeByteArrayCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.dequantize_byte_array_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.DequantizeByteArrayCalculatorOptions)
  ))
_sym_db.RegisterMessage(DequantizeByteArrayCalculatorOptions)

_DEQUANTIZEBYTEARRAYCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_DEQUANTIZEBYTEARRAYCALCULATOROPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\242\002\tMediaPipe'))
# @@protoc_insertion_point(module_scope)
