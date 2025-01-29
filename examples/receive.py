from rabbitmq_connector.consumer import RabbitMQConsumer

def message_handler(ch, method, properties, body):
    print(f" [✔] Received: {body.decode()}")

consumer = RabbitMQConsumer(queue_name="test_queue")
consumer.start_consuming(message_handler)
