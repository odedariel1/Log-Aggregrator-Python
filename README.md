# Log Aggregrator Project 
## How do I get set up? ###
first Run poker-poker-project.main.py in your python compiler (i used Pycharm) \n
then follow the steps in the console (so the producer wiil create some messages to the queues)
then run the log_consumer.py (so the file will create in your project)
then run main.py or consolemain.py (to your choise) to see the results!

### Instructions

* Description: Create a log aggregator that collects log messages from multiple sources, processes them, and stores them in files using RabbitMQ as the messaging queue system. This project will help you understand file handling, RabbitMQ integration, and distributed systems communication.

Features:

* Log Message Producer:

Simulate multiple applications or services that produce log messages.

Generate log messages with various levels (info, warning, error) and timestamps.

RabbitMQ Integration:

Set up RabbitMQ queues to receive log messages from producers.

Use the Pika library in Python for RabbitMQ integration.

* Log Message Processor:

Create a consumer to process incoming log messages.

Parse log messages and perform actions based on severity (e.g., send alerts for errors).

Implement logging to track the processing of messages.

* File Writing:

Store processed log messages in separate files based on severity and/or time intervals.

Use Python's file handling capabilities to write log messages to files.

* Monitoring and Dashboard (Optional):

Create a simple monitoring system to track incoming log messages and processed logs.

Develop a dashboard to visualize log statistics such as message counts, error rates, etc.
