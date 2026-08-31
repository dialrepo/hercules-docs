# IU-CSP-0201-009 - Crear convocatoria - Documentos

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0201-009 Crear convocatoria - Documentos******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario  Crear convocatoria - Documentos

La información de una convocatoria estará distribuida en los siguientes apartados:

* Datos generales
* Entidades convocantes
* Entidades financiadoras
* Enlaces
* Fases
* Periodos justificación
* Seguimiento científico
* Hitos
* **Documentos**
* Requisitos IP
* Requisitos Equipo
* Elegibilidad
* Configuración de solicitudes

### Documentos

En ese apartado se permite registrar nuevos documentos asociados a la convocatoria, visualizando el árbol de documentos que ya estuviesen incluidos.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de documentos de la convocatoria | | |
| Árbol de documentos del proyecto | Componente gráfico de árbol | Se mostrará el árbol de documentos de la convocatoria, se estructurará por Fases y dentro de éstas por Tipo de documento. Si hubiera documentos sin fase o sin tipo, se mostrarán agrupados al final bajo epígrafes con nombres genéricos. Al seleccionar un elemento del árbol se mostrará el detalle del documento seleccionado, permitiendo  la modificación, descarga o borrado del mismo. |
| Datos del documento seleccionado | | |
| Nombre | Texto | Nombre del documento |
| Documento | Documento |  |
| Tipo de fase | Texto corto | Nombre del tipo de fase. Procedente de la tabla "Tipo de fase" del modelo de ejecución, gestionados en [IU-CSP-0030 - Gestión de tipos de fases](https://confluence.um.es/confluence/pages/viewpage.action?pageId=87821829) |
| Tipo de documento | Texto corto | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" del modelo de ejecución, gestionados en [IU-CSP-0040 - Gestión de tipos de documento](https://confluence.um.es/confluence/pages/viewpage.action?pageId=87821831) |
| Observaciones | Texto largo | Observaciones del documento |
| Público | Booleano  Valores: Sí, No | Tomará los valores Sí/No. Indica si el documento va a ser visible para los ACT- CSP-001-Investigador |
| Editar documento | Botón | Acción modificar |
| Eliminar documento | Botón | Acción eliminar |
| Descargar | Icono de acción | Acción descargar el documento |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Editar | Muestra la pantalla de Edición del documento | Muestra la pantalla [IU-CSP-0204-009 - Modificar convocatoria - Documentos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0204-modificar-convocatoria/iu-csp-0204-009-modificar-convocatoria-documentos) | CSP-CON-C  CSP-CON-C\_UO |
| Eliminar | Elimina el documento de la convocatoria | Elimina el documento de la vista del árbol de documento. Al dar a Guardar la convocatoria se aplicará el cambio en base de datos eliminando el fichero del sistema documental y eliminando el registro de la tabla de documentos de la convocatoria. | CSP-CON-C  CSP-CON-C\_UO |
| Descargar | Descargar el fichero seleccionado |  | CSP-CON-C  CSP-CON-C\_UO |
| Añadir nuevo documento | Muestra la pantalla Nuevo documento | Muestra la pantalla [IU-CSP-202-010 - Añadir documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-202-010-anadir-documento) | CSP-CON-C  CSP-CON-C\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea la Convocatoria con la información introducida en el formulario.  Al guardar una convocatoria se guardar la información de todas las pestañas de la pantalla. | En caso de añadir un nuevo documento  habrá que subir dicho documento al sistema documental (ESB GDOC) y almacenar e registro en al tabla de documentos de convocatoria.  En caso de eliminar un documento se eliminará el fichero del sistema documental y se eliminará el registro de la tabla de documentos de la convocatoria.  En caso de modificar un documento, se actualizará el registro en la base de datos, pero si se modifica el fichero habrá que eliminar el anterior y subir el nuevo al sistema documental | CSP-CON-C  CSP-CON-C\_UO |
| Cancelar | Retorna al listado de Convocatorias sin salvar los posibles cambios.  Al cancelar una convocatoria se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-CON-C, CSP-CON-C\_UO |
| ACT-CSP-003-Gestor | CSP-CON-C, CSP-CON-C\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-C, CSP-CON-C\_UO |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.