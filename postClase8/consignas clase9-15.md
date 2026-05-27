## CLASE 9
Ejercicio práctico:
Mariana te ha asignado una tarea clave para el proyecto de TalentoLab: desarrollar un pequeño programa que permita gestionar una lista de productos utilizando funciones. El objetivo es que la usuaria o usuario pueda agregar, consultar y eliminar productos, aplicando lo que aprendiste sobre funciones y listas. Este ejercicio te ayudará a modularizar el código y a practicar la interacción con el usuario. Así te lo ha comunicado Mariana:
¡Hola!
Tu tarea es crear un programa en Python con las siguientes características:
● Agregar productos: Permite a la usuaria o usuario agregar productos a una lista. Cada producto debe tener un nombre y un precio.
● Consultar productos: Muestra todos los productos en la lista junto con sus precios.
● Eliminar productos: Elimina un producto de la lista a partir de su nombre.
● Menú interactivo: El programa debe ofrecer un menú para que el usuario o usuaria pueda elegir qué acción realizar. Debe incluirse una opción para salir del programa.


Preguntas para reflexionar:
1. ¿Por qué es útil dividir el código en funciones en lugar de escribir todo en un solo bloque? Reflexioná sobre cómo las funciones ayudan a organizar y simplificar tareas complejas en tu programa. ¿Qué ventajas notás al estructurar el código de esta manera?
2. ¿Cómo podría mejorar el programa de gestión de productos que desarrollaste?
Considerá qué funcionalidades adicionales podrías agregar (por ejemplo, modificar el precio de un producto o buscar productos específicos). ¿Cómo cambiaría el código si implementaras estas mejoras?
3. ¿Cómo podrías aplicar lo aprendido sobre funciones en tu Trabajo Final Integrador (TFI)? Pensá en qué partes del TFI podrías simplificar o mejorar usando funciones. ¿Qué beneficios tendría modularizar tu código para el proyecto final?
4. ¿Podrías crear una función que permita modificar un producto ya cargado? ¿Cómo la diseñarías?

---

## CLASE 10
Ejercicio práctico:
El día finaliza con otra reunión en la oficina de Mariana. Con su energía habitual, te felicita por el progreso que estás logrando. "Luis me mostró el programa de gestión de frutas que desarrollaste, y estoy muy impresionada con lo bien que aplicaste las funciones para organizar el código. Sin embargo, quiero proponerte un desafío adicional:
Tu tarea es modificar el programa que escribiste la clase anterior, para que realice las mismas tareas, pero utilizando funciones que devuelvan valores cuando sea posible. Recordá que el programa te permitía:
● Agregar productos: Cada producto debe tener un nombre y un precio.
● Consultar productos: Muestra todos los productos en la lista junto con sus precios.
● Eliminar productos: A partir de su nombre.
● Menú interactivo: Debe ofrecer un menú para que se pueda elegir qué acción realizar.

Preguntas para reflexionar:
1. ¿De qué manera las funciones que devuelven valores pueden hacer que tu código sea más modular y reutilizable? Pensá en cómo podrías aplicar este concepto en proyectos más grandes.
2. ¿Cómo te ayuda la posibilidad de devolver múltiples valores con tuplas a resolver problemas de programación de forma más eficiente? ¿Podés pensar en un ejemplo práctico donde esto sea útil?
3. ¿Qué importancia tiene documentar tus funciones con docstrings? Reflexioná sobre cómo esto puede facilitar la colaboración en proyectos de equipo.

---

## CLASE 11

Ejercicio Práctico
Cómo es habitual, finalizas el día con una reunión de trabajo en la oficina de Mariana, que te felicita por tu progreso. "Luis me mostró el programa de gestión de frutas que desarrollaste, y estoy muy impresionada con lo bien que aplicaste las funciones para organizar el código. Sin embargo, es hora de mejorarlo:
Tu tarea es volver a modificar el programa que escribiste la clase anterior, para que realice las mismas tareas, pero que su interacción mediante la terminal esté mejorada utilizando Colorama. También sería genial si agregas un dato a cada producto que contenga la fecha y hora de la compra, usando la librería datetime

Preguntas para Reflexionar:
1. ¿Cómo creés que el uso de módulos puede ayudarte a mejorar la organización de tus proyectos? Pensá en ejemplos concretos donde dividir el código en módulos podría simplificar su mantenimiento.
2. Los módulos estándar como random y datetime ofrecen muchas funcionalidades predefinidas. ¿Qué ventajas encontrás al usar estas herramientas en lugar de desarrollar todo desde cero? ¿Podrías pensar en aplicaciones prácticas para estos módulos en tus proyectos?
3. La biblioteca colorama permite personalizar la interacción en la consola con colores. ¿Cómo podría mejorar la experiencia del usuario en programas que diseñes? ¿Qué otras aplicaciones creativas podrías imaginar para este módulo?
4. Ahora que entendiste cómo crear tus propios módulos, ¿cómo los usarías para estructurar un proyecto más grande? ¿Qué partes del código podrías separar en diferentes archivos para facilitar el trabajo en equipo?

