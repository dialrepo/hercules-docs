# ESB - SGI - Invenciones - Consultar invenciones modificadas

|  |  |
| --- | --- |
| Método | GET |
| URL | /invenciones/modificados-ids |
| Parámetros | q+s (query + sort)  La query estará formada por:   * fechaModificacion: fecha a partir de la cual se quieren ver los cambios. |
| Respuesta | Lista[Long] |
| Descripción | Listado de identificadores de invenciones que han sido modificadas (tanto la entidad Invencion como las entidades relacionadas: sectores de aplicación, áreas de conocimiento, palabras clave,  inventores, periodos de titularidad, titulares, solicitudes de protección)  Ejemplo:   * fechaModificacion=ge="2021-08-18T22:00:00Z" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)