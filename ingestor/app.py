import json
from io import BytesIO
import os
import boto3


IN_BUCKET = os.environ['IN_BUCKET']
OUT_BUCKET = os.environ['OUT_BUCKET']
IN_FILE = os.environ['IN_FILE']
OUT_FILE = os.environ['OUT_FILE']
s3 = boto3.resource('s3')
inbucket = s3.Bucket(IN_BUCKET)
outbucket = s3.Bucket(OUT_BUCKET)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    bio = BytesIO()
    inbucket.download_fileobj(IN_FILE, bio)
    bio.seek(0)
    outbucket.upload_fileobj(bio, OUT_FILE)
    bio.close()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
