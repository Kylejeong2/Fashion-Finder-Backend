# for demo purposes

import json
from serpapi import GoogleSearch
import os
import base64
from dotenv import load_dotenv
import boto3

load_dotenv()

def lambda_handler(event, context):
    print(event)
    # Extract the image input from the event
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    image_input = f"https://{bucket}.s3.us-west-1.amazonaws.com/{key}"

    print(image_input)
    
    if not image_input:
        return {
            'statusCode': 400,
            'body': json.dumps('No image input provided')
        }

    similar_items = search_similar_items(image_input)

    print(similar_items)
    
    return {
        'statusCode': 200,
        'body': json.dumps(similar_items)
    }

def search_similar_items(base64_input): 

    s3_client = boto3.client('s3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID_TEST"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY_TEST"),
        region_name=os.getenv("AWS_REGION_TEST")
    )
    s3_bucket = os.getenv("S3_BUCKET_STORAGE")
    file_name = f"image_{os.urandom(8).hex()}.jpg"

    # Decode base64 image input to URL
    image_input = base64.b64decode(base64_input)
    # upload and store img url in s3 bucket 
    s3_client.put_object(Body=image_input, Bucket=s3_bucket, Key=file_name)

    #get the img from the bucket that you just uploaded
    image_input = f"https://{s3_bucket}.s3.amazonaws.com/{file_name}"
    
    params = {
        "engine": "google_lens",
        "url": image_input,
        "api_key": os.getenv("SERP_API_KEY")
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    similar_items = []
    if "visual_matches" in results:
        for item in results["visual_matches"]:
            if "price" in item and "title" in item and "link" in item:
                price = item["price"]
                if price["currency"] == "$":
                    similar_items.append({
                        "title": item["title"],
                        "price": price,
                        "link": item["link"]
                    })
    
    print(similar_items)
    return similar_items[:5]  # Return top 5 similar items