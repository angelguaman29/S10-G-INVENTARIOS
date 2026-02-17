# Gestion de Inventarios

Sistema simple para gestionar un inventario de productos.

Permite:
- Agregar nuevos productos
- Eliminar productos
- Actualizar cantidad y precio
- Buscar productos por nombre
- Listar todos los productos
- Ver estadisticas del inventario

---

## Estructura del Proyecto

```
sistema-inventarios/
├── modelos/
│   ├── __init__.py
│   └── producto.py           
├── servicios/
│   ├── __init__.py
│   └── inventario.py         
├── main.py                   
└── README.md                 
```

---

## Como usar

### 1. Ejecutar el programa

```bash
python main.py
```

### 2. Seleccionar una opcion del menu

El programa muestra un menu con estas opciones:

```
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar todos los productos
6. Ver estadisticas del inventario
0. Salir del sistema
```

## Estructura de clases

### Clase Producto

**Atributos:**
- ID: identificador unico
- Nombre: nombre del producto
- Cantidad: cantidad en stock
- Precio: precio unitario

**Metodos principales:**
- `obtener_id()`: retorna el ID
- `obtener_nombre()`: retorna el nombre
- `obtener_cantidad()`: retorna la cantidad
- `obtener_precio()`: retorna el precio
- `establecer_cantidad()`: cambia la cantidad
- `establecer_precio()`: cambia el precio

### Clase Inventario

**Atributos:**
- `_productos`: lista de productos

**Metodos principales:**
- `agregar_producto()`: agrega un nuevo producto
- `eliminar_producto()`: elimina un producto por ID
- `actualizar_cantidad()`: actualiza la cantidad
- `actualizar_precio()`: actualiza el precio
- `buscar_por_nombre()`: busca productos por nombre
- `listar_todos_productos()`: muestra todos los productos
- `obtener_valor_total_inventario()`: calcula el valor total

---

## Caracteristicas importantes

### Validaciones

- **ID unico**: no permite IDs repetidos
- **Cantidad**: debe ser positiva
- **Precio**: debe ser positivo
- **Entrada de usuario**: valida que sea del tipo correcto

### Encapsulacion

- Usa atributos privados (_)
- Acceso controlado mediante getters y setters
- Validacion en los setters

---
