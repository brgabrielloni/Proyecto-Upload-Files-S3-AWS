# importar módulo para interactuar con el S.O
import os

# importar función load_dotenv del módulo dotenv para cargar las variables definidas en .env
from dotenv import load_dotenv 

# cargar variables de entorno desde el archivo .env
load_dotenv()

#--------definir de variables para obtener variables de entorno:--------

# obtener clave de acceso de AWS desde la variable definida en el archivo .env
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

# obtener clave secreta de AWS desde la variable definida en el archivo .env
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# obtener clave región de AWS desde la variable definida en el archivo .env
AWS_REGION = os.getenv('AWS_REGION')

# obtener el nombr del bucket de S3 de AWS desde la variable definida en el archivo .env
BUCKET_NAME = os.getenv('BUCKET_NAME')

#-----------------------------------------------------------------------

if not all([AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_REGION, BUCKET_NAME]):
    raise ValueError ("No se cargaron todas las variables de entorno en el archivo .env")