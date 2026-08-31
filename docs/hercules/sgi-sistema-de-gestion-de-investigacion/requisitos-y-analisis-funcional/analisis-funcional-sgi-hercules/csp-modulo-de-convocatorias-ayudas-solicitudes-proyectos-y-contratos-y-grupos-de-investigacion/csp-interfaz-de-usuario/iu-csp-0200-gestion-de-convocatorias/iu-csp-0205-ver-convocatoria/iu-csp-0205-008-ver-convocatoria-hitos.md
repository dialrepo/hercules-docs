# IU-CSP-0205-008 - Ver convocatoria - Hitos

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0205-008 - Ver convocatoria - Hitos******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Ver convocatoria - Hitos

Formulario para ver los hitos de una convocatoria. No estará disponible para ACT-CSP-001-Investigador.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de hitos de la convocatoria | | |
| Fecha | Fecha + Hora | Fecha del hito recuperada de la tabla "hitos convocatoria".  Expresado en formato fecha + hora |
| Tipo de hito | Texto corto | Nombre del tipo de hito recuperado de la tabla "tipos hito convocatoria" a partir del identificador de la relación "hitos convocatoria" |
| Observaciones | Texto largo | Observaciones recuperadas de "hitos convocatoria" |
| Aviso | Booleano | Campo "genera aviso" "hitos convocatoria" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Ver | Accede a la pantalla con el formulario para Ver detalle del hito [IU-CSP-0206-007 - Ver hito](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0206-007-ver-hito). |  | CSP-CON-V |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Cancelar | Retorna al listado de Convocatorias. |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-005-Visor | CSP-CON-V |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-V |