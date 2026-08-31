# CSP-PPEX - Modelo lógico multiidioma - Documentación

### Entidades del modelo Participación en proyectos externos

#### Entidad Solicitud de autorización de participación en proyecto externo: "Autorizacion"

Entidad que representa las solicitudes de autorización de participación en proyectos externos.

| **ATTRIBUTES** |
| --- |
| id : Long  Private  Identificador único. Secuencial. Clave primaria. |
| convocatoria : Convocatoria  Private  Si la convocatoria bajo la que se realizará el proyecto externo está registrada en el SGI se establecerá la relación a través de este campo (en caso contrario la convocatoria se recogerá a través del campo "datos convocatoria"). Es una FK a la tabla convocatoria. |
| entidadRef : String  Private  Referencia de la entidad con la solicita participar en el proyecto externo. Es el identificador de la entidad en el sistema de gestión de empresas corporativo. Durante el ciclo de aprobación de la solicitud de participación la entidad externa podría no estar aún referenciada contra el sistema de gestión de empresas corporativo, en este caso los datos de la entidad de participación estarán recogidos en el campo "dato entidad" como un literal de texto. |
| responsableRef : String  Private  Referencia de la persona que actuará como IP del proyecto externo para el que se solicita autorización. Es el identificador de la persona en el sistema de gestión de personas corporativo. Durante el ciclo de aprobación de la solicitud puede que la persona responsable aún no haya sido dada de alta en el sistema de gestión de personas corporativo, en este caso, los datos de la persona IP del proyecto estarán especificados como un literal de texto en en el campo "datos responsable". |
| horasDedicacion : int  Private  Horas totales que la persona solicitante dedicará al proyecto externo. |
| datosEntidad : String  Private  Datos de identificación, nombre y/o CIF, de la entidad/universidad en la que realizará el proyecto externo para el que se solicita autorización. La entidad externa podría estar dada de alta en el sistema de gestión de empresas corporativo en cuyo caso la referencia a la entidad de participación estaría recogida en el campo "entidad ref". Sin embargo, si la entidad aún no está registrada en el sistema de empresas, los datos se recogerán en este campo. La doble existencia de estos dos campos (datos entidad y entidad ref) se debe a que en primera instancia una solicitud de autorización de participación en proyecto externo es registrada en el SGI por el personal investigador (solicitante) que no tiene permisos para solicitar el alta de una nueva entidad en el sistema de gestión de empresas. Si en el momento de creación de la solicitud, la entidad de partipación aún no existe en el sistema de empresas corporativo, la persona solicitante podrá seguir registrando la solicitud indicando en modo texto los datos de la entidad. Será la unidad de gestión, en la fase de validación de la solicitud, quien podrá solicitar el alta de la entidad en el sistema de empresas. |
| datosResponsable : String  Private  Datos personales, nombre y apellidos, de la persona que actuará como IP en el proyecto externo para el que se solicita la autorización de participación. La persona responsable podría estar dada de alta en el sistema de gestión de personas corporativo en cuyo caso la referencia a la persona responsable estaría recogida en el campo "reponsable ref". Sin embargo, si la persona responsable aún no está registrada en el sistema de personas, los datos personales se recogerán en este campo. La doble existencia de estos dos campos (datos responsable y resposable ref) se debe a que en primera instancia una solicitud de autorización de participación en proyecto externo es registrada en el SGI por el personal investigador (solicitante) que no tiene permisos para solicitar el alta de una nueva persona en el sistema de gestión de personas. Si en el momento de creación de la solicitud, la persona que se indica como IP del proyecto externo aún no existe en el SGP corporativo, la persona solicitante podrá seguir registrando la solicitud indicando en modo texto el nombre y apellidos de la persona IP. Será la unidad de gestión, en la fase de validación de la solicitud, quien podrá solicitar el alta de la persona IP en el SGP, pasando, en este caso a quedar cumplimentado el campo "responsable ref". |
| estado : EstadoAutorizacion  Private  Estado actual de la solicitud de participación en proyecto externo. Es un FK a la entidad "estado autorización". |
| solicitanteRef : String  Private  Referencia de la persona que solicita autorización para participar en proyecto externo. Se corresponde con el identificador de la persona en el sistema de gestión de personas corporativo. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [0..\*] | Target: Public (Class) Convocatoria  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [1] | Target: Public (Class) EstadoAutorizacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [1] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [0..1] | Target: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionTituloProyecto  Cardinality:  [1..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionObservaciones  Cardinality:  [0..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionDatosConvocatoria  Cardinality:  [0..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |

#### Entidad  Título de proyecto de una solicitud de autorización de participación en proyecto externo: "AutorizacionTituloProyecto"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el campo "título del proyecto" de una solicitud de autorización de participación en un proyecto externo. El campo "título" está disponible en la pantalla de Datos generales de la solicitud de Autorización y es un campo obligatorio. Debe de ser introducido en al menos uno de los idiomas habilitados.

| **ATTRIBUTES** |
| --- |
| autorizacion : Autorizacion  Private  Identificador de la solicitud de autorización de participación en proyecto externo a la que pertenece el título del proyecto. Es una FK a la tabla "autorización". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo "título de proyecto" de la solicitud de autorización de participación en un proyecto externo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor que toma el campo "título del proyecto" de una solicitud de participación en un proyecto externo. Está expresado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionTituloProyecto  Cardinality:  [1..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |

#### Entidad Datos de convocatoria de una solicitud de autorización de participación en proyecto externo: "AutorizacionDatosConvocatoria"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el campo "datos convocatoria" de una solicitud de autorización de participación en proyecto externo. Este campo "datos convocatoria" hace referencia al nombre o título de la convocatoria bajo la que se realizará el proyecto externo para el que se solicita autorización de participación. Esta convocatoria podría estar dada de alta ya en el SGI en cuyo caso el identificador de la misma estaría recogido en el campo "convocatoria" de la entidad "autorización". Sin embargo, si la convocatoria no estuviese registrada en el SGI, el nombre de la misma se recogerá en un campo abierto "datos de convocatoria". La doble existencia de estos dos campos (datos convocatoria y convocatoria) se debe a que, en primera instancia, una solicitud de autorización de participación en proyecto externo es registrada en el SGI por el personal investigador (solicitante) que no tiene permisos para crear una convocatoria en el SGI. Si en el momento de creación de la solicitud, la convocatoria no existe en el SGI, la persona solicitante podrá seguir registrando la solicitud indicando en modo texto los datos de la convocatoria. Será la unidad de gestión, en la fase de validación de la solicitud, quien decidirá si registra la convocatoria en el SGI. El campo "datos de la convocatoria" es un campo opcional, ya que la solicitud de autorización se puede rellenar indicando o bien los datos de la convocatoria en modo texto o bien directamente la convocatoria a través del buscador de convocatorias registradas en el SGI.

| **ATTRIBUTES** |
| --- |
| autorizacion : Autorizacion  Private  Identificador de la solictud de autorización de participación en proyecto externo a la que pertenece el campo "datos de convocatoria". Es una FK a la tabla "autorización". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo "datos de convocatoria" de la solicitud de autorización de participación en un proyecto externo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor que toma el campo "datos de convocatoria" de una solicitud de participación en un proyecto externo. Está expresado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionDatosConvocatoria  Cardinality:  [0..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |

#### Entidad Observaciones de una solicitud de autorización de participación en proyecto externo: "AutorizacionObservaciones"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el campo "observaciones" de una solicitud de participación en proyecto externo. Estas observaciones se introducen a través de un campo de texto y son opcionales. No es obligatorio que se cumplimenten en ningún idioma.

| **ATTRIBUTES** |
| --- |
| autorizacion : Autorizacion  Private  Identificador de la solicitud de autorización de participación en proyecto externo a la que pertenecen las observaciones. Es una FK a la tabla "autorización". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo "observaciones" de la solicitud de autorización de participación en un proyecto externo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor que toma el campo "observaciones" de una solicitud de participación en un proyecto externo. Está expresado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) AutorizacionObservaciones  Cardinality:  [0..\*] | Target: Public (Class) Autorizacion  Cardinality:  [1] |

#### Entidad Certificados de autorización de participación en proyecto externo: "CertificadoAutorización"

Documentos acreditativos (certificados) correspondientes a una solicitud de autorización de participación en proyecto externo. Para poder generar el certificado, la autorización ha de estar en estado "autorizada".

| **ATTRIBUTES** |
| --- |
| id : Long  Private  Identificador único. Secuencial. Clave primaria. |
| visible : Boolean  Private  Flag que indica si el certificado de autorización está disponible para la persona solicitante a través de su acceso al SGI. |
| autorizacion : Autorizacion  Private  Registro de la tabla autorización al que pertenece el certificado. Es una FK a la tabla "autorización". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) CertificadoAutorizacion  Cardinality:  [1] | Target: Public (Class) Documento  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) CertificadoAutorizacionNombre  Cardinality:  [0..\*] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) CeriticadoAutorizacionDocumentoRef  Cardinality:  [1..\*] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [1] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [0..\*] |

#### Entidad Nombre del documento para un certificado de autorización de participación en proyecto externo: "CertificadoAutorizacionNombre"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el nombre asociado al documento que contiene el informe de autorización (certificado) de participación en un proyecto externo. El nombre del documento es un literal identificativo del documento que contiene el informe de autorización. Es opcional, no siendo obligatorio introducirlo en ninguno de los idiomas.

| **ATTRIBUTES** |
| --- |
| certificadoAutorizacion : CertificadoAutorizacion  Private  Identificador del certificado de autorización de participación en proyecto externo a la que pertenece el nombre del documento. Es una FK a la tabla "Certificado Autorización". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo "nombre" del documento que contiene el informe de autorización de participación en un proyecto externo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del nombre del documento que contiene el informe de autorización. Está expresado en el idioma indicado en el campo "lang" |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) CertificadoAutorizacionNombre  Cardinality:  [0..\*] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [1] |

