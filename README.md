# Gestion de Inventarios Mejorado

## Descripcion

Sistema mejorado para gestionar inventarios de una tienda de electrodomesticos.

Permite:
- Agregar nuevos productos (Celulares, Televisiones, etc)
- Eliminar productos
- Actualizar cantidad y precio
- Buscar productos por nombre
- Listar todos los productos
- Ver estadisticas del inventario
- NUEVO: Guardar y cargar datos desde archivo automaticamente

---

## MEJORAS AGREGADAS EN ESTA VERSION

### 1. Persistencia de Datos (Guardar en Archivo)

Los productos ahora se guardan automaticamente en un archivo `inventario.txt` cuando:
- Agregas un producto nuevo
- Eliminas un producto
- Actualizas cantidad o precio

**Ventaja:** Los productos no se pierden al cerrar el programa.

### 2. Carga Automatica

Al abrir el programa, carga automaticamente todos los productos guardados anteriormente.

**Ventaja:** No necesitas agregar los productos de nuevo cada vez.

### 3. Manejo de Excepciones

El programa ahora maneja errores gracefully:
- Si el archivo no existe, lo crea automaticamente
- Si falta permiso de lectura/escritura, avisa al usuario
- Si datos estan corruptos, los ignora y continua
- No se crachea por errores de archivo

**Tipos de errores manejados:**
- `FileNotFoundError` - Archivo no existe
- `PermissionError` - Sin permisos de lectura/escritura
- `ValueError` - Datos con formato incorrecto
- `IOError` - Problemas de entrada/salida

### 4. Formato del Archivo

El archivo `inventario.txt` guarda los productos en formato simple:

```
ID|Nombre|Cantidad|Precio
1|Celular Samsung|10|50.99
2|Television LG|5|200.99
3|Refrigerador|3|500.99
```

Cada linea representa un producto con sus datos separados por `|`.

## Estructura del Proyecto

```
sistema-inventarios/
├── modelos/
│   ├── __init__.py
│   └── producto.py              (Clase Producto - SIN CAMBIOS)
├── servicios/
│   ├── __init__.py
│   ├── inventario.py            (Modificado - ahora guarda en archivo)
│   └── gestor_archivos.py       (NUEVO - maneja lectura/escritura)
├── main.py                      (Modificado - carga automatica)
├── inventario.txt               (NUEVO - archivo con datos que se generan)               
└── README.md                    (Este archivo)
```

---

## Como usar

### 1. Ejecutar el programa

```bash
python main.py
```

### 2. Seleccionar opcion del menu

```
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar todos los productos
6. Ver estadisticas del inventario
0. Salir del sistema
```

### 3. Ejemplo de sesion completa

**Primera vez (archivo vacio):**
```
- Inicia el programa
- Mensaje: "Archivo 'inventario.txt' no encontrado."
- Mensaje: "Se creara un nuevo archivo al agregar productos."
- Opcion 1: Agregar Celular Samsung (ID: 1, Cantidad: 10, Precio: 50.99)
- Mensaje: "Producto 'Celular Samsung' agregado correctamente al inventario y guardado en archivo."
- Opcion 1: Agregar Television LG (ID: 2, Cantidad: 5, Precio: 200.99)
- Opcion 5: Listar todos los productos (ve los 2 productos)
- Opcion 0: Salir
```

**Segunda vez (archivo con datos):**
```
- Inicia el programa
- Mensaje: "Se cargaron 2 productos del archivo."
- Opcion 5: Listar todos los productos
- ¡Ve los 2 productos que guardaste antes!
- Puedes editar, eliminar o agregar mas productos
- Opcion 0: Salir
```

---

## Nuevas Clases y Metodos

### Clase GestorArchivos (NUEVA)

**Responsabilidades:**
- Guardar productos en archivo
- Cargar productos desde archivo
- Manejar errores de archivo

**Metodos publicos:**
- `guardar_productos(productos)` - Guarda lista de productos en archivo
- `cargar_productos()` - Carga productos desde archivo
- `archivo_existe()` - Verifica si el archivo existe

**Metodos privados en Inventario:**
- `_cargar_productos_del_archivo()` - Carga datos al iniciar
- `_guardar_en_archivo()` - Guarda datos despues de cambios

