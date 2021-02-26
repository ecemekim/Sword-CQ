import redis
import logging

level = logging.DEBUG


def listen_and_generate():
    r = redis.Redis(host="172.17.0.1", port=6379, db=0)
    pubsub = r.pubsub()
    pubsub.subscribe("jsonrows")

    f = open("final.json", "a")
    for message in pubsub.listen():
        if message.get("data") == 1:
            continue
        else:
            f.writelines(message.get("data").decode('utf-8'))
            f.write("\n")
    logging.debug("final.json file created in users directory.")


listen_and_generate()
