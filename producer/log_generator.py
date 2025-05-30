import random, time

services = ["auth-service", "payment-service", "order-service"]
levels = ["INFO", "DEBUG", "WARN", "ERROR"]
messages = [
    "User login successful", "Payment gateway timeout",
    "Order placed", "RabbitMQ connection reset", 
    "Database query took too long", "Unauthorized access attempt"
]

with open("logs.txt", "a") as f:
    while True:
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {random.choice(levels)} | {random.choice(services)} | {random.choice(messages)}\n"
        f.write(line)
        f.flush()
        time.sleep(1)
