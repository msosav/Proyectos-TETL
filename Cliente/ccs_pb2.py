# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ccs.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tccs.proto\"T\n\x0fTransferRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\tfile_data\x18\x02 \x01(\x0c\x12\x1b\n\x13\x63urrent_replication\x18\x04 \x01(\x05\"#\n\x10TransferResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\nurlRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"\x1a\n\x0burlResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\"5\n\x13SaveNodeFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"\'\n\x14SaveNodeFileResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb2\x01\n\x13\x46ileTransferService\x12\x35\n\x0cTransferFile\x12\x10.TransferRequest\x1a\x11.TransferResponse\"\x00\x12%\n\x06GetUrl\x12\x0b.urlRequest\x1a\x0c.urlResponse\"\x00\x12=\n\x0cSaveNodeFile\x12\x14.SaveNodeFileRequest\x1a\x15.SaveNodeFileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ccs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRANSFERREQUEST']._serialized_start=13
  _globals['_TRANSFERREQUEST']._serialized_end=97
  _globals['_TRANSFERRESPONSE']._serialized_start=99
  _globals['_TRANSFERRESPONSE']._serialized_end=134
  _globals['_URLREQUEST']._serialized_start=136
  _globals['_URLREQUEST']._serialized_end=167
  _globals['_URLRESPONSE']._serialized_start=169
  _globals['_URLRESPONSE']._serialized_end=195
  _globals['_SAVENODEFILEREQUEST']._serialized_start=197
  _globals['_SAVENODEFILEREQUEST']._serialized_end=250
  _globals['_SAVENODEFILERESPONSE']._serialized_start=252
  _globals['_SAVENODEFILERESPONSE']._serialized_end=291
  _globals['_FILETRANSFERSERVICE']._serialized_start=294
  _globals['_FILETRANSFERSERVICE']._serialized_end=472
# @@protoc_insertion_point(module_scope)
