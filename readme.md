# Fashion Finder Backend Service
### Shop for any piece of clothing. 

NOTE: This was built to be hosted as an AWS Lambda Function, but you can also just run it locally in using Streamlit. You'll need the AWS S3 buckets still, but don't worry about lambda_function.py, requirements2.txt, or anything here that says "lambda". 

The image search is also using Base64 encoded images, so you'll need to encode your images before searching for them. Here's a link to a site that can encode your images: https://elmah.io/tools/base64-image-encoder/.

- Create venv

python -m venv venv
source venv/bin/activate

- Install requirements

pip install -r requirements.txt

- Used: 

AWS S3 (img storage) *you only need one bucket for Lambda Service to work but i used 2 here so that i could have a little front end to demo

FOR DEMO:
- Create 2 s3 buckets and set up permissions below:
- Fill .env with AWS info.

- Permissions Tab:
    - Make sure you turn OFF "block all public access"
    - Add this to bucket policy (link to generate policy)[https://awspolicygen.s3.amazonaws.com/policygen.html] 
        - principal set to "*" 
        - resource set to bucket ARN + /*

    {
        "Version": "2012-10-17",
        "Id": "  ",
        "Statement": [
            {
                "Sid": "  ",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "s3:GetObject",
                "Resource": "{bucket ARN}/*"
            }
        ]
    }

SERP API (google lens search)[https://serpapi.com/]

*** test_img.txt is a supreme shirt in base64