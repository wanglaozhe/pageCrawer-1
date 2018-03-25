# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='analyse_service.proto',
  package='tencent.search.isoso',
  serialized_pb='\n\x15\x61nalyse_service.proto\x12\x14tencent.search.isoso\x1a\x16poppy/rpc_option.proto\x1a\x1dservers/analyser/common.proto2]\n\rAnalyseServer\x12L\n\tGetResult\x12\x1b.tencent.search.isoso.Input\x1a\x1c.tencent.search.isoso.Output\"\x04\x80\xe2\td')



import poppy.rpc_option_pb2
import servers.analyser.common_pb2



_ANALYSESERVER = descriptor.ServiceDescriptor(
  name='AnalyseServer',
  full_name='tencent.search.isoso.AnalyseServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=102,
  serialized_end=195,
  methods=[
  descriptor.MethodDescriptor(
    name='GetResult',
    full_name='tencent.search.isoso.AnalyseServer.GetResult',
    index=0,
    containing_service=None,
    input_type=servers.analyser.common_pb2._INPUT,
    output_type=servers.analyser.common_pb2._OUTPUT,
    options=descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\200\342\td'),
  ),
])

class AnalyseServer(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _ANALYSESERVER
class AnalyseServer_Stub(AnalyseServer):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _ANALYSESERVER

# @@protoc_insertion_point(module_scope)