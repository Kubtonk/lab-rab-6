import os
from dotenv import load_dotenv
import boto3

load_dotenv()

client = boto3.client(
    's3',
    endpoint_url=os.getenv('STORAGE_ENDPOINT'),
    aws_access_key_id=os.getenv('STORAGE_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('STORAGE_SECRET_KEY'),
    region_name=os.getenv('STORAGE_REGION')
)

bucket = os.getenv('STORAGE_BUCKET')

try:
    client.create_bucket(Bucket=bucket)
except Exception:
    pass

# Базовые операции
client.upload_file('uploads/test.txt', bucket, 'lab9/test.txt')
print('Файл успешно загружен')

client.download_file(bucket, 'lab9/test.txt', 'uploads/downloaded_test.txt')
print('Файл успешно получен')

# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: Вывод списка объектов из заданного префикса
print('\n--- ДОП. ЗАДАНИЕ: Список объектов в префиксе lab9/ ---')
response = client.list_objects_v2(Bucket=bucket, Prefix='lab9/')
if 'Contents' in response:
    for obj in response['Contents']:
        print(f" [Файл] {obj['Key']} | Размер: {obj['Size']} байт | Изменен: {obj['LastModified']}")
else:
    print('В данном префиксе объекты не найдены.')
