# IU-ETI-0100-003 Evaluar memoria seguimiento- Comentarios - Añadir

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0100-003- Evaluar memoria seguimiento - Comentarios - Añadir******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Evaluar memoria seguimiento - Comentarios - Añadir

Pantalla que muestra el formulario para crear un comentario en una evaluación de seguimiento de una memoria.

En el caso de que el dictamen seleccionado sea "Solicitud de modificaciones" (en un seguimiento anual) o "Solicitud de aclaraciones"  (en un seguimiento final) es obligatorio que al menos exista un comentario.

Para dar de alta un comentario se necesitan los siguientes campos:

* Bloque: desplegable con el nombre de los 5 bloques del formulario asociado al comité que tiene asignada la memoria.
* Apartado: desplegable con los apartados del bloque seleccionado.
* Subapartado: desplegable con los subapartados del apartado seleccionado.
* Comentario: caja de texto para introducir el comentario respecto al subapartado o apartado.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Bloque | Desplegable  Texto corto  Obligatorio | Desplegable con el nombre de los bloques de Seguimiento. Se listarán los elementos asociados al formulario de "Seguimiento Anual" o "Seguimiento final", según el tipo de seguimiento que se esté evaluando.  Se debe de permitir además realizar un comentario general a la memoria. |
| Apartado | Árbol  Texto corto  Obligatorio | Árbol con los apartados y subapartados del bloque seleccionado. |
| Comentario | Texto  Obligatorio | Comentario a introducir. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Añadir | Añade un nuevo comentario al listado de comentarios. | [CU-ETI-0090-004 - Evaluar memoria seguimiento - Comentarios - Añadir](http://CU-ETI-0090-004 - Evaluar memoria seguimiento - Comentarios - Añadir) | ETI-EVC-EVAL |
| Cancelar | Se vuelve al listado de comentarios sin añadir el comentario |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-EVC-EVAL |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-EVC-EVAL |