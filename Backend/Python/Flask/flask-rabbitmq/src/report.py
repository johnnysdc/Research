import logging
import pika
from pika.adapters.blocking_connection import BlockingChannel
import json

logging.basicConfig(level=logging.WARNING)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue = channel.queue_declare('order_report')
queue_name = queue.method.queue

channel.queue_bind(
   exchange='order',
   queue=queue_name,
   routing_key='order.report'
)

def callback(ch: BlockingChannel, method, properties, body):
   payload = json.loads(body)
   logging.info(' [x] Generating report')
   logging.info({
      'ID': payload.get('id'),
      'User Email': payload.get('user_email'),
      'Product': payload.get('product'),
      'Quantity': payload.get('quantity')
   })

   logging.info(' [x] Done')
   
   ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
   queue=queue_name,
   on_message_callback=callback
)

logging.info(' [*] Waiting for report messages. To exit press CTRL + C')

channel.start_consuming()
