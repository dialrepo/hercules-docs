# ESB - SGI - Grupos de investigación - Consultar grupos de investigación modificados

|  |  |
| --- | --- |
| Método | GET |
| URL | /grupos/modificados-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion: fecha a partir de la cual se quieren ver los cambios |
| Respuesta | Lista[String] |
| Descripción | Listado de Identificadores de Grupo activos que han sido modificados en los datos generales (tabla GRUPO) o en algunas de las siguientes tablas con las que se relaciona:   * GRUPO\_EQUIPO * GRUPO\_PALABRA\_CLAVE * GRUPO\_ENLACE * GRUPO\_RESPONSABLE\_ECONOMICO * GRUPO\_EQUIPO\_INSTRUMENTAL * GRUPO\_LINEA\_INVESTIGACION * GRUPO\_LINEA\_INVESTIGADOR * GRUPO\_LINEA\_CLASIFICACION   Ejemplo:   * fechaModificacion=ge="2021-08-18T22:00:00Z" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)