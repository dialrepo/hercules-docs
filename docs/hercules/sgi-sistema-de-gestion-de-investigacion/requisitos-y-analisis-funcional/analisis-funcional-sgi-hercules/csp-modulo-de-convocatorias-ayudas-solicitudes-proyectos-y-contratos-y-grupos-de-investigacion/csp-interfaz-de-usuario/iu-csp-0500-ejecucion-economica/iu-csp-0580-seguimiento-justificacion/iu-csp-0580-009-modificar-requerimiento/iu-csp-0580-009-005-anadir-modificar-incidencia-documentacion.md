# IU-CSP-0580-009-005 - Añadir-modificar incidencia documentación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0580-009-005 - Añadir-modificar incidencia documentación******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Añadir-modificar incidencia documentación

Formulario que permite añadir o modificar una incidencia de documentación dentro del apartado de datos generales de un requerimiento.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Documento de justificación | Texto  Obligatorio | Nombre del documento al que refiere el requerimiento. Es simplemente un nombre de documento, no será necesario adjuntar el documento en sí ni que éste hubiera sido previamente adjuntado al SGI.  Es un campo obligatorio.  Se corresponde con el campo "nombre documento" de la tabla "incidencia documentación requerimiento". |
| Incidencia/motivo de rechazo | Texto largo  Opcional | Campo de texto para recoger la incidencia sobre el documento o motivo de rechazo del mismo recogida en el requerimiento de justificación.  Es un campo opcional.  Se corresponde con el campo "incidencia" de la tabla "incidencia documentación requerimiento". |

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Añadir/Aceptar | El botón se muestra como:   * Añadir, cuando se accede al formulario para añadir una nueva incidencia * Aceptar, cuando se accede al formulario para modificar los datos de una incidencia previamente añadida | El botón solo estará activo una vez que se hayan introducido cambios sobre alguno de los campos del formulario.  Inserta  o modifica el registro correspondiente en la tabla "incidencia documentación requerimiento". | CSP-SJUS-E  CSP-SJUS-E\_UO |
| Cancelar | Retorna al formulario datos generales del requerimiento sin crear o modificar la incidencia de documentación | Retorna al formulario de datos generales del requerimiento, creación [IU-CSP-0580-008-001 - Requerimiento - Datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-008-crear-requerimiento/iu-csp-0580-008-001-requerimiento-datos-generales) o modificación [IU-CSP-0580-009-001 - Modificar requerimiento - Datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-009-modificar-requerimiento/iu-csp-0580-009-001-modificar-requerimiento-datos-generales) según el punto de procedencia | CSP-SJUS-E  CSP-SJUS-E\_UO |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-004-Administrador** | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-005-Visor** | CSP-SJUS-V, CSP-SJUS-V\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SJUS-E, CSP-SJUS-E\_UO, CSP-SJUS-V, CSP-SJUS-V\_UO |