from conexion import Conexion

class Productos:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar_producto(self, id, nombre, descripcion, precio):
        query = "INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)"
        params = (id, nombre, descripcion, precio)
        return self.conexion.ejecutar_consulta(query, params)

    def editar_producto(self, id, nombre, descripcion, precio):
        query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s"
        params = (nombre, descripcion, precio, id)
        return self.conexion.ejecutar_consulta(query, params)

    def eliminar_producto(self, id):
        query = "DELETE FROM productos WHERE id = %s"
        params = (id,)
        return self.conexion.ejecutar_consulta(query, params)

    def listar_productos(self):
        query = "SELECT * FROM productos"
        return self.conexion.obtener_filas(query)

    def cerrar_conexion(self):
        self.conexion.cerrar_conexion()
