# IU-CSP-0550-003 - Validación de gastos - Histórico de estados

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0550-003 - Validación de gastos - Histórico de estados******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-001-Investigador |
| Frecuencia | Media |

## Formulario Ejecución económica - Validación de gastos - Histórico de estados

Formulario que permite consultar el listado de estados por los que ha pasado el gasto pendiente de contabilización. Cada vez que se modifica el estado del gasto se añadirá a la tabla de "histórico estado" el estado, la fecha del estado se corresponderá siempre con la fecha en la que se realiza la acción de "Guardar" y el comentario asociado al cambio. El apartado histórico de estados comenzará a estar disponible una vez que tiene el primer cambio de estado.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de estados del proyecto (se muestran los registros almacenados en la tabla "EstadoGastoProyecto") | | |
| Estado | Texto corto | Estado del gasto pendiente contabilización |
| Fecha de estado | Fecha | Fecha en la que el gasto pasó a dicho estado |
| Comentario | Texto | Comentario añadido cuando se produce el cambio de estado |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Cancelar | Retorna al formulario de gastos pendientes de contabilización |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-003-Gestor | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-004-Administrador** | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-001-Investigador** | CSP-EJEC-INV-ER | Ver documentación en [CU-CSP-1200-008 - Ver ejecución económica - Investigador (rol responsable económico)](https://confluence.um.es/confluence/pages/viewpage.action?pageId=108593251) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-EJEC-E, CSP-EJEC-E\_UO, CSP-EJEC-INV-ER |