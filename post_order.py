import json
import boto3
import uuid

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    customer_name = request.body['customer_name']
    coffee_blend = request_body['coffee_blend']
    return {
        'statusCode': 200,
        'body': json.dumps(create_order_in_dynamodb(customer_name, coffee_blend))
    }

def create_order_in_dynamodb(customer_name, coffee_blend):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CoffeeOrders')

    order_id = str(uuid.uuid4())

    try:
      table.put_item(
          Item={
              'OrderID': order_id,
              'CustomerName': customer_name,
              'CoffeBlend': coffee_blend,
              'Order_Status': Pending
          }
      )
      return {'message': 'Order created successfully!', 'OrderId': order_id}
    except Exception as e:
        return {'error': str(e)}