#### Entidad Referencia del documento para un certificado de autorización de participación en proyecto externo: "CertificadoAutorizacionDocumentoRef"

Entidad para almacenar la referencia al archivo físico que contiene el informe de autorización (certificado) de participación en un proyecto externo. Los documentos estarán almacenados en el SGDOC. Cada certificado generado tendrá una referencia al archivo en el SGDOC. Para los certificados de participación generados automáticamente se generará un informe en cada uno de los idiomas habilitados. Cada informe en cada idioma será un documento independiente en el SGDOC, por tanto, cada uno con una referencia (documentoRef) diferente. Si el certificado se genera manualmente (el documento se crea de manera ajena al SGI y se sube a través de la aplicación) se asociará al idioma seleccionado en el momento de la acción de subida. Cada certificado de autorización creado tendrá al menos un documento asociado en el SGDOC. La referencia es un identificador del sistema de archivos o sistema de gestión documental (SGDOC) a través del que el SGI implementa la gestión de documentos (según implantación).

| **ATTRIBUTES** |
| --- |
| certificadoAutorizacion : CertificadoAutorizacion  Private  Identificador del certificado de autorización de participación en proyecto externo a la que pertenece el nombre del documento. Es una FK a la tabla "Certificado Autorización". |
| lang : String  Private  Idioma en el que se genera el informe de autorización. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Referencia al archivo almacenado en el SGDOC que contiene el informe de autorización. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) CeriticadoAutorizacionDocumentoRef  Cardinality:  [1..\*] | Target: Public (Class) CertificadoAutorizacion  Cardinality:  [1] |

