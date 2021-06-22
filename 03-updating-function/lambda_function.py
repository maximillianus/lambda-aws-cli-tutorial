
def lambda_handler(event, context):
    message = 'Hello AWS CLI Ninja! I am {} {}!'.format(event['first_name'])

    # Context env
    context_memory = context.memory_limit_in_mb
    context_remainingtime = context.get_remaining_time_in_millis()
    LAMBDA_DEFAULT_TIMEOUT = 3000
    invoked_time = LAMBDA_DEFAULT_TIMEOUT - context_remainingtime

    return { 
        'message' : message,
        'stats': {
          'memory': context_memory,
          'invoked_time': invoked_time
        },
				'statusCode': 200
    }
