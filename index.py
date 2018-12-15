
'''
https://docs.aws.amazon.com/cloud9/latest/user-guide/lambda-functions.html#lambda-functions-debug
'''

import json
import datetime

def handler(event, context):
    
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
        
    }
