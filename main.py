from conexion import Conexion
from insumos import Insumos
from produccion_diaria import ProduccionDiaria
from recetas import Recetas

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Insumos")
    print("2. Producción Diaria")
    print("3. Recetas")
    print("0. Salir")

def mostrar_menu_insumos():
    print("===== MENÚ INSUMOS =====")
    print("1. Listar insumos")
    print("2. Agregar insumo")
    print("3. Editar insumo")
    print("4. Eliminar insumo")
    print("0. Volver al menú principal")

def mostrar_menu_produccion_diaria():
    print("===== MENÚ PRODUCCIÓN DIARIA =====")
    print("1. Listar producción diaria")
    print("2. Agregar producción diaria")
    print("3. Editar producción diaria")
    print("4. Eliminar producción diaria")
    print("0. Volver al menú principal")

def mostrar_menu_recetas():
    print("===== MENÚ RECETAS =====")
    print("1. Listar recetas")
    print("2. Agregar receta")
    print("3. Editar receta")
    print("4. Eliminar receta")
    print("0. Volver al menú principal")

def ejecutar_menu_insumos():
    conexion = Conexion("host", "port", "user", "password", "database")
    insumos = Insumos(conexion)

    while True:
        mostrar_menu_insumos()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            listar_insumos(insumos)
        elif opcion == "2":
            agregar_insumo(insumos)
        elif opcion == "3":
            editar_insumo(insumos)
        elif opcion == "4":
            eliminar_insumo(insumos)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    insumos.cerrar_conexion()

def listar_insumos(insumos):
    print("===== LISTA DE INSUMOS =====")
    lista_insumos = insumos.listar_insumos()

    if lista_insumos:
        for insumo in lista_insumos:
            print(f"ID: {insumo[0]} | Nombre: {insumo[1]} | Descripción: {insumo[2]}")
    else:
        print("No se encontraron insumos.")

def agregar_insumo(insumos):
    print("===== AGREGAR INSUMO =====")
    nombre = input("Ingrese el nombre del insumo: ")
    descripcion = input("Ingrese la descripción del insumo: ")

    if nombre and descripcion:
        if insumos.agregar_insumo(nombre, descripcion):
            print("Insumo agregado exitosamente.")
        else:
            print("Error al agregar el insumo.")
    else:
        print("Nombre y descripción son campos obligatorios.")

def editar_insumo(insumos):
    print("===== EDITAR INSUMO =====")
    id_insumo = input("Ingrese el ID del insumo a editar: ")
    nombre = input("Ingrese el nuevo nombre del insumo: ")
    descripcion = input("Ingrese la nueva descripción del insumo: ")

    if id_insumo and nombre and descripcion:
        if insumos.editar_insumo(id_insumo, nombre, descripcion):
            print("Insumo editado exitosamente.")
        else:
            print("Error al editar el insumo.")
    else:
        print("ID, nombre y descripción son campos obligatorios.")

def eliminar_insumo(insumos):
    print("===== ELIMINAR INSUMO =====")
    id_insumo = input("Ingrese el ID del insumo a eliminar: ")

    if id_insumo:
        if insumos.eliminar_insumo(id_insumo):
            print("Insumo eliminado exitosamente.")
        else:
            print("Error al eliminar el insumo.")
    else:
        print("ID es un campo obligatorio.")

def ejecutar_menu_produccion_diaria():
    conexion = Conexion("host", "port", "user", "password", "database")
    produccion_diaria = ProduccionDiaria(conexion)

    while True:
        mostrar_menu_produccion_diaria()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            listar_produccion_diaria(produccion_diaria)
        elif opcion == "2":
            agregar_produccion_diaria(produccion_diaria)
        elif opcion == "3":
            obtener_produccion_total_dia(produccion_diaria)
        elif opcion == "4":
            eliminar_produccion_diaria(produccion_diaria)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    produccion_diaria.cerrar_conexion()

def listar_produccion_diaria(produccion_diaria):
    print("===== LISTA DE PRODUCCIÓN DIARIA =====")
    lista_produccion = produccion_diaria.listar_produccion()

    if lista_produccion:
        for produccion in lista_produccion:
            print(f"ID: {produccion[0]} | Fecha: {produccion[1]} | Cantidad: {produccion[2]}")
    else:
        print("No se encontró producción diaria.")

def agregar_produccion_diaria(produccion_diaria):
    print("===== AGREGAR PRODUCCIÓN DIARIA =====")
    fecha = input("Ingrese la fecha de producción (YYYY-MM-DD): ")
    cantidad = input("Ingrese la cantidad producida: ")

    if fecha and cantidad:
        if produccion_diaria.insertar_produccion(fecha, cantidad):
            print("Producción diaria agregada exitosamente.")
        else:
            print("Error al agregar la producción diaria.")
    else:
        print("Fecha y cantidad son campos obligatorios.")

def editar_produccion_diaria(produccion_diaria):
    print("===== EDITAR PRODUCCIÓN DIARIA =====")
    id_produccion = input("Ingrese el ID de la producción diaria a editar: ")
    fecha = input("Ingrese la nueva fecha de producción (YYYY-MM-DD): ")
    cantidad = input("Ingrese la nueva cantidad producida: ")

    if id_produccion and fecha and cantidad:
        if produccion_diaria.editar_produccion(id_produccion, fecha, cantidad):
            print("Producción diaria editada exitosamente.")
        else:
            print("Error al editar la producción diaria.")
    else:
        print("ID, fecha y cantidad son campos obligatorios.")

