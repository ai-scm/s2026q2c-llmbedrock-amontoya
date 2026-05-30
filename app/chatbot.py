import os
import json

import boto3
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

load_dotenv()

MODEL_ID = os.getenv("MODEL_ID")
AWS_REGION = os.getenv("AWS_REGION")

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)


import os
import json

import boto3
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

load_dotenv()

MODEL_ID = os.getenv("MODEL_ID")
AWS_REGION = os.getenv("AWS_REGION")

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)


def generate_response(messages):

    nova_messages = []

    for msg in messages:

        nova_messages.append(
            {
                "role": msg["role"],
                "content": [
                    {
                        "text": msg["content"]
                    }
                ]
            }
        )

    request_body = {
        "system": [
            {
                "text": SYSTEM_PROMPT
            }
        ],
        "messages": nova_messages,
        "inferenceConfig": {
            "maxTokens": 250,
            "temperature": 0.2,
            "topP": 0.9
        }
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(request_body)
    )

    response_body = json.loads(
        response["body"].read()
    )

    response_text = (
        response_body["output"]["message"]["content"][0]["text"]
    )

    return response_text.strip()