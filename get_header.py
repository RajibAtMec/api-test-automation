""" Returns the appropriate headers after generating the JWT """
import json
import boto3
import input_params_1
import input_params_2

def get_header(arg):
    ''' Takes in arg to figure out the step of the loan agreement,
        then returns the appropriate header containing the JWT
        to call the POST method'''
    lambda_client = boto3.client('lambda')

    if arg == 1 :
        # Invoking the jwt_generate lambda to generate jwt for step1 of the loan agreement
        result = lambda_client.invoke(
            FunctionName = "jwt_generate",
            InvocationType = 'RequestResponse',
            Payload = json.dumps(input_params_1.input_params_1) # payload for step1
        )
        data = json.loads(result['Payload'].read())

        # Extracting the JWT for step1
        jwt_1 = data['jwt']

        # Constructing Headers for step1
        headers_1 = {
            'Authorization': 'Bearer ' + jwt_1
        }
        return headers_1

    else :
        # Invoking the jwt_generate lambda to generate jwt for step2 of the loan agreement
        result = lambda_client.invoke(
            FunctionName = "jwt_generate",
            InvocationType = 'RequestResponse',
            Payload = json.dumps(input_params_2.input_params_2) # payload for step2
        )
        data = json.loads(result['Payload'].read())
        
        # Extracting the JWT for step2
        jwt_2 = data['jwt']

        # Constructing Headers for step2
        headers_2 = {
            'Authorization': 'Bearer ' + jwt_2
        }
        return headers_2
