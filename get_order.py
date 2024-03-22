import json
import boto3

def lambda_handler(event, context):
  return {
    'statusCode: 200,
    'body': json.dumps(get_orders_from_dynamodb())
  }

def get_orders_from_dynamodb():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CoffeeOrders')

    try:
        response = table.scan()
        orders = response['Items']
        return orders
    except Exception as e:
        return {'error': str(e)}
