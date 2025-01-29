import pika

def callback(ch, method, properties, body):
    print(f" [x] Received: {body.decode()}")

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='test_queue')

# Consume messages
channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
