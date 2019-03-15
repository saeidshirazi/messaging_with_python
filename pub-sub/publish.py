import message_queue
import pika

if __name__ == '__main__':

    adapter = message_queue.AMQPAdapter(host='127.0.0.1')
    # Configurate queue
    adapter.configurate_queue(queue='python.publish.test')
    # Instantiate publisher
    publisher = message_queue.Publisher(adapter)

    # Create a new message
    message = message_queue.Message(
    {
        'id': 12345,
        'message': 'welcome to integration system class'
    }

    )

    # Publish message
    publisher.publish(message)
