#--------------------------------------------------imports---------------------------------------------------

# importar módulo para interactuar con el S.O
import os

# importar módulo de pandas para trabajar con dataframes
import pandas as pd

# importar el archivo settings del módulo config para obtener las variables necesarias para crear el objetio S3
from config import settings

# Importar la librería boto3, que es el SDK oficial de AWS para Python
import boto3

# importar la función clean_dataframe del módulo pipeline.transform, que devuelve el dataframe procesado
from pipeline.transform import clean_dataframe

#------------------------------------------------------------------------------------------------------------

# función que crea y devuelve un cliente de AWS S3 usando boto3 y las credenciales del archivo settings
def create_client_s3():
    return boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

# función que guarda el df como csv
def save_df_to_csv(df: pd.DataFrame, ruta_csv: str) -> None:
    df.to_csv(ruta_csv, index=False)

# función para subir el arcihvo csv a S3
def load_file_to_s3(local_path: str, s3_key: str) -> bool:
    s3 = create_client_s3()
    try:
        s3.upload_file(local_path, settings.BUCKET_NAME, s3_key)
        print(f"Archivo subido a S3 como: {s3_key}")
        return True
    except Exception as e:
        print(f"Error al subir archivo a S3: {e}")
        return False