def eliminar_produccion_diaria(produccion_diaria):
    print("===== ELIMINAR PRODUCCIÓN DIARIA =====")
    id_produccion = input("Ingrese el ID de la producción diaria a eliminar: ")

    if id_produccion:
        if produccion_diaria.eliminar_produccion(id_produccion):
            print("Producción diaria eliminada exitosamente.")
        else:
            print("Error al eliminar la producción diaria.")
    else:
        print("ID es un campo obligatorio.")
        
def obtener_produccion_total_rango_tiempo(produccion_diaria):
    print("===== PRODUCCIÓN TOTAL DE UN RANGO DE TIEMPO =====")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

    if fecha_inicio and fecha_fin:
        total = produccion_diaria.obtener_produccion_total_rango_tiempo(fecha_inicio, fecha_fin)
        if total is not None:
            print(f"La producción total para el rango de tiempo {fecha_inicio} - {fecha_fin} es: {total}")
        else:
            print("No se encontró producción para el rango de tiempo especificado.")
    else:
        print("Fecha de inicio y fecha de fin son campos obligatorios.")
        

def ejecutar_menu_recetas():
    conexion = Conexion("host", "port", "user", "password", "database")
    recetas = Recetas(conexion)

    while True:
        mostrar_menu_recetas()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            listar_recetas(recetas)
        elif opcion == "2":
            agregar_receta(recetas)
        elif opcion == "3":
            editar_receta(recetas)
        elif opcion == "4":
            eliminar_receta(recetas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    recetas.cerrar_conexion()

def listar_recetas(recetas):
    print("===== LISTA DE RECETAS =====")
    lista_recetas = recetas.listar_recetas()

    if lista_recetas:
        for receta in lista_recetas:
            print(f"ID: {receta[0]} | Producto ID: {receta[1]} | Insumo ID: {receta[2]} | Cantidad: {receta[3]}")
    else:
        print("No se encontraron recetas.")

def agregar_receta(recetas):
    print("===== AGREGAR RECETA =====")
    producto_id = input("Ingrese el ID del producto asociado a la receta: ")
    insumo_id = input("Ingrese el ID del insumo asociado a la receta: ")
    cantidad = input("Ingrese la cantidad requerida del insumo en la receta: ")

    if producto_id and insumo_id and cantidad:
        if recetas.insertar_receta(producto_id, insumo_id, cantidad):
            print("Receta agregada exitosamente.")
        else:
            print("Error al agregar la receta.")
    else:
        print("Producto ID, insumo ID y cantidad son campos obligatorios.")

def editar_receta(recetas):
    print("===== EDITAR RECETA =====")
    id_receta = input("Ingrese el ID de la receta a editar: ")
    producto_id = input("Ingrese el nuevo ID del producto asociado a la receta: ")
    insumo_id = input("Ingrese el nuevo ID del insumo asociado a la receta: ")
    cantidad = input("Ingrese la nueva cantidad requerida del insumo en la receta: ")

    if id_receta and producto_id and insumo_id and cantidad:
        if recetas.editar_receta(id_receta, producto_id, insumo_id, cantidad):
            print("Receta editada exitosamente.")
        else:
            print("Error al editar la receta.")
    else:
        print("ID de receta, producto ID, insumo ID y cantidad son campos obligatorios.")
        
def calcular_insumos(recetas):
    print("===== CALCULADORA DE INSUMOS =====")
    receta_id = input("Ingrese el ID de la receta que desea producir: ")
    cantidad = input("Ingrese la cantidad a producir: ")

    if receta_id and cantidad:
        insumos = recetas.calcular_insumos_receta(receta_id, cantidad)
        if insumos:
            print("Insumos requeridos:")
            for insumo in insumos:
                print(f"{insumo['nombre']}: {insumo['cantidad']} {insumo['unidad']}")
        else:
            print("La receta no existe o no hay suficientes datos.")
    else:
        print("ID de receta y cantidad son campos obligatorios.")
        

def eliminar_receta(recetas):
    print("===== ELIMINAR RECETA =====")
    id_receta = input("Ingrese el ID de la receta a eliminar: ")

    if id_receta:
        if recetas.eliminar_receta(id_receta):
            print("Receta eliminada exitosamente.")
        else:
            print("Error al eliminar la receta.")
    else:
        print("ID de receta es un campo obligatorio.")

def obtener_produccion_total_dia(produccion_diaria):
    print("===== PRODUCCIÓN TOTAL DE UN DÍA =====")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

    if fecha:
        total = produccion_diaria.obtener_produccion_total_dia(fecha)
        if total is not None:
            print(f"La producción total para el día {fecha} es: {total}")
        else:
            print("No se encontró producción para la fecha especificada.")
    else:
        print("Fecha es un campo obligatorio.")


# Programa principal
conexion = Conexion("host", "port", "user", "password", "database")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ejecutar_menu_insumos()
    elif opcion == "2":
        ejecutar_menu_produccion_diaria()
    elif opcion == "3":
        ejecutar_menu_recetas()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

conexion.cerrar_conexion()
