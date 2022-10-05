
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    #storage_client = storage.Client()
    #storage_client = storage.Client.from_service_account_json("../keys.json")
    storage_client = storage.Client.from_service_account_json("/app/keys.json")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

    blob.download_to_filename("text-download.txt")

    print('File downloaded again..')

upload_blob("pepe-semantics-artif", "/app/scripts/text.txt", "text-bucket.txt")