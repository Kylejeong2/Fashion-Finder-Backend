# Fashion Finder Backend Service

- Create venv

python -m venv venv
source venv/bin/activate

- Install requirements

pip install -r requirements.txt

- Used: 

AWS Lambda
AWS S3 (img storage) *you only need one bucket for it to work but i used 2 here so that i could have a little front end to demo

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

test_img.txt is a supreme shirt in b64