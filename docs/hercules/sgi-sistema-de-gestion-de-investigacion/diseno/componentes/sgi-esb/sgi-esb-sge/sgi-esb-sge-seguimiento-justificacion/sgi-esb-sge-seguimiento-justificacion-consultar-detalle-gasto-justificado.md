# SGI - ESB - SGE - Seguimiento justificación - Consultar detalle gasto justificado

| Método | GET |
| --- | --- |
| URL | /seguimiento-justificacion/{id} |
| Parámetros | proyectoId  justificacionId |
| Respuesta | [GastoJustificadoDetalle](https://confluence.um.es/confluence/pages/viewpage.action?pageId=140641365#SGIESBSGESeguimientojustificaci%C3%B3n-GastoJustificadoDetalle) |
| Descripción | Detalle del gasto con todas sus columnas.   * Identificador del gasto * Identificador del proyecto SGE * Identificador justificación (del SGE) * Listado de campos con su nombre y valor (Ver el apartado "**Campos Detalle Gasto Justificado**" para ver que campos se deben de mostrar. * Listado de documentos (identificador, nombre del documento y nombre del fichero, sin el contenido) |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)