from kafka import KafkaConsumer
from kafka.errors import KafkaError

import sys
import threading
import json

running = True
conf = {'bootstrap.servers': "localhost:9092",
        'auto.offset.reset': 'smallest',
        'group.id': "user_group"}

topic = 'topic_task_notification'


class NotificationConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.consumer = KafkaConsumer(conf)

    def run(self):
        print('Inside Notification Consumer Service :  Created Listener ')
        try:

            self.consumer.subscribe(topic)
            while running:
                # Poll for message
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue
                # Handle Error
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                         (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaError(msg.error())
                else:
                    # Handle Message
                    print('---------> Got message Sending email.....')
                    message = json.loads(msg.value().decode('utf-8'))
                    # In Real world, write email sending logic here
                    print(message)
        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()
