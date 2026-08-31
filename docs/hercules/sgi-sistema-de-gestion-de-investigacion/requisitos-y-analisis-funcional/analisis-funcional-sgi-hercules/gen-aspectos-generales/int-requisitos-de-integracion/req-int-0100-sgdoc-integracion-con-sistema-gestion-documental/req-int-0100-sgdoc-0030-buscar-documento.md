# REQ-INT-0100-SGDOC-0030 - Buscar documento

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0100-SGDOC-0030 - Buscar documento** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Buscar un documento en el Sistema de Gestión Documental usando diferentes criterios para filtrar.

Parámetros de entrada:

* Identificador del documento.
* Nombre.
* Versión.
* Fecha de creación.
* Tipo de documento.
* Identificador del autor del documento.

Parámetros de salida: el resultado serán todos los documentos  que cumplan con los criterios establecidos. La información a devolver para cada documento es:

* Identificador del documento.
* Nombre.
* Versión.
* Fecha de creación.
* Tipo de documento.
* Identificador del autor del documento.

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión Documental [SGI - ESB - SGDOC](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgdoc).

El servicio del API que cubre este requisito es [ESB - SGI - Documentos - Buscar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgdoc/esb-sgi-documentos-buscar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)