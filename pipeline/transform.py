#--------------------------------------------------imports---------------------------------------------------

# importar la función load_csv del módulo pipeline para obtener el dataframe que vamos a transformar
from pipeline.load import load_csv

# importar módulo de pandas para trabajar con dataframes
import pandas as pd

# importar módulo de fechas
from datetime import datetime

#------------------------------------------------------------------------------------------------------------

# función para limpiar el dataframe y normalizar valores
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # para no modificar el original

    # normalizar 'nombre'
    if 'nombre' in df.columns:
        df['nombre'] = df['nombre'].fillna('N/A').astype(str).str.strip()
        df['nombre'] = df['nombre'].replace(['', 'na', 'nan', 'NA', 'NaN'], 'N/A', regex=True)

    # normalizar 'edad'. Definimos rango válido y si no existe, seteamos "0" por defecto
    if 'edad' in df.columns:
       df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
       df['edad'] = df['edad'].where((df['edad'] >= 0) & (df['edad'] <= 150), other=0)
       df['edad'] = df['edad'].astype(int)

    # normalizar 'obra_social'
    if 'obra_social' in df.columns:
        df['obra_social'] = df['obra_social'].fillna('No Informada').astype(str).str.strip()
        df['obra_social'] = df['obra_social'].replace(['', 'na', 'nan', 'NA', 'NaN'], 'No Informada', regex=True)

    # normalizar 'fecha_turno'. Si está vacía, seteamos la fecha actual del sistema
   
    if 'fecha_turno' in df.columns:
        fechas = pd.to_datetime(df['fecha_turno'], errors='coerce', dayfirst=False)
        fechas = fechas.fillna(pd.Timestamp(datetime.today()))   
        df['fecha_turno'] = fechas.dt.strftime('%d/%m/%Y')

    return df
