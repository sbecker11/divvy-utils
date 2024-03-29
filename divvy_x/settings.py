import os

if os.getenv('AWS_ACCESS_KEY_ID') is None:
    raise ValueError("environment variable AWS_ACCESS_KEY_ID is undefined")
if os.getenv('AWS_SECRET_ACCESS_KEY') is None:
    raise ValueError("environment variable AWS_SECRET_ACCESS_KEY is undefined")
if os.getenv('AWS_DEFAULT_REGION') is None:
    raise ValueError("environment variable AWS_DEFAULT_REGION is undefined")

REGION_NAME = 'us-east-1'
S3_BUCKET_NAME = 'sbecker-11-divvy'
