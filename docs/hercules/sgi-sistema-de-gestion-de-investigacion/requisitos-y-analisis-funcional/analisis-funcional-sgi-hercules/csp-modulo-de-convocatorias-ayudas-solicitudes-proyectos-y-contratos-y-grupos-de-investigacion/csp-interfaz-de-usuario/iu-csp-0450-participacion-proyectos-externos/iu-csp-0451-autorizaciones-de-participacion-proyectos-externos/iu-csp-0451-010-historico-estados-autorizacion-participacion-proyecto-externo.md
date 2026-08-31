# IU-CSP-0451-010 - Histórico estados autorización participación proyecto externo

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0451-010 - Histórico estados autorización participación proyecto externo******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Baja |

## Formulario Histórico estados autorización participación proyecto externo

Formulario que muestra el listado con el histórico de estados de una solicitud de participación en proyecto externo.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de estados de una solicitud de autorización. Se mostrarán todos los estados por los que ha pasado la solicitud de autorización (tabla "estado autorización"). | | |
| Estado | Modo Consulta  Texto corto | Se corresponde con el campo "estado" de la tabla "estado autorización". Se mostrará el valor correspondiente del campo "estado" sobre el enumerado "tipo estado autorización". |
| Fecha estado | Fecha + hora  Obligatorio | Fecha y hora en la que se efectuó el cambio estado.  Se corresponde con el campo "fecha" de la tabla "estado autorización". |
| Comentario | Texto largo  Opcional | Se corresponde con el campo "comentario" de la tabla "estado autorización". |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Realiza la operación de guardado sobre la autorización afectando solamente al apartado  Datos generales. | La operación de guardar no tiene ningún efecto para esta pantalla de histórico de estados. |  |
| Cancelar | Retorna a la pantalla de Datos generales de la autorización. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-AUT-E |
| ACT-CSP-003-Gestor | CSP-AUT-E |
| ACT-CSP-005-Visor | CSP-AUT-V |
| ACT-CSP-001-Investigador | CSP-AUT-INV-ER |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-AUT-E, CSP-AUT-V, CSP-AUT-INV-ER |