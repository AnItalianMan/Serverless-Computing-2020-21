from datetime import datetime
import pika

def send_message(channel, queue, data):
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=bytes(data, encoding='utf8'))


def create_connection():
    credentials = pika.PlainCredentials("admin", "serverlessistheway")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.56.1', port=5672, credentials=credentials))
    return connection.channel()


def get_danger(x):
    return (x - 200) * (3 - 1) / (1000 - 200) + 1


def generate_message(danger, body):
    if danger == 1:
        severity = "LOW"
    elif danger == 2:
        severity = "MEDIUM"
    elif danger == 3:
        severity = "HIGH"
    else:
        severity = "ERROR"

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return f"INFO - Danger: {severity} - Sensor value: {body} - Date: {dt_string}"


def handler(context, event):
    body = int(event.body.decode())
    context.logger.info(f'Received body: {body}')
    danger = int(get_danger(body))
    context.logger.info(f'Danger body: {danger}')
    message = generate_message(danger, body)
    context.logger.info(f'Generated message: {message}')
    channel = create_connection()
    context.logger.info('Sending message for log queue')
    send_message(channel, "log", message)
    if danger == 3:
        context.logger.info('Sending message for alarm queue')
        send_message(channel, "alarm", message)
    return
