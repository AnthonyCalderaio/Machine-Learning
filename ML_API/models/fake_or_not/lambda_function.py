from run import predictComment

file_name = 'lambda_function.py';

def lambda_handler(event, context):
    return predictComment('is this a fake comment?')