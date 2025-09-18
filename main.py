# importar módulo para interactuar con el S.O
import os

# importar el archivo load del módulo pipeline
from pipeline import load

# importar del archivo logger que está en utils la variable logger
from utils.logger import logger

#ruta del archivo a subir
input_file = "data/input/pacientes_crudo.csv"

#S3 donde se subirá el archivo
s3_key = "uploads/pacientes_crudo.csv"

def main():
    logger.info("Iniciando pipeline")

    if not os.path.exists(input_file):
        logger.error("Archivo no encontrado")
        return
    
    logger.info("Subiendo a S3")

    exito = load.subir_archivo_s3(input_file, s3_key)

    if exito:
        logger.info("Archivo subido correctamente")
    else:
        logger.error("Falló la subida a S3")

if __name__ == "__main__":
    main()