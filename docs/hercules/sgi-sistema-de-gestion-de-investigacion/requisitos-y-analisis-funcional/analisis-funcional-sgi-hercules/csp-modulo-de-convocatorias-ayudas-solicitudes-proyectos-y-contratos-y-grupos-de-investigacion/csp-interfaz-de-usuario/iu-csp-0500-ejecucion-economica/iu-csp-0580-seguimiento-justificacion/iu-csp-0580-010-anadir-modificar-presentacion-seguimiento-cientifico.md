# IU-CSP-0580-010 - Añadir-modificar presentación seguimiento científico

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0580-010 Añadir-modificar presentación seguimiento científico******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir-modificar presentación seguimiento científico

Formulario que permite introducir la fecha en la que se realiza la presentación de la documentación asociada al periodo de seguimiento científico

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Fecha presentación documentación | Fecha + Hora  Obligatorio | Fecha en la que se presenta la documentación asociada al periodo de seguimiento científico.  Se corresponde con el campo "fecha presentación documentación" de la tabla "proyecto periodo seguimiento". |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Aceptar | Almacenará la información introducida para el periodo de seguimiento científico.  En este caso no hay diferencia entre Aceptar y Añadir, ya que el periodo de justificación ya existe y siempre se realiza una actualización de sus datos. Desde esta pantalla nunca se creará un periodo de justificación nuevo. | Se actualizará el registro correspondiente de la tabla "proyecto periodo seguimiento" actualizando los campos:   * "fecha presentación documentación"   de acuerdo a los valores introducidos en el formulario  Tras realizar la operación se volverá a la pantalla [IU-CSP-0580-001 - Resumen](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-001-resumen) | CSP-SJUS-E  CSP-SJUS-E\_UO |
| Cancelar | No se realizará ninguna operación. | Se cerrará el formulario sin realizar ninguna operación y se volverá a la pantalla [IU-CSP-0580-001 - Resumen](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-001-resumen) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-SJUS-E  CSP-SJUS-E\_UO |
| **ACT-CSP-004-Administrador** | CSP-SJUS-E  CSP-SJUS-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SJUS-E, CSP-SJUS-E\_UO |