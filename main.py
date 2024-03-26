import os

from minio import Minio

ACCESS_KEY_MINIO = '242WUKfVVMwgcDWIyV1z'
SECRET_KEY_MINIO = 'UhDDsRNAzE3vXqfgfE3FfUqOMCm0cZBOWHErOlwp'
BUCKET_NAME = 'loducode'
URL_MINIO = '172.16.0.126:49000'


def upload_file_to_minio(file_name):
    try:
        img_dir = 'media/'
        file_path = os.path.join(img_dir, file_name)
        MINIO_CLIENT = Minio(URL_MINIO, access_key=ACCESS_KEY_MINIO,
                             secret_key=SECRET_KEY_MINIO,
                             secure=False)
        found = MINIO_CLIENT.bucket_exists(BUCKET_NAME)
        if not found:
            MINIO_CLIENT.make_bucket(BUCKET_NAME)
        else:
            print("Bucket already exists")
        MINIO_CLIENT.fput_object(
            BUCKET_NAME, f'test/{file_name}', file_path,
        )
        print("It is successfully uploaded to bucket")
    except Exception as error:
        print(f'upload_file_to_minio: {error}')


# upload_file_to_minio('test.jpg')


def delete_file_minio(file_name):
    try:
        MINIO_CLIENT = Minio(URL_MINIO, access_key=ACCESS_KEY_MINIO,
                             secret_key=SECRET_KEY_MINIO,
                             secure=False)
        MINIO_CLIENT.remove_object(BUCKET_NAME, f'test/{file_name}')
        print("It is successfully deleted from bucket")
    except Exception as error:
        print(f'delete_file_minio: {error}')

# delete_file_minio('test.jpg')