---

## Manejo de Excepciones Implementado

El sistema maneja gracefully los siguientes errores:

| Error | Causa | Como se maneja |
|-------|-------|-----------------|
| FileNotFoundError | Archivo no existe | Se crea uno nuevo al agregar productos |
| PermissionError | Sin permisos de lectura/escritura | Se muestra error y se continua |
| ValueError | Datos con formato incorrecto | Se ignora la linea corrupta |
| IOError | Problemas de disco/entrada-salida | Se muestra el error especifico |

---

## Flujo de Datos

### Al Iniciar el Programa:
```
1. Se crea objeto Inventario
2. Constructor llama a _cargar_productos_del_archivo()
3. GestorArchivos.cargar_productos() lee inventario.txt
4. Se convierten lineas a objetos Producto
5. Los productos se cargan en memoria
```

### Al Agregar/Actualizar/Eliminar:
```
1. Usuario ejecuta opcion en menu
2. Se modifica lista de productos en memoria
3. Se llama a _guardar_en_archivo()
4. GestorArchivos.guardar_productos() escribe en inventario.txt
5. Se muestra confirmacion al usuario
```

---

## Mejoras Tecnicas Implementadas

✓ **Persistencia de Datos** - Los datos se guardan en archivo
✓ **Carga Automatica** - Se cargan datos al iniciar
✓ **Manejo Robusto de Excepciones** - No se cra cha por errores
✓ **Validacion de Datos** - Verifica formato correcto
✓ **Mensajes Informativos** - Avisa al usuario de exito/error
✓ **Codigo Modularizado** - GestorArchivos separado de Inventario
✓ **Comentarios Claros** - Explicacion detallada del codigo

---

## Cambios por Archivo

### modelos/producto.py
- **Estado:** SIN CAMBIOS
- **Razon:** La clase Producto sigue siendo igual

### servicios/inventario.py
- **Estado:** MODIFICADO
- **Cambios:**
  - Importa GestorArchivos
  - Constructor carga productos del archivo
  - Metodos guardan cambios en archivo
  - Nuevos metodos privados para cargar/guardar

### servicios/gestor_archivos.py
- **Estado:** NUEVO
- **Contenido:**
  - Manejo completo de lectura/escritura
  - Manejo de excepciones
  - Validacion de datos

### main.py
- **Estado:** MODIFICADO
- **Cambios:**
  - Comentarios actualizados
  - Mensajes de persistencia
  - Carga automatica al iniciar

---

## Problemas Conocidos y Soluciones

**Problema:** El programa dice "Archivo no encontrado"
**Solucion:** Es normal la primera vez. Se creara el archivo cuando agreques tu primer producto.

**Problema:** "Error de permisos al escribir"
**Solucion:** Verifica que tengas permisos de escritura en la carpeta del programa.

**Problema:** Los datos se muestran corruptos
**Solucion:** Borra `inventario.txt` y comienza de nuevo.

---

## Como hacer una prueba rapida

1. Ejecuta el programa: `python main.py`
2. Opcion 1: Agregar producto
   - ID: 1
   - Nombre: Celular Samsung
   - Cantidad: 10
   - Precio: 50.99
3. Opcion 1: Agregar otro producto
   - ID: 2
   - Nombre: Television LG
   - Cantidad: 5
   - Precio: 200.99
4. Opcion 5: Ver todos los productos
5. Opcion 0: Salir
6. Cierra el programa
7. Abre el archivo `inventario.txt` (en la carpeta del proyecto)
8. ¡Veras que los datos se guardaron!
9. Ejecuta de nuevo `python main.py`
10. Opcion 5: Listar productos
11. ¡Los productos se cargaron automaticamente!

## Notas Importantes

1. **Copia de Seguridad:** El archivo `inventario.txt` es tu copia de seguridad de datos
2. **Permisos:** Asegura que la carpeta del programa tenga permisos de escritura
3. **Corrupcion:** Si el archivo se corrompe, borra `inventario.txt` y comienza de nuevo
4. **Formato:** No edites `inventario.txt` a mano, siempre usa el programa