import pika
import json
import re

def parse_log(message):
    match = re.search(r"ERROR|WARN|INFO", message)
    if match:
        print(f"Anomaly Detected: {match.group()}")
    else:
        print("No anomaly found.")

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Received log: {message}")
    parse_log(message)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='log_queue')

    channel.basic_consume(queue='log_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
