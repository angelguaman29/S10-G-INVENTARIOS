# Programa principal con menu interactivo para el sistema de inventarios
# Este archivo contiene la interfaz de usuario en consola.
# Permite al usuario interactuar con el inventario mediante un menu.

from servicios.inventario import Inventario


def mostrar_menu_principal():
    """
    Muestra el menu principal.
    
    Imprime las opciones disponibles para el usuario.
    """
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTION DE INVENTARIOS")
    print("=" * 60)
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar todos los productos")
    print("6. Ver estadisticas del inventario")
    print("0. Salir del sistema")
    print("=" * 60)


def opcion_agregar_producto(inventario):
    """
    Funcion que ejecuta la opcion de agregar un producto.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    try:
        # Solicitar los datos del producto
        id_producto = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad inicial: "))
        precio = float(input("Precio unitario: "))
        
        # Validar que los datos sean validos
        if cantidad < 0 or precio < 0:
            print("Error: Cantidad y precio no pueden ser negativos.")
            return
        
        # Llamar al metodo del inventario
        inventario.agregar_producto(id_producto, nombre, cantidad, precio)
    
    except ValueError:
        print("Error: Ingrese datos validos (numeros donde corresponda).")


def opcion_eliminar_producto(inventario):
    """
    Funcion que ejecuta la opcion de eliminar un producto.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    print("\n--- ELIMINAR PRODUCTO ---")
    
    try:
        # Solicitar el ID del producto a eliminar
        id_producto = int(input("ID del producto a eliminar: "))
        
        # Llamar al metodo del inventario
        inventario.eliminar_producto(id_producto)
    
    except ValueError:
        print("Error: Ingrese un ID valido (numero).")


def opcion_actualizar_producto(inventario):
    """
    Funcion que ejecuta la opcion de actualizar un producto.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    try:
        # Solicitar el ID del producto
        id_producto = int(input("ID del producto a actualizar: "))
        
        # Mostrar submenu de actualizacion
        print("\n¿Que desea actualizar?")
        print("1. Cantidad")
        print("2. Precio")
        print("3. Ambos")
        
        opcion = input("Seleccione (1-3): ")
        
        if opcion == "1":
            # Actualizar solo cantidad
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)
        
        elif opcion == "2":
            # Actualizar solo precio
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id_producto, nuevo_precio)
        
        elif opcion == "3":
            # Actualizar ambos
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.actualizar_cantidad(id_producto, nueva_cantidad)
            inventario.actualizar_precio(id_producto, nuevo_precio)
        
        else:
            print("Opcion no valida.")
    
    except ValueError:
        print("Error: Ingrese datos validos.")


def opcion_buscar_producto(inventario):
    """
    Funcion que ejecuta la opcion de buscar un producto.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    print("\n--- BUSCAR PRODUCTO ---")
    
    # Solicitar nombre a buscar
    nombre = input("Ingrese el nombre del producto a buscar: ")
    
    # Llamar al metodo buscar del inventario
    resultados = inventario.buscar_por_nombre(nombre)
    
    # Mostrar resultados
    if len(resultados) == 0:
        print(f"No se encontraron productos con '{nombre}'.")
    else:
        print(f"\nProductos encontrados ({len(resultados)}):")
        print("-" * 60)
        
        # Mostrar cada resultado
        for producto in resultados:
            producto.mostrar_informacion()


def opcion_listar_todos(inventario):
    """
    Funcion que ejecuta la opcion de listar todos los productos.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    # Llamar al metodo del inventario
    inventario.listar_todos_productos()


def opcion_estadisticas(inventario):
    """
    Funcion que muestra estadisticas del inventario.
    
    Parametro:
    - inventario: objeto de tipo Inventario
    """
    print("\n" + "=" * 60)
    print("ESTADISTICAS DEL INVENTARIO")
    print("=" * 60)
    
    # Obtener datos del inventario
    total_productos = inventario.obtener_total_productos()
    valor_total = inventario.obtener_valor_total_inventario()
    
    # Mostrar estadisticas
    print(f"Total de productos distintos: {total_productos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print("=" * 60)


def main():
    """
    Funcion principal que ejecuta el programa.
    
    Contiene el bucle principal que mantiene el menu activo.
    """
    # Crear el inventario
    inventario = Inventario()
    
    # Mensaje de bienvenida
    print("\nBienvenido al Sistema de Gestion de Inventarios")
    print("Universidad Estatal Amazonica")
    
    # Variable para controlar el bucle
    programa_activo = True
    
    # Bucle principal del programa
    while programa_activo:
        # Mostrar el menu
        mostrar_menu_principal()
        
        # Solicitar opcion al usuario
        opcion = input("Seleccione una opcion: ")
        
        # Procesar la opcion seleccionada
        if opcion == "1":
            opcion_agregar_producto(inventario)
        
        elif opcion == "2":
            opcion_eliminar_producto(inventario)
        
        elif opcion == "3":
            opcion_actualizar_producto(inventario)
        
        elif opcion == "4":
            opcion_buscar_producto(inventario)
        
        elif opcion == "5":
            opcion_listar_todos(inventario)
        
        elif opcion == "6":
            opcion_estadisticas(inventario)
        
        elif opcion == "0":
            # Salir del programa
            print("\nGracias por usar el Sistema de Gestion de Inventarios.")
            print("Hasta luego!")
            programa_activo = False
        
        else:
            # Opcion no valida
            print("\nOpcion no valida. Por favor intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    # Ejecutar la funcion principal
    main()