# IU-CSP-0600-004 - Búsqueda y listado de timesheet - Rol principal - Búsqueda directa - Propios

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0600-004 - Búsqueda y listado de timesheet - Rol principal - Búsqueda directa - Propios******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT- CSP-001-Investigador (rol principal) |
| Frecuencia | Media |

## Formulario Búsqueda y listado de timesheet - Rol principal - Búsqueda directa - Propios

Pantalla que muestra el formulario de búsqueda por defecto para los ACT- CSP-001-Investigador que actúan con rol principal en algún proyecto. ACT-CSP-001-Investigador con rol principal, podrá:

* Realizar el registro de horas propiamente dicho.
* Realizar la validación del registro de horas realizado por los miembros del o los equipos de proyecto de los que actúa con rol principal.

Los timesheet que se encuentren en estado "Propuesta" no podrán ser visualizados por el ACT- CSP-001-Investigador.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de búsqueda de timesheet | | | |
| Opción de búsqueda directa | TS propios estado Abierto | Check  Obligatorio | En función de la opción seleccionada se mostrarán los timesheet propios del ACT-CSP-001-Investigador en estado abierto para dar acceso al registro de horas propiamente dicho o se listarán los timesheet que el ACT-CSP-001-Investigador actuando con rol principal tiene pendientes de validar ( Ver [IU-CSP-0500-005 - Búsqueda y listado de timesheet - Rol principal - Búsqueda directa - Equipo](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0600-timesheet/iu-csp-0600-005-busqueda-y-listado-de-timesheet-rol-principal-busqueda-directa-equipo)) |
| TS pendientes de validar |
| Buscar | | Icono de acción | Acción de búsqueda por defecto |
| Búsqueda avanzada | | Icono de acción | Acción de búsqueda |
| Listado de timesheets | | | |
| Periodo | | Texto corto | Mes y año del periodo de registro de horas de dedicación |
| Estado | | Texto corto | Estado en el que se encuentra el timesheet |
| Modificar | | Icono de acción | Acción "Modificar" |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Formulario de búsqueda de timesheet | | |
| Buscar | Ejecuta la búsqueda directa | Se muestra el listado de timesheet donde ACT-CSP-001-Investigador sea el titular y que se encuentren en estado "Abierto" |
| Búsqueda avanzada | Buscador avanzado | Se resuelve con [IU-CSP-0500-006 - Búsqueda y listado de timesheet - Rol principal - Avanzada - Propios](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0600-timesheet/iu-csp-0600-006-busqueda-y-listado-de-timesheet-rol-principal-avanzada-propios) y [IU-CSP-0500-007 - Búsqueda y listado de timesheet - Rol principal - Avanzada - Equipo](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0600-timesheet/iu-csp-0600-007-busqueda-y-listado-de-timesheet-rol-principal-avanzada-equipo) |
| Listado de timesheets que cumplen las condiciones indicadas en el filtro y además están asociados a la Unidad Gestora | | |
| Modificar | Muestra la pantalla de modificación del timesheet seleccionado del listado de timesheet  Disponible para usuarios ACT- CSP-001-Investigador cuando el timesheet se encuentra en estado "Abierto" o "Subsanación" | Se resuelve con la pantalla [IU-CSP-0500-008 - Timesheet - Detalle - Comprensión general](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0600-timesheet/iu-csp-0600-008-timesheet-detalle-comprension-general) |

### Acciones

|  |  |
| --- | --- |
| ACT- CSP-001-Investigador | CSP-TIMESHEET-EDITAR |