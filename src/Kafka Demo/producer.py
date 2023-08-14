from kafka import KafkaProducer
import json, time
from data import get_registed_user
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# if you have two partitions, you will use P0
# One consumer can consume from more than one partition
# same partition cant be assigned to multiple consumer in same group
'''def get_partition(key, all, available):
    return 0

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition)'''

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)


if __name__ == "__main__":
    while True:
        registered_user = get_registed_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)