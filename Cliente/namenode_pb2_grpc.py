# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import namenode_pb2 as namenode__pb2


class NameNodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/NameNodeService/ListFiles',
                request_serializer=namenode__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=namenode__pb2.ListFilesResponse.FromString,
                )


class NameNodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameNodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=namenode__pb2.ListFilesRequest.FromString,
                    response_serializer=namenode__pb2.ListFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameNodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameNodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/ListFiles',
            namenode__pb2.ListFilesRequest.SerializeToString,
            namenode__pb2.ListFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)