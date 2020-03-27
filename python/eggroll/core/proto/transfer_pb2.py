# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transfer.proto',
  package='com.webank.eggroll.core.transfer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0etransfer.proto\x12 com.webank.eggroll.core.transfer\"L\n\x0eTransferHeader\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x11\n\ttotalSize\x18\x03 \x01(\x03\x12\x0e\n\x06status\x18\x04 \x01(\t\"r\n\rTransferBatch\x12@\n\x06header\x18\x01 \x01(\x0b\x32\x30.com.webank.eggroll.core.transfer.TransferHeader\x12\x11\n\tbatchSize\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xa2\x02\n\x0eRollSiteHeader\x12\x19\n\x11rollSiteSessionId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12\x0f\n\x07srcRole\x18\x04 \x01(\t\x12\x12\n\nsrcPartyId\x18\x05 \x01(\t\x12\x0f\n\x07\x64stRole\x18\x06 \x01(\t\x12\x12\n\ndstPartyId\x18\x07 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x08 \x01(\t\x12N\n\x07options\x18\n \x03(\x0b\x32=.com.webank.eggroll.core.transfer.RollSiteHeader.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xdb\x02\n\x0fTransferService\x12j\n\x04send\x12/.com.webank.eggroll.core.transfer.TransferBatch\x1a/.com.webank.eggroll.core.transfer.TransferBatch(\x01\x12j\n\x04recv\x12/.com.webank.eggroll.core.transfer.TransferBatch\x1a/.com.webank.eggroll.core.transfer.TransferBatch0\x01\x12p\n\x08sendRecv\x12/.com.webank.eggroll.core.transfer.TransferBatch\x1a/.com.webank.eggroll.core.transfer.TransferBatch(\x01\x30\x01\x62\x06proto3')
)




_TRANSFERHEADER = _descriptor.Descriptor(
  name='TransferHeader',
  full_name='com.webank.eggroll.core.transfer.TransferHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.webank.eggroll.core.transfer.TransferHeader.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='com.webank.eggroll.core.transfer.TransferHeader.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalSize', full_name='com.webank.eggroll.core.transfer.TransferHeader.totalSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='com.webank.eggroll.core.transfer.TransferHeader.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=52,
  serialized_end=128,
)


_TRANSFERBATCH = _descriptor.Descriptor(
  name='TransferBatch',
  full_name='com.webank.eggroll.core.transfer.TransferBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.eggroll.core.transfer.TransferBatch.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchSize', full_name='com.webank.eggroll.core.transfer.TransferBatch.batchSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.webank.eggroll.core.transfer.TransferBatch.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=244,
)


_ROLLSITEHEADER_OPTIONSENTRY = _descriptor.Descriptor(
  name='OptionsEntry',
  full_name='com.webank.eggroll.core.transfer.RollSiteHeader.OptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.OptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.OptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=491,
  serialized_end=537,
)

_ROLLSITEHEADER = _descriptor.Descriptor(
  name='RollSiteHeader',
  full_name='com.webank.eggroll.core.transfer.RollSiteHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rollSiteSessionId', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.rollSiteSessionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='srcRole', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.srcRole', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='srcPartyId', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.srcPartyId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dstRole', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.dstRole', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dstPartyId', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.dstPartyId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.dataType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='com.webank.eggroll.core.transfer.RollSiteHeader.options', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ROLLSITEHEADER_OPTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=537,
)

_TRANSFERBATCH.fields_by_name['header'].message_type = _TRANSFERHEADER
_ROLLSITEHEADER_OPTIONSENTRY.containing_type = _ROLLSITEHEADER
_ROLLSITEHEADER.fields_by_name['options'].message_type = _ROLLSITEHEADER_OPTIONSENTRY
DESCRIPTOR.message_types_by_name['TransferHeader'] = _TRANSFERHEADER
DESCRIPTOR.message_types_by_name['TransferBatch'] = _TRANSFERBATCH
DESCRIPTOR.message_types_by_name['RollSiteHeader'] = _ROLLSITEHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransferHeader = _reflection.GeneratedProtocolMessageType('TransferHeader', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERHEADER,
  __module__ = 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.transfer.TransferHeader)
  ))
_sym_db.RegisterMessage(TransferHeader)

TransferBatch = _reflection.GeneratedProtocolMessageType('TransferBatch', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERBATCH,
  __module__ = 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.transfer.TransferBatch)
  ))
_sym_db.RegisterMessage(TransferBatch)

RollSiteHeader = _reflection.GeneratedProtocolMessageType('RollSiteHeader', (_message.Message,), dict(

  OptionsEntry = _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ROLLSITEHEADER_OPTIONSENTRY,
    __module__ = 'transfer_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.transfer.RollSiteHeader.OptionsEntry)
    ))
  ,
  DESCRIPTOR = _ROLLSITEHEADER,
  __module__ = 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.eggroll.core.transfer.RollSiteHeader)
  ))
_sym_db.RegisterMessage(RollSiteHeader)
_sym_db.RegisterMessage(RollSiteHeader.OptionsEntry)


_ROLLSITEHEADER_OPTIONSENTRY._options = None

_TRANSFERSERVICE = _descriptor.ServiceDescriptor(
  name='TransferService',
  full_name='com.webank.eggroll.core.transfer.TransferService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=540,
  serialized_end=887,
  methods=[
  _descriptor.MethodDescriptor(
    name='send',
    full_name='com.webank.eggroll.core.transfer.TransferService.send',
    index=0,
    containing_service=None,
    input_type=_TRANSFERBATCH,
    output_type=_TRANSFERBATCH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='recv',
    full_name='com.webank.eggroll.core.transfer.TransferService.recv',
    index=1,
    containing_service=None,
    input_type=_TRANSFERBATCH,
    output_type=_TRANSFERBATCH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sendRecv',
    full_name='com.webank.eggroll.core.transfer.TransferService.sendRecv',
    index=2,
    containing_service=None,
    input_type=_TRANSFERBATCH,
    output_type=_TRANSFERBATCH,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSFERSERVICE)

DESCRIPTOR.services_by_name['TransferService'] = _TRANSFERSERVICE

# @@protoc_insertion_point(module_scope)