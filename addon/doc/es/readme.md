# Thunderbird+

* Autores: Pierre-Louis Renaud (Thunderbird 78 a 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 a 91), Yannick (TB 45 a 60);
* URL: [Manual de usuario][4] ;
  [Historial de cambios en RPTools.org][5] ;
  [Contacto en francés e inglés][6];
* Descargar [Versión estable][1]
* Descargar [Versión más reciente en RPTools.org][3];
* Compatibilidad con NVDA: de 2019.3 en adelante;
* Compatibilidad con Thunderbird: versiones 102.x;
* [Código fuente en GitHub][2]

Nota: este complemento no es compatible con el complemento Mozilla Apps Enhancements. Si tienes instalado el complemento Mozilla Apps Enhancements, deberás deshabilitarlo o desinstalarlo antes de usar Thunderbird+;

## Descripción

Este complemento mejora increíblemente la accesibilidad, eficiencia y comodidad a la hora de usar el cliente de correo Mozilla Thunderbird con NVDA.

Las mejoras se relacionan con los siguientes aspectos:

### Confort auditivo

* Las alertas  "fulano ha solicitado que se le notifique cuando Vd. lea este mensaje." se puede desactivar a través de una opción;
* Las alertas "Este mensaje es un borrador" y "Thunderbird piensa que este mensaje es correo basura" simplemente se ignoran; 
* Las opciones posibilitan desactivar el anuncio de los nombres de listas de correo, eliminar o agrupar las menciones "re" y depurar los nombres de los participantes eliminando los números y otros caracteres especiales incómodos;

### Navegación en la ventana principal

* Para navegar al siguiente panel se usa la tecla tab, mientras que la tecla escape permite volver al panel anterior. Esto es más cómodo que f6 y shift+f6.
* La selección de pestañas con Control+Tab y Control+ un número con verbalización como en este ejemplo: Pestaña 1 de 4, Bandeja de entrada; 
* Un atajo de teclado le permite enumerar las pestañas en un menú para activar una de ellas fácilmente;
* Un atajo de teclado le permite mostrar el menú contextual de la barra de pestaña;

### Carpetas en vista de árbol

* Alt+flechas arriba y abajo permiten navegar entre carpetas con mensajes no leídos;
* Al pulsar una letra o un número se selecciona la siguiente carpeta cuyo nombre empiece por el carácter tecleado. Con la tecla shift, el movimiento se hace de abajo a arriba. Además, el nombre de la cuenta a la que pertenece la carpeta se anuncia;
* Pulsando la barra espaciadora en una carpeta con mensajes no  leídos selecciona el primer mensaje no leído de la lista;
* Dos diálogos de cuentas y sus carpetas asociadas permiten permiten filtrarlas por palabras clave o mostrar sólo carpetas con mensajes no leídos;

### Lista de mensajes

La elección de columnas, así como su orden en la lista de mensajes, es accesible con un simple diálogo;
* Consulta de las columnas de la lista de mensajes: permite escuchar de nuevo, deletrear o copiar fácilmente el nombre del remitente, el asunto o la fecha del mensaje pulsando un número del teclado alfanumérico: por ejemplo 1 o ! anuncia el remitente, 2 pulsaciones deletrean el nombre y 3 lo copian al portapapeles;
* Consulta de las cabeceras del panel de cabeceras con f8: con alt+números, una pulsación verbaliza las direcciones del remitente o los destinatarios, dos pulsaciones abren un diálogo que permite copiarlas, y 3 pulsaciones abren el menú contextual nativo de Thunderbird asociado a la cabecera;
* Previsualización rápida limpia del texto del mensaje con la barra espaciadora, alt+flecha abajo o f4: los bloques grandes de cabeceras en las citas del mensaje se sustituyen por la frase "nombre del remitente escribió". NVDA también anunciará "enlace clicable" en lugar de la dirección larga del enlace.
* Vista rápida de citas en orden cronológico, de abajo hacia arriba, mediante shift+espacio, alt+flecha arriba o shift+f4;
* Fácil acceso a los adjuntos usando el atajo alt+avance página o el número 1 del teclado alfanumérico;

### Barra de filtrado rápido y Administrar etiquetas de prioridad

* Es posible navegar entre las opciones de filtrado utilizando las flechas arriba y abajo. La tecla intro permite marcar o desmarcar una opción;
* Añadir o eliminar etiquetas de prioridad es tan simple como pulsar shift+números del teclado alfanumérico. Por ejemplo, pulsa 4 para añadir la etiqueta "por hacer" a un mensaje. Después puedes filtrar la lista de mensajes por etiquetas mediante la barra de filtrado rápido, que ahora es accesible;

### Ventana de Escribir un mensaje

Alt+1 anuncia el remitente, alt+2 destinatario, alt+3 adjuntos, etc. Con dos pulsaciones se sitúa el foco en uno de estos campos;

### Diálogo de Revisar ortografía

* La palabra mal escrita se anuncia antes que la palabra sugerida. Los atajos NVDA+tab o alt+flecha arriba anuncian las palabras mal escritas y sus sustituciones: una pulsación deletrea las palabras a velocidad normal, 2 pulsaciones las deletrean rápido, y 3 pulsaciones copian la palabra mal escrita al portapapeles para su análisis en otro cuadro de edición;
* Se han añadido diversas combinaciones de la tecla intro activan los botones Reemplazar, Reemplazar todas, Ignorar, Ignorar todas o Añadir la palabra al diccionario para mayor comodidad usando este diálogo;

### Actualización automática

ThunderBirdPlus tiene un sistema de actualización automática independiente con opciones de desactivación / reactivación y aplazamiento;

### Funcionamiento en dúo con Chichi

ThunderbirdPlus está previsto para funcionar armoniosamente con Chichi, un complemento que se instala directamente en Thunderbird.

Lea sobre este tema yendo a la [página de Chichi][7];


Y muchas otras cosas que descubrirás leyendo el [manual de usuario][4];

<!-- Traductores: en los enlaces 4, 5 y 7 a continuación, donde ves lang=en, reemplace en por el código de tu idioma -->

[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.9/thunderbirdPlus-4.9-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://www.rptools.org/?p=8610

[4]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=manual&lang=es

[5]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=changes&lang=es

[6]: https://www.rptools.org/NVDA-Thunderbird/toContact.html

[7]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=chichi&lang=es
