# IU-CSP-202-008 - Añadir periodo de seguimiento científico

|  |  |
| --- | --- |
| Cod. IU | **IU-CSP-202-008 - Añadir periodo de seguimiento científico** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Añadir periodo de seguimiento científico

Pantalla que muestra un formulario, que permite crear un nuevo periodo de seguimiento científico de una convocatoria.

Los periodos se añaden desde la pestaña de "Seguimiento científico" de la convocatoria [IU-CSP-0201-007 - Crear convocatoria - Seguimiento científico](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0201-crear-convocatoria/iu-csp-0201-007-crear-convocatoria-seguimiento-cientifico).

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Número de periodo | Secuencia  Numérico entero genérico  Obligatorio | Número secuencial dentro de la convocatoria que asignará directamente el sistema en función de la ordenación de la fecha de inicio. Modo consulta. |
| Tipo | Selector  Texto corto  Obligatorio | Tipo del periodo de seguimiento. Se corresponde con el campo "tipo seguimiento"  El valor se seleccionará del listado disponible, cargado a partir del enumerado "Tipo seguimiento".  Será un campo obligatorio. |
| Mes inicial | Entero  Obligatorio | Mes inicial y mes final definen el rango del periodo de seguimiento. Son relativos a la duración total de los proyectos derivados de la convocatoria. |
| Mes final | Entero  Obligatorio | Mes inicial y mes final definen el rango del periodo de seguimiento. Son relativos a la duración total de los proyectos derivados de la convocatoria. |
| Fecha inicio presentación | Fecha + Hora  Opcional | Fecha de inicio del plazo de presentación del seguimiento científico, expresada en formato fecha y hora. La hora de la fecha de inicio tomará por defecto el valor 00:00. El usuario podrá modificar este valor.  Se seleccionará a partir de un componente de Calendario que permitirá marcar el día y  hora de inicio del plazo de presentación de la documentación de la justificación económica. |
| Fecha fin presentación | Fecha + Hora  Opcional | Fecha de fin del plazo de presentación del seguimiento científico, expresada en formato fecha y hora. La hora de la fecha de inicio tomará por defecto el valor 00:00. El usuario podrá modificar este valor.  Se seleccionará a partir de un componente de Calendario que permitirá marcar el día y  hora de inicio del plazo de presentación de la documentación de la justificación económica. |
| Observaciones | Texto largo  Opcional | Observaciones del periodo de seguimiento científico |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Guardar | Añade el periodo de justificación a la convocatoria. | El número de periodo se calculará de forma secuencial y ordenada de acuerdo al mes inicial, de forma que que se recalcule a medida que se realicen inserciones, modificaciones o borrados  Solo deberá existir un periodo de tipo "final". No se permitirá la creación de nuevos periodos cuando ya exista un tipo "final".  Se comprobará que no se solapen rangos de mes inicial - mes final. Para ello:   * El número de mes (inicial o final) de cualquier periodo será único * Para cualquier periodo mes final ha de ser mayor que mes inicial * No pueden existir solapamientos de meses, si existe un periodo del mes 5 al 10, se puede crear otro periodo del mes 1 al 4. Habrá que reordenar los distintos periodos cada vez que se añade un nuevo periodo o se modifica uno. * El mes inicial o final de cualquier periodo no podrán superar nunca la duración en meses indicada en datos generales de la convocatoria, siempre que este campo estuviese informado. En caso de no estar informado no se aplicaría esta comprobación.   Sobre las fechas de inicio y fin de presentación:   * Fecha de fin de presentación de un nuevo periodo ha de ser mayor que fecha de inicio de su mismo periodo * No se limitará que las fechas de inicio y fin de presentación de diferentes periodos se solapen o coincidan |
| Cancelar | Retorna al formulario de la convocatoria, sin salvar los posibles cambios. |  |