from cargar_entrada import leerArchivoInicial
from cargar_movimientos import cargarMovimientos
from crear_informe import crearInforme

ubicaciones = {}

opcion = 0

while opcion != 4:
    print("-" * 10)
    print("Practica 1")
    print("1. Cargar inventario inicial")
    print("2. Cargar movimientos")
    print("3. Crear informe")
    print("4. Salir \n")
    print("Ingrese una opcion:")
    opcion = int(input())

    if opcion == 1:
        archivo_inventario = input("Ingrese la ruta del archivo de inventario: ")
        leerArchivoInicial(archivo_inventario, ubicaciones)
    elif opcion == 2:
        archivo_movimientos = input("Ingrese la ruta del archivo de movimientos: ")
        cargarMovimientos(archivo_movimientos, ubicaciones)
    elif opcion == 3:
        print("Crear informe")
        crearInforme(ubicaciones)
    elif opcion == 4:
        print("Salida")
        break
