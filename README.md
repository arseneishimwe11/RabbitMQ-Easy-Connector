# 🐇 RabbitMQ Easy Connector  

A **lightweight and easy-to-use** Python library for sending and receiving messages using **RabbitMQ**.  
With just a few lines of code, you can **send and receive messages** without worrying about complex setup.  

---

## 🚀 Features  
✅ **Simple API** – Send & receive messages with minimal setup.  
✅ **Reusable Classes** – No need to write RabbitMQ boilerplate code.  
✅ **Auto Connection Handling** – Opens and closes connections automatically.  
✅ **Easily Extendable** – Modify as needed for your project.  

---

## 📦 Installation  

First, make sure you have **RabbitMQ** installed and running.  

### **1️⃣ Install Dependencies**  
```sh
pip install pika
```

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/rabbitmq-connector.git
cd rabbitmq-connector
```

## **3️⃣ Install the Package Locally**

```sh
pip install -e .
```

## 📌 Usage

### **1️⃣ Sending Messages (Producer)**

Create a file called send.py and use the following code:

```python
from rabbitmq_connector.producer import RabbitMQProducer

producer = RabbitMQProducer(queue_name="test_queue")
producer.send_message("Hello, RabbitMQ!")
producer.close()
```

### ✅ Output: 

```sh
 [✔] Sent: Hello, RabbitMQ!
```
 
### **2️⃣ Receiving Messages (Consumer) **
Create a file called **receive.py**: 

```python
from rabbitmq_connector.consumer import RabbitMQConsumer

def message_handler(ch, method, properties, body):
    print(f" [✔] Received: {body.decode()}")

consumer = RabbitMQConsumer(queue_name="test_queue")
consumer.start_consuming(message_handler)
```

### ✅ Output (when message is received): ###

```sh
 [✔] Received: Hello, RabbitMQ!
 ```

## 🛠 Project Structure

```markdown
rabbitmq_connector/
│── examples/
│   ├── send.py  # Example sender
│   ├── receive.py  # Example receiver
│── rabbitmq_connector/
│   ├── __init__.py
│   ├── producer.py  # Handles sending messages
│   ├── consumer.py  # Handles receiving messages
│── README.md  # Instructions
│── .gitignore
│── requirements.txt  # Dependencies
│── setup.py  # Packaging for easy installation
```

## 🐳 Docker Support (Optional) ##
Want to run this in Docker? Create a Dockerfile:

```dockerfile
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "examples/receive.py"]
```

### Build & Run

```sh
docker build -t rabbitmq-connector .
docker run rabbitmq-connector
```

## 💡 Future Enhancements ##
- Add async support using aio_pika
- Add error handling for robust messaging
- Provide integration with Django/FastAPI/Flask

## 🤝 Contributing ##
- Fork the repo & clone it
- Create a feature branch (git checkout -b feature-name)
- Commit changes (git commit -m 'Add new feature')
- Push to GitHub & open a PR

## 📜 License ##
This project is licensed under the MIT License.

## ⭐ Show Some Love ##
If you find this useful, please ⭐ star the repo and share! 🚀
