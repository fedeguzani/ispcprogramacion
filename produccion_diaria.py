
class ProduccionDiaria:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar_produccion(self, fecha, cantidad):
        query = "INSERT INTO produccion_diaria ( fecha, cantidad) VALUES ( %s, %s)"
        params = ( fecha, cantidad)
        return self.conexion.ejecutar_consulta(query, params)

    def editar_produccion(self, id, fecha, cantidad):
        query = "UPDATE produccion_diaria SET fecha = %s, cantidad = %s WHERE id = %s"
        params = (fecha, cantidad, id)
        return self.conexion.ejecutar_consulta(query, params)

    def eliminar_produccion(self, id):
        query = "DELETE FROM produccion_diaria WHERE id = %s"
        params = (id,)
        return self.conexion.ejecutar_consulta(query, params)

    def listar_produccion(self):
        query = "SELECT * FROM produccion_diaria"
        return self.conexion.obtener_filas(query)

    def cerrar_conexion(self):
        self.conexion.cerrar_conexion()
    
    
    
