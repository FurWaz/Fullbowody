# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/detections_to_rects_calculator.proto

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
  name='mediapipe/calculators/util/detections_to_rects_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n?mediapipe/calculators/util/detections_to_rects_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xfd\x03\n\"DetectionsToRectsCalculatorOptions\x12,\n$rotation_vector_start_keypoint_index\x18\x01 \x01(\x05\x12*\n\"rotation_vector_end_keypoint_index\x18\x02 \x01(\x05\x12$\n\x1crotation_vector_target_angle\x18\x03 \x01(\x02\x12,\n$rotation_vector_target_angle_degrees\x18\x04 \x01(\x02\x12-\n%output_zero_rect_for_empty_detections\x18\x05 \x01(\x08\x12U\n\x0f\x63onversion_mode\x18\x06 \x01(\x0e\x32<.mediapipe.DetectionsToRectsCalculatorOptions.ConversionMode\"F\n\x0e\x43onversionMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x14\n\x10USE_BOUNDING_BOX\x10\x01\x12\x11\n\rUSE_KEYPOINTS\x10\x02\x32[\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xdf\xb7\xa1} \x01(\x0b\x32-.mediapipe.DetectionsToRectsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DETECTIONSTORECTSCALCULATOROPTIONS_CONVERSIONMODE = _descriptor.EnumDescriptor(
  name='ConversionMode',
  full_name='mediapipe.DetectionsToRectsCalculatorOptions.ConversionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_BOUNDING_BOX', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_KEYPOINTS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=463,
  serialized_end=533,
)
_sym_db.RegisterEnumDescriptor(_DETECTIONSTORECTSCALCULATOROPTIONS_CONVERSIONMODE)


_DETECTIONSTORECTSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='DetectionsToRectsCalculatorOptions',
  full_name='mediapipe.DetectionsToRectsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation_vector_start_keypoint_index', full_name='mediapipe.DetectionsToRectsCalculatorOptions.rotation_vector_start_keypoint_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation_vector_end_keypoint_index', full_name='mediapipe.DetectionsToRectsCalculatorOptions.rotation_vector_end_keypoint_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation_vector_target_angle', full_name='mediapipe.DetectionsToRectsCalculatorOptions.rotation_vector_target_angle', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation_vector_target_angle_degrees', full_name='mediapipe.DetectionsToRectsCalculatorOptions.rotation_vector_target_angle_degrees', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_zero_rect_for_empty_detections', full_name='mediapipe.DetectionsToRectsCalculatorOptions.output_zero_rect_for_empty_detections', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conversion_mode', full_name='mediapipe.DetectionsToRectsCalculatorOptions.conversion_mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.DetectionsToRectsCalculatorOptions.ext', index=0,
      number=262691807, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _DETECTIONSTORECTSCALCULATOROPTIONS_CONVERSIONMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=626,
)

_DETECTIONSTORECTSCALCULATOROPTIONS.fields_by_name['conversion_mode'].enum_type = _DETECTIONSTORECTSCALCULATOROPTIONS_CONVERSIONMODE
_DETECTIONSTORECTSCALCULATOROPTIONS_CONVERSIONMODE.containing_type = _DETECTIONSTORECTSCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['DetectionsToRectsCalculatorOptions'] = _DETECTIONSTORECTSCALCULATOROPTIONS

DetectionsToRectsCalculatorOptions = _reflection.GeneratedProtocolMessageType('DetectionsToRectsCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _DETECTIONSTORECTSCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.detections_to_rects_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.DetectionsToRectsCalculatorOptions)
  ))
_sym_db.RegisterMessage(DetectionsToRectsCalculatorOptions)

_DETECTIONSTORECTSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _DETECTIONSTORECTSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_DETECTIONSTORECTSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
