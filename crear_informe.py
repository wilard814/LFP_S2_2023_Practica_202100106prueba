def crearInforme(ubicaciones):
    try:
        with open("informe.txt", "w", encoding="utf-8") as file:
            file.write("Informe de Inventario:\n")
            file.write("Producto          Cantidad     Precio Unitario     Valor Total     Ubicación\n")
            file.write("-" * 78 + "\n")
            for ubicacion, productos in ubicaciones.items():
                for producto, info in productos.items():
                    valor_total = info["cantidad"] * info["precio"]
                    file.write(f"{producto.ljust(16)} {str(info['cantidad']).ljust(12)} {str(info['precio']).ljust(20)} ${valor_total:.2f} {ubicacion}\n")
            print("Informe creado exitosamente.")
    except Exception as e:
        print("Error al crear el informe:", e)
