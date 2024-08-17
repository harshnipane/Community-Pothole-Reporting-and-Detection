from flask import Flask, request, render_template, jsonify
import boto3
import os

app = Flask(__name__)

S3_BUCKET = '..bucket_name..'
S3_REGION = '..region..'
aws_access_key = '..access key..'
secret_access_key = '..secret access key'


s3_client = boto3.client('s3', region_name=S3_REGION, aws_access_key_id=aws_access_key, aws_secret_access_key=secret_access_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_photo():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    file_name = str(latitude)+"_"+str(longitude)+".jpg"
    
    try:
        s3_client.upload_fileobj(
            file,
            S3_BUCKET,
            file_name,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )

        print(f"Uploaded file: {file_name} with coordinates: Latitude: {latitude}, Longitude: {longitude}")

        file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{file_name}"
        
        return jsonify({"message": "File uploaded successfully", "url": file_url}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
