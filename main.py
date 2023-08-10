opcion = 0

while opcion != 4:
    print("-"*20)
    print("Practica 1")

    print("1. Cargar inventario inicial")
    print("2. Cargar movimientos")
    print("3. Crear informe")
    print("4. Salir \n" )
          
    print("Ingrese una opcion: ")
    opcion = int(input())

    if opcion == 1:
        print("Cargar inventario inicial")
        lineas = leer_archivo_inicial()
        print("Archivo cargado exitosamente")
        for i in lineas:
            instruccion = i.split(" ")
            print(instruccion)
            if(instruccion [0] == "crear_producto"):
                print("Encontre una instruccion para crear")
            datos = instruccion[1].split(";")
        pass
    elif opcion == 2:
        print("Cargar movimientos")
        cargar_movimientos()
        pass
    elif opcion == 3:
        print("Crear informe")
        pass
    elif opcion == 4:
        print("Salir")
        break