import pika
import json
from datetime import datetime


class RabbitMQLogger:
    def __init__(self, host='localhost'):
        # Establish connection parameters and create the connection and channel
        self.connection_params = pika.ConnectionParameters(host)
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()

        # Declare queues for different log levels
        self.setup_queues()

    def setup_queues(self):
        # Declare three separate queues for different log levels
        levels = ['info', 'warning', 'error']
        for level in levels:
            self.channel.queue_declare(queue=f"{level}_logs", durable=True)

    def send_log(self, message, status):
        # Ensure the status is one of the predefined levels
        if status not in ['info', 'warning', 'error']:
            raise ValueError("Invalid log status. Use 'info', 'warning', or 'error'.")

        # Prepare the message
        enhanced_message = json.dumps({
            'timestamp': datetime.now().isoformat(),
            'message': message,
            'status': status
        })

        # Publish the message to the appropriate queue
        self.channel.basic_publish(
            exchange='',
            routing_key=f"{status}_logs",
            body=enhanced_message,
            properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
        )
        print(f"Sent log {status}: {message}")

    def __del__(self):
        # Close the connection when it's no longer needed
        if self.connection.is_open:
            self.connection.close()
            print("RabbitMQ connection closed.")


# Example usage within the poker application:
if __name__ == '__main__':
    logger = RabbitMQLogger()
    logger.send_log("Starting new game", "info")
    logger.send_log("Invalid move attempted", "warning")
    logger.send_log("Database connection failed", "error")
