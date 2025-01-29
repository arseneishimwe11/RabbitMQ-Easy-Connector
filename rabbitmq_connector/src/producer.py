import pika
from .config import RABBITMQ_CONFIG

class RabbitMQProducer:
    def __init__(self):
        self.credentials = pika.PlainCredentials(
            RABBITMQ_CONFIG['username'],
            RABBITMQ_CONFIG['password']
        )
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_CONFIG['host'],
                port=RABBITMQ_CONFIG['port'],
                credentials=self.credentials
            )
        )
        self.channel = self.connection.channel()

    def publish(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message
        )

    def close(self):
        if self.connection:
            self.connection.close()
