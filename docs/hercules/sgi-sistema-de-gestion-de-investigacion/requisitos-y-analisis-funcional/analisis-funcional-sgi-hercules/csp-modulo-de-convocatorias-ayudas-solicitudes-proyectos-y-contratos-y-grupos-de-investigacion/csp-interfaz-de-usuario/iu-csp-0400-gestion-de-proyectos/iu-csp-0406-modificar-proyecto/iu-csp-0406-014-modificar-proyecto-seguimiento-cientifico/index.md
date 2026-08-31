# IU-CSP-0406-014 - Modificar proyecto - Seguimiento científico

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-014 - Modificar proyecto - Seguimiento científico******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Modificar proyecto - Seguimiento científico

Formulario que permitirá mantener historificados los periodos de seguimiento científico. No se limitará  el número de periodos  y no será obligatorio indicar los periodos de seguimiento científico. Si el proyecto proviene de la concesión de una solicitud de convocatoria se podrán recuperar de la misma.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de seguimiento científico del proyecto: recuperados de la tabla "proyecto periodo seguimiento" (filas sin icono o con el icono naranja) y "convocatoria periodo seguimiento" (filas con el icono rojo) | | |
|  | Icono de ayuda con tooltip | Se dibujará el icono de ayuda de color naranja en las siguientes situaciones:   1. Datos del periodo de seguimiento del proyecto no coinciden con los datos del periodo de seguimiento de la convocatoria ( los campos del registro de la tabla "proyecto periodo seguimiento" no son iguales al registro de la tabla de la convocatoria "convocatoria periodo seguimiento"): El texto del tootip en este caso será "La configuración del periodo de seguimiento tiene diferencias respecto a la convocatoria. Pulse el botón Editar para revisar sus datos." 2. El periodo de seguimiento se ha creado en el proyecto directamente (el identificador del registro de la convocatoria es null en la tabla "proyecto periodo seguimiento"): El texto del tootip en este caso será "Este periodo de seguimiento no está incluido en la configuración de la convocatoria.""   Se dibujará el icono de ayuda de color rojo en la siguiente situación:   3 . El periodo de seguimiento no existe en el proyecto (registro no existe en la tabla "proyecto periodo seguimiento")  pero sí en la convocatoria (registro en la tabla "convocatoria periodo seguimiento"), bien porque se ha eliminado en el proyecto o porque se ha creado nuevo en la convocatoria una vez creado el proyecto: El texto del tootip en este caso será "Este periodo de seguimiento está incluido en la configuración de la convocatoria pero no en el proyecto. Pulse el botón Editar si desea añadirlo al proyecto." |
| Núm. periodo | Numérico entero genérico | Número secuencial dentro del proyecto que asignará directamente el sistema en función de la ordenación de la fecha de inicio |
| Fecha inicio | Fecha | Fecha inicial del periodo de seguimiento científico. Se corresponde con el campo "fecha inicio". |
| Fecha fin | Fecha | Fecha final del periodo de seguimiento científico. Se corresponde con el campo "fecha fin". |
| Fecha inicio presentación | Fecha + hora | Fecha y hora de inicio del plazo de presentación asociado al periodo de seguimiento científico. Se corresponde con el campo "fecha inicio presentación". |
| Fecha fin presentación | Fecha + hora | Fecha y hora de fin del plazo de presentación asociado al periodo de seguimiento científico. Se corresponde con el campo "fecha fin presentación". |
| Tipo | Texto | Tipo del periodo de seguimiento. Se mostrará el valor correspondiente del enumerado "Tipo seguimiento" recuperado a partir del campo "tipo seguimiento". |
| Observaciones | Texto largo | Observaciones del periodo de seguimiento científico. Se corresponde con el campo "observaciones" |
| Modificar | Icono de acción | Acción "Modificar" |
| Eliminar | Icono de acción | Acción "Eliminar" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Produce un cambio de contexto al seguimiento científico seleccionado del listado de seguimientos | Se resuelve con la pantalla [IU-CSP-0406-014-001 - Modificar proyecto - Seguimiento científico - Datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0406-modificar-proyecto/iu-csp-0406-014-modificar-proyecto-seguimiento-cientifico/iu-csp-0406-014-001-modificar-proyecto-seguimiento-cientifico-datos-generales).  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-INV-VR  CSP-PRO-E  CSP-PRO-E\_UO |
| Eliminar | Elimina el seguimiento científico del proyecto | Únicamente para los registros que son del proyecto (los de la convocatoria no, los que tienen el icono de ayuda de color rojo)  Se elimina el registro del listado  Si hay registros en la tabla  "ProyectoPeriodoSeguimientoDocumento"  del periodo de seguimiento que se desea eliminar, mostrar en el propio mensaje de confirmación de la acción de eliminar el siguiente texto: "Existen documentos asociados a este periodo de seguimiento, ¿desea continuar?".  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |
| Añadir periodo de seguimiento científico | Produce un cambio de contexto y muestra la pantalla "Añadir nuevo socio" | Muestra la pantalla [IU-CSP-0406-014-001 - Modificar proyecto - Seguimiento científico - Datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0406-modificar-proyecto/iu-csp-0406-014-modificar-proyecto-seguimiento-cientifico/iu-csp-0406-014-001-modificar-proyecto-seguimiento-cientifico-datos-generales).  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modifica el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todos los apartados de definición del proyecto. | En caso de eliminación de un periodo de seguimiento, se realizará un borrado físico del registro en la tabla "ProyectoPeriodoSeguimiento". Se eliminarán en cascada los documentos, vinculados al seguimiento científico (tabla "ProyectoPeriodoSeguimientoDocumento").  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Comunicados

Se enviarán avisos/comunicados relativos al inicio y/o final de los períodos de presentación de justificación del seguimiento científico, que serán gestionados externamente a esta gestión por parte del módulo de tareas programadas y del de comunicados (o envío de emails).

La descripción detallada para la generación de este tipo de comunicado se encuentra en el apartado **Proyectos - Seguimiento científico** dentro de [CSP - Comunicados](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-comunicados) y el flujo general de operativa de este tipo de comunicados en [CU-COM-0020 - Generar comunicado programado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/com-modulo-de-comunicados/com-casos-de-uso/cu-com-0020-generar-comunicado-programado).

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR | Para investigador sin rol principal ni responsable económico:  Todos los campos de la pantalla estarán en modo consulta y los botones de acción de la tabla des-habilitados. No se podrá ir al detalle del seguimiento, solo puede ver el listado de seguimientos. Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador)  Para investigador con rol principal o responsable económico:  Todos los campos de la pantalla estarán en modo consulta y podrá acceder al detalle del seguimiento en modo consulta como a sus apartados (Ver detalle en documentación asociada en [CU-CSP-1200-003 - Ver proyecto - Investigador (rol principal/responsable económico)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-003-ver-proyecto-investigador-rol-principalresponsable-economico)):   * Datos generales * Documentación |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) (sería el caso del Visor) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.