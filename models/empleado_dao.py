from config.database import obtener_conexion

class EmpleadoDAO:
    """
    Patrón DAO: Encapsula la persistencia y operaciones CRUD para Empleados[cite: 2].
    """

    @staticmethod
    def crear(nombre: str, apellido: str, documento_identidad: str, rol: str, email: str) -> dict:
        """Registra un nuevo empleado en la base de datos[cite: 3]."""
        supabase = obtener_conexion()
        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "documento_identidad": documento_identidad,
            "rol": rol,
            "email": email
        }
        respuesta = supabase.table("empleado").insert(datos).execute()
        return respuesta.data

    @staticmethod
    def obtener_todos() -> list:
        """Obtiene el listado completo de empleados[cite: 3]."""
        supabase = obtener_conexion()
        respuesta = supabase.table("empleado").select("*").execute()
        return respuesta.data

    @staticmethod
    def actualizar(id_empleado: str, rol: str = None, email: str = None) -> dict:
        """Actualiza el rol o email de un empleado[cite: 3]."""
        supabase = obtener_conexion()
        datos = {}
        if rol:
            datos["rol"] = rol
        if email:
            datos["email"] = email

        respuesta = supabase.table("empleado").update(datos).eq("id", id_empleado).execute()
        return respuesta.data

    @staticmethod
    def eliminar(id_empleado: str) -> dict:
        """Elimina un empleado de la base de datos mediante su ID[cite: 3]."""
        supabase = obtener_conexion()
        respuesta = supabase.table("empleado").delete().eq("id", id_empleado).execute()
        return respuesta.data