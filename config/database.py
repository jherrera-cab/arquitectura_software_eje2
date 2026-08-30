import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las variables del archivo .env
load_dotenv()

SUPABASE_URL = os.getenv("supabase_url")
SUPABASE_KEY = os.getenv("subapase_key")

def obtener_conexion() -> Client:
    """
    Crea e inicializa el cliente de Supabase utilizando las variables de entorno.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Error: Faltan las variables SUPABASE_URL o SUPABASE_KEY en el archivo .env")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)