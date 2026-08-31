# IU-CSP-0204-007 - Modificar convocatoria - Seguimiento científico

|  |  |
| --- | --- |
| Cod. IU | **IU-CSP-0204-007 - Modificar convocatoria - Seguimiento científico** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Modificar convocatoria - Seguimiento científico

### Formulario con el listado de Seguimiento científico

**La modificación de los datos de una convocatoria se rige por lo establecido en las precondiciones de [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)**

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| **La modificación de los datos de una convocatoria se rige por lo establecido en las precondiciones de [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)** | | |
| Listados de periodos de seguimiento científico de la convocatoria | | |
| Núm. periodo | Secuencia  Numérico entero genérico | Número secuencial dentro de la convocatoria que asignará directamente el sistema en función de la ordenación de la fecha de inicio |
| Mes inicial | Entero | Mes inicial y mes final definen el periodo de seguimiento científico. Son relativos a la duración de los proyectos que posteriormente derive la convocatoria. |
| Mes final | Entero | Mes inicial y mes final definen el periodo de seguimiento científico. Son relativos a la duración de los proyectos que posteriormente derive la convocatoria. |
| Fecha inicio presentación | Fecha + Hora | Fecha de inicio y fecha de fin definen el plazo de presentación del seguimiento científico a la entidad correspondiente. Ambas están expresadas en formato de fecha y hora. |
| Fecha fin presentación | Fecha + Hora | Fecha de inicio y fecha de fin definen el plazo de presentación del seguimiento científico a la entidad correspondiente. Ambas están expresadas en formato de fecha y hora. |
| Tipo | Texto corto | Tipo del periodo de seguimiento.  Se corresponde con el campo "tipo seguimiento" y se mostrará el valor correspondiente recuperado del enumerado "Tipo  seguimiento" |
| Observaciones | Texto largo | Observaciones del periodo de seguimiento científico |
| Modificar | Icono de acción | Acción modificar |
| Eliminar | Icono de acción | Acción eliminar |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Muestra la pantalla de modificación del periodo seleccionado del listado de periodos de seguimiento científico de la convocatoria | Muestra la pantalla de abajo de "Modificar periodo de seguimiento científico".  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Eliminar | Elimina periodo de seguimiento científico | Elimina el registro de la tabla "Periodos seguimiento científico" de la convocatoria.  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |
| Añadir nuevo periodo de seguimiento científico | Muestra la pantalla Nuevo periodo de seguimiento científico | Muestra la pantalla [IU-CSP-202-008 - Añadir periodo de seguimiento científico](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-202-008-anadir-periodo-de-seguimiento-cientifico).  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |

### Formulario para modificar un periodo de seguimiento científico de una convocatoria

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| **La modificación de los datos de una convocatoria se rige por lo establecido en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)** | | |
| Numero de periodo | Secuencia  Numérico entero genérico  Obligatorio | Número secuencial dentro de la convocatoria que asignará directamente el sistema en función de la ordenación de la fecha de inicio. Modo consulta. |
| Tipo | Selector  Texto corto  Obligatorio | Se corresponde con el campo "tipo seguimiento". Mostrará el valor correspondiente del enumerado "Tipo  seguimiento"  El cambio de valor se realizará a través de un selector cargado con el listado de valores del enumerado "Tipo seguimiento" |
| Mes inicial | Entero  Obligatorio | Mes inicial y mes final definen el rango del periodo de seguimiento científico. Son relativos a la duración total de los proyectos derivados de la convocatoria. |
| Mes final | Entero  Obligatorio | Mes inicial y mes final definen el rango del periodo de seguimiento científico. Son relativos a la duración total de los proyectos derivados de la convocatoria. |
| Fecha inicio presentación | Fecha + Hora  Opcional | Fecha de inicio del plazo de presentación del seguimiento científico, expresada en formato fecha y hora. La hora de la fecha de inicio tomará por defecto el valor 00:00:00. El usuario podrá modificar este valor.  Se seleccionará a partir de un componente de Calendario que permitirá marcar el día y  hora de inicio del plazo de presentación de la documentación del seguimiento científico. |
| Fecha fin presentación | Fecha + Hora  Opcional | Fecha de inicio del plazo de presentación del seguimiento científico, expresada en formato fecha y hora. La hora de la fecha de inicio tomará por defecto el valor 00:00:00. El usuario podrá modificar este valor.  Se seleccionará a partir de un componente de Calendario que permitirá marcar el día y  hora de inicio del plazo de presentación de la documentación del seguimiento científico. |
| Observaciones | Texto largo  Opcional | Observaciones del del seguimiento científico. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Aceptar | Actualiza el registro en base de datos | El número de periodo se calculará de forma secuencial y ordenada de acuerdo al mes inicial, de forma que que se recalcule a medida que se realicen inserciones, modificaciones o borrados  Solo deberá existir un periodo de tipo "final". No se permitirá la creación de nuevos periodos de seguimiento  cuando ya exista un tipo "final".  Se comprobará que no se solapen rangos de mes inicial - mes final. Para ello:   * El número de mes (inicial o final) de cualquier periodo será único * Para cualquier periodo mes final ha de ser mayor o igual que mes inicial * No pueden existir solapamientos de meses, si existe un periodo del mes 5 al 10, se puede crear otro periodo del mes 1 al 4. Habrá que reordenar los distintos periodos cada vez que se añade un nuevo periodo o se modifica uno. * El mes inicial o final de cualquier periodo no podrán superar nunca la duración en meses indicada en datos generales de la convocatoria, siempre que este campo estuviese informado. En caso de no estar informado no se aplicaría esta comprobación. * El primer periodo siempre comenzará en el mes 1 * No pueden existir salto de meses entre periodos, ya que no se puede dar la situación de que queden días fuera desde el día de inicio del primer periodo hasta el día fin del último periodo.   Sobre las fechas de inicio y fin de presentación:   * Fecha de fin de presentación de un nuevo periodo ha de ser mayor que fecha de inicio de su mismo periodo * No se limitará que las fechas de inicio y fin de presentación de diferentes periodos se solapen o coincidan   Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Cancelar | No realiza ninguna operación en base de datos | No se tendrán en cuenta los cambios indicados en el formulario y se volverá al listado de periodos de seguimiento científico de la convocatoria |  |

### Permiso de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-CON-E, CSP-CON-E\_UO |
| ACT-CSP-003-Gestor | CSP-CON-E, CSP-CON-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-V, CSP-CON-V\_UO, CSP-CON-E, CSP-CON-E\_UO |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.