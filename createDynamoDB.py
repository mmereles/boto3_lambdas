import boto3

def create_table():
    dynamodb = boto3.client('dynamodb')
    
    response = dynamodb.create_table(
        AttributeDefinitions =[
            {   
                'AttributeName': 'OrderID',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'CustomerName',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'OrderID',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'CustomerName',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        TableName='CoffeOrders',
    )
    
    print('Successfully created DB')
