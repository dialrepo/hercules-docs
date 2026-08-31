# IU-PRC-0200-003 - Rechazar item de producción científica - Unidad de gestión

|  |  |
| --- | --- |
| Cod. IU | ********IU-PRC-0200-003 - Rechazar item de producción científica - Unidad de gestión******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PRC-003-Gestor |
| Frecuencia | Media |

## Formulario Rechazar item de producción científica - Unidad de gestión

Formulario que se muestra al dar al botón de "Rechazar".

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Introduce el motivo del rechazo | Texto largo  Obligatorio | Motivo del rechazo |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Aceptar | Se rechaza el item y se vuelve a la pantalla del consulta del item con el item en estado Rechazado e  informando de que el item se ha cambiado de estado correctamente | Si se pulsa el botón de "Aceptar" se hará un cambio de estado, para ello se creará un nuevo registro de la tabla "EstadoProduccionCientifica" con el estado a "Rechazado" y con una fecha igual a la actual y con el motivo del rechazo, y se actualizará el campo "estado" del item en la tabla "ProduccionCientifica" con el nuevo estado creado. | PRC-VAL-E |
| Cancelar | Retorna a la pantalla del consulta del item sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-PRC-003-Gestor | PRC-VAL-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | PRC-VAL-E |