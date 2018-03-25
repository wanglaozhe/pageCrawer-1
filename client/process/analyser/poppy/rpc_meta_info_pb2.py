# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='poppy/rpc_meta_info.proto',
  package='poppy',
  serialized_pb='\n\x19poppy/rpc_meta_info.proto\x12\x05poppy\x1a\x16poppy/rpc_option.proto\"\xbb\x02\n\x07RpcMeta\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.poppy.RpcMeta.Type\x12\x13\n\x0bsequence_id\x18\x02 \x02(\x03\x12\x0e\n\x06method\x18\x64 \x01(\t\x12\x0f\n\x07timeout\x18\x65 \x01(\x03\x12\x0f\n\x06\x66\x61iled\x18\xc8\x01 \x01(\x08\x12\x11\n\x08\x63\x61nceled\x18\xc9\x01 \x01(\x08\x12\x13\n\nerror_code\x18\xca\x01 \x01(\x05\x12\x0f\n\x06reason\x18\xcb\x01 \x01(\t\x12+\n\rcompress_type\x18\xcc\x01 \x01(\x0e\x32\x13.poppy.CompressType\x12=\n\x1f\x65xpected_response_compress_type\x18\xcd\x01 \x01(\x0e\x32\x13.poppy.CompressType\"!\n\x04Type\x12\x0b\n\x07REQUEST\x10\x00\x12\x0c\n\x08RESPONSE\x10\x01\x42\x10\n\x0e\x63om.soso.poppy')



_RPCMETA_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='poppy.RpcMeta.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='REQUEST', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RESPONSE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=343,
  serialized_end=376,
)


_RPCMETA = descriptor.Descriptor(
  name='RpcMeta',
  full_name='poppy.RpcMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='poppy.RpcMeta.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sequence_id', full_name='poppy.RpcMeta.sequence_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method', full_name='poppy.RpcMeta.method', index=2,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='poppy.RpcMeta.timeout', index=3,
      number=101, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed', full_name='poppy.RpcMeta.failed', index=4,
      number=200, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='canceled', full_name='poppy.RpcMeta.canceled', index=5,
      number=201, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='error_code', full_name='poppy.RpcMeta.error_code', index=6,
      number=202, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reason', full_name='poppy.RpcMeta.reason', index=7,
      number=203, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='compress_type', full_name='poppy.RpcMeta.compress_type', index=8,
      number=204, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='expected_response_compress_type', full_name='poppy.RpcMeta.expected_response_compress_type', index=9,
      number=205, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RPCMETA_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=61,
  serialized_end=376,
)

import poppy.rpc_option_pb2

_RPCMETA.fields_by_name['type'].enum_type = _RPCMETA_TYPE
_RPCMETA.fields_by_name['compress_type'].enum_type = poppy.rpc_option_pb2._COMPRESSTYPE
_RPCMETA.fields_by_name['expected_response_compress_type'].enum_type = poppy.rpc_option_pb2._COMPRESSTYPE
_RPCMETA_TYPE.containing_type = _RPCMETA;

class RpcMeta(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPCMETA
  
  # @@protoc_insertion_point(class_scope:poppy.RpcMeta)

# @@protoc_insertion_point(module_scope)