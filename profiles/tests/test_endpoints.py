"""
Integration tests for gRPC
"""
import os
from unittest import TestCase
import uuid

import grpc
import names

from grpc_files import profiles_pb2, profiles_pb2_grpc

from randoms import random_email, random_phone
from utils.reply import reply_to_dict
from ..src.logger import logger


class TestEndpoints(TestCase):
    def setUp(self) -> None:
        host = os.environ["PROFILES_SERVICE_HOST"]
        port = os.environ.get("PROFILES_SERVICE_PORT", 50051)
        self.host_port = f"{host}:{port}"

    def _register(self, id_):
        with grpc.insecure_channel(self.host_port) as channel:
            stub = profiles_pb2_grpc.ProfilesStub(channel)
            name1 = names.get_first_name()
            name2 = names.get_last_name()
            name3 = names.get_first_name()
            email = random_email()
            phone = random_phone()
            all_attrs = {
                "id": id_,
                "first_name": name1,
                "family_name": name2,
                "father_name": name3,
                "email": email,
                "phone": phone,
            }
            response = stub.Register(profiles_pb2.RegisterCredentials(**all_attrs))

            logger.info("Client received: %s", response.success)
            return all_attrs

    def _get(self, id_):
        with grpc.insecure_channel(self.host_port) as channel:
            stub = profiles_pb2_grpc.ProfilesStub(channel)
            response = stub.Get(profiles_pb2.GettingRequest(id=id_))

            logger.info("Client received: %s", response)
            return response

    def _delete(self, id_):
        with grpc.insecure_channel(self.host_port) as channel:
            stub = profiles_pb2_grpc.ProfilesStub(channel)
            response = stub.DeleteProfile(profiles_pb2.GettingRequest(id=id_))

            logger.info("Client received: %s", response)
            return response

    def test_register(self):
        id_ = str(uuid.uuid4())
        inserted = self._register(id_)
        self.assertIsNotNone(inserted)

    def test_get(self):
        id_ = str(uuid.uuid4())
        inserted = self._register(id_)
        got = self._get(id_)
        got_dict = reply_to_dict(got)
        if inserted["phone"] is None:
            inserted["phone"] = ""  # Because gRPC Reply converts None to ''.
        self.assertDictEqual(inserted, got_dict)

    def test_delete(self):
        id_ = str(uuid.uuid4())
        inserted = self._register(id_)
        deleted = self._delete(id_)
        self.assertTrue(deleted)

    def get_default_avatar(self):
        id_ = str(uuid.uuid4())
        inserted = self._register(id_)
