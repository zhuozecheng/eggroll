# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='command.proto',
  package='com.webank.eggroll.core.command',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rcommand.proto\x12\x1f\x63om.webank.eggroll.core.command\"\xb3\x01\n\x0e\x43ommandRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\x0c\x12K\n\x06kwargs\x18\x04 \x03(\x0b\x32;.com.webank.eggroll.core.command.CommandRequest.KwargsEntry\x1a-\n\x0bKwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"p\n\x0f\x43ommandResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x07request\x18\x02 \x01(\x0b\x32/.com.webank.eggroll.core.command.CommandRequest\x12\x0f\n\x07results\x18\x03 \x03(\x0c\x32{\n\x0e\x43ommandService\x12i\n\x04\x63\x61ll\x12/.com.webank.eggroll.core.command.CommandRequest\x1a\x30.com.webank.eggroll.core.command.CommandResponseb\x06proto3')
)




_COMMANDREQUEST_KWARGSENTRY = _descriptor.Descriptor(
  name='KwargsEntry',
  full_name='com.webank.eggroll.core.command.CommandRequest.KwargsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.eggroll.core.command.CommandRequest.KwargsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.eggroll.core.command.CommandRequest.KwargsEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=230,
)

_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='com.webank.eggroll.core.command.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.webank.eggroll.core.command.CommandRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='com.webank.eggroll.core.command.CommandRequest.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='com.webank.eggroll.core.command.CommandRequest.args', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='com.webank.eggroll.core.command.CommandRequest.kwargs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COMMANDREQUEST_KWARGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=230,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='com.webank.eggroll.core.command.CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.webank.eggroll.core.command.CommandResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='com.webank.eggroll.core.command.CommandResponse.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='com.webank.eggroll.core.command.CommandResponse.results', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=344,
)

_COMMANDREQUEST_KWARGSENTRY.containing_type = _COMMANDREQUEST
_COMMANDREQUEST.fields_by_name['kwargs'].message_type = _COMMANDREQUEST_KWARGSENTRY
_COMMANDRESPONSE.fields_by_name['request'].message_type = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), dict(

  KwargsEntry = _reflection.GeneratedProtocolMessageType('KwargsEntry', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDREQUEST_KWARGSENTRY,
    __module__ = 'command_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.command.CommandRequest.KwargsEntry)
    ))
  ,
  DESCRIPTOR = _COMMANDREQUEST,
  __module__ = 'command_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.command.CommandRequest)
  ))
_sym_db.RegisterMessage(CommandRequest)
_sym_db.RegisterMessage(CommandRequest.KwargsEntry)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDRESPONSE,
  __module__ = 'command_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.command.CommandResponse)
  ))
_sym_db.RegisterMessage(CommandResponse)


_COMMANDREQUEST_KWARGSENTRY._options = None

_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='CommandService',
  full_name='com.webank.eggroll.core.command.CommandService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=346,
  serialized_end=469,
  methods=[
  _descriptor.MethodDescriptor(
    name='call',
    full_name='com.webank.eggroll.core.command.CommandService.call',
    index=0,
    containing_service=None,
    input_type=_COMMANDREQUEST,
    output_type=_COMMANDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE)

DESCRIPTOR.services_by_name['CommandService'] = _COMMANDSERVICE

# @@protoc_insertion_point(module_scope)
