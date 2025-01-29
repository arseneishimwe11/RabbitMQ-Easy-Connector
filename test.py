from rabbitmq_easy_connector import RabbitMQConnector

# Initialize RabbitMQ connection
rabbit = RabbitMQConnector(host='localhost', queue='test_queue')

# Producer: Sending a message
rabbit.send_message("Hello from RabbitMQ Easy Connector!")

# Consumer: Receiving a message
def handle_message(body):
    print(f"Received: {body}")

rabbit.start_consumer(callback=handle_message)
