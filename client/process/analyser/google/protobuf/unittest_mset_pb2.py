# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='google/protobuf/unittest_mset.proto',
  package='protobuf_unittest',
  serialized_pb='\n#google/protobuf/unittest_mset.proto\x12\x11protobuf_unittest\"\x1e\n\x0eTestMessageSet*\x08\x08\x04\x10\x80\x80\x80\x80\x02:\x02\x08\x01\"Q\n\x17TestMessageSetContainer\x12\x36\n\x0bmessage_set\x18\x01 \x01(\x0b\x32!.protobuf_unittest.TestMessageSet\"\x96\x01\n\x18TestMessageSetExtension1\x12\t\n\x01i\x18\x0f \x01(\x05\x32o\n\x15message_set_extension\x12!.protobuf_unittest.TestMessageSet\x18\xb0\xa6^ \x01(\x0b\x32+.protobuf_unittest.TestMessageSetExtension1\"\x98\x01\n\x18TestMessageSetExtension2\x12\x0b\n\x03str\x18\x19 \x01(\t2o\n\x15message_set_extension\x12!.protobuf_unittest.TestMessageSet\x18\xf9\xbb^ \x01(\x0b\x32+.protobuf_unittest.TestMessageSetExtension2\"n\n\rRawMessageSet\x12\x33\n\x04item\x18\x01 \x03(\n2%.protobuf_unittest.RawMessageSet.Item\x1a(\n\x04Item\x12\x0f\n\x07type_id\x18\x02 \x02(\x05\x12\x0f\n\x07message\x18\x03 \x02(\x0c\x42\x02H\x01')




_TESTMESSAGESET = descriptor.Descriptor(
  name='TestMessageSet',
  full_name='protobuf_unittest.TestMessageSet',
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\010\001'),
  is_extendable=True,
  extension_ranges=[(4, 536870912), ],
  serialized_start=58,
  serialized_end=88,
)


_TESTMESSAGESETCONTAINER = descriptor.Descriptor(
  name='TestMessageSetContainer',
  full_name='protobuf_unittest.TestMessageSetContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message_set', full_name='protobuf_unittest.TestMessageSetContainer.message_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=90,
  serialized_end=171,
)


_TESTMESSAGESETEXTENSION1 = descriptor.Descriptor(
  name='TestMessageSetExtension1',
  full_name='protobuf_unittest.TestMessageSetExtension1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='i', full_name='protobuf_unittest.TestMessageSetExtension1.i', index=0,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    descriptor.FieldDescriptor(
      name='message_set_extension', full_name='protobuf_unittest.TestMessageSetExtension1.message_set_extension', index=0,
      number=1545008, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=174,
  serialized_end=324,
)


_TESTMESSAGESETEXTENSION2 = descriptor.Descriptor(
  name='TestMessageSetExtension2',
  full_name='protobuf_unittest.TestMessageSetExtension2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='str', full_name='protobuf_unittest.TestMessageSetExtension2.str', index=0,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    descriptor.FieldDescriptor(
      name='message_set_extension', full_name='protobuf_unittest.TestMessageSetExtension2.message_set_extension', index=0,
      number=1547769, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=327,
  serialized_end=479,
)


_RAWMESSAGESET_ITEM = descriptor.Descriptor(
  name='Item',
  full_name='protobuf_unittest.RawMessageSet.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='protobuf_unittest.RawMessageSet.Item.type_id', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protobuf_unittest.RawMessageSet.Item.message', index=1,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=551,
  serialized_end=591,
)

_RAWMESSAGESET = descriptor.Descriptor(
  name='RawMessageSet',
  full_name='protobuf_unittest.RawMessageSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item', full_name='protobuf_unittest.RawMessageSet.item', index=0,
      number=1, type=10, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RAWMESSAGESET_ITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=481,
  serialized_end=591,
)


_TESTMESSAGESETCONTAINER.fields_by_name['message_set'].message_type = _TESTMESSAGESET
_RAWMESSAGESET_ITEM.containing_type = _RAWMESSAGESET;
_RAWMESSAGESET.fields_by_name['item'].message_type = _RAWMESSAGESET_ITEM

class TestMessageSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTMESSAGESET
  
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestMessageSet)

class TestMessageSetContainer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTMESSAGESETCONTAINER
  
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestMessageSetContainer)

class TestMessageSetExtension1(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTMESSAGESETEXTENSION1
  
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestMessageSetExtension1)

class TestMessageSetExtension2(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTMESSAGESETEXTENSION2
  
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestMessageSetExtension2)

class RawMessageSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Item(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RAWMESSAGESET_ITEM
    
    # @@protoc_insertion_point(class_scope:protobuf_unittest.RawMessageSet.Item)
  DESCRIPTOR = _RAWMESSAGESET
  
  # @@protoc_insertion_point(class_scope:protobuf_unittest.RawMessageSet)

_TESTMESSAGESETEXTENSION1.extensions_by_name['message_set_extension'].message_type = _TESTMESSAGESETEXTENSION1
TestMessageSet.RegisterExtension(_TESTMESSAGESETEXTENSION1.extensions_by_name['message_set_extension'])
_TESTMESSAGESETEXTENSION2.extensions_by_name['message_set_extension'].message_type = _TESTMESSAGESETEXTENSION2
TestMessageSet.RegisterExtension(_TESTMESSAGESETEXTENSION2.extensions_by_name['message_set_extension'])
# @@protoc_insertion_point(module_scope)
