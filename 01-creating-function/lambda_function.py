
def lambda_handler(event, context):
    message = 'Hello AWS CLI Ninja! I am {} {}!'.format(event['first_name'])

    return { 
        'message' : message,
				'statusCode': 200
    }
