# IU-CSP-0560-004 - Periodo justificación - Documentos

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0560-004 - Periodo justificación - Documentos******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Ejecución económica - Periodo justificación - Documentos

Formulario que permitirá indicar todos los documentos que sean de interés para justificación del periodo.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Documentos de la justificación del periodo | | | |
| Documento subido | | Texto | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" del modelo de ejecución, gestionados en [IU-CSP-0040 - Gestión de tipos de documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0040-gestion-de-tipos-de-documento) |
| Tipo documento | | Texto corto | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" del modelo de ejecución, gestionados en [IU-CSP-0040 - Gestión de tipos de documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0040-gestion-de-tipos-de-documento) |
| Comentarios al documento subido | | Texto largo | Comentarios sobre el documento subido |
| Descargar | | Icono de acción | Acción "Descargar" |
| Adjuntar | | Icono de acción | Acción "Adjuntar" |
| Modificar | | Icono de acción | Acción "Modificar" |
| Eliminar | | Icono de acción | Acción "Eliminar" |
| Añadir documento | | Icono de acción | Acción "Añadir documento" |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Descargar | Descarga el fichero seleccionado del listado de documentos de la justificación, subido con anterioridad |  |
| Adjuntar | Muestra pantalla de búsqueda para seleccionar documento a adjuntar, sobrescribiendo el fichero previo |  |
| Modificar | Muestra la pantalla de modificación del documento seleccionado del listado de documentos de la justificación | Se resuelve con la pantalla [IU-CSP-0405-003 - Añadir documento a la justificación en ejecución económica de proyecto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0560-periodos-de-justificacion/iu-csp-0560-009-anadir-documento-a-periodo-de-justificacion) |
| Eliminar | Elimina el documento de la justificación | Elimina el registro de la tabla "Documentos proyecto" |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |
| Añadir documento | Muestra la pantalla para añadir nuevo documento a la justificación | Muestra la pantalla [IU-CSP-0405-003 - Añadir documento a la justificación en ejecución económica de proyecto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0560-periodos-de-justificacion/iu-csp-0560-009-anadir-documento-a-periodo-de-justificacion) |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Guardar | Guarda la justificación del periodo con la información introducida en el formulario.  Al guardar una justificación del periodo se guarda la información de todos los apartados de definición del proyecto. |  |
| Cancelar | Retorna al listado de Justificaciones sin salvar los posibles cambios.  Al cancelar una justificación del periodo se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |

### Acciones

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-EJECUCION-ECONOMICA-CREAR, CSP-EJECUCION-ECONOMICA-EDITAR |
| ACT-CSP-004-Administrador | CSP-EJECUCION-ECONOMICA-CREAR, CSP-EJECUCION-ECONOMICA-EDITAR |