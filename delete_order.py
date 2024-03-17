import json
import boto3

def lambda_handler(event, context):
    request_body = json_loads(event['body'])
    order_id = request_body['order_id']
    customer_name = request_body['customer_name']
    return {
        'statusCode': 200,
        'body': json.dumps(delete_order_from_dynamodb(order_id, customer_name))
    }

def delete_order_from_dynamodb(order_id, customer_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CoffeeOrders')

    try:
        table.delete_item(
          Key={
              'OrderId': order_id,
              'CustomerName': customer_name
          }
        )
        return {'message': 'Order deleted successfully!', 'OrderId': order_id}
    except Exception as e:
        return {'error': str(e)}
