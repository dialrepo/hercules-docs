# IU-CSP-0600-020 - Detalle - Unidad Gestión - Cerrado

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0600-020 - Detalle - Unidad Gestión - Cerrado******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT- CSP-003-Gestor, ACT- CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Timesheet - Detalle

Formulario que muestra el timesheet de un miembro de equipo para un mes al  ACT-CSP-003-Gestor de la Unidad de gestión responsable del proyecto, una vez que éste se encuentra en estado "Cerrado".

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Detalle de timesheet | | | |
| Investigador | | Texto  Solo lectura | Nombre y apellidos del titular del timesheet. Modo lectura.  Los datos se recuperarán a través del requisito de integración [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona). |
| Periodo | | Texto corto  Solo lectura | Mes y año del timesheet. Modo lectura. |
| Estado | | Texto corto  Solo lectura | Si el timesheet se encuentra en estado "Cerrado", no podrá ser introducida ninguna modificación. |
| Título proyecto | | Texto  Obligatorio  Solo lectura | Título de cada proyecto que forma parte del timesheet. |
| Paquete | | Texto  Opcional  Solo lectura | Nombre de cada paquete de trabajo en los que puede descomponerse cada proyecto. |
| Actividad común | | Texto  Opcional  Solo lectura | Nombre de otras actividades comunes que forman parte del timesheeet. |
| Días | | Numérico entero  Solo lectura | Para cada paquete de trabajo, de cada proyecto, se mostrarán las columnas correspondientes a los días del mes del periodo de timesheet conteniendo la dedicación diaria expresada en horas. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
|  |  |  |

### Botones generales a la pantalla

| Acciones | Descripción | Descripción CU |
| --- | --- | --- |
| Guardar | Opción deshabilitada | No podrán ser introducidas modificaciones sobre un timesheet en estado cerrado |
| Cancelar | Retorna al listado de timesheet sin salvar los posibles cambios. |  |

### Acciones

|  |  |
| --- | --- |
| **ACT- CSP-001-Investigador** | CSP-TSH-V |
| ACT- CSP-003-Gestor | CSP-TSH-V |
| **ACT- CSP-004-Administrador** | CSP-TSH-V |