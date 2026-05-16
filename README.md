======================================================================
     DOCUMENTACIÓN TÉCNICA: SIMULADOR DE E-COMMERCE (ecommerce_m3.py)
     REPOSITORIO: https://github.com/FleeInPaz/M3-Python-Tienda
======================================================================

1. DESCRIPCIÓN GENERAL DEL SISTEMA
----------------------------------------------------------------------
El script "ecommerce_m3.py" es un simulador de tienda virtual que se 
ejecuta completamente desde la consola de comandos utilizando Python 3.
Está desarrollado bajo el paradigma de programación estructurada/funcional,
donde un conjunto de funciones independientes procesan y manipulan 
estructuras de datos dinámicas en memoria (RAM) de forma continua.


2. ESTRUCTURAS DE DATOS PRINCIPALES (DEFINIDAS EN MAIN)
----------------------------------------------------------------------
* catalogo (Lista de Diccionarios): 
  Representa el inventario fijo de la tienda. Almacena 18 productos 
  distribuidos equitativamente en 3 categorías (Ropa, Tecnología, Hogar).
  Cada producto es un diccionario con tipos de datos básicos: 
  int (id, precio) y str (nombre, categoria).

* carrito (Lista Compuesta): 
  Estructura compuesta inicialmente vacía. Funciona como el contenedor 
  dinámico donde se duplican las referencias de los productos que el 
  usuario decide comprar para luego calcular los totales de la compra.


3. RESUMEN DE FUNCIONES Y COMPONENTES
----------------------------------------------------------------------

A) mostrar_menu()
   - Parámetros: Ninguno
   - Retorno: Ninguno
   - Descripción: Se encarga exclusivamente de la interfaz de usuario, 
     imprimiendo en la consola las opciones numéricas del sistema (0 al 5).

B) listar_productos(catalogo)
   - Parámetros: catalogo (lista)
   - Retorno: Ninguno
   - Descripción: Recorre cualquier estructura de productos utilizando un 
     ciclo 'for'. Formatea la salida en texto alineando las columnas de 
     ID, Nombre, Categoría y Precio para una lectura ordenada.

C) buscar_productos(catalogo)
   - Parámetros: catalogo (lista)
   - Retorno: resultados (lista de productos filtrados)
   - Descripción: [FUNCIÓN CON RETORNO] Identifica las categorías únicas 
     en el catálogo usando un conjunto (set). Muestra un submenú de grupos 
     y RETORNA una nueva lista filtrada que contiene únicamente los 
     productos de la categoría seleccionada por el usuario.

D) agregar_al_carrito(catalogo, carrito)
   - Parámetros: catalogo (lista), carrito (lista)
   - Retorno: Ninguno
   - Descripción: Solicita al usuario el ID de un artículo. Si el ID existe, 
     pide la cantidad y aplica una validación condicional estricta: si la 
     cantidad es mayor a 0, añade el producto el número de veces indicado 
     al carrito; de lo contrario, despliega un mensaje de error.

E) mostrar_carrito_y_total(carrito)
   - Parámetros: carrito (lista)
   - Retorno: Ninguno
   - Descripción: Implementa lógica condicional para evaluar el estado del 
     carrito. Si está vacío, muestra un mensaje informativo específico. 
     Si contiene elementos, los lista en pantalla y calcula en tiempo real 
     el monto total a pagar utilizando la función nativa 'sum()'.

F) vaciar_carrito(carrito)
   - Parámetros: carrito (lista)
   - Retorno: Ninguno
   - Descripción: Ejecuta el método nativo '.clear()' sobre la lista del 
     carrito, eliminando de golpe todos los elementos guardados y 
     restableciendo su estado a vacío.


4. MECANISMOS DE CONTROL, FLUJO Y ROBUSTEZ
----------------------------------------------------------------------
* Ciclo de Vida: Un bucle 'while' en la función 'main()' mantiene el 
  programa en ejecución constante. Solo se rompe cuando la variable 
  'opcion' pasa a ser 0.

* Validación del Menú: Estructuras condicionales 'if-elif-else' validan 
  que la opción ingresada corresponda a una acción integrada, derivando 
  el flujo a la función correspondiente o mostrando un mensaje de alerta.

* Control de Excepciones: Bloques 'try-except' capturan errores del tipo 
  'ValueError'. Esto evita que el programa se caiga (crash) si el usuario 
  introduce letras por accidente en campos que exigen números enteros.

* Buenas Prácticas y Estilo: El código aplica el estándar 'snake_case' 
  para el nombrado de variables y funciones, mantiene una sangría 
  reglamentaria de 4 espacios e incorpora comentarios breves que guían 
  la evaluación.
======================================================================
