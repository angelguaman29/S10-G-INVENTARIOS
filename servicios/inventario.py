# Definimos la clase Inventario que gestiona los productos
# Esta clase maneja todas las operaciones del inventario.
# Permite agregar, eliminar, buscar y actualizar productos.

from modelos.producto import Producto


class Inventario:
    """
    Gestiona el inventario de productos.
    
    Encargada de:
    - Almacenar una lista de productos
    - Agregar nuevos productos
    - Eliminar productos
    - Buscar productos
    - Actualizar informacion de productos
    """
    
    def __init__(self):
        """
        Constructor de la clase Inventario.
        
        Inicializa una lista vacia para almacenar los productos.
        """
        # Lista privada que almacena todos los productos
        # Es una lista vacia al principio
        self._productos = []
    
    
    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """
        Metodo para agregar un nuevo producto al inventario.
        
        VALIDACION: Verifica que el ID no este repetido.
        Si el ID ya existe, muestra error y no agrega el producto.
        
        Parametros:
        - id_producto: ID unico del producto (integer)
        - nombre: nombre del producto (string)
        - cantidad: cantidad inicial (integer)
        - precio: precio unitario (float)
        
        Retorna: True si se agrego correctamente, False si hubo error
        """
        # Validar que el ID no este repetido
        # Recorrer la lista de productos
        for producto in self._productos:
            # Si encontramos un producto con el mismo ID
            if producto.obtener_id() == id_producto:
                # Mostrar error
                print(f"Error: El ID {id_producto} ya existe en el inventario.")
                return False
        
        # Si el ID no existe, crear el nuevo producto
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        
        # Agregar el producto a la lista
        self._productos.append(nuevo_producto)
        
        # Mensaje de confirmacion
        print(f"Producto '{nombre}' agregado correctamente al inventario.")
        return True
    
    
    def eliminar_producto(self, id_producto):
        """
        Metodo para eliminar un producto del inventario por ID.
        
        Parametro:
        - id_producto: ID del producto a eliminar (integer)
        
        Retorna: True si se elimino, False si no existe
        """
        # Recorrer la lista de productos
        for i, producto in enumerate(self._productos):
            # Si encontramos el producto con ese ID
            if producto.obtener_id() == id_producto:
                # Guardar el nombre antes de eliminar
                nombre_eliminado = producto.obtener_nombre()
                
                # Eliminar el producto de la lista
                # pop() elimina en la posicion i
                self._productos.pop(i)
                
                # Mensaje de confirmacion
                print(f"Producto '{nombre_eliminado}' eliminado del inventario.")
                return True
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """
        Metodo para actualizar la cantidad de un producto.
        
        Parametros:
        - id_producto: ID del producto a actualizar (integer)
        - nueva_cantidad: la nueva cantidad (integer)
        
        Retorna: True si se actualizo, False si no existe
        """
        # Buscar el producto por ID
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                # Usar el setter para cambiar la cantidad
                # El setter valida que sea positiva
                producto.establecer_cantidad(nueva_cantidad)
                
                print(f"Cantidad del producto ID {id_producto} actualizada a {nueva_cantidad}.")
                return True
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def actualizar_precio(self, id_producto, nuevo_precio):
        """
        Metodo para actualizar el precio de un producto.
        
        Parametros:
        - id_producto: ID del producto a actualizar (integer)
        - nuevo_precio: el nuevo precio (float)
        
        Retorna: True si se actualizo, False si no existe
        """
        # Buscar el producto por ID
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                # Usar el setter para cambiar el precio
                # El setter valida que sea positivo
                producto.establecer_precio(nuevo_precio)
                
                print(f"Precio del producto ID {id_producto} actualizado a ${nuevo_precio:.2f}.")
                return True
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def buscar_por_nombre(self, nombre_busqueda):
        """
        Metodo para buscar productos por nombre.
        
        Parametro:
        - nombre_busqueda: nombre (o parte del nombre) a buscar (string)
        
        Retorna: lista con los productos encontrados
        """
        # Lista para guardar los resultados
        resultados = []
        
        # Recorrer la lista de productos
        for producto in self._productos:
            # Obtener el nombre del producto
            nombre_producto = producto.obtener_nombre()
            
            # Convertir ambos a minusculas para ignorar mayusculas/minusculas
            # Verificar si el nombre buscado esta contenido en el nombre del producto
            if nombre_busqueda.lower() in nombre_producto.lower():
                # Agregar a resultados
                resultados.append(producto)
        
        return resultados
    
    
    def obtener_producto_por_id(self, id_producto):
        """
        Metodo para obtener un producto especifico por su ID.
        
        Parametro:
        - id_producto: ID del producto a buscar (integer)
        
        Retorna: el objeto Producto si existe, None si no existe
        """
        # Recorrer la lista de productos
        for producto in self._productos:
            # Si encontramos el producto
            if producto.obtener_id() == id_producto:
                return producto
        
        # Si no existe, retorna None
        return None
    
    
    def listar_todos_productos(self):
        """
        Metodo para mostrar todos los productos del inventario.
        
        Imprime informacion de todos los productos de forma
        ordenada y facil de leer.
        """
        # Verificar si hay productos
        if len(self._productos) == 0:
            print("\nEl inventario esta vacio.")
            return
        
        # Mostrar encabezado
        print("\n" + "=" * 70)
        print("INVENTARIO COMPLETO")
        print("=" * 70)
        
        # Variable para enumerar
        numero = 1
        
        # Recorrer y mostrar cada producto
        for producto in self._productos:
            # Mostrar la informacion
            print(f"{numero}. {producto.obtener_informacion_texto()}")
            numero += 1
        
        # Mostrar cantidad total
        print("=" * 70)
        print(f"Total de productos en el inventario: {len(self._productos)}")
        print("=" * 70)
    
    
    def obtener_total_productos(self):
        """
        Metodo que retorna la cantidad total de productos distintos.
        
        Retorna: numero de productos en el inventario (integer)
        """
        return len(self._productos)
    
    
    def obtener_valor_total_inventario(self):
        """
        Metodo que calcula el valor total del inventario.
        
        Calcula: suma de (cantidad * precio) para todos los productos.
        
        Retorna: valor total en dinero (float)
        """
        # Variable para acumular el total
        total = 0
        
        # Recorrer cada producto
        for producto in self._productos:
            # Obtener cantidad y precio
            cantidad = producto.obtener_cantidad()
            precio = producto.obtener_precio()
            
            # Agregar al total: cantidad * precio
            total += cantidad * precio
        
        return total