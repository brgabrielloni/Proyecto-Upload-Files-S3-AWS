#--------------------------------------------------imports---------------------------------------------------

# importar módulo de pandas para trabajar con dataFrames
import pandas as pd

#------------------------------------------------------------------------------------------------------------

# función que recibe un CSV y lo guarda como dataframe
def load_csv(path: str) -> pd.DataFrame:

    try:
        return pd.read_csv(path)
    
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
        raise


