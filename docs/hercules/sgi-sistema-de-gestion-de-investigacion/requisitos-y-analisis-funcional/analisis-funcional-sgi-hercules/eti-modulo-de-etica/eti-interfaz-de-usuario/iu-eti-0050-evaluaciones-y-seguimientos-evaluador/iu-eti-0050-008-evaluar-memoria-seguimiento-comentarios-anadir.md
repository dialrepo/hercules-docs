# IU-ETI-0050-008 Evaluar memoria seguimiento- Comentarios - Añadir

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0050-008- Evaluar memoria seguimiento - Comentarios - Añadir******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ O\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-004-Evaluador  ACT-ETI-005-Técnico |
| Frecuencia | Media |

## Formulario de Evaluar memoria seguimiento - Comentarios - Añadir

Pantalla que muestra el formulario para crear uno comentario en una evaluación de una memoria.

Para dar de alta un comentario se necesitan los siguientes campos:

* Bloque: desplegable con el nombre del bloque del formulario asociado al comité que tiene asignada la memoria.
* Apartado: árbol con los apartados y subapartados del bloque seleccionado
* Comentario: caja de texto para introducir el comentario respecto al subapartado o apartado.

Todos los cambios se realizarán en memoria, no serán efectivos hasta que el usuario pulse el botón Guardar de la pantalla.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Bloque | Desplegable  Texto corto  Obligatorio | Desplegable con el nombre de los bloques de Seguimiento. Se listarán los elementos asociados al formulario de "Seguimiento Anual" o "Seguimiento final", según el tipo de seguimiento que se esté evaluando.  Se debe de permitir además realizar un comentario general a la memoria. |
| Apartado | Árbol  Texto corto  Obligatorio | Árbol con los apartados y subapartados del bloque seleccionado |
| Comentario | Texto  Obligatorio | Comentario a introducir. |

| Acciones | Descripción | Enlace CU. | Permsios |
| --- | --- | --- | --- |
| Añadir | Añade un nuevo comentario al listado de comentarios. |  | ETI-EVC-EVALR  ETI-EVC-INV-EVALR |
| Cancelar | Se vuelve al listado de comentarios sin añadir el comentario |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-004-Evaluador | ETI-EVC-INV-EVALR |
| ACT-ETI-005-Técnico | ETI-EVC-EVALR |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |