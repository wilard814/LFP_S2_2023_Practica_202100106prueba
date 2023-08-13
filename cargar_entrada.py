def leerArchivoInicial(ruta_archivo, ubicaciones):
    try:
        with open(ruta_archivo, encoding="utf-8") as file:
            for linea in file:
                if not linea.startswith("crear_producto"):
                    print("Error en línea:", linea.strip())
                    continue

                _, datos = linea.strip().split(" ", 1)
                producto, cantidad, precio, ubicacion = datos.split(";")
                if ubicacion in ubicaciones:
                    ubicaciones[ubicacion][producto] = {
                        "cantidad": float(cantidad),
                        "precio": float(precio),
                    }
                else:
                    ubicaciones[ubicacion] = {
                        producto: {"cantidad": float(cantidad), "precio": float(precio)}
                    }
        print("Archivo cargado exitosamente")
    except Exception as e:
        print("Error al leer el archivo:", e)
