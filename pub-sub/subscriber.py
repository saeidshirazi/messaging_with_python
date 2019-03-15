import json

import message_queue
import pika

def my_worker(channel, method, properties, body):
    print (json.loads(body))

if __name__ == '__main__':

    adapter = message_queue.AMQPAdapter(host='127.0.0.1')
    adapter.configurate_queue(queue='python.publish.test')
    subscriber = message_queue.Subscriber(adapter)
    # Print message
    subscriber.consume(my_worker)