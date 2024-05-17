import json

print('Loading function')


def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": "This is a test"
    }

    return response
