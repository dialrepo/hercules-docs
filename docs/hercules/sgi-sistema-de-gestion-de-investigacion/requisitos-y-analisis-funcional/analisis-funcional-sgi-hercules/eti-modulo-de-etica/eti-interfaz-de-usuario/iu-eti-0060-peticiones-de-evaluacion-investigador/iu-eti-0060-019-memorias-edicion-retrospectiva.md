# IU-ETI-0060-019 Memorias - Edición retrospectiva

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0060-019- Memorias - Edición retrospectiva******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | PENDIENTE\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-002-Investigador  ACT-ETI-003-Solicitante  ACT-ETI-006-Responsable memoria |
| Frecuencia | Media |

## Formulario de Memorias - Edición retrospectiva

Será un formulario de retrospectiva de la memoria (formularios dinámicos)

Únicamente se mostrará el formulario de Retrospectiva si la memoria es de tipo CEEA y el investigador había indicado en la memoria que requería retrospectiva. (campo "requiereRetrospeciva" a "true" de la tabla Memoria)

Si la fecha actual es igual o mayor a la fecha de retrospectiva indicada en la memoria por el investigador  y  el campo estado de la retrospectiva es Pendiente o Completada el formulario se mostrará en modo edición, sino se mostrará en modo consulta. (Ver campo "estadoRetrospectiva" y "fechaRetrospectiva" de la tabla Retrospectiva vinculada a la memoria)

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario dinámico | | |
| 4 apartados con los datos del formulario  (dentro del mismo bloque) | Formulario dinámico | Objetivos (obligatorio)  Supervisión (obligatorio)  Severidad (obligatorio)  Reducción, reemplazo y refinamiento (obligatorio) |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Guarda el contenido del formulario y los documentos adjuntados | [CU-ETI-0060-015 - Memorias - Edición formulario retrospectiva](http://CU-ETI-0060-015 - Memorias - Edición formulario retrospectiva) | ETI-MEM-INV-ER |
| Ver fichero | Se visualiza el documento almacenado. |  | ETI-MEM-INV-ER |
| Eliminar | Se elimina el documento del listado |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-002-Investigador | ETI-MEM-INV-ER |
| ACT-ETI-003-Solicitante | ETI-MEM-INV-ER |
| ACT-ETI-006-Responsable memoria | ETI-MEM-INV-ER |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-MEM-INV-ER |