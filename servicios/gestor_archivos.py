# Manejar la lectura y escritura de archivos del inventario
# Esta clase gestiona la persistencia de datos (guardar y cargar productos).
# Usa manejo de excepciones para evitar errores al trabajar con archivos.

from modelos.producto import Producto


class GestorArchivos:
    """
    Gestiona la lectura y escritura de archivos del inventario.
    
    Responsabilidades:
    - Guardar productos en un archivo de texto
    - Cargar productos desde un archivo de texto
    - Manejar errores si algo falla 
    """
    
    def __init__(self, nombre_archivo="inventario.txt"):
        """
        Constructor de la clase GestorArchivos.
        
        Parametro:
        - nombre_archivo: nombre del archivo donde guardar datos (default: inventario.txt)
        """
        # Nombre del archivo donde se guardaran los productos
        self.nombre_archivo = nombre_archivo
    
    
    def guardar_productos(self, productos):
        """
        Metodo que guarda todos los productos en un archivo de texto.
        
        Formato del archivo:
        ID|Nombre|Cantidad|Precio
        
        Ejemplo:
        1|Celular|10|499.99
        2|Television|5|799.99
        
        Parametro:
        - productos: lista de objetos Producto
        
        Retorna: True si se guardo exitosamente, False si hubo error
        """
        try:
            # Abrir el archivo en modo escritura
            # 'w' = modo escritura (sobrescribe el archivo)
            with open(self.nombre_archivo, 'w') as archivo:
                # Recorrer cada producto
                for producto in productos:
                    # Obtener los datos del producto
                    id_prod = producto.obtener_id()
                    nombre = producto.obtener_nombre()
                    cantidad = producto.obtener_cantidad()
                    precio = producto.obtener_precio()
                    
                    # Crear una linea con formato: ID|Nombre|Cantidad|Precio
                    linea = f"{id_prod}|{nombre}|{cantidad}|{precio}\n"
                    
                    # Escribir la linea en el archivo
                    archivo.write(linea)
            
            # Si llega aqui, todo salio bien
            return True
        
        except PermissionError:
            # Error: No tenemos permisos para escribir en el archivo
            print("Error: No tiene permisos para escribir en el archivo.")
            return False
        
        except IOError as error:
            # Error: Problema de entrada/salida (problemas con el disco, etc)
            print(f"Error al guardar el archivo: {error}")
            return False
        
        except Exception as error:
            # Error: Cualquier otro error inesperado
            print(f"Error inesperado al guardar: {error}")
            return False
    
    
    def cargar_productos(self):
        """
        Carga todos los productos desde el archivo.
        
        Lee el archivo linea por linea y convierte cada linea en un objeto Producto.
        
        Retorna: lista de objetos Producto si todo va bien, lista vacia si hay error
        """
        # Lista para almacenar los productos cargados
        productos_cargados = []
        
        try:
            # Abrir el archivo en modo lectura
            # 'r' = modo lectura
            with open(self.nombre_archivo, 'r') as archivo:
                # Leer todas las lineas del archivo
                lineas = archivo.readlines()
                
                # Recorrer cada linea
                for linea in lineas:
                    # Eliminar saltos de linea y espacios al inicio/final
                    linea = linea.strip()
                    
                    # Saltar lineas vacias
                    if not linea:
                        continue
                    
                    try:
                        # Dividir la linea por el separador '|'
                        # Formato: ID|Nombre|Cantidad|Precio
                        partes = linea.split('|')
                        
                        # Validar que la linea tenga exactamente 4 partes
                        if len(partes) != 4:
                            print(f"Advertencia: Linea corrupta omitida: {linea}")
                            continue
                        
                        # Convertir los datos al tipo correcto
                        id_prod = int(partes[0])           # Convertir ID a integer
                        nombre = partes[1]                 # Nombre es string
                        cantidad = int(partes[2])          # Convertir cantidad a integer
                        precio = float(partes[3])          # Convertir precio a float
                        
                        # Crear un nuevo objeto Producto
                        producto = Producto(id_prod, nombre, cantidad, precio)
                        
                        # Agregar el producto a la lista
                        productos_cargados.append(producto)
                    
                    except ValueError:
                        # Error: No se pudo convertir un valor al tipo esperado
                        print(f"Advertencia: Datos invalidos en linea: {linea}")
                        continue
            
            # Si cargamos productos, mostrar mensaje
            if productos_cargados:
                print(f"Se cargaron {len(productos_cargados)} productos del archivo.")
            
            return productos_cargados
        
        except FileNotFoundError:
            # Error: El archivo no existe
            # En lugar de falla, retornamos una lista vacia
            print(f"Archivo '{self.nombre_archivo}' no encontrado.")
            print("Se creara un nuevo archivo al agregar productos.")
            return []
        
        except PermissionError:
            # Error: No tenemos permisos para leer el archivo
            print("Error: No tiene permisos para leer el archivo.")
            return []
        
        except IOError as error:
            # Error: Problema de entrada/salida
            print(f"Error al leer el archivo: {error}")
            return []
        
        except Exception as error:
            # Error: Cualquier otro error inesperado
            print(f"Error inesperado al cargar: {error}")
            return []
    
    
    def archivo_existe(self):
        """
        Verifica si el archivo del inventario existe.
        
        Retorna: True si existe, False si no existe
        """
        import os
        return os.path.exists(self.nombre_archivo)