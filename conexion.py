import mysql.connector

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=33065,
            user='root',
            password='',
            database='big_bread_s'
        )
        self.cursor = self.conn.cursor()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

    def ejecutar_consulta(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return False

    def obtener_filas(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return []












