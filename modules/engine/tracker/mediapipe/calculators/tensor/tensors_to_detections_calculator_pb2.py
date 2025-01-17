# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensors_to_detections_calculator.proto

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
  name='mediapipe/calculators/tensor/tensors_to_detections_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\nCmediapipe/calculators/tensor/tensors_to_detections_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xee\x04\n$TensorsToDetectionsCalculatorOptions\x12\x13\n\x0bnum_classes\x18\x01 \x01(\x05\x12\x11\n\tnum_boxes\x18\x02 \x01(\x05\x12\x12\n\nnum_coords\x18\x03 \x01(\x05\x12\x1d\n\x15keypoint_coord_offset\x18\t \x01(\x05\x12\x18\n\rnum_keypoints\x18\n \x01(\x05:\x01\x30\x12\"\n\x17num_values_per_keypoint\x18\x0b \x01(\x05:\x01\x32\x12\x1b\n\x10\x62ox_coord_offset\x18\x0c \x01(\x05:\x01\x30\x12\x12\n\x07x_scale\x18\x04 \x01(\x02:\x01\x30\x12\x12\n\x07y_scale\x18\x05 \x01(\x02:\x01\x30\x12\x12\n\x07w_scale\x18\x06 \x01(\x02:\x01\x30\x12\x12\n\x07h_scale\x18\x07 \x01(\x02:\x01\x30\x12,\n\x1d\x61pply_exponential_on_box_size\x18\r \x01(\x08:\x05\x66\x61lse\x12#\n\x14reverse_output_order\x18\x0e \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0eignore_classes\x18\x08 \x03(\x05\x12\x1c\n\rsigmoid_score\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x15score_clipping_thresh\x18\x10 \x01(\x02\x12\x1e\n\x0f\x66lip_vertically\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x10min_score_thresh\x18\x13 \x01(\x02\x32^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xaf\x8d\x8c\xa0\x01 \x01(\x0b\x32/.mediapipe.TensorsToDetectionsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TENSORSTODETECTIONSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorsToDetectionsCalculatorOptions',
  full_name='mediapipe.TensorsToDetectionsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_classes', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.num_classes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_boxes', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.num_boxes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_coords', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.num_coords', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoint_coord_offset', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.keypoint_coord_offset', index=3,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_keypoints', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.num_keypoints', index=4,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_values_per_keypoint', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.num_values_per_keypoint', index=5,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_coord_offset', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.box_coord_offset', index=6,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_scale', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.x_scale', index=7,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_scale', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.y_scale', index=8,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w_scale', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.w_scale', index=9,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_scale', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.h_scale', index=10,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_exponential_on_box_size', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.apply_exponential_on_box_size', index=11,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_output_order', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.reverse_output_order', index=12,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_classes', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.ignore_classes', index=13,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sigmoid_score', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.sigmoid_score', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_clipping_thresh', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.score_clipping_thresh', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flip_vertically', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.flip_vertically', index=16,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_score_thresh', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.min_score_thresh', index=17,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorsToDetectionsCalculatorOptions.ext', index=0,
      number=335742639, type=11, cpp_type=10, label=1,
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
  serialized_start=121,
  serialized_end=743,
)

DESCRIPTOR.message_types_by_name['TensorsToDetectionsCalculatorOptions'] = _TENSORSTODETECTIONSCALCULATOROPTIONS

TensorsToDetectionsCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorsToDetectionsCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _TENSORSTODETECTIONSCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.tensors_to_detections_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorsToDetectionsCalculatorOptions)
  ))
_sym_db.RegisterMessage(TensorsToDetectionsCalculatorOptions)

_TENSORSTODETECTIONSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORSTODETECTIONSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORSTODETECTIONSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
