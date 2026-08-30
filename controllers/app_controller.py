from models.product_dao import ProductDAO
from models.empleado_dao import EmpleadoDAO
from views.consola_view import ConsolaView

class AppController:
    """Capa Controlador: Procesa entradas del usuario e invoca DAOs[cite: 2, 3]."""

    def __init__(self):
        self.view = ConsolaView()

    def ejecutar(self):
        while True:
            opcion = self.view.menu_principal()
            if opcion == '1':
                self.gestionar_productos()
            elif opcion == '2':
                self.gestionar_empleados()
            elif opcion == '3':
                self.view.mostrar_mensaje("Finalizando la aplicación...")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Intente de nuevo.")

    def gestionar_productos(self):
        while True:
            sub_opc = self.view.menu_crud("Productos")
            try:
                if sub_opc == '1':
                    c, n, d, p = self.view.captura_producto()
                    ProductDAO.crear(c, n, d, p)
                    self.view.mostrar_mensaje("Producto creado exitosamente.")
                elif sub_opc == '2':
                    prods = ProductDAO.obtener_todos()
                    self.view.mostrar_productos(prods)
                elif sub_opc == '3':
                    id_p, n, p = self.view.capturar_actualizacion_producto()
                    ProductDAO.actualizar(id_p, n, p)
                    self.view.mostrar_mensaje("Producto actualizado exitosamente.")
                elif sub_opc == '4':
                    id_p = self.view.solicitar_id("producto")
                    ProductDAO.eliminar(id_p)
                    self.view.mostrar_mensaje("Producto eliminado exitosamente.")
                elif sub_opc == '5':
                    break
            except Exception as e:
                self.view.mostrar_mensaje(f"Error procesando solicitud: {e}")

    def gestionar_empleados(self):
        while True:
            sub_opc = self.view.menu_crud("Empleados")
            try:
                if sub_opc == '1':
                    n, a, d, r, e = self.view.capturar_empleado()
                    EmpleadoDAO.crear(n, a, d, r, e)
                    self.view.mostrar_mensaje("Empleado registrado exitosamente.")
                elif sub_opc == '2':
                    emps = EmpleadoDAO.obtener_todos()
                    self.view.mostrar_empleados(emps)
                elif sub_opc == '3':
                    id_e, r, e_mail = self.view.capturar_actualizacion_empleado()
                    EmpleadoDAO.actualizar(id_e, r, e_mail)
                    self.view.mostrar_mensaje("Empleado actualizado exitosamente.")
                elif sub_opc == '4':
                    id_e = self.view.solicitar_id("empleado")
                    EmpleadoDAO.eliminar(id_e)
                    self.view.mostrar_mensaje("Empleado eliminado exitosamente.")
                elif sub_opc == '5':
                    break
            except Exception as e:
                self.view.mostrar_mensaje(f"Error procesando solicitud: {e}")