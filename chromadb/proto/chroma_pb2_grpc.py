# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chromadb.proto import chroma_pb2 as chromadb_dot_proto_dot_chroma__pb2


class VectorReaderStub(object):
    """Vector Reader Interface 

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVectors = channel.unary_unary(
                '/chroma.VectorReader/GetVectors',
                request_serializer=chromadb_dot_proto_dot_chroma__pb2.GetVectorsRequest.SerializeToString,
                response_deserializer=chromadb_dot_proto_dot_chroma__pb2.GetVectorsResponse.FromString,
                )
        self.QueryVectors = channel.unary_unary(
                '/chroma.VectorReader/QueryVectors',
                request_serializer=chromadb_dot_proto_dot_chroma__pb2.QueryVectorsRequest.SerializeToString,
                response_deserializer=chromadb_dot_proto_dot_chroma__pb2.QueryVectorsResponse.FromString,
                )


class VectorReaderServicer(object):
    """Vector Reader Interface 

    """

    def GetVectors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryVectors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorReaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVectors': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVectors,
                    request_deserializer=chromadb_dot_proto_dot_chroma__pb2.GetVectorsRequest.FromString,
                    response_serializer=chromadb_dot_proto_dot_chroma__pb2.GetVectorsResponse.SerializeToString,
            ),
            'QueryVectors': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryVectors,
                    request_deserializer=chromadb_dot_proto_dot_chroma__pb2.QueryVectorsRequest.FromString,
                    response_serializer=chromadb_dot_proto_dot_chroma__pb2.QueryVectorsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chroma.VectorReader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorReader(object):
    """Vector Reader Interface 

    """

    @staticmethod
    def GetVectors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chroma.VectorReader/GetVectors',
            chromadb_dot_proto_dot_chroma__pb2.GetVectorsRequest.SerializeToString,
            chromadb_dot_proto_dot_chroma__pb2.GetVectorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryVectors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chroma.VectorReader/QueryVectors',
            chromadb_dot_proto_dot_chroma__pb2.QueryVectorsRequest.SerializeToString,
            chromadb_dot_proto_dot_chroma__pb2.QueryVectorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
