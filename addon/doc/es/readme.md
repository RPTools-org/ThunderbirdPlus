# Thunderbird+ #

* Autor: Pierre-Louis Renaud, Daniel Poiraud
* URL: Documentación y contacto: [Pierre-Louis](http://www.rptools.org/Outils-DV/contact.html] , en Francés y Inglés);
* Descargar:
	* [versión estable][1]
* Compatibilidad:
	* versión mínima de NVDA requerida: 2019.3
	* última versión de NVDA probada: 2022.1

Este complemento mejora enormemente la comodidad y la eficiencia del uso del cliente de correo electrónico Mozilla Thunderbird con NVDA.

* **Confort auditivo:**
	* Las alertas  "fulano ha solicitado que se le notifique cuando Vd. lea este mensaje." se puede desactivar a través de una opción;
	* Las alertas "Este mensaje es un borrador" y "Thunderbird piensa que este mensaje es correo basura" simplemente se ignoran; 
	* Las opciones permiten desactivar el anuncio de los nombres de las listas de correo, eliminar o agrupar las menciones "RE" y depurar los nombres de los correspondientes eliminando los números y otros caracteres especiales incómodos;  
	* **Navegación mejorada:**
	* Pasar al siguiente panel se realiza con la tecla TAB, mientras que la tecla Escape le permite volver al panel anterior. Esto es más cómodo que F6 y -shift+F6. 
	* dos cuadros de diálogo de cuentas y sus carpetas asociadas permiten filtrarlas por palabras clave o mostrar solo las carpetas con mensajes no leídos;
	* En las carpetas en vista de árbol, Alt+flecha abajo y Alt+flecha arriba le permiten navegar entre carpetas con mensajes no leídos;
	* Todavía en las carpetas en vista de árbol, al escribir una letra o un número se selecciona la siguiente carpeta cuyo nombre comienza con el carácter escrito. Con la tecla -shift, el desplazamiento se efectua de abajo hacia arriba. Además, se anuncia el nombre de la cuenta a la que pertenece  la carpeta;
	* La tecla Espacio  en una carpeta con mensajes no  leídos selecciona el primer mensaje no leído de la lista;
	* En la lista de mensajes, tres modos para Leer el texto de los mensajes sin salir de la lista:
	* Vista rápida depurada del texto del mensaje con espacio, Alt+flecha abajo o F4: los grandes bloques de cabeceras en las citas de los mensajes se reemplazan con la expresión "Nombre del remitente escribió". NVDA también anunciará "enlace cliqueable" en lugar de la larga dirección del enlace.
	* Vista rápida de citas en su orden cronológico, de abajo hacia arriba, mediante -shift+Espacio, Alt+flecha arriba o -shift+F4;
	* Fácil acceso a los adjuntos mediante el atajo Alt+avance página o el número 1 del teclado alfanumérico; 
* **Ventana de Escribir un mensaje:**
	* Alt+1 anuncia el remitente, Alt+2 el destinatario, Alt+3 los adjuntos, etc. Dos pulsaciones colocan el foco en uno de estos campos;
	* En el cuadro de diálogo de Revisar ortografía: 
	*	 la palabra mal escrita se anuncia antes de la palabra sugerida. Los atajos NVDA+Tab o Alt+flecha arriba anuncian las palabras mal escritas y de reemplazo: pulsando una vez deletreará las palabras a velocidad normal, pulsando dos veces deletreará rápidamente, pulsando tres veces copiará   la palabra mal escrita al portapapeles para su análisis en otro campo de edición; 
	*	 varias combinaciones de la tecla intro que permite un accionamiento de los botones Reemplazar, Reemplazar todo, Ignorar, Ignorar todo o Añadir palabra para que este diálogo sea más cómodo; 
	* Mejora para revisar la ortografía mientras escribes: dos atajos para ir a la palabra mal escrita siguiente y anterior. Esto aún no funciona en las versiones 2022.1 y posteriores de NVDA;
* **Barra de filtrado rápido se hace accesible y Administrar etiquetas simplificado:**
	* Es posible navegar entre las opciones de filtrado usando las flechas verticales. La tecla Intro le permite marcar o desmarcar una opción;
	* La adición o eliminación de etiquetas se realiza simplemente pulsando -shift+un número en el teclado alfanumérico. Por ejemplo, pulse  4 para agregar la etiqueta "Por hacer" a un mensaje. Luego puede filtrar la lista de mensajes por etiquetas a través de la barra de filtrado rápido que ahora es accesible;
* **Características diversas:**
	* La elección de las columnas, así como su disposición en la lista de mensajes, se hace accesible a través de un simple diálogo;
	* Consulta de las columnas de la lista de mensajes: permite volver a escuchar, deletrear o copiar fácilmente el nombre del remitente, el asunto o la fecha de un mensaje pulsando un número en el teclado alfanumérico: por ejemplo, 1 o & anuncia el remitente, 2 pulsaciones deletrea el nombre y 3 pulsaciones lo copia al portapapeles;
	* Consulta de cabeceras del panel  de cabeceras que se muestra con F8: con Alt+un número, 1 pulsación verbaliza una cabecera que contiene las direcciones del remitente o de los destinatarios, 2 pulsaciones  abre un diálogo que permite copiarlas, 3 pulsaciones abre el menú contextual nativo de Thunderbird asociado con la cabecera;
* Actualización automática del complemento;
* Y muchas cosas más que descubrirás leyendo el resto de [esta documentación][2];

[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.4/ThunderbirdPlus-v4.4-TB102.nvda-addon

[2]: http://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-es.html