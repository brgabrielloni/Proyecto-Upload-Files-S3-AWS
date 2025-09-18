#--------------------------------------------------impports---------------------------------------------------

# importar módulo para interactuar con el S.O
import os

# importar la función load del módulo pipeline.load en dónde se pasará el path del archivo CSV a transformar
from pipeline.load import load_csv

# importar la función clean_dataframe del módulo pipeline.transform que devolverá el dataframe procesado
from pipeline.transform import clean_dataframe

# importar la función save del módulo pipeline.save que convierte el dataframe procesado a CSV
from pipeline.save import save_df_to_csv

# importar la función load_file_to_s3 del módulo pipeline.save que guarda el archivo en S3
from pipeline.save import load_file_to_s3

# importar las variables con los patchs de los archivos y S3 del módulo config.settings
from config.settings import input_file, output_file, s3_key

# importar del archivo logger que está en utils la variable logger
from utils.logger import logger

#-------------------------------------------------------------------------------------------------------------

def main():
    logger.info("Iniciando pipeline")

    if not os.path.exists(input_file):
        logger.error("Archivo no encontrado")
        return
    
    logger.info("Cargando archivo a procesar")
    df = load_csv(input_file)
    
    # Mostramos primeras filas del dataframe original
    print("Primeras 10 filas del archivo original:")
    print(df.head(10))

    print("\n")

    logger.info("Transformando archivo a procesar")
    df_procesado = clean_dataframe(df)

    # Mostramos 10 primeras filas del dataframe transformado
    print("Primeras 10 filas del archivo procesado:")
    print(df_procesado.head(10))
    
    print("\n")

    logger.info("Guardando como CSV archivo procesado")
    save_df_to_csv(df_procesado,output_file)

    logger.info("Subiendo a S3")

    exito = load_file_to_s3(input_file, s3_key)

    if exito:
        logger.info("Archivo subido correctamente")
    else:
        logger.error("Falló la subida a S3")

if __name__ == "__main__":
    main()
