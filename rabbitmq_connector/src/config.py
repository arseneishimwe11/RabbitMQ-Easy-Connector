from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_CONFIG = {
    'host': os.getenv('RABBITMQ_HOST', 'localhost'),
    'port': int(os.getenv('RABBITMQ_PORT', 5672)),
    'username': os.getenv('RABBITMQ_USER', 'guest'),
    'password': os.getenv('RABBITMQ_PASS', 'guest')
}
