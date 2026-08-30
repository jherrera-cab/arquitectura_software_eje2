from config.database import obtener_conexion

class ProductDAO:
    """
        Se a crean las operaciones CRUD en la tabla producto
    """

    @staticmethod
    def crear(codigo_barras:str, nombre: str, descripcion:str, precio_venta:float) -> dict:
        """
            Crea un nuevo registro en la tabla producto
        """

        supabase= obtener_conexion()
        info={
            "codigo_barras":codigo_barras,
            "nombre":nombre,
            "descripcion":descripcion,
            "precio_venta":precio_venta
        }

        respuesta =supabase.table("producto").insert(info).execute()
        return respuesta.data

    @staticmethod
    def obtener_todos() -> list:
        """
            Lee la tabla y trae todos los registros de la tabla
        """

        supabase = obtener_conexion()
        respuesta = supabase.table("producto").select("*").execute()
        return respuesta.data

    @staticmethod
    def actualizar(id_producto: str, nombre: str = None, precio_venta: float=None) -> dict:
        """
            Actualiza los campos especificos de un producto ya existente en la tabla
        """

        supabase = obtener_conexion()
        datos_actualizar = {}
        if nombre:
            datos_actualizar["nombre"] = nombre
        if precio_venta:
            datos_actualizar["precio_venta"] = precio_venta

        respuesta = supabase.table("producto").update(datos_actualizar).eq("id", id_producto).execute()
        return respuesta.data

    @staticmethod
    def eliminar(id_producto: str)->dict:
        """
            Elimina un registro de producto por su ID
        """

        supabase = obtener_conexion()
        respuesta = supabase.table("producto").delete().eq("id", id_producto).execute()
        return respuesta.data