---

## CLASE 12

Ejercicio Práctico:
Como parte del proyecto de TalentoLab, el cliente necesita un sistema que permita registrar los datos de los usuarios en un archivo de texto, para que puedan ser recuperados y utilizados en futuras sesiones. Diego te asignó la tarea de desarrollar este sistema básico de persistencia de datos, aplicando todo lo que aprendiste. Tu tarea consiste en:
1) Creá un programa que permita ingresar los datos de un cliente: nombre, apellido y correo electrónico. Usá try-except para manejar posibles errores durante la entrada de datos. Por ejemplo:
● Si el archivo no puede abrirse para escritura.
● Si los datos ingresados no son válidos (por ejemplo, si el correo no contiene una "@" o el nombre está vacío).
2) Guardá los datos ingresados en un archivo de texto llamado clientes.txt, de forma que cada cliente quede registrado en una nueva línea.
3)Una vez guardados los datos, mostrá un mensaje de confirmación al usuario y cerrá el archivo correctamente.
La salida por la terminal podría ser algo asi:

=== Registro de Clientes ===
Ingresá los datos del cliente:
Nombre: Ana
Apellido: López
Correo: ana.lopez@email.com

Cliente registrado con exito en clientes.txt

//Si ocurre un error, el programa debería mostrar un mensaje claro:
[ERROR] No se puedo guardar la información.

Preguntas para Reflexionar:
1. ¿Por qué es importante la persistencia de datos en las aplicaciones que desarrollamos? ¿Cómo creés que afecta esto a la experiencia del usuario final?
2. ¿Qué ventajas encontrás en el uso de archivos de texto para guardar información? ¿Cuáles serían las limitaciones de esta técnica frente a otras opciones como las bases de datos?
3. ¿Cómo te sentiste utilizando try-except para manejar errores? ¿Podés identificar situaciones reales en las que su uso sería esencial?

---

## CLASE 13
Ejercicio Práctico
Al finalizar el día, Diego se acerca con una solicitud concreta:
"Mariana ha hablado con el cliente, y tienen una tarea específica que quieren resolver ya mismo. Nos pidieron que hagamos una prueba con el sistema SQLite. Necesitamos algo básico pero funcional: registrar productos con su nombre y precio, y luego mostrarlos en pantalla para asegurarnos de que el registro funciona correctamente. ¿Te animás a encargarte de esta parte? Es clave para que avancemos hacia la solución más completa." Necesitaras:
1. Crear una base de datos SQLite llamada productos.db.
2. Definir una tabla llamada productos con los campos id (clave primaria autoincremental), nombre (texto, no nulo) y precio (real, no nulo).
3. Diseñar un programa que permita:
○ Registrar un producto ingresando su nombre y precio.
○ Mostrar todos los productos almacenados en la base de datos.
El sistema debe incluir validaciones básicas:
● El nombre no puede estar vacío.
● El precio debe ser un número mayor que cero.



Preguntas para Reflexionar:
1. Aprendiste a crear tablas y realizar consultas básicas. ¿Qué beneficios encontrás en estructurar los datos en tablas con campos definidos en lugar de usar listas o diccionarios?
2. Pensando en las operaciones SQL que vimos (SELECT, INSERT, UPDATE, DELETE), ¿cuál te pareció más intuitiva y por qué?
3. ¿Qué errores podrías prever al trabajar con bases de datos en programas reales y cómo creés que podrías evitarlos usando lo aprendido?
4. ¿Cómo podrías aplicar el uso de bases de datos SQLite en un proyecto más complejo, como el Trabajo Final Integrador?

---

## CLASE 14
Ejercicio Práctico
La jornada en TalentoLab transcurre con el habitual ritmo de trabajo cuando Mariana se acerca a tu escritorio con su tablet en la mano.
"¡Felicitaciones! El cliente ha quedado muy conforme con la primera versión del registro de productos. Pudieron cargar información y recuperarla sin problemas. Pero ahora nos piden algunas mejoras para garantizar que el sistema sea más seguro y fácil de administrar."
Te muestra en pantalla un par de puntos que debemos agregar:
1. Validación de datos al registrar un producto: Actualmente, el sistema permite agregar productos, pero no verifica si los datos ingresados son válidos. Es necesario asegurarse de que el nombre del producto no esté vacío y que el precio sea un número positivo antes de almacenarlo en la base de datos.
2. Eliminar un producto con confirmación: El cliente quiere evitar eliminaciones accidentales. Por lo tanto, al eliminar un producto, el sistema debe solicitar una confirmación antes de ejecutar la acción.
Desde su escritorio, Luis se suma a la conversación:
Podrías aprovechar Colorama para mejorar la experiencia visual. Por ejemplo, podrías resaltar los mensajes de advertencia en rojo, las confirmaciones en verde, y la información general en azul. Haría que la interfaz sea más clara y atractiva para el usuario

