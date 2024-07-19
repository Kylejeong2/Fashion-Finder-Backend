import streamlit as st
import boto3
import os
import base64
from dotenv import load_dotenv
from app import search_similar_items

# Load environment variables
load_dotenv()

def upload_image_to_s3(base64_image):
    # AWS S3 configuration
    s3_bucket = os.getenv("AWS_S3_BUCKET") # this bucket is purely for the demo
    s3_client = boto3.client('s3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID_TEST"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY_TEST"),
        region_name=os.getenv("AWS_REGION_TEST")
    )
    
    # Upload base64 encoded image to S3
    try:
        file_name = f"image_{os.urandom(8).hex()}.txt"  # Generate a random filename with .txt extension
        s3_client.put_object(Body=base64_image, Bucket=s3_bucket, Key=file_name)
        s3_url = f"https://{s3_bucket}.s3.amazonaws.com/{file_name}"
        return {"success": True, "url": s3_url}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    st.title("Image Upload Dashboard")

    base64_input = st.text_area("Paste your base64 encoded image here:")
    st.write("Command Enter to Submit.")

    if base64_input:
        try:
            # Display the image
            image_data = base64.b64decode(base64_input)
            st.image(image_data, caption='Uploaded Image', use_column_width=True)
            
            with st.spinner("Uploading image..."):
                result = upload_image_to_s3(base64_input)
            
            if result["success"]:
                file_name = result["url"]
                st.success(f"Image successfully uploaded! File name: {file_name}")
                similar_items = search_similar_items(base64_input)
                st.write("Similar items:", similar_items)
            else:
                st.error(f"Failed to upload image: {result['error']}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()