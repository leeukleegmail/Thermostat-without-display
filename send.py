from umqtt.simple import MQTTClient
from config import queue_topic, mq_host, send_client


def send_message_to_queue(message):
    c = MQTTClient(send_client, mq_host)
    c.connect()
    message = bytes(str(message), 'utf-8')
    c.publish(str.encode(queue_topic), message, retain=True)
    # c.disconnect()

