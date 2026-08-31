# SGI - ESB - SGP - Personas - Consultar personas con modificaciones en formación

|  |  |
| --- | --- |
| Método | GET |
| URL | /formacion/modificados-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion: fecha a partir de la cual se quieren ver los cambios * tipoFormacion: tipo de formación que se quiere recuperar, usando los códigos de CVN |
| Respuesta | Lista[String] |
| Descripción | Listado de identificadores de las personas que han tenido modificaciones en formación realizada.  Ejemplo:   * /formacion/modificados-ids?q=fechaModificacion=ge="2022-01-01T00:00:00Z";tipoFormacion="020.010.020.000" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)