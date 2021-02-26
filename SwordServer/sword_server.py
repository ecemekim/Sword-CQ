from concurrent import futures
import logging

import json
import redis
import grpc

import sword_pb2
import sword_pb2_grpc


class Sword(sword_pb2_grpc.SwordServicer):
    r = redis.Redis(host="localhost", port=6379, db=0)

    def DumpJsons(self, request, context):
        for i in range(1, 11):
            with open(f"./users/{i}.json", "r") as f:
                file = json.load(f)
            for message in file:
                self.r.publish("jsonrows", json.dumps(message))
        return sword_pb2.Message(message="Success.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sword_pb2_grpc.add_SwordServicer_to_server(Sword(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
