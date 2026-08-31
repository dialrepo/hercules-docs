# IU-CSP-0204-014 - Modificar convocatoria - Configuración de solicitudes

|  |  |
| --- | --- |
| Cod. IU | **IU-CSP-0204-014 - Modificar convocatoria - Configuración de solicitudes** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Modificar configuración de solicitudes

Formulario para modificar los datos de la configuración de las solicitudes de una convocatoria.

**La modificación de los datos de una convocatoria se rige por lo establecido en las precondiciones de [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)**

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| **La modificación de los datos de una convocatoria se rige por lo establecido en las precondiciones de [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)** | | |
| ¿Habilitar presentación de solicitudes en SGI? | Selector  Booleano  Valores: Sí, No  Opcional (es obligatorio para pasar al estado Registrada) | Indica la habilitación o no del registro de solicitudes a través del SGI para el personal investigador ACT- CSP-001-Investigador.  Tomará los valores Sí/No. |
| Fecha de inicio | Fecha + Hora  Consulta | Fecha de inicio del plazo seleccionado para la presentación de solicitudes.  Se muestra en modo consulta. Expresado en formato Fecha + Hora  Se obtiene directamente de la fecha de inicio indicada en el apartado "Plazos y fases" para la fase seleccionada en el campo "Seleccione plazo de presentación de solicitudes". |
| Fecha de fin | Fecha + Hora  Consulta | Fecha de fin del plazo seleccionado para la presentación de solicitudes.  Se muestra en modo consulta. Expresado en formato Fecha + Hora.   Se obtiene directamente de la fecha de fin indicada en el apartado "Plazos y fases" para la fase seleccionada en el campo "Seleccione plazo de presentación de solicitudes". |
| Documentos requeridos: documentos que se solicitarán de forma obligatoria al cumplimentar la solicitud en el SGI | | |
| Nombre | Texto | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" a través del identificador del tipo de documento. |
| Descripción | Texto | Descripción del tipo de documento. Procedente de la tabla "Tipo de documento" a través del identificador del tipo de documento |
| Observaciones | Texto | Indicaciones u observaciones sobre el documento solicitado |
| Acción editar | Icono de acción |  |
| Acción eliminar | Icono de acción |  |
| Paginación | Componente estándar de paginación sobre la tabla del listado de documentos |  |
| Añadir documento requerido | Botón | Muestra la ventana [IU-CSP-0202-014 - Añadir documento requerido](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0202-014-anadir-documento-requerido) |
| Seleccione el tipo de formulario para solicitud | Selector  Texto corto  Obligatorio | Listado, extraído de un tipo enumerado, con los siguientes valores:   * Estándar. Modelo de solicitud genérico, válido con carácter general para el desarrollo de proyectos/actividades de investigación * RRHH (Predoctoral y posdoctoral) * Apoyo a grupos de investigación   SE MOSTRARÁ EN MODO CONSULTA si el estado de la convocatoria es "Registrada" y existen solicitudes o proyectos vinculados a la convocatoria.  Mostrar icono de información a nivel de vista cuando no se pueda modificar con el siguiente texto: "No se puede modificar el campo porque existen solicitudes y/o proyectos vinculados a la convocatoria" |
| Importe máximo a conceder en la solicitud | Económico  Opcional | Importe máximo a conceder en la solicitud |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Añadir nuevo documento requerido | Inserta un nuevo documento requerido a la convocatoria | Muestra la ventana para añadir un nuevo documento [IU-CSP-0202-014 - Añadir documento requerido](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0202-014-anadir-documento-requerido).  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Editar documento requerido | Modifica los datos de un documento requerido | Muestra la ventana [IU-CSP-0202-014 - Añadir documento requerido](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0202-014-anadir-documento-requerido) en modo edición.  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Eliminar documento requerido | Elimina el documento requerido | Elimina el registro de la tabla de Documentos requeridos de la convocatoria.  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Guardar | Actualiza el registro en base de datos | Si el campo "¿Habilitar presentación de solicitudes en sGI?" toma valor afirmativo, deberá haberse seleccionado un elemento en el desplegable "Fase de presentación de solicitudes"  Se guardarán los cambios modificando los datos de la configuración de la convocatoria en base de datos.  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Cancelar | No realiza ninguna operación en base de datos | No se tendrán en cuenta los cambios indicados en el formulario. |  |

### Permisos de acceso a la pantalla

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