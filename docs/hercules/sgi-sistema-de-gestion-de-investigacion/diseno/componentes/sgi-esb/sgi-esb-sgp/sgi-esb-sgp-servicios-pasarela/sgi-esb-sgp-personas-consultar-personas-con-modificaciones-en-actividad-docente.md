# SGI - ESB - SGP - Personas - Consultar personas con modificaciones en actividad docente

|  |  |
| --- | --- |
| Método | GET |
| URL | /actividad-docente/modificados-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion: fecha a partir de la cual se quieren ver los cambios * tipoActividad: tipo de actividad docente que se quiere recuperar, usando los códigos de CVN |
| Respuesta | Lista[String] |
| Descripción | Listado de identificadores de las personas que han tenido modificaciones en la actividad docente.  Ejemplo:   * actividad-docente/modificados-ids?q=fechaModificacion=ge="2022-01-01T00:00:00Z";tipoActividad="030.040.000.000" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)