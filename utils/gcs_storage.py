import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'utils/credential-key.json'



class GCStorage:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket_name = 'capstone-app-car'
    
    def upload_file(self,file):
        bucket = self.storage_client.get_bucket(self.bucket_name)
        file_path = f"{os.path.basename(file)}"
        blob = bucket.blob(file_path)
        blob.upload_from_filename(file, content_type='image/jpeg')
        return f'https://storage.googleapis.com/{self.bucket_name}/{file_path}'

