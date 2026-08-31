# IU-CSP-0560-012 - Rechazar gasto en periodo de justificaciónn

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0560-012 - Rechazar gasto en periodo de justificación******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Rechazar gasto en periodo de justificación

Formulario que permite añadir el motivo de rechazo y un comentario asociado al justificante/factura si el periodo de justificación se encuentra en estado "Entregada" o "Justificación", en cualquier otro estado los campos "motivo de rechazo" y "comentario de rechazo" estarán visibles pero no podrán ser modificados. No se mantendrá un histórico para estos campos, solo se permitirá un único valor para los mismos, siendo sobrescrito en caso de que sea modificado.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Motivo del rechazo | | Selector  Texto corto | Motivo de rechazo el justificante |
| Comentario del rechazo | | Texto largo | Comentario sobre el motivo de rechazo |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Guardar | Añade el motivo y comentario de rechazo al justificante/factura |  |
| Cancelar | Retorna al formulario de justificación sin salvar los posibles cambios |  |

### Acciones

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |
| ACT-CSP-004-Administrador | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |