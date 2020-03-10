# producer.py

import json

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from kafka import KafkaProducer


class KafkaLogProducer:
    def __init__(self, brokers):

        self.topic = "niobrara-70979.elastic-log"
        self.__producer = KafkaProducer(
            api_version=(2, 2, 1),
            bootstrap_servers=self.get_kafka_brokers(brokers),
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            batch_size=0,  # Speed optimization to not batch data before sending
            acks=1,  # Speed optimization so the producer does minimal acknowledgement checks
        )

    def get_kafka_brokers(self, brokers):
        """
        Parses the KAKFA_URL and returns a list of hostname:port pairs in the format
        that kafka-python expects.
        """

        return [
            "{}:{}".format(parsedUrl.hostname, parsedUrl.port)
            for parsedUrl in [urlparse(url) for url in brokers]
        ]

    def produce_log(self, index="", doc={}, doc_type=""):

        assert index != ""

        # data = {"index": index, "doc": json.dumps(doc), "doc_type": doc_type}
        self.__producer.send(self.topic, doc)
        self.__producer.flush()
