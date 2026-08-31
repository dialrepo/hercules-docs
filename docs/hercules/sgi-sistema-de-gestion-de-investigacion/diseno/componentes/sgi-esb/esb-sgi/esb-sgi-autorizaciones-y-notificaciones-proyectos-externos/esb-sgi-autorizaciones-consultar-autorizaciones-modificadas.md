# ESB - SGI - Autorizaciones - Consultar autorizaciones modificadas

|  |  |
| --- | --- |
| Método | GET |
| URL | /autorizaciones/modificadas-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion |
| Respuesta | Lista[String] |
| Descripción | Listado de Identificadores de Autorizaciones cuyo estado actual sea "autorizada" y la fecha de dicho estado sea igual o superior a la fecha recibida como parámetro de entrada.  Ejemplo:   * fechaModificacion=ge="2021-08-18T22:00:00Z" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)