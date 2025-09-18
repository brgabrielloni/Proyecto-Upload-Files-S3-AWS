# importar módulo para interactuar con el S.O
import os

# importar el archivo settings del módulo config
from config import settings

# Importar la librería boto3, que es el SDK oficial de AWS para Python
import boto3

# función que crea y devuelve un cliente de AWS S3 usando boto3 y las credenciales
def cargar_cliente_s3():
    return boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

# Función para subir un archivo local a un bucket de S3
# local_path: ruta al archivo local
# s3_key: nombre con el que se guardará el archivo en el bucket, ej:'carpeta/archivo.txt')
def subir_archivo_s3(local_path, s3_key):
    s3 = cargar_cliente_s3()
    try:
        s3.upload_file(local_path, settings.BUCKET_NAME, s3_key)
        return True
    except Exception as e:
        print(f"Error al subir archivo: {e}")
        return False