# EER-Modelo lógico - Documentación Multiidioma

* [Entidades del modelo Empresas de Explotación de Resultados](#EERModelológicoDocumentaciónMultiidioma-EntidadesdelmodeloEmpresasdeExplotacióndeResultados)
  + [Entidad Empresa de explotación de resultados: “Empresa”](#EERModelológicoDocumentaciónMultiidioma-EntidadEmpresadeexplotaciónderesultados:“Empresa”)
  + [Entidad Nombre o razón social de una empresa de explotación de resultados: “EmpresaNombreRazonSocial”](#EERModelológicoDocumentaciónMultiidioma-EntidadNombreorazónsocialdeunaempresadeexplotaciónderesultados:“EmpresaNombreRazonSocial”)
  + [Entidad Conocimiento o tecnología de una empresa de explotación de resultados: “EmpresaConocimientoTecnologia”](#EERModelológicoDocumentaciónMultiidioma-EntidadConocimientootecnologíadeunaempresadeexplotaciónderesultados:“EmpresaConocimientoTecnologia”)
  + [Entidad Objeto social de una empresa de explotación de resultados: “EmpresaObjetoSocial”](#EERModelológicoDocumentaciónMultiidioma-EntidadObjetosocialdeunaempresadeexplotaciónderesultados:“EmpresaObjetoSocial”)
  + [Entidad Observaciones de una empresa de explotación de resultados: “EmpresaObservaciones”](#EERModelológicoDocumentaciónMultiidioma-EntidadObservacionesdeunaempresadeexplotaciónderesultados:“EmpresaObservaciones”)
  + [Entidad Datos notaría de una empresa de explotación de resultados: “EmpresaNotario”](#EERModelológicoDocumentaciónMultiidioma-EntidadDatosnotaríadeunaempresadeexplotaciónderesultados:“EmpresaNotario”)
  + [Entidad Equipo de administración de una empresa de explotación de resultados: “EmpresaAdministracionSociedad”](#EERModelológicoDocumentaciónMultiidioma-EntidadEquipodeadministracióndeunaempresadeexplotaciónderesultados:“EmpresaAdministracionSociedad”)
  + [Entidad Miembros que componen la sociedad de una empresa de explotación de resultados: “EmpresaComposicionSociedad”](#EERModelológicoDocumentaciónMultiidioma-EntidadMiembrosquecomponenlasociedaddeunaempresadeexplotaciónderesultados:“EmpresaComposicionSociedad”)
  + [Entidad Miembros del equipo emprendedor de una empresa de explotación de resultados: “EmpresaEquipoEmprendedor”](#EERModelológicoDocumentaciónMultiidioma-EntidadMiembrosdelequipoemprendedordeunaempresadeexplotaciónderesultados:“EmpresaEquipoEmprendedor”)
  + [Entidad Documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumento”](#EERModelológicoDocumentaciónMultiidioma-EntidadDocumentoadjuntadoaunaempresadeexplotaciónderesultados:“EmpresaDocumento”)
  + [Entidad Nombre de un documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumentoNombre”](#EERModelológicoDocumentaciónMultiidioma-EntidadNombredeundocumentoadjuntadoaunaempresadeexplotaciónderesultados:“EmpresaDocumentoNombre”)
  + [Entidad Comentarios sobre un documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumentoComentarios”](#EERModelológicoDocumentaciónMultiidioma-EntidadComentariossobreundocumentoadjuntadoaunaempresadeexplotaciónderesultados:“EmpresaDocumentoComentarios”)
  + [Entidad Tipo de documento: “TipoDocumento”](#EERModelológicoDocumentaciónMultiidioma-EntidadTipodedocumento:“TipoDocumento”)
  + [Entidad Nombre de un tipo de documento: “TipoDocumentoNombre”](#EERModelológicoDocumentaciónMultiidioma-EntidadNombredeuntipodedocumento:“TipoDocumentoNombre”)
  + [Entidad Descripción de un tipo de documento: “TipoDocumentoDescripcion”](#EERModelológicoDocumentaciónMultiidioma-EntidadDescripcióndeuntipodedocumento:“TipoDocumentoDescripcion”)
* [Enumerados del modelo lógico de EER](#EERModelológicoDocumentaciónMultiidioma-EnumeradosdelmodelológicodeEER)
  + [Enumerado Estados de una empresa de explotación de resultados: “EstadoEmpresa”](#EERModelológicoDocumentaciónMultiidioma-EnumeradoEstadosdeunaempresadeexplotaciónderesultados:“EstadoEmpresa”)
  + [Enumerado Tipo de administración: “TipoAdministracion”](#EERModelológicoDocumentaciónMultiidioma-EnumeradoTipodeadministración:“TipoAdministracion”)
  + [Enumerado Tipo de aportación: “TipoAportacion”](#EERModelológicoDocumentaciónMultiidioma-EnumeradoTipodeaportación:“TipoAportacion”)
  + [Enumerado Tipo de empresa de explotación de resultados: “TipoEmpresa”](#EERModelológicoDocumentaciónMultiidioma-EnumeradoTipodeempresadeexplotaciónderesultados:“TipoEmpresa”)

### Entidades del modelo Empresas de Explotación de Resultados

#### Entidad Empresa de explotación de resultados: “Empresa”

Representa a cada una de las empresas de explotación de resultados vinculadas a la Universidad que se considera que es interesante gestionar en el SGI.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Empresa". Obligatorio. |
| tipoEmpresa : String  Tipo de la empresa de explotación de resultados. Posibles valores:   - EBT (Empresa de base tecnológica).   - EINCNT (Empresa intensiva en conocimiento no tecnológico).  Obligatorio. |
| solicitanteRef : String  Referencia al solicitante que consta en la solicitud de creación de la empresa de explotación de resultados en los sistemas de la Universidad. Es una clave ajena al modelo SGP que se encuentra en otro esquema de BBDD. Opcional. |
| estado : String  Estado de la empresa. Tomará uno de los valores:   - En tramitación   - No aprobada   - Activa   - Sin actividad   - Disuelta  Obligatorio. |
| entidadRef : String  Referencia a la entidad que representa a la empresa de explotación de resultados en los sistemas de la Universidad. Es una FK al modelo del SGEMP. Opcional. |
| fechaAprobacionCG : Date  Fecha de aprobación en Consejo de Gobierno de la constitución o incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| fechaCese: Date  Fecha de cese de la empresa de explotación de resultados. Opcional. |
| fechaConstitucion: Date  Fecha de constitución de la empresa de explotación de resultados. Opcional. |
| fechaDesvinculacion : Date  Fecha de desvinculación de la Universidad de la empresa de explotación de resultados. Opcional. |
| fechaIncorporacion: Date  Fecha de incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| fechaSolicitud : Date  Fecha de la solicitud de creación de la empresa de explotación de resultados o de la petición de la Universidad de incorporarse a ella. Obligatorio. |
| numeroProtocolo : String  Número de la notaría asociado a la constitución o a la incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| activo: Boolean = True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. Obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [1] | Target: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..1] | Target: Public (Class) Empresa  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoEmpresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Enumeration) EstadoEmpresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaObservaciones  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaNotario  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaNombreRazonSocial  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaObjetoSocial  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaConocimientoTecnologia  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Nombre o razón social de una empresa de explotación de resultados: “EmpresaNombreRazonSocial”

Entidad para almacenar, en todos los idiomas habilitados, el nombre o razón social de la empresa de explotación de resultados.

Una empresa de explotación de resultados puede estar vinculada a una entidad que ya exista en el SGEMP. En este caso, no aplicaría el uso del campo nombre o razón social introducido a través de las pantallas del SGI, sino que los datos que aplicaría serían los recuperados desde el SGEMP. El vínculo entre la empresa de explotación de resultados y una entidad existente en el SGEMP se hace a través del buscador integrado en el campo "EntidadRef" de la tabla "Empresa". Si una empresa de explotación de resultados no está vinculada a ninguna entidad del SGEMP, entonces deberá tener informado el campo nombre o razón social. En este caso el campo nombre o razón social será obligatorio, debiendo ser introducido al menos en un idioma.

Si el campo nombre o razón social está informado y posteriormente la empresa de explotación de resultados se vincula a una entidad del SGEMP a través del campo "entidadRef", aplicaría el uso del nombre de la entidad recuperado desde el SGEMP.

|  |
| --- |
| **ATTRIBUTES** |
| empresa : Empresa  Private   Empresa de explotación de resultados a la que pertenece el nombre o razón social. Es una FK a la tabla "Empresa". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo nombre o razón social de la empresa de explotación de resultados. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor del nombre o razón social. Está expresado en el idioma indicado por el campo "lang" |

|  |  |
| --- | --- |
| **ASSOCIA****TIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaNombreRazonSocial  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Conocimiento o tecnología de una empresa de explotación de resultados: “EmpresaConocimientoTecnologia”

Entidad para almacenar, en todos los idiomas habilitados en la aplicación, la descripción del conocimiento o tecnología de la empresa de explotación de resultados. Si se trata de una EBT, representará la tecnología. Si se trata de una EINCNT, el conocimiento. Es un campo obligatorio, deberá de introducirse al menos en un idioma.

|  |
| --- |
| **ATTRIBUTES** |
| empresa : Empresa  Private  Empresa de explotación de resultados a la que se asocia el conocimiento/tecnología. Es una FK a la tabla "Empresa" |
| lang : String  Private   Idioma en el que está almacenado el valor del campo conocimiento/tecnología de la empresa de explotación de resultados. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Contenido de la tecnología/conocimiento. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaConocimientoTecnologia  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Objeto social de una empresa de explotación de resultados: “EmpresaObjetoSocial”

Entidad para almacenar, en todos los idiomas habilitados en la aplicación, el objeto social de la empresa de explotación de resultados. El objeto social es un campo de texto. Es obligatorio, debiendo introducirse al menos en un idioma.

|  |
| --- |
| **ATTRIBUTES** |
| empresa : Empresa  Private   Empresa de explotación de resultados a la que pertenece el objeto social. Es una FK a la tabla "Empresa" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo objeto social de la empresa de explotación de resultados. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor del campo objeto social. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaObjetoSocial  Cardinality:  [1..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Observaciones de una empresa de explotación de resultados: “EmpresaObservaciones”

Entidad para almacenar en todos los idiomas habilitados en la aplicación, el campo observaciones de una empresa de explotación de resultados. Es un campo de texto libre para introducir cualquier aclaración sobre la empresa. Es opcional, no siendo necesario que se introduzca en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| empresa : Empresa  Private  Empresa de explotación de resultados a la que está asociado el campo observaciones. Es una FK a la tabla "Empresa" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo observaciones de la empresa de explotación de resultados. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones perteneciente a una empresa de explotación de resultados. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaObservaciones  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Datos notaría de una empresa de explotación de resultados: “EmpresaNotario”

Entidad para almacenar, en todos los idiomas habilitados en la aplicación, datos sobre la notaría que interviene en el proceso de constitución de la empresa de explotación de resultados o en el de proceso de incorporación de la Universidad a la empresa de explotación de resultados. Es un campo de texto, de introducción opcional.

|  |
| --- |
| **ATTRIBUTES** |
| empresa : Empresa  Private  Empresa de explotación de resultados a la que está asociado el campo relativo a la notaría. Es una FK a la tabla "Empresa". |
| lang : String  Private   Idioma en el que está almacenado el valor del campo referente a la intervención notarial. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor del campo relativo a la intervención notarial. Está expresado en el idioma recogido en el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaNotario  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Equipo de administración de una empresa de explotación de resultados: “EmpresaAdministracionSociedad”

Representa a cada uno de los miembros de los equipos de administración de las distintas empresas de explotación de resultados.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaAdministracionSociedad". |
| empresaId : Long  Identificador de la empresa a la que pertenece el miembro del equipo de administración de la sociedad. Es una FK sobre la tabla "Empresa". Obligatorio. |
| miembroEquipoAdministracionRef : String  Referencia a la persona miembro del equipo de administración de la sociedad. Es una FK al modelo del SGP. Obligatorio. |
| tipoAdministracion : String  Tipo de administración del miembro del equipo de administración de la sociedad. Los miembros que componen la administración de la sociedad podrán ejercer uno de los tipos de administración del enumerado TipoAdministracion. Obligatorio. |
| fechaInicio : Date  Fecha desde que el miembro forma parte del equipo de administración con tipo indicado en tipoAdministracion. Obligatorio. |
| fechaFin : Date  Fecha hasta la que la persona desempeña su labor como miembro del equipo de administración de la sociedad del tipo indicado en tipoAdministracion. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoAdministracion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [1] | Target: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] |

#### Entidad Miembros que componen la sociedad de una empresa de explotación de resultados: “EmpresaComposicionSociedad”

Representa a cada uno de los miembros de las sociedades que representan las distintas empresas de explotación de resultados.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaComposicionSociedad". |
| empresaId : Long  Identificador de la empresa al que pertenece el miembro de la composición de la sociedad. Clave ajena a "Empresa". Obligatorio. |
| miembroSociedadEmpresaRef : String  Referencia a la entidad miembro de la sociedad. Es una FK al modelo del SGEMP. Estará informado cuando el miembro de la sociedad sea una entidad. Opcional. |
| miembroSociedadPersonaRef : String  Referencia a la persona miembro de la sociedad. Es una FK al modelo del SGP. Estará informado cuando el mimbro de la sociedad sea una persona. Opcional. |
| fechaInicio : Date  Fecha desde que es socio la entidad/persona. Obligatorio. |
| fechaFin : Date  Fecha hasta la que es socio la entidad/persona. Opcional. |
| participacion : Decimal  Porcentaje de participación del socio en la sociedad. Numérico decimal menor o igual que 100. Obligatorio. |
| tipoAportacion : String  Tipo de aportación a la sociedad. Los miembros que componen la sociedad podrán aportar uno de los tipos de aportación del enumerado TipoAportacion. Obligatorio. |
| capitalSocial : Decimal  Importe del capital social aportado por el socio. Numérico decimal. Opcional. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoAportacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### Entidad Miembros del equipo emprendedor de una empresa de explotación de resultados: “EmpresaEquipoEmprendedor”

Representa a cada uno de los miembros de los equipos emprendedores de las distintas empresas de explotación de resultados.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaEquipoEmprendedor". |
| empresaId : Long  Identificador de la empresa al que pertenece el miembro del equipo emprendedor. Clave ajena a "Empresa". Obligatorio. |
| miembroEquipoRef : String  Referencia a la persona miembro del equipo emprendedor. Es una FK al modelo del SGP. Obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |

#### Entidad Documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumento”

Representa a cada uno de los documentos asociados a una empresa de explotación de resultados. Los documentos quedarán registrados en el repositorio de documentos global del SGI.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Identificador único del registro. Secuencia. Clave primaria. |
| empresaId : Long  Identificador de la empresa a la que pertenece el documento. Es una FK sobre la tabla "Empresa". Obligatorio. |
| documentoRef : String  Referencia identificativa del documento en el repositorio de documentos global del SGI. |
| tipoDocumentoId : Long  Clasificación del documento según su tipología. Es una FK a la tabla "TipoDocumento". Obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [1] | Target: Public (Class) EmpresaDocumentoNombre  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [1] | Target: Public (Class) EmpresaDocumentoComentarios  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..1] | Target: Public (Class) Documento  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [0..1] |

#### Entidad Nombre de un documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumentoNombre”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre de un documento que se adjunta a una empresa de explotación de resultados. El nombre es un campo de texto a modo de identificador o título del contenido del documento, de forma independiente al nombre del archivo físico propiamente dicho.

Es un campo obligatorio, ha de introducirse al menos en uno de los idiomas habilitados.

|  |
| --- |
| **ATTRIBUTES** |
| empresaDocumento : EmpresaDocumento  Private   Identificador del documento adjuntado a los datos de una empresa de explotación de resultados al que pertenece el nombre. Es una FK a la tabla "EmpresaDocumento" |
| lang : String  Private   Idioma en el que está almacenado el valor del campo nombre del documento Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo nombre para un documento de una empresa de explotación de resultados. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [1] | Target: Public (Class) EmpresaDocumentoNombre  Cardinality:  [1..\*] |

#### Entidad Comentarios sobre un documento adjuntado a una empresa de explotación de resultados: “EmpresaDocumentoComentarios”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, los comentarios asociados a un documento que se adjunta a una empresa de explotación de resultados. El campo "comentarios" es un campo de texto a través del que se puede introducir cualquier observación sobre el documento. Su cumplimentación es opcional, no siendo obligatorio que se introduzca en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| empresaDocumento : EmpresaDocumento  Private  Identificador del documento al que pertenecen los comentarios. Es una FK a la tabla "EmpresaDocumento" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo comentarios del documento. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo comentarios asociado a un documento que se adjunta a una empresa de explotación de resultados. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [1] | Target: Public (Class) EmpresaDocumentoComentarios  Cardinality:  [0..\*] |

#### Entidad Tipo de documento: “TipoDocumento”

Contiene los tipos de documento disponibles para categorización de los documentos que se adjuntan a las empresas de explotación de resultados. El tipo de documento permitirá clasificar los documentos de acuerdo con la naturaleza de la información que contienen. Es una clasificación jerárquica. Ejemplos de tipos de documento podrían ser: documentos de procedimiento, documentos corporativos, estatutos sociales, ...

Es una tabla que no tiene gestión desde el interface de la aplicación. La introducción de nuevos valores o modificación de los existentes se realizará directamente por BD.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Identificador único de la tabla. Secuencia. Clave primaria. |
| padreId : Long  Identificador del tipo padre (en caso de que sea un subtipo). FK a TipoDocumento (a sí misma). Opcional. |
| activo : Booelan    = True  Flag con el que se da cobertura al borrado lógico de los registros de esta tabla. Un tipo de documento con al flag "activo" a "false" no estará disponible para su vinculación a los documentos de la empresa de explotación de resultados. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality:  [1] | Target: Public (Class) TipoDocumento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumentoNombre  Cardinality:  [1..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality:  [1] | Target: Public (Class) TipoDocumento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumentoDescripcion  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [0..1] |

#### Entidad Nombre de un tipo de documento: “TipoDocumentoNombre”

Entidad para almacenar, en todos los idiomas habilitados en la aplicación, el campo nombre asociado a un tipo de documento bajo el que se clasifican los documentos adjuntos a las empresas de explotación de resultados. El campo nombre será el utilizado para listar los tipos de documento en el selector que permite clasificar un documento adjunto a una empresa de explotación de resultados.

Es un campo obligatorio, debe de existir un valor para el campo nombre al menos en uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| tipoDocumento : TipoDocumento  Private   Identificador del tipo de documento al que pertenece el campo nombre. Es una FK a la tabla "TipoDocumento" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo nombre del tipo de documento Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor del campo nombre del tipo de documento. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumentoNombre  Cardinality:  [1..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [1] |

#### Entidad Descripción de un tipo de documento: “TipoDocumentoDescripcion”

Entidad para almacenar, en todos los idiomas habilitados en la aplicación, el campo descripción asociado a un tipo de documento bajo el que se clasifican los documentos adjuntos a las empresas de explotación de resultados.

El campo descripción es un campo de texto opcional, no es obligatorio que sea introducido en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| tipoDocumento : TipoDocumento  Private   Identificador del tipo de documento al que pertenece el campo descripción. Es una FK a la tabla "TipoDocumento" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo descripción del tipo de documento Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor del campo descripción del tipo de documento. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumentoDescripcion  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [1] |

### Enumerados del modelo lógico de EER

#### Enumerado Estados de una empresa de explotación de resultados: “EstadoEmpresa”

Enumerado que contiene los posibles estados de las empresas de explotación de resultados. Valores:

* En tramitación
* No aprobada
* Activa
* Sin actividad
* Disuelta

|  |
| --- |
| **ATTRIBUTES** |
| En tramitación : Long |
| No aprobada : Long |
| Activa : Long |
| Sin actividad : Long |
| Disuelta : Long |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source:  (Class) Empresa  Cardinality:  [0..\*] | Target:  (Enumeration) EstadoEmpresa  Cardinality:  [1] |

#### Enumerado Tipo de administración: “TipoAdministracion”

Enumerado que contiene los posibles tipos de administración de la sociedad que representa la empresa de explotación de resultados. Valores:

* Administrador único (1 persona)
* Administrador solidario (2 personas o más)
* Administrador mancomunado (2 personas o más)
* Consejo de administración (3 personas o más)

|  |
| --- |
| **ATTRIBUTES** |
| Administrador único : Long |
| Administrador solidario : Long |
| Administrador mancomunado : Long |
| Consejo de administración : Long |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source:  (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target:  (Enumeration) TipoAdministracion  Cardinality:  [1] |

#### Enumerado Tipo de aportación: “TipoAportacion”

Enumerado que contiene los posibles tipos de aportación a la composición de la sociedad que representa la empresa de explotación de resultado por parte de los miembros de la misma. Valores:

* Dineraria
* No dineraria

|  |
| --- |
| **ATTRIBUTES** |
| Dineraria : Long |
| No dineraria : Long |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source:  (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target:  (Enumeration) TipoAportacion  Cardinality:  [1] |

#### Enumerado Tipo de empresa de explotación de resultados: “TipoEmpresa”

Enumerado que contiene los posibles tipos de empresa de explotación de resultados. Valores:

* EBT (Empresa de base tecnológica).
* EINCNT (Empresa intensiva en conocimiento no tecnológico).

|  |
| --- |
| **ATTRIBUTES** |
| EBT : Long |
| EINCNT : Long |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source:  (Class) Empresa  Cardinality:  [0..\*] | Target:  (Enumeration) TipoEmpresa  Cardinality:  [1] |