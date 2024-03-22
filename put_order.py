import json
import boto3

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    order_id = request_body['order_id']
    new_status = request_body['new_status']
    customer_name = request_body['customer_name']
    return {
        'statusCode': 200,
        'body': json.dumps(update_order_status_in_dynamodb(order_id, new_status, customer_name))
    }

def update_order_status_in_dynamodb(order_id, new_status, customer_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CoffeeOrders')

    try:
        table.update_item(
            Key={
                'OrderID': order_id,
                'CustomerName': customer_name
            },
            UpdateExpression='SET OrderStatus = :status',
            ExpressionAttributeValues={
                ":status": new_status
            }
        )
        return {'message': 'Order status updated successfully!', 'OrderId': order_id}
    except Exception as e:
        return {'error': str(e)}
