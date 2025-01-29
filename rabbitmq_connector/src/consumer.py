import pika

class RabbitMQConsumer:
    def __init__(self, queue_name='default_queue', host='localhost'):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def start_consuming(self, callback):
        print(f" [*] Waiting for messages in {self.queue_name}. To exit, press CTRL+C")
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()
    
    def close(self):
        self.connection.close()
