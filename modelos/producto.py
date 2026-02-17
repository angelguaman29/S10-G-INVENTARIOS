# Definimos la clase Producto que representa un producto en el inventario
# Esta clase encapsula los atributos y metodos de un producto.
# Cada producto posee ID, nombre, cantidad y precio.

class Producto:
    
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Se ejecuta cuando se crea un nuevo objeto Producto.
        Inicializa todos los atributos del producto.
        
        Parametros:
        - id_producto: identificador unico del producto (integer)
        - nombre: nombre del producto (string)
        - cantidad: cantidad disponible en inventario (integer)
        - precio: precio unitario del producto (float)
        """
        # Atributo privado: ID unico del producto
        # Se usa _ para indicar que es privado
        self._id = id_producto
        
        # Atributo privado: nombre del producto
        self._nombre = nombre
        
        # Atributo privado: cantidad en stock
        self._cantidad = cantidad
        
        # Atributo privado: precio unitario
        self._precio = precio
    
    
    #  GETTERS (Metodos para obtener datos)
    
    def obtener_id(self):
        """
        Metodo getter para obtener el ID del producto.
        
        Retorna: ID del producto (integer)
        """
        return self._id
    
    
    def obtener_nombre(self):
        """
        Metodo getter para obtener el nombre del producto.
        
        Retorna: nombre del producto (string)
        """
        return self._nombre
    
    
    def obtener_cantidad(self):
        """
        Metodo getter para obtener la cantidad en inventario.
        
        Retorna: cantidad del producto (integer)
        """
        return self._cantidad
    
    
    def obtener_precio(self):
        """
        Metodo getter para obtener el precio del producto.
        
        Retorna: precio del producto (float)
        """
        return self._precio
    
    
    # SETTERS (Metodos para cambiar datos)
    
    def establecer_nombre(self, nuevo_nombre):
        """
        Metodo setter para cambiar el nombre del producto.
        
        Los setters permiten cambiar atributos privados
        de forma controlada.
        
        Parametro:
        - nuevo_nombre: el nuevo nombre del producto (string)
        """
        # Validar que el nombre no esté vacío
        if nuevo_nombre.strip():  # strip() elimina espacios
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre no ir vacio.")
    
    
    def establecer_cantidad(self, nueva_cantidad):
        """
        Metodo setter para cambiar la cantidad.
        
        Parametro:
        - nueva_cantidad: la nueva cantidad (integer)
        """
        # Validar que la cantidad sea positiva
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")
    
    
    def establecer_precio(self, nuevo_precio):
        """
        Metodo setter para cambiar el precio.
        
        Parametro:
        - nuevo_precio: el nuevo precio (float)
        """
        # Validar que el precio sea positivo
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")
    
    
    # METODOS ADICIONALES
    
    def mostrar_informacion(self):
        """
        Metodo que muestra toda la informacion del producto.
        
        Este metodo imprime los detalles del producto de forma
        formateada y facil de leer.
        """
        print("\n" + "-" * 50)
        print(f"ID: {self._id}")
        print(f"Nombre: {self._nombre}")
        print(f"Cantidad: {self._cantidad}")
        print(f"Precio: ${self._precio:.2f}")
        print("-" * 50)
    
    
    def obtener_informacion_texto(self):
        """
        Metodo que retorna la informacion del producto como texto.
        
        Retorna: cadena de texto con la informacion del producto
        """
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"