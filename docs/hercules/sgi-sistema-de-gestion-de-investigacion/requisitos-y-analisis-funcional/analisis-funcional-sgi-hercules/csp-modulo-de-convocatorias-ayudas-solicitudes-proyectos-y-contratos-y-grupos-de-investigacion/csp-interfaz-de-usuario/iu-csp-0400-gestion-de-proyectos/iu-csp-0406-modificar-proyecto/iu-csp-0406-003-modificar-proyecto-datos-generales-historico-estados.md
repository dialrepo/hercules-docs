# IU-CSP-0406-003 - Modificar proyecto - Datos generales - Histórico estados

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-003 - Modificar proyecto - Datos generales - Histórico estados******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Modificar proyecto - Datos generales - Histórico estados

Formulario que permite consultar el listado de estados por los que ha pasado el proyecto. Cada vez que se modifica el estado del proyecto se añadirá a la tabla de "histórico estado" el estado y la fecha del estado se corresponderá siempre con la fecha en la que se realiza la acción de "Guardar". El apartado histórico de estados comenzará a estar disponible una vez que tiene el primer cambio de estado, es decir, cuando el proyecto pasa de estado "Borrador" a estado "Concedido" o "Renunciado/rescindido".

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| La información se presenta en modo solo lectura. El listado de estados de un proyecto se obtiene de la tabla "EstadoProyecto". La tabla se mostrará por defecto ordenada del estado más reciente al más antiguo. | | |
| Estado | Texto corto | Estado del proyecto. Los estados son definidos en [Estados de un proyecto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-proyectos-contratos-becas-y-ayudas#CSPProyectos,contratos,becasyayudas-estados_proyectoEstadosdeunproyecto) |
| Fecha de estado | Fecha | Fecha en la que el proyecto pasó a dicho estado |
| Comentario | Texto | Comentario añadido cuando se produce el cambio de estado. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| No existen acciones particulares en esta pantalla |  | La información de la tabla y de todo el apartado se presenta en modo solo lectura. |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modifica el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todos los apartados de definición del proyecto. | Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.