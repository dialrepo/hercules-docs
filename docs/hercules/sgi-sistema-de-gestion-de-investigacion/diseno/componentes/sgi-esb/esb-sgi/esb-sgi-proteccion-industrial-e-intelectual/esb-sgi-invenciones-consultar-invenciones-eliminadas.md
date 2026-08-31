# ESB - SGI - Invenciones - Consultar invenciones eliminadas

|  |  |
| --- | --- |
| Método | GET |
| URL | /invenciones/eliminadas-ids |
| Parámetros | q+s (query + sort)  La query estará formada por:   * fechaEliminacion: fecha a partir de la cual se quieren ver las eliminaciones. |
| Respuesta | Lista[Long] |
| Descripción | Listado de Identificadores de Invención que han sido eliminados (campo activo = false) a partir de una fecha.  Se utilizará el siguiente parámetro en la llamada al servicio:   * fechaEliminacion: se le pasará la fecha a partir de la cual se quieren ver las invenciones eliminadas o bien un rango entre las que se quiere buscar   Ejemplo1:   * fechaEliminacion=ge="2024-01-01T22:00:00Z";   Ejemplo2:   * fechaEliminacion=ge="2024-01-01T22:00:00Z";fechaEliminacion=le="2024-12-31T22:00:00Z" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)