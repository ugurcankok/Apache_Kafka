from kafka import KafkaProducer
import json, time
from data import get_registed_user
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partition(key, all, available):
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition)


if __name__ == "__main__":
    while True:
        registered_user = get_registed_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)