# producer.py

import json

from kafka import KafkaProducer


class Notification:
    def __init__(self):
        self.topic = "arc-rte-notifications"
        broker_url = ["arc-kafka.pt-staging.com:9092"]
        self.__producer = KafkaProducer(
            bootstrap_servers=broker_url,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send_notification(self, notification_type, payload):
        if notification_type == "LOGIN_SUCCESSFUL": 
            self.__producer.send(self.topic, payload)
            self.__producer.flush()
            return True
        else:
            return False
