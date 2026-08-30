from config.database import obtener_conexion

def probar_conexion():
    print("Conectando a Supabase...")
    try:
        supabase = obtener_conexion()
        # Intentamos hacer una consulta simple a la tabla 'producto'
        respuesta = supabase.table("producto").select("*").limit(1).execute()
        
        print("\n✅ ¡Conexión exitosa a Supabase!")
        print(f"Respuesta de la BD: {respuesta.data}")
    except Exception as e:
        print("\n❌ Error al conectar con Supabase:")
        print(e)

if __name__ == "__main__":
    probar_conexion()