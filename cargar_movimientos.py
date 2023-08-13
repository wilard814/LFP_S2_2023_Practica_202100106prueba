def cargarMovimientos(archivo_movimientos, ubicaciones):
    try:
        with open(archivo_movimientos, encoding="utf-8") as file:
            for num_linea, linea in enumerate(file, start=1):
                instruccion, informacion = linea.strip().split(" ")
                producto, cantidad, ubicacion = informacion.split(";")

                if instruccion == "agregar_stock":
                    if ubicacion not in ubicaciones:
                        print(f"Error en línea {num_linea}: Ubicación '{ubicacion}' no existe.")
                        continue
                    if producto not in ubicaciones[ubicacion]:
                        print(f"Error en línea {num_linea}: Producto '{producto}' no existe en '{ubicacion}'.")
                        continue
                    ubicaciones[ubicacion][producto]['cantidad'] += float(cantidad)
                elif instruccion == "vender_producto":
                    if ubicacion not in ubicaciones:
                        print(f"Error en línea {num_linea}: Ubicación '{ubicacion}' no existe.")
                        continue
                    if producto not in ubicaciones[ubicacion]:
                        print(f"Error en línea {num_linea}: Producto '{producto}' no existe en '{ubicacion}'.")
                        continue
                    ubicaciones[ubicacion][producto]['cantidad'] -= float(cantidad)
                else:
                    print(f"Error en línea {num_linea}: Instrucción no válida: {instruccion}")
    except Exception as e:
        print(f"Error al leer el archivo {archivo_movimientos}: {e}")
