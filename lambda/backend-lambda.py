import boto3
import json

print('Loading function')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    print(event)
    table = dynamodb.Table('ServerlessApplicationCdkStack-Users0A0EEA89-EPF37SQEPAKR')
    print(event['requestContext']['http']['method'])
    if event['requestContext']['http']['method'] == 'GET':
        # Read user information
        try:
            # Assuming user ID is in query string
            user_id = event['queryStringParameters']['userId']
            response = table.get_item(Key={'userId': user_id})
            # Check for successful retrieval and return user data or error message
            if 'Item' in response:
                return {
                    'statusCode': 200,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    'body': json.dumps(response['Item'])
                }
            else:
                return {
                    'statusCode': 404,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    'body': json.dumps({'message': 'User not found'})
                }
        except KeyError:
            # Handle missing user ID or other potential errors
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required parameter: userId'})
            }
    elif event['requestContext']['http']['method'] == 'POST':
        # Write user information (assuming data is in the request body)
        try:
            user_data = json.loads(event['body'])
            print(user_data)
            table.put_item(Item=user_data)
            return {
                'statusCode': 201,
                "headers": {
                    "Content-Type": "application/json"
                },
                'body': json.dumps({'message': 'User created successfully'})
            }
        except json.JSONDecodeError:
            # Handle invalid JSON data in the request body
            return {
                'statusCode': 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                'body': json.dumps({'message': 'Invalid JSON data provided'})
            }
    else:
        # Handle unsupported HTTP methods
        return {
            'statusCode': 405,
            "headers": {
                "Content-Type": "application/json"
            },
            'body': json.dumps({'message': 'Method not allowed'})
        }