#### Entidad Estados de una solicitud de autorización de participación en proyecto externo: "EstadoAutorizacion"

Estado actual e histórico de estados de una solicitud de autorización de participación en proyecto externo.

| **ATTRIBUTES** |
| --- |
| id : Long  Private  Identificador único. Secuencial. Clave primaria |
| estado : TipoEstadoAutorizacion  Private  Estado de la solicitud de autorizazión. Es un valor del enumerado "tipo estado autorización". |
| fecha : Timestamp  Private  Fecha en la que la solicitud de autorización pasa al estado recogido en el campo "estado". |
| autorizacionId : Long  Private  Identificador de la solicitud de autorización a la que pertenece el registro de Estado. Es una FK a la tabla "autorización". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoAutorizacion | Target: Public (Enumeration) TipoEstadoAutorizacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoAutorizacionComentario  Cardinality:  [0..\*] | Target: Public (Class) EstadoAutorizacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [1] | Target: Public (Class) EstadoAutorizacion  Cardinality:  [0..\*] |

#### Entidad Comentario del estado de una solicitud de autorización de participación en proyecto externo: "EstadoAutorizacionComentario"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el comentario asociado al cambio de estado de una solicitud de autorización de participación en un proyecto externo. El comentario está disponible desde la acción "cambiar estado" y permite recoger cualquier observación. Es introducido por el perfil de unidad de gestión. Es un campo opcional, no es obligatorio que se introduzca el comentario, en ninguno de los idiomas, para realizar un cambio de estado.

