# SGI - ESB - SGP - Personas - Consultar personas modificadas

|  |  |
| --- | --- |
| Método | GET |
| URL | /personas/modificadas-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion |
| Respuesta | Lista[String] |
| Descripción | Listado de los identificadores de personas que han sufrido cambios en los datos identificativos (nombre, apellidos, sexo, número de documento y tipo de documento) y/o en los datos personales (fecha de nacimiento, país de nacimiento, comunidad autónoma de nacimiento y ciudad de nacimiento) y/o en datos de contacto (país de contacto, comunidad autónoma de contacto, provincia de contacto, ciudad de contacto, dirección de contacto, código postal, listado de teléfonos y listado de emails) y/o en la fotografía a partir de la fecha de modificación pasada por parámetro y/o en los sexenios. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)