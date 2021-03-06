import time
import grpc
import logging

from sword_pb2 import Message
from sword_pb2_grpc import SwordStub

level = logging.DEBUG


def run():
    start = time.time()
    with grpc.insecure_channel('172.20.0.5:50051', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub = SwordStub(channel)
        response = stub.GetServerResponse(Message(message='ecem'))

    stop = time.time()
    _time = stop - start
    print("Sword client received: " + response.message)
    logging.debug(f"RUNTIME: {_time} seconds!")
    return _time
