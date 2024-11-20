# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from crawlab.grpc.entity import model_service_request_pb2 as entity_dot_model__service__request__pb2
from crawlab.grpc.entity import response_pb2 as entity_dot_response__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in services/model_base_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ModelBaseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetById = channel.unary_unary(
                '/grpc.ModelBaseService/GetById',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceGetByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.GetOne = channel.unary_unary(
                '/grpc.ModelBaseService/GetOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceGetOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.GetMany = channel.unary_unary(
                '/grpc.ModelBaseService/GetMany',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceGetManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.DeleteById = channel.unary_unary(
                '/grpc.ModelBaseService/DeleteById',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceDeleteByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.DeleteOne = channel.unary_unary(
                '/grpc.ModelBaseService/DeleteOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceDeleteOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.DeleteMany = channel.unary_unary(
                '/grpc.ModelBaseService/DeleteMany',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceDeleteManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.UpdateById = channel.unary_unary(
                '/grpc.ModelBaseService/UpdateById',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceUpdateByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.UpdateOne = channel.unary_unary(
                '/grpc.ModelBaseService/UpdateOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceUpdateOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.UpdateMany = channel.unary_unary(
                '/grpc.ModelBaseService/UpdateMany',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceUpdateManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.ReplaceById = channel.unary_unary(
                '/grpc.ModelBaseService/ReplaceById',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceReplaceByIdRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.ReplaceOne = channel.unary_unary(
                '/grpc.ModelBaseService/ReplaceOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceReplaceOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.InsertOne = channel.unary_unary(
                '/grpc.ModelBaseService/InsertOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceInsertOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.InsertMany = channel.unary_unary(
                '/grpc.ModelBaseService/InsertMany',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceInsertManyRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.UpsertOne = channel.unary_unary(
                '/grpc.ModelBaseService/UpsertOne',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceUpsertOneRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)
        self.Count = channel.unary_unary(
                '/grpc.ModelBaseService/Count',
                request_serializer=entity_dot_model__service__request__pb2.ModelServiceCountRequest.SerializeToString,
                response_deserializer=entity_dot_response__pb2.Response.FromString,
                _registered_method=True)


class ModelBaseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplaceOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertMany(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpsertOne(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelBaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetById,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceGetByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'GetOne': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceGetOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'GetMany': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMany,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceGetManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteById': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteById,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceDeleteByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteOne': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceDeleteOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'DeleteMany': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMany,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceDeleteManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateById': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateById,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceUpdateByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateOne': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceUpdateOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpdateMany': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMany,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceUpdateManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'ReplaceById': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceById,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceReplaceByIdRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'ReplaceOne': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplaceOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceReplaceOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'InsertOne': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceInsertOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'InsertMany': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertMany,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceInsertManyRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'UpsertOne': grpc.unary_unary_rpc_method_handler(
                    servicer.UpsertOne,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceUpsertOneRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=entity_dot_model__service__request__pb2.ModelServiceCountRequest.FromString,
                    response_serializer=entity_dot_response__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ModelBaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpc.ModelBaseService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ModelBaseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/GetById',
            entity_dot_model__service__request__pb2.ModelServiceGetByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/GetOne',
            entity_dot_model__service__request__pb2.ModelServiceGetOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/GetMany',
            entity_dot_model__service__request__pb2.ModelServiceGetManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/DeleteById',
            entity_dot_model__service__request__pb2.ModelServiceDeleteByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/DeleteOne',
            entity_dot_model__service__request__pb2.ModelServiceDeleteOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/DeleteMany',
            entity_dot_model__service__request__pb2.ModelServiceDeleteManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/UpdateById',
            entity_dot_model__service__request__pb2.ModelServiceUpdateByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/UpdateOne',
            entity_dot_model__service__request__pb2.ModelServiceUpdateOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/UpdateMany',
            entity_dot_model__service__request__pb2.ModelServiceUpdateManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReplaceById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/ReplaceById',
            entity_dot_model__service__request__pb2.ModelServiceReplaceByIdRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReplaceOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/ReplaceOne',
            entity_dot_model__service__request__pb2.ModelServiceReplaceOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InsertOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/InsertOne',
            entity_dot_model__service__request__pb2.ModelServiceInsertOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InsertMany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/InsertMany',
            entity_dot_model__service__request__pb2.ModelServiceInsertManyRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpsertOne(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/UpsertOne',
            entity_dot_model__service__request__pb2.ModelServiceUpsertOneRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/grpc.ModelBaseService/Count',
            entity_dot_model__service__request__pb2.ModelServiceCountRequest.SerializeToString,
            entity_dot_response__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
