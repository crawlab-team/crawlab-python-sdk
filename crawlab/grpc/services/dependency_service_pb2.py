# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/dependency_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crawlab.grpc.entity import response_pb2 as entity_dot_response__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!services/dependency_service.proto\x12\x04grpc\x1a\x15\x65ntity/response.proto\"+\n\nDependency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"3\n\x1f\x44\x65pendencyServiceConnectRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\"\x90\x01\n DependencyServiceConnectResponse\x12)\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1b.grpc.DependencyServiceCode\x12\x0c\n\x04lang\x18\x02 \x01(\t\x12\r\n\x05proxy\x18\x03 \x01(\t\x12$\n\ndependency\x18\x04 \x01(\x0b\x32\x10.grpc.Dependency\"f\n\x1c\x44\x65pendencyServiceSyncRequest\x12\x10\n\x08node_key\x18\x01 \x01(\t\x12\x0c\n\x04lang\x18\x02 \x01(\t\x12&\n\x0c\x64\x65pendencies\x18\x03 \x03(\x0b\x32\x10.grpc.Dependency\"I\n\"DependencyServiceUpdateLogsRequest\x12\x15\n\rdependency_id\x18\x01 \x01(\t\x12\x0c\n\x04logs\x18\x02 \x03(\t*=\n\x15\x44\x65pendencyServiceCode\x12\x08\n\x04SYNC\x10\x00\x12\x0b\n\x07INSTALL\x10\x01\x12\r\n\tUNINSTALL\x10\x02\x32\xfb\x01\n\x11\x44\x65pendencyService\x12\\\n\x07\x43onnect\x12%.grpc.DependencyServiceConnectRequest\x1a&.grpc.DependencyServiceConnectResponse\"\x00\x30\x01\x12<\n\x04Sync\x12\".grpc.DependencyServiceSyncRequest\x1a\x0e.grpc.Response\"\x00\x12J\n\nUpdateLogs\x12(.grpc.DependencyServiceUpdateLogsRequest\x1a\x0e.grpc.Response\"\x00(\x01\x42\x08Z\x06.;grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.dependency_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\006.;grpc'
  _globals['_DEPENDENCYSERVICECODE']._serialized_start=490
  _globals['_DEPENDENCYSERVICECODE']._serialized_end=551
  _globals['_DEPENDENCY']._serialized_start=66
  _globals['_DEPENDENCY']._serialized_end=109
  _globals['_DEPENDENCYSERVICECONNECTREQUEST']._serialized_start=111
  _globals['_DEPENDENCYSERVICECONNECTREQUEST']._serialized_end=162
  _globals['_DEPENDENCYSERVICECONNECTRESPONSE']._serialized_start=165
  _globals['_DEPENDENCYSERVICECONNECTRESPONSE']._serialized_end=309
  _globals['_DEPENDENCYSERVICESYNCREQUEST']._serialized_start=311
  _globals['_DEPENDENCYSERVICESYNCREQUEST']._serialized_end=413
  _globals['_DEPENDENCYSERVICEUPDATELOGSREQUEST']._serialized_start=415
  _globals['_DEPENDENCYSERVICEUPDATELOGSREQUEST']._serialized_end=488
  _globals['_DEPENDENCYSERVICE']._serialized_start=554
  _globals['_DEPENDENCYSERVICE']._serialized_end=805
# @@protoc_insertion_point(module_scope)
