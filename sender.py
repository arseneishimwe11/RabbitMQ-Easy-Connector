import pika

# Connecting to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaring queue
channel.queue_declare(queue='test_queue')

# Sending message
message = "Hello from Sender! Mqtt ! "
channel.basic_publish(exchange='', routing_key='test_queue', body=message)

print(f" [x] Sent: {message}")

# Close connection
connection.close()
