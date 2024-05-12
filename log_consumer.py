import pika
import json

# On call load the message to file
def on_message_received(ch, method, properties, body):
    log = json.loads(body)
    log_file = f"Logs/{log['status']}_logs.txt"
    with open(log_file,'a') as file:
        file.write(f"{log['timestamp']};{log['message']}\n")
        print(f"Processed log {log['status']}:{log['message']}")

# Start consuming the rabbitMQ
def start_consuming():
    connection = None
    try:
        params = pika.ConnectionParameters('localhost')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        for status in ['info', 'warning', 'error']:
            channel.queue_declare(queue=f"{status}_logs", durable=True)
            channel.basic_consume(queue=f"{status}_logs", auto_ack=True, on_message_callback=on_message_received)

        print(f"Starting Consuming Messages")
        channel.start_consuming()
    except KeyboardInterrupt:
        print('the consumer stoped manually')


if __name__ == "__main__":
    start_consuming()


