import logging
from time import sleep
import pika
from pika.exchange_type import ExchangeType
import json
import uuid

logging.basicConfig(level=logging.WARNING)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
   exchange='order',
   exchange_type=ExchangeType.direct
)

while True:
   order = {
      'id': str(uuid.uuid4()),
      'user_email': 'john.doe@example.com',
      'product': 'Leather Jacket',
      'quantity': 1
   }

   channel.basic_publish(
      exchange='order',
      routing_key='order.notify',
      body=json.dumps({ 'user_email': order['user_email']})
   )
   logging.info(' [x] Sent notify message')

   channel.basic_publish(
      exchange='order',
      routing_key='order.report',
      body=json.dumps(order)
   )
   logging.info(' [x] Sent report message')
   sleep(1)
