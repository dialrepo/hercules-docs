# REL-Modelo Lógico - Multiidioma

![](/attachments/1251377162/1251377164.bmp)

### Entidades del modelo lógico de Relaciones

#### Entidad Relaciones de un proyecto: "Relacion"

Un proyecto puede quedar relacionado con más elementos del SGI además de con su convocatoria y/o solicitud de origen. Esta tabla identifica las relaciones del proyecto/contrato con otras entidades del SGI. Las entidades con las que se pueden establecer relaciones adicionales sobre un proyecto/contrato son:

* Otro proyecto/contrato.
* Una convocatoria distinta a la que origina el proyecto. Por ejemplo, para vincular el proyecto con otra posible convocatoria con la que pudiera estar relacionado (convocatoria de selección de contratados, a modo de ejemplo). No se establecerá ninguna dependencia entre ambos, simplemente se trata de registrar el vínculo entre ambos.
* Invención.
* Grupo de investigación.

|  |
| --- |
| **ATTRIBUTES** |
| entidadDestinoRef : String  Private   Identificador de la entidad destino de la relación. Es el identificador único de la tabla correspondiente del SGI de acuerdo al "tipo entidad". |
| entidadOrigenRef : String  Private   Identificador de la entidad desde la que se establece la relación. Es el identificador único de la tabla correspondiente del SGI de acuerdo al "tipo entidad". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoEntidadDestino : TipoEntidad  Private   Identifica el tipo de entidad hacia el que se establece la relación. Es un valor del enumerado "tipo entidad". |
| tipoEntidadOrigen : TipoEntidad  Private    Identifica el tipo de entidad desde el que se establece la relación. Es un valor del enumerado "tipo entidad". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Relacion | Target: Public (Class) Oportunidad |
| Association (direction: Unspecified) | |
| Source: Public (Class) Relacion | Target: Public (Class) RelacionObservaciones |
| Association (direction: Unspecified) | |
| Source: Public (Class) Relacion  Cardinality:  [0..\*] | Target: Public (Class) Convocatoria  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEntidad | Target: Public (Class) Relacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invención | Target: Public (Class) Relacion |

#### Entidad Observaciones de la relación de un proyecto: "RelacionObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el campo "observaciones" asociado a la relación establecida sobre un proyecto. Es un campo opcional, no es obligatorio cumplimenar el campo observaciones en ningún idioma para crear una relación sobre un proyecto.

| **ATTRIBUTES** |
| --- |
| relacion : Relacion  Private  Identificador de la relación de proyecto a la que pertenecen las observaciones. Es una FK a un registro de la tabla "Relacion" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo "observaciones" de una relación de proyecto. El idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones de una relación de proyecto. Está almacenado en el idioma recogido en el campo lang. |

#### Enumerado Tipos de entidad: "TipoEntidad"

Enumerado que recoge los tipos de entidad del SGI con los que se permite establecer una relación de proyecto. Valores: 

* PROYECTO
* CONVOCATORIA
* INVENCION
* GRUPO

|  |
| --- |
| Proyecto :   Public |
| Convocatoria :   Public |
| Invención :   Public |
| Grupo de investigación: Public |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEntidad | Target: Public (Class) Relacion |