Preguntas para Reflexionar:
1. Cuando trabajamos con bases de datos en Python, ¿por qué es importante utilizar parámetros en las consultas en lugar de concatenar directamente los valores ingresados por el usuario?
2. En la implementación de transacciones con SQLite, ¿qué problema se podría generar si olvidamos hacer un COMMIT después de una serie de modificaciones en la base de datos?
3. El manejo de excepciones con try-except es clave para evitar errores inesperados. ¿Qué tipo de situaciones creés que podrían requerir un ROLLBACK dentro de un bloque except?
4. Si tuvieras que optimizar un sistema CRUD para mejorar su seguridad y rendimiento, ¿qué técnicas o herramientas considerarías implementar más allá de lo aprendido en esta clase

---

## CLASE 15

Objetivo general
El objetivo de estas actividades es que puedas usar la inteligencia artificial como una herramienta que te ayude a mejorar tu proyecto, así que te invitamos a utilizar herramientas de inteligencia artificial como apoyo para diseñar y validar la solución completa del inventario: desde la creación de la base de datos y su(s) tabla(s) hasta las operaciones CRUD, búsqueda, reporte de bajo stock y una interfaz por consola clara. La IA debe ayudarte a tomar mejores decisiones técnicas (tipos de datos, claves, restricciones, validaciones, consultas) y a presentar un proyecto prolijo, robusto y bien documentado.


Entrega del Proyecto Final con IA
En esta etapa del curso, es común sentirse abrumado por la cantidad de elementos que hay que integrar: base de datos, CRUD, validaciones, reportes y presentación. Usá tu asistente de IA como guía para organizar tu trabajo y resolver dudas puntuales mientras desarrollás tu sistema de inventario.


Podés pedirle que:
Te ayude a dividir tu proyecto en etapas: diseño del modelo de datos (DDL), implementación de operaciones CRUD, búsquedas y reportes, manejo de errores, interfaz por consola y documentación final.
Revise si tu esquema de base de datos en SQLite está bien definido (tipos de datos, PRIMARY KEY, NOT NULL, CHECK, FOREIGN KEY si corresponde).
Analice tus consultas parametrizadas (INSERT, SELECT, UPDATE, DELETE) y sugiera mejoras para mayor seguridad y claridad.
Proponga mejoras en la estructura del código para modularizarlo (separar conexión, consultas y menú).
Recomiende mensajes de error/éxito más claros y una navegación por menú más amigable.
Preguntas útiles para hacerle a la IA
“¿Mi DDL para productos(id, nombre, descripcion, cantidad, precio, categoria) está bien? ¿Qué CHECK conviene para cantidad y precio?”
“¿Uso REAL, NUMERIC o INTEGER para el campo precio en SQLite? ¿Por qué?”
“¿Cómo manejo si un id no existe al hacer un UPDATE o DELETE?”
“¿Cómo optimizar mi consulta de reporte de bajo stock (cantidad <= umbral)?”
“¿Podés sugerirme una estructura de README.txt para la entrega final?”

Criterio de uso:
La IA no va a hacer tu proyecto por vos, pero sí puede ayudarte a ordenar tus ideas, detectar errores y mejorar la presentación. Usala como una herramienta de apoyo para verificar decisiones y obtener sugerencias, pero asegurate de entender y adaptar cada cambio que apliques. El código final debe ser tuyo, y debés comprender cómo y por qué funciona.

Reflexión:
Antes de dar por finalizado tu proyecto, reflexioná:
¿La IA me ayudó a planificar mejor mi trabajo?
¿Qué parte logré simplificar gracias a su ayuda?
¿Aprendí una forma más eficiente de estructurar el código o las consultas SQL?
¿Pude encontrar soluciones que no conocía?
¿Mi base de datos y mis funciones reflejan bien las necesidades reales del proyecto?
Ahora te toca a vos:
Basado en las consignas del proyecto final que leímos al inicio, abrí tu asistente de IA favorito y explícale las mejoras que querés implementar.
Para ello, podés usar cualquier modelo de IA generativa que tengas disponible (ChatGPT, Gemini, Copilot, etc.).

---