| **ATTRIBUTES** |
| --- |
| estadoAutorizacion : EstadoAutorizacion  Private  Identificador del estado de la solicitud de autorización de participación en proyecto externo a la que pertenece el comentario. Es una FK a la tabla "Estado Autorización". |
| lang : String  Private  Idioma en el que está almacenado el valor el comentario del estado de la solicitud de autorización de participación en un proyecto externo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del comentario asociado a un estado de una solicitud de participación en proyecto externo. Está expresado en el idioma indicado por el camp "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoAutorizacionComentario  Cardinality:  [0..\*] | Target: Public (Class) EstadoAutorizacion  Cardinality:  [1] |

#### Entidad Notificación de registro de proyecto/contrato de CVN: "NotificacionProyectoExternoCVN"

Desde el sistema de gestión de CVN corporativo se notificarán al SGI los ítems aportados manualmente en el CVN en los apartados 050.020.010.000 Proyectos de I+D+i financiados en convocatorias competitivas de administraciones o entidades públicas y privadas y 050.020.020.000 Contratos, convenios o proyectos de I+D+i no competitivos con administraciones o entidades públicas y privadas. Esta entidad almacenará los datos de las notificaciones recibidas del sistema CVN

| **ATTRIBUTES** |
| --- |
| id : Long  Private  Identificador único. Secuencial. Clave primaria. |
| solicitanteRef : String  Private  Referencia de la persona que registra el ítem proyecto/contrato en su CVN. Es el identificador de la persona en el sistema de gestión de personas corporativo. |
| responsableRef : String  Private  Referencia o identificador en el sistema de gestión de personas corporativo asociado a la persona indicada como responsable (IP) del proyecto/contrato en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponderá con el campo 050.020.010.140 Nombre del/de la investigador/a principal (IP, Co-IP,...), en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.250 Nombre del/de la investigador/a principal (IP, Co-IP,...), en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| fechaInicio : Date  Private  Fecha de inicio del proyecto/contrato recogida en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponderá con el campo 050.020.010.270 - Fecha de inicio del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.180 - Fecha de inicio del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| fechaFin : Date  Private  Fecha de fin del proyecto o contrato recogida en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponderá con el campo 050.020.010.410 - Fecha de finalización, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas. En el caso de que el proyecto se registre bajo el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas, este campo no estará disponible, al no estar contemplado en la norma CVN. |
| ambitoGeografico : String  Private  Ámbito geográfico del proyecto/contrato recogido en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponde con el campo 050.020.010.040 - Ámbito del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.040 Ámbito del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| gradoContribucion : String  Private  Tipo de participación en el proyecto/contrato recogido en el sistema de CVN. La correspondencia con la norma FECTY de CVN es: se corresponde con el campo 050.020.010.170 - Grado de contribución, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas y con el campo 050.020.020.280 - Grado de contribución, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| datosEntidadParticipacion : String  Private  Nombre de la entidad de participación recogida sobre el campo "Entidad donde se desarrolla" en el sistema CVN. La correspondencia con la norma FECYT será: campo 050.020.010.100 Entidad donde se desarrolla, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.370 Entidad donde se desarrolla, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas.  En caso que el sistema de CVN no se pueda recoger la referencia correspondiente a la entidad de participación en el Sistema de gestión de empresas corporativo, se remitirán en este campo los datos de la entidad (nombre y/o CIF) como cadena de texto. |
| importeTotal : Bigdecimal  Private  Importe total del proyecto/programa recogido en el sistema de CVN. Se corresponde con el campo 050.020.010.290 Financiación del proyecto, cuantía total, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.200 Financiación del proyecto, cuantía total, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| porcentajeSubvencion : Bigdecimal  Private  Porcentaje subvencionado recogido en el sistema de CVN. Se corresponde con el campo 050.020.010.310 Financiación del proyecto, porcentaje en subvención, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.220 Financiación del proyecto, porcentaje en subvención, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| documentoRef : String  Private  Documento que acredita la concesión/realización del proyecto/contrato. Es el identificador del documento en el sistema de archivos o SGDOC según implantación del SGI. |
| autorizacion : Autorizacion  Private  Solicitud de autorización de participación en proyecto externo con la que se vincula el ítem de CVN. El sistema de CVN habrá consultado previamente al SGI las solicitudes de participación en proyectos externos autorizadas, de forma que al registrar un nuevo ítem proeycto/contrato en el sistema de CVN, pueda vincularse en este sistema con la solicitud de participación con la que se corresponde, Es una FK a la tabla "autorización". |
| proyecto : Proyecto  Private  Proyecto del SGI con el que se asocia la notificación de CVN. Es una FK a la tabla "proyecto". |
| datosResponsable : String  Private  Nombre de la persona que ocupa el cargo de IP del proyecto/contrato, recogida en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponderá con el campo 050.020.010.140 Nombre del/de la investigador/a principal (IP, Co-IP,...), en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.250 Nombre del/de la investigador/a principal (IP, Co-IP,...), en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas.  En caso que desde el sistema de CVN no se pueda recoger la referencia correspondiente a la persona responsable (IP) del proyecto/contrato en el Sistema de gestión de personas corporativo, se remitirán en este campo los datos personales (nombre y apellidos) como cadena de texto. |
| entidadParticipacionRef : String  Private  Referencia a la entidad dentro del Sistema de gestión de empresas corporativo asociada a la entidad recogida sobre el campo "Entidad donde se desarrolla" del sistema de CVN. La correspondencia con la norma FECYT será: campo 050.020.010.100 Entidad donde se desarrolla, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.370 Entidad donde se desarrolla, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| codExterno : String  Private  Referencia que se le ha dado el proyecto en la entidad convocante/financiadora recogida en el sistema de CVN. La correspondencia con la norma FECYT de CVN es: se corresponderá con el campo 050.020.010.260 - Código de proyecto según la entidad financiadora, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.110 - Código de proyecto según la entidad financiadora, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| nombrePrograma : String  Private  Nombre del programa de financiación recogido en el sistema de CVN. Se corresponde con el campo 050.020.010.250 Nombre del programa de financiación, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.170 Nombre del programa asociado al proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| proyectoCVNId : String  Private  Identificador del ítem (proyecto/contrato) en el sistema de CVN. |
| urlDocumentoAcreditacion : String  Private  URL en la que está contenida la acreditación de la realización/concesión del proyecto/contrato. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [1] | Target: Public (Class) Documento  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN | Target: Public (Class) Persona |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [1] | Target: Public (Class) NotificacionProyectoExternoCVNTitulo  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [1] | Target: Public (Class) NotificacionCVNEntidadFinanciadora  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [0..\*] | Target: Public (Class) Proyecto  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion  Cardinality:  [0..1] | Target: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [0..1] |

