# IU-CSP-0205-005 - Ver convocatoria - Fases

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0205-005 - Ver convocatoria - Fases******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT- CSP-001-Investigador, ACT-CSP-005-Visor  Usuario externo |
| Frecuencia | Media |

## Formulario Ver convocatoria - Fases

Formulario para ver las fases de una convocatoria.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de fases y plazos de la convocatoria | | |
| Fecha inicio | Fecha + Hora | Fecha de inicio de la fase. Expresada en formato fecha y hora. |
| Fecha fin | Fecha + Hora | Fecha de fin de la fase. Expresada en formato fecha y hora.  En caso que una fase pueda recogerse en una sola fecha, en este caso se indicaría el mismo valor tanto en fecha de inicio como en fecha de fin. |
| Tipo de fase | Texto corto | Tipo de fase de la convocatoria. |
| Observaciones | Texto largo | Observaciones de la fase de la convocatoria. |
| Aviso | Booleano | Campo "genera aviso" del registro de la tabla "fases convocatoria" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Ver | Accede a la pantalla con el formulario para Ver detalle de la fase [IU-CSP-0206-004 - Ver fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0206-004-ver-fase) |  | CSP-CON-V  CSP-CON-INV-V |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Cancelar | Retorna al listado de Convocatorias. |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-001-Investigador | CSP-CON-INV-V |
| ACT-CSP-005-Visor | CSP-CON-V |
| Usuario externo | Sin permisos |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-INV-V, CSP-CON-V |