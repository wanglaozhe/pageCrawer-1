# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='poppy/rpc_option.proto',
  package='poppy',
  serialized_pb='\n\x16poppy/rpc_option.proto\x12\x05poppy\x1a google/protobuf/descriptor.proto*[\n\x0c\x43ompressType\x12\x1d\n\x10\x43ompressTypeAuto\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x14\n\x10\x43ompressTypeNone\x10\x00\x12\x16\n\x12\x43ompressTypeSnappy\x10\x01:A\n\x0fservice_timeout\x12\x1f.google.protobuf.ServiceOptions\x18\xa0\x9c\x01 \x01(\x03:\x05\x31\x30\x30\x30\x30:8\n\x0emethod_timeout\x12\x1e.google.protobuf.MethodOptions\x18\xa0\x9c\x01 \x01(\x03:h\n\x15request_compress_type\x12\x1e.google.protobuf.MethodOptions\x18\xa1\x9c\x01 \x01(\x0e\x32\x13.poppy.CompressType:\x12\x43ompressTypeSnappy:i\n\x16response_compress_type\x12\x1e.google.protobuf.MethodOptions\x18\xa2\x9c\x01 \x01(\x0e\x32\x13.poppy.CompressType:\x12\x43ompressTypeSnappyB\x10\n\x0e\x63om.soso.poppy')

_COMPRESSTYPE = descriptor.EnumDescriptor(
  name='CompressType',
  full_name='poppy.CompressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CompressTypeAuto', index=0, number=-1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CompressTypeNone', index=1, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CompressTypeSnappy', index=2, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=158,
)


CompressTypeAuto = -1
CompressTypeNone = 0
CompressTypeSnappy = 1

SERVICE_TIMEOUT_FIELD_NUMBER = 20000
service_timeout = descriptor.FieldDescriptor(
  name='service_timeout', full_name='poppy.service_timeout', index=0,
  number=20000, type=3, cpp_type=2, label=1,
  has_default_value=True, default_value=10000,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
METHOD_TIMEOUT_FIELD_NUMBER = 20000
method_timeout = descriptor.FieldDescriptor(
  name='method_timeout', full_name='poppy.method_timeout', index=1,
  number=20000, type=3, cpp_type=2, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
REQUEST_COMPRESS_TYPE_FIELD_NUMBER = 20001
request_compress_type = descriptor.FieldDescriptor(
  name='request_compress_type', full_name='poppy.request_compress_type', index=2,
  number=20001, type=14, cpp_type=8, label=1,
  has_default_value=True, default_value=1,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
RESPONSE_COMPRESS_TYPE_FIELD_NUMBER = 20002
response_compress_type = descriptor.FieldDescriptor(
  name='response_compress_type', full_name='poppy.response_compress_type', index=3,
  number=20002, type=14, cpp_type=8, label=1,
  has_default_value=True, default_value=1,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

import google.protobuf.descriptor_pb2


google.protobuf.descriptor_pb2.ServiceOptions.RegisterExtension(service_timeout)
google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(method_timeout)
request_compress_type.enum_type = _COMPRESSTYPE
google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(request_compress_type)
response_compress_type.enum_type = _COMPRESSTYPE
google.protobuf.descriptor_pb2.MethodOptions.RegisterExtension(response_compress_type)
# @@protoc_insertion_point(module_scope)
