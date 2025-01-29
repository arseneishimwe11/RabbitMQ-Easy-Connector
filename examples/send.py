from rabbitmq_connector.producer import RabbitMQProducer

producer = RabbitMQProducer(queue_name="test_queue")
producer.send_message("Hello, RabbitMQ!")
producer.close()