#### Entidad Título del proyecto/contrato registrado en CVN: "NotificacionProyectoExternoCVNTitulo"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el campo título de proyecto de una notificación de proyecto de cvn. Las notificaciones de proyecto de cvn se recogen en el SGI a través de integración,  proceden de un sistema externo de gestión de CVN. Será este sistema el que se debe de encargar de remitir el título en los diferentes idiomas.  
La  correspondencia del campo título con la norma FECYT de CVN se establece con  el campo 050.020.010.010 - Nombre del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.010 - Nombre del proyecto, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas.

| **ATTRIBUTES** |
| --- |
| notificacionProyectoExternoCVN : NotificacionProyectoExternoCVN  Private  Identificador de la notificación de proyecto externo a la que pertenece el título. Es una FK a la tabla "Notificación Proyecto Externo CVN". |
| lang : String  Private  Idioma en el que está expresado el valor del campo título de la notificación de proyecto externo. Cada idioma se representa por un código de dos carecteres.   * es * en * eu |
| value\_ : String  Private  Valor del campo título de una notificación de proyecto externo. Está expresado en el idioma indicado por el campo "lang". LA disponibilidad del valor en los diferentes idiomas dependerá de la recepción del mismo desde el servicio de integración. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [1] | Target: Public (Class) NotificacionProyectoExternoCVNTitulo  Cardinality:  [0..\*] |

