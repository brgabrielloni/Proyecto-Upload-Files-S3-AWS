#--------------------------------------------------imports---------------------------------------------------

#importar módulo para mostrar mensajes
import logging

#------------------------------------------------------------------------------------------------------------

#configurar logging y definir que los mensajes se mostraron por la consola estándar
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("file_s3_uploader")