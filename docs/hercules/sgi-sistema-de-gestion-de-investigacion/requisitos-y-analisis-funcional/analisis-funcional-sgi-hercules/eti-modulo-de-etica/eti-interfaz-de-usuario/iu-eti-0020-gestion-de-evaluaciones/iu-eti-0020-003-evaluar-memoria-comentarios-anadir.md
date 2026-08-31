# IU-ETI-0020-003 Evaluar memoria- Comentarios - Añadir

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0020-003- Evaluar memoria - Comentarios - Añadir******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Evaluar memoria - Comentarios - Añadir

Pantalla que muestra el formulario para crear un comentario en una evaluación de una memoria.

En el caso de que el dictamen seleccionado sea "Favorable pendiente de revisión mínima" o "Pendiente de correcciones" es obligatorio que al menos exista un comentario.

Para dar de alta un comentario se necesitan los siguientes campos:

* Bloque: desplegable con el nombre de los 5 bloques del formulario asociado al comité que tiene asignada la memoria.
* Apartado: desplegable con los apartados del bloque seleccionado.
* Subapartado: desplegable con los subapartados del apartado seleccionado.
* Comentario: caja de texto para introducir el comentario respecto al subapartado o apartado.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Bloque | Desplegable  Texto corto  Obligatorio | Desplegable con el nombre de los bloques del formulario asociado al comité que tiene asignada la memoria.  Se debe de permitir además realizar un comentario general a la memoria. |
| Apartado | Árbol  Texto corto  Obligatorio | Árbol con los apartados y subapartados del bloque seleccionado. |
| Comentario | Texto  Obligatorio | Comentario a introducir. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Añadir | Añade un nuevo comentario al listado de comentarios. | [CU-ETI-0020-004 - Evaluar memoria - Comentarios - Añadir](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0020-gestion-de-evaluaciones/cu-eti-0020-004-evaluar-memoria-comentarios-anadir) | ETI-EVC-EVAL |
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