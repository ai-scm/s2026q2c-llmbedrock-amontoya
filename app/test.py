import boto3
import os
from dotenv import load_dotenv

load_dotenv()

sts = boto3.client(
    "sts",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

print(sts.get_caller_identity())