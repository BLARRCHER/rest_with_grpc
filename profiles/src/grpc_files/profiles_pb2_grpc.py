# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import profiles_pb2 as profiles__pb2


class ProfilesStub(object):
    """Comment for the service"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
            "/profiles.Profiles/Register",
            request_serializer=profiles__pb2.RegisterCredentials.SerializeToString,
            response_deserializer=profiles__pb2.BooleanReply.FromString,
        )
        self.Get = channel.unary_unary(
            "/profiles.Profiles/Get",
            request_serializer=profiles__pb2.GettingRequest.SerializeToString,
            response_deserializer=profiles__pb2.UserReply.FromString,
        )
        self.ChangeEMail = channel.unary_unary(
            "/profiles.Profiles/ChangeEMail",
            request_serializer=profiles__pb2.ChangeEmailRequest.SerializeToString,
            response_deserializer=profiles__pb2.BooleanReply.FromString,
        )
        self.UpdateProfile = channel.unary_unary(
            "/profiles.Profiles/UpdateProfile",
            request_serializer=profiles__pb2.UpdateProfileRequest.SerializeToString,
            response_deserializer=profiles__pb2.BooleanReply.FromString,
        )
        self.GetProfiles = channel.unary_stream(
            "/profiles.Profiles/GetProfiles",
            request_serializer=profiles__pb2.GettingProfilesRequest.SerializeToString,
            response_deserializer=profiles__pb2.UserReply.FromString,
        )
        self.DeleteProfile = channel.unary_unary(
            "/profiles.Profiles/DeleteProfile",
            request_serializer=profiles__pb2.GettingRequest.SerializeToString,
            response_deserializer=profiles__pb2.BooleanReply.FromString,
        )
        self.UploadAvatar = channel.unary_unary(
            "/profiles.Profiles/UploadAvatar",
            request_serializer=profiles__pb2.UploadFileRequest.SerializeToString,
            response_deserializer=profiles__pb2.BooleanReply.FromString,
        )
        self.DownloadAvatar = channel.unary_unary(
            "/profiles.Profiles/DownloadAvatar",
            request_serializer=profiles__pb2.GettingRequest.SerializeToString,
            response_deserializer=profiles__pb2.FileResponse.FromString,
        )


class ProfilesServicer(object):
    """Comment for the service"""

    def Register(self, request, context):
        """Comment for the procedure."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ChangeEMail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetProfiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UploadAvatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DownloadAvatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProfilesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Register": grpc.unary_unary_rpc_method_handler(
            servicer.Register,
            request_deserializer=profiles__pb2.RegisterCredentials.FromString,
            response_serializer=profiles__pb2.BooleanReply.SerializeToString,
        ),
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=profiles__pb2.GettingRequest.FromString,
            response_serializer=profiles__pb2.UserReply.SerializeToString,
        ),
        "ChangeEMail": grpc.unary_unary_rpc_method_handler(
            servicer.ChangeEMail,
            request_deserializer=profiles__pb2.ChangeEmailRequest.FromString,
            response_serializer=profiles__pb2.BooleanReply.SerializeToString,
        ),
        "UpdateProfile": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateProfile,
            request_deserializer=profiles__pb2.UpdateProfileRequest.FromString,
            response_serializer=profiles__pb2.BooleanReply.SerializeToString,
        ),
        "GetProfiles": grpc.unary_stream_rpc_method_handler(
            servicer.GetProfiles,
            request_deserializer=profiles__pb2.GettingProfilesRequest.FromString,
            response_serializer=profiles__pb2.UserReply.SerializeToString,
        ),
        "DeleteProfile": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteProfile,
            request_deserializer=profiles__pb2.GettingRequest.FromString,
            response_serializer=profiles__pb2.BooleanReply.SerializeToString,
        ),
        "UploadAvatar": grpc.unary_unary_rpc_method_handler(
            servicer.UploadAvatar,
            request_deserializer=profiles__pb2.UploadFileRequest.FromString,
            response_serializer=profiles__pb2.BooleanReply.SerializeToString,
        ),
        "DownloadAvatar": grpc.unary_unary_rpc_method_handler(
            servicer.DownloadAvatar,
            request_deserializer=profiles__pb2.GettingRequest.FromString,
            response_serializer=profiles__pb2.FileResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("profiles.Profiles", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Profiles(object):
    """Comment for the service"""

    @staticmethod
    def Register(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/Register",
            profiles__pb2.RegisterCredentials.SerializeToString,
            profiles__pb2.BooleanReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Get(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/Get",
            profiles__pb2.GettingRequest.SerializeToString,
            profiles__pb2.UserReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ChangeEMail(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/ChangeEMail",
            profiles__pb2.ChangeEmailRequest.SerializeToString,
            profiles__pb2.BooleanReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateProfile(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/UpdateProfile",
            profiles__pb2.UpdateProfileRequest.SerializeToString,
            profiles__pb2.BooleanReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetProfiles(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/profiles.Profiles/GetProfiles",
            profiles__pb2.GettingProfilesRequest.SerializeToString,
            profiles__pb2.UserReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteProfile(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/DeleteProfile",
            profiles__pb2.GettingRequest.SerializeToString,
            profiles__pb2.BooleanReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UploadAvatar(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/UploadAvatar",
            profiles__pb2.UploadFileRequest.SerializeToString,
            profiles__pb2.BooleanReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DownloadAvatar(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/profiles.Profiles/DownloadAvatar",
            profiles__pb2.GettingRequest.SerializeToString,
            profiles__pb2.FileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )