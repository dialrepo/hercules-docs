# IU-CSP-0560-009 - Añadir documento a periodo de justificación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0560-009 - Añadir documento a periodo de justificación******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir documento a periodo de justificación

Formulario que permitirá añadir en la justificación un documento asociado a un periodo de justificación.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario para añadir documentación a la justificación | | | |
| Documento (Subir documento) | | Icono de acción  Obligatorio | Acción "Subir documento" |
| Tipo de documento | | Selector  Texto  Opcional | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" del modelo de ejecución, gestionados en [IU-CSP-0040 - Gestión de tipos de documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0040-gestion-de-tipos-de-documento) |
| Comentarios sobre el documento subido | | Texto largo  Opcional | Indicaciones u observaciones sobre el documento subido |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Acción "Subir documento" | Muestra pantalla de búsqueda para seleccionar documento a adjuntar, sobrescribiendo el fichero previo |  |
| Guardar | Añade el documento a la justificación del socio colaborador del proyecto |  |
| Cancelar | Retorna al formulario de justificación sin salvar los posibles cambios |  |

### Acciones

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |
| ACT-CSP-004-Administrador | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |