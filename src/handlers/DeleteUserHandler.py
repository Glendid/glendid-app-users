
from boto3.dynamodb.conditions import Key
import boto3
import json
import os

def delete_user(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    USERS_TABLE = dynamodb.Table(os.environ['USERS_TABLE'])
    print('[INPUT]:', event)

    try:
        response = USERS_TABLE.update_item(
            Key={
                'userId': event['pathParameters']['id']
            },
            ConditionExpression='attribute_exists(userId)',
            UpdateExpression='SET active = :active',
            ExpressionAttributeValues={':active': False}
        )
        print('[GET RESPONSE]:', response)
        return {
            'statusCode': 200,
            'body': json.dumps('user deleted.')
        }
    except Exception as e:
        print("Error deleting user:")
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps('Error deleting the user')
        }