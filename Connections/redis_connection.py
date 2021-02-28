import redis
import logging

level = logging.DEBUG


def listen_and_generate():
    r = redis.Redis(host="172.20.0.6", port=6379, db=0, socket_keepalive=3000)
    pubsub = r.pubsub()
    pubsub.subscribe("jsonrows")

    f = open("final.json", "a")
    for message in pubsub.listen():
        if message.get("data") == 1:
            f.write("")
        else:
            f.writelines(message.get("data").decode('utf-8'))
            f.write("\n")
    logging.debug("final.json file created.")


if __name__ == "__main__":
    listen_and_generate()
