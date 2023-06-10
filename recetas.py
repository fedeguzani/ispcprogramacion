from conexion import Conexion

class Recetas:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar_receta(self, id, producto_id, insumo_id, cantidad):
        query = "INSERT INTO recetas (id, producto_id, insumo_id, cantidad) VALUES (%s, %s, %s, %s)"
        params = (id, producto_id, insumo_id, cantidad)
        return self.conexion.ejecutar_consulta(query, params)

    def editar_receta(self, id, producto_id, insumo_id, cantidad):
        query = "UPDATE recetas SET producto_id = %s, insumo_id = %s, cantidad = %s WHERE id = %s"
        params = (producto_id, insumo_id, cantidad, id)
        return self.conexion.ejecutar_consulta(query, params)

    def eliminar_receta(self, id):
        query = "DELETE FROM recetas WHERE id = %s"
        params = (id,)
        return self.conexion.ejecutar_consulta(query, params)

    def listar_recetas(self):
        query = "SELECT * FROM recetas"
        return self.conexion.obtener_filas(query)

    def cerrar_conexion(self):
        self.conexion.cerrar_conexion()
