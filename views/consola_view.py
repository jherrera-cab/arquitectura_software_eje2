class ConsolaView:
    """
        Capa de vista dedicada para manejar la interfaz de usuario en la terminal o consola
    """

    @staticmethod  
    def menu_principal()-> str:
        print("\n" + "="*35)
        print("   ARQUITECTURA DE SOFTWARE")
        print("   Actividad evaluativa eje 2")
        print("="*35)
        print("1. Gestión de Productos")
        print("2. Gestión de Empleados")
        print("3. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def menu_crud(entidad: str) -> str:
        print(f"\n--- MENÚ DE {entidad.upper()} ---")
        print("1. Crear / Registrar")
        print("2. Listar Todos")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")
        return input("Seleccione una opción: ")

    @staticmethod
    def captura_producto() -> tuple:
        print("\n -- Registro de producto--" )
        codigo = input("Código de barras: ")
        nombre = input("Nombre del producto: ")
        desc = input("Descripción: ")
        precio = float(input("Precio de venta: "))
        return codigo, nombre, desc, precio

    @staticmethod
    def capturar_actualizacion_producto() -> tuple:
        id_prod = input("\nIngrese el UUID del producto a actualizar: ")
        nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
        precio_str = input("Nuevo precio (dejar vacío para no cambiar): ")
        precio = float(precio_str) if precio_str else None
        return id_prod, nombre, precio

    # --- ENTRADAS DE EMPLEADOS ---
    @staticmethod
    def capturar_empleado() -> tuple:
        print("\n-- Registro de Empleado --")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        doc = input("Documento de identidad: ")
        rol = input("Rol (ej. Cajero, Administrador): ")
        email = input("Correo electrónico: ")
        return nombre, apellido, doc, rol, email

    @staticmethod
    def capturar_actualizacion_empleado() -> tuple:
        id_emp = input("\nIngrese el UUID del empleado a actualizar: ")
        rol = input("Nuevo rol (dejar vacío para no cambiar): ")
        email = input("Nuevo email (dejar vacío para no cambiar): ")
        return id_emp, rol, email

    # --- SALIDAS Y TABLAS ---
    @staticmethod
    def solicitar_id(entidad: str) -> str:
        return input(f"\nIngrese el UUID del {entidad} a eliminar: ")

    @staticmethod
    def mostrar_productos(productos: list):
        print("\n" + "-"*65)
        print(f"{'ID (UUID)':<38} | {'NOMBRE':<15} | {'PRECIO':<8}")
        print("-" * 65)
        if not productos:
            print("No hay productos registrados.")
        for p in productos:
            print(f"{p.get('id'):<38} | {p.get('nombre'):<15} | ${p.get('precio_venta'):<8}")
        print("-" * 65)

    @staticmethod
    def mostrar_empleados(empleados: list):
        print("\n" + "-"*75)
        print(f"{'ID (UUID)':<38} | {'NOMBRE COMPLETO':<20} | {'ROL':<10}")
        print("-" * 75)
        if not empleados:
            print("No hay empleados registrados.")
        for e in empleados:
            nombre_completo = f"{e.get('nombre')} {e.get('apellido')}"
            print(f"{e.get('id'):<38} | {nombre_completo:<20} | {e.get('rol'):<10}")
        print("-" * 75)

    @staticmethod
    def mostrar_mensaje(mensaje: str):
        print(f"\n[SISTEMA]: {mensaje}")
