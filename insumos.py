
from conexion import Conexion

class Insumos:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar_insumo(self, nombre, descripcion):
        query = "INSERT INTO insumos (  nombre, descripcion) VALUES (%s, %s)"
        params = ( nombre, descripcion)
        return self.conexion.ejecutar_consulta(query, params)


    def editar_insumo(self, id, nombre, descripcion):
        query = "UPDATE insumos SET nombre = %s, descripcion = %s WHERE id = %s"
        params = (nombre, descripcion, id)
        return self.conexion.ejecutar_consulta(query, params)

    def eliminar_insumo(self, id):
        query = "DELETE FROM insumos WHERE id = %s"
        params = (id,)
        return self.conexion.ejecutar_consulta(query, params)

    def listar_insumos(self):
        query = "SELECT * FROM insumos"
        return self.conexion.obtener_filas(query)

    def cerrar_conexion(self):
        self.conexion.cerrar_conexion()
