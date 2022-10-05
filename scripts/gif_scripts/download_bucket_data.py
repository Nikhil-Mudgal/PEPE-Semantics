from pathlib import Path
from pepe_semantics import config
from google.cloud import storage

_GIDS_PATHS = (
    config.BERTWEET_WEIGHTS_PATHS,
    config.GIF_ID_TO_INFERRED_FEATURE_PATHS,
    config.GIF_ID_TO_GIPHY_ID_PATHS,
)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    #storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json("/app/keys.json")

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f'{destination_file_name} has been downloaded from bucket')


def main():
    for blob, save_fpath in _GIDS_PATHS:
        save_fpath.resolve().parent.mkdir(exist_ok=True, parents=True)
        download_blob(bucket_name="pepe-semantics-artif", 
                      source_blob_name = blob,
                      destination_file_name = str(save_fpath))


if __name__ == "__main__":
    main()