#### Entidad Entidades financiadoras del proyecto/contrato registrado en CVN: "NotificaciónCVNEntidadFinanciadora"

Listado de entidades financiadoras incluidas en los datos del proyecto/contrato notificado desde el sistema de gestión de CVN corporativo.

| **ATTRIBUTES** |
| --- |
| id : Long  Private  Identificador único de la tabla. Secuencial. Clave primaria. |
| entidadFinanciadoraRef : String  Private  Referencia a la entidad dentro del Sistema de gestión de empresas corporativo correspondiente a la entidad financiadora recogida en el sistema de CVN. Se corresponde con el campo 050.020.010.190 Entidad/es financiadora/s, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.120 Nombre/s entidad/es financiadora/s, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas. |
| datosEntidadFinanciadora : String  Private  Nombre de la entidad financiadora recogida en el sistema CVN  Se corresponde con el campo 050.020.010.190 Entidad/es financiadora/s, en el caso de que el proyecto se registre en el epígrafe 050.020.010.000 - Proyectos de I+D+i financiados en convocatorias competitivas de Administraciones o entidades públicas y privadas, o con el campo 050.020.020.120 Nombre/s entidad/es financiadora/s, en el caso de que el proyecto se registre en el epígrafe 050.020.020.000 - Contratos, convenios o proyectos de I+D+i no competitivos con Administraciones o entidades públicas o privadas.  En caso que el sistema de CVN no se pueda recoger la referencia correspondiente a la entidad en el Sistema de gestión de empresas corporativo, se remitirán en este campo los datos de la entidad (nombre y/o CIF) como cadena de texto. |
| notificacionCVN : NotificacionProyectoExternoCVN  Private  Notificación CVN a la que pertenece el registro. Es una FK a la tabla "notificación CVN". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionCVNEntidadFinanciadora | Target: Public (Class) Empresa |
| Association (direction: Unspecified) | |
| Source: Public (Class) NotificacionProyectoExternoCVN  Cardinality:  [1] | Target: Public (Class) NotificacionCVNEntidadFinanciadora  Cardinality:  [0..\*] |

### Enumerados del modelo Participación en proyectos externos

#### Enumerado Estado de solicitud de autorización de participación en proyecto externo: "TipoEstadoAutorizacion"

Enumerado que contiene los posibles estados por los que puede pasar una solicitud de autorización de participación en proyecto externo. Los valores son:

* Borrador (estado inicial, el que toma durante su creación).
* Presentada (la persona solicitante pondrá la solicitud en este estado para que sea revisada por la unidad de gestión).
* Revisión (la unidad de gestión indicará con este estado que la solicitud está en proceso de revisión).
* Autorizada (estado final, será la unidad de gestión quien marque este estado).

| **ATTRIBUTES** |
| --- |
| Borrador :   Public |
| Presentada :   Public |
| Autorizada :   Public |
| Revisión :   Public |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoAutorizacion | Target: Public (Enumeration) TipoEstadoAutorizacion |