# Definir la clase Inventario que gestiona los productos
# Esta clase maneja todas las operaciones del inventario.
# MODIFICACION: Ahora guarda y carga productos desde un archivo.

from modelos.producto import Producto
from servicios.gestor_archivos import GestorArchivos


class Inventario:
    """
    Clase que gestiona el inventario de productos.
    
    Encargada de:
    - Almacenar una lista de productos
    - Agregar nuevos productos y guardarlos en archivo
    - Eliminar productos y actualizar el archivo
    - Buscar productos
    - Actualizar informacion de productos
    
    CAMBIO: Ahora persiste los datos en un archivo (inventario.txt)
    """
    
    def __init__(self):
        """
        Constructor de la clase Inventario.
        
        Inicializa una lista vacia para almacenar productos.
        CAMBIO: Crea un GestorArchivos para manejo de archivos.
        """
        # Lista privada que almacena todos los productos
        self._productos = []
        
        # CAMBIO: Crear gestor de archivos para persistencia de datos
        self._gestor = GestorArchivos("inventario.txt")
        
        # CAMBIO: Cargar productos existentes del archivo
        self._cargar_productos_del_archivo()
    
    
    def _cargar_productos_del_archivo(self):
        """
        Metodo PRIVADO que carga los productos desde el archivo al iniciar.
        
        Este metodo se llama automaticamente en el constructor.
        Si el archivo no existe, simplemente comienza con lista vacia.
        """
        # Llamar al gestor para cargar productos
        productos_cargados = self._gestor.cargar_productos()
        
        # Asignar los productos cargados a nuestra lista
        self._productos = productos_cargados
    
    
    def _guardar_en_archivo(self):
        """
        Metodo PRIVADO que guarda los productos en el archivo.
        
        Se llama automaticamente cada vez que agregamos, eliminamos o
        actualizamos un producto.
        """
        # Llamar al gestor para guardar productos
        exito = self._gestor.guardar_productos(self._productos)
        
        if exito:
            # Si se guardo correctamente, retorna True
            return True
        else:
            # Si hubo error, retorna False
            return False
    
    
    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """
        Metodo para agregar un nuevo producto al inventario.
        
        VALIDACION: Verifica que el ID no este repetido.
        CAMBIO: Guarda el producto en el archivo automaticamente.
        
        Parametros:
        - id_producto: ID unico del producto (integer)
        - nombre: nombre del producto (string)
        - cantidad: cantidad inicial (integer)
        - precio: precio unitario (float)
        
        Retorna: True si se agrego correctamente, False si hubo error
        """
        # Validar que el ID no este repetido
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                print(f"Error: El ID {id_producto} ya existe en el inventario.")
                return False
        
        # Crear el nuevo producto
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        
        # Agregar el producto a la lista
        self._productos.append(nuevo_producto)
        
        # CAMBIO: Guardar en archivo
        if self._guardar_en_archivo():
            print(f"Producto '{nombre}' agregado correctamente al inventario y guardado en archivo.")
            return True
        else:
            # Si no se pudo guardar, eliminar el producto que agregamos
            self._productos.remove(nuevo_producto)
            print(f"Error: No se pudo guardar '{nombre}' en el archivo.")
            return False
    
    
    def eliminar_producto(self, id_producto):
        """
        Metodo para eliminar un producto del inventario por ID.
        
        CAMBIO: Actualiza el archivo automaticamente.
        
        Parametro:
        - id_producto: ID del producto a eliminar (integer)
        
        Retorna: True si se elimino, False si no existe
        """
        # Buscar el producto
        for i, producto in enumerate(self._productos):
            if producto.obtener_id() == id_producto:
                # Guardar el nombre antes de eliminar
                nombre_eliminado = producto.obtener_nombre()
                
                # Eliminar el producto
                self._productos.pop(i)
                
                # CAMBIO: Guardar en archivo
                if self._guardar_en_archivo():
                    print(f"Producto '{nombre_eliminado}' eliminado del inventario y actualizado en archivo.")
                    return True
                else:
                    # Si no se pudo guardar, restaurar el producto
                    self._productos.insert(i, producto)
                    print(f"Error: No se pudo actualizar el archivo.")
                    return False
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """
        Metodo para actualizar la cantidad de un producto.
        
        CAMBIO: Guarda los cambios en el archivo.
        
        Parametros:
        - id_producto: ID del producto a actualizar (integer)
        - nueva_cantidad: la nueva cantidad (integer)
        
        Retorna: True si se actualizo, False si no existe
        """
        # Buscar el producto
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                # Cambiar la cantidad
                producto.establecer_cantidad(nueva_cantidad)
                
                # CAMBIO: Guardar en archivo
                if self._guardar_en_archivo():
                    print(f"Cantidad del producto ID {id_producto} actualizada a {nueva_cantidad} y guardada en archivo.")
                    return True
                else:
                    print(f"Error: No se pudo guardar los cambios en el archivo.")
                    return False
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def actualizar_precio(self, id_producto, nuevo_precio):
        """
        Metodo para actualizar el precio de un producto.
        
        CAMBIO: Guarda los cambios en el archivo.
        
        Parametros:
        - id_producto: ID del producto a actualizar (integer)
        - nuevo_precio: el nuevo precio (float)
        
        Retorna: True si se actualizo, False si no existe
        """
        # Buscar el producto
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                # Cambiar el precio
                producto.establecer_precio(nuevo_precio)
                
                # CAMBIO: Guardar en archivo
                if self._guardar_en_archivo():
                    print(f"Precio del producto ID {id_producto} actualizado a {nuevo_precio} y guardado en archivo.")
                    return True
                else:
                    print(f"Error: No se pudo guardar los cambios en el archivo.")
                    return False
        
        # Si no encuentra el producto
        print(f"Error: No existe producto con ID {id_producto}.")
        return False
    
    
    def buscar_por_nombre(self, nombre_busqueda):
        """
        Metodo para buscar productos por nombre.
        
        CARACTERISTICA: Permite coincidencias parciales.
        
        Parametro:
        - nombre_busqueda: nombre (o parte del nombre) a buscar (string)
        
        Retorna: lista con los productos encontrados
        """
        resultados = []
        
        for producto in self._productos:
            nombre_producto = producto.obtener_nombre()
            
            # Buscar coincidencias sin importar mayusculas/minusculas
            if nombre_busqueda.lower() in nombre_producto.lower():
                resultados.append(producto)
        
        return resultados
    
    
    def obtener_producto_por_id(self, id_producto):
        """
        Metodo para obtener un producto especifico por su ID.
        
        Parametro:
        - id_producto: ID del producto a buscar (integer)
        
        Retorna: el objeto Producto si existe, None si no existe
        """
        for producto in self._productos:
            if producto.obtener_id() == id_producto:
                return producto
        
        return None
    
    
    def listar_todos_productos(self):
        """
        Metodo para mostrar todos los productos del inventario.
        """
        if len(self._productos) == 0:
            print("\nEl inventario esta vacio.")
            return
        
        print("\n" + "=" * 70)
        print("INVENTARIO COMPLETO")
        print("=" * 70)
        
        numero = 1
        
        for producto in self._productos:
            print(f"{numero}. {producto.obtener_informacion_texto()}")
            numero += 1
        
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
        total = 0
        
        for producto in self._productos:
            cantidad = producto.obtener_cantidad()
            precio = producto.obtener_precio()
            
            total += cantidad * precio
        
        return total