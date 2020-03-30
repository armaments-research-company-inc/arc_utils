# producer.py

import json
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from kafka import KafkaProducer
from kafka import KafkaProducer
from schema import Schema



login_schema = Schema({
                "type": "LOGIN_SUCCESSFUL",
                "payload":
                {
                    "user_email": str,
                    "app_name": str
                }
                })
class Notification:
    def __init__(self,broker_url):
        self.schema_list={"LOGIN_SUCCESSFUL":login_schema}
        self.topic = "arc-rte-notifications"
        
        self.__producer = KafkaProducer(
            bootstrap_servers=self.get_kafka_brokers(broker_url),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
    def get_kafka_brokers(self, brokers):
        return [
            "{}:{}".format(parsedUrl.hostname, parsedUrl.port)
            for parsedUrl in [urlparse(url) for url in brokers]
        ]
    def send_notification(self, notification_type, payload):
        if self.schema_list[notification_type].validate(payload): 
            self.__producer.send(self.topic, payload)
            self.__producer.flush()
        