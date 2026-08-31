# EER - Modelo lógico - Documentación

* [Entidades del modelo Empresas de Explotación de Resultados](#EERModelológicoDocumentación-EntidadesdelmodeloEmpresasdeExplotacióndeResultados)
  + [Empresa](#EERModelológicoDocumentación-Empresa)
  + [EmpresaAdministracionSociedad](#EERModelológicoDocumentación-EmpresaAdministracionSociedad)
  + [EmpresaComposicionSociedad](#EERModelológicoDocumentación-EmpresaComposicionSociedad)
  + [EmpresaDocumento](#EERModelológicoDocumentación-EmpresaDocumento)
  + [EmpresaEquipoEmprendedor](#EERModelológicoDocumentación-EmpresaEquipoEmprendedor)
  + [TipoDocumento](#EERModelológicoDocumentación-TipoDocumento)
* [Enumerados](#EERModelológicoDocumentación-Enumerados)
  + [EstadoEmpresa](#EERModelológicoDocumentación-EstadoEmpresa)
  + [TipoAdministracion](#EERModelológicoDocumentación-TipoAdministracion)
  + [TipoAportacion](#EERModelológicoDocumentación-TipoAportacion)
  + [TipoEmpresa](#EERModelológicoDocumentación-TipoEmpresa)

### Entidades del modelo Empresas de Explotación de Resultados

#### Empresa

Representa a cada una de las empresas de explotación de resultados vinculadas a la Universidad que se considera que es interesante gestionar en el SGI.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Empresa". Obligatorio. |
| tipoEmpresa : String  Tipo de la empresa de explotación de resultados. Posibles valores:   - EBT (Empresa de base tecnológica).   - EINCNT (Empresa intensiva en conocimiento no tecnológico).  Obligatorio. |
| solicitanteRef : String  Referencia al solicitante que consta en la solicitud de creación de la empresa de explotación de resultados en los sistemas de la Universidad. Es una clave ajena al modelo SGP que se encuentra en otro esquema de BBDD. Opcional. |
| estado : String  Estado de la empresa. Tomará uno de los valores:   - En tramitación   - No aprobada   - Activa   - Sin actividad   - Disuelta  Obligatorio. |
| nombreRazonSocial : String  Nombre / Razón social de la empresa de explotación de resultados.  Estará informado únicamente si el campo entidadRef no tiene valor, en otro caso, no se deberá estar informado o, aunque lo estuviese anteriormente, su valor no se utilizará, ya que se manejará el nombre de la entidad que provenga de los sistemas de la Universidad.  Obligatorio mientras no esté informado el campo empresaRef, Opcional en otro caso. |
| entidadRef : String  Referencia a la entidad que representa a la empresa de explotación de resultados en los sistemas de la Universidad. Es una FK al modelo del SGEMP. Opcional. |
| objetoSocial : String  Objeto social de la empresa de explotación de resultados. Obligatorio. |
| conocimientoTecnologia : String  Descripción del conocimiento o tecnología de la empresa de explotación de resultados. Si se trata de una EBT, representará la tecnología. Si se trata de una EINCNT, el conocimiento. Obligatorio. |
| fechaAprobacionCG : Date  Fecha de aprobación en Consejo de Gobierno de la constitución o incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| fechaCese: Date  Fecha de cese de la empresa de explotación de resultados. Opcional. |
| fechaConstitucion: Date  Fecha de constitución de la empresa de explotación de resultados. Opcional. |
| fechaDesvinculacion : Date  Fecha de desvinculación de la Universidad de la empresa de explotación de resultados. Opcional. |
| fechaIncorporacion: Date  Fecha de incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| fechaSolicitud : Date  Fecha de la solicitud de creación de la empresa de explotación de resultados o de la petición de la Universidad de incorporarse a ella. OIbligatorio. |
| Notario: String  Datos del notario que intervino en la constitución o a la incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| numeroProtocolo : String  Número de la notaría asociado a la constitución o a la incorporación de la Universidad a la empresa de explotación de resultados. Opcional. |
| observaciones: String  Observaciones que se quieran aportar a la empresa de explotación de resultados. Opcional. |
| activo: Boolean = True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..1] | Target: Public (Class) Empresa  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Enumeration) EstadoEmpresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoEmpresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [1] | Target: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### EmpresaAdministracionSociedad

Representa a cada uno de los miembros de los equipos de administración de las distintas empresas de explotación de resultados.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaAdministracionSociedad". |
| empresaId : Long  Identificador de la empresa a la que pertenece el miembro del equipo de administración de la sociedad. Es una FK sobre la tabla "Empresa". Obligatorio. |
| miembroEquipoAdministracionRef : String  Referencia a la persona miembro del equipo de administración de la sociedad. Es una FK al modelo del SGP. Obligatorio. |
| tipoAdministracion : String  Tipo de administración del miembro del equipo de administración de la sociedad. Los miembros que componen la administración de la sociedad podrán ejercer uno de los tipos de administración del enumerado TipoAdministracion. Obligatorio. |
| fechaInicio : Date  Fecha desde que el miembro forma parte del equipo de administración con tipo indicado en tipoAdministracion. Obligatorio. |
| fechaFin : Date  Fecha hasta la que la persona desempeña su labor como miembro del equipo de administración de la sociedad del tipo indicado en tipoAdministracion. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoAdministracion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Empresa  Cardinality:  [1] | Target: Public (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] |

#### EmpresaComposicionSociedad

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaComposicionSociedad". |
| empresaId : Long  Identificador de la empresa al que pertenece el miembro de la composición de la sociedad. Clave ajena a "Empresa". Obligatorio. |
| miembroSociedadEmpresaRef : String  Referencia a la entidad miembro de la sociedad. Es una FK al modelo del SGEMP. Estará informado cuando el miembro de la sociedad sea una entidad. Opcional. |
| miembroSociedadPersonaRef : String  Referencia a la persona miembro de la sociedad. Es una FK al modelo del SGP. Estará informado cuando el mimbro de la sociedad sea una persona. Opcional. |
| fechaInicio : Date  Fecha desde que es socio la entidad/persona. Obligatorio. |
| fechaFin : Date  Fecha hasta la que es socio la entidad/persona. Opcional. |
| participacion : Decimal  Porcentaje de participación del socio en la sociedad. Numérico decimal menor o igual que 100. Obligatorio. |
| tipoAportacion : String  Tipo de aportación a la sociedad. Los miembros que componen la sociedad podrán aportar uno de los tipos de aportación del enumerado TipoAportacion. Obligatorio. |
| capitalSocial : Decimal  Importe del capital social aportado por el socio. Numérico decimal. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Enumeration) TipoAportacion  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |

#### EmpresaDocumento

| **ATTRIBUTES** |
| --- |
| id : Long  Identificador único del registro. Secuencia. Clave primaria. |
| empresaId : Long  Identificador de la empresa a la que pertenece el documento. Es una FK sobre la tabla "Empresa". Obligatorio. |
| nombre : String  Nombre del documento a nivel de usuario. No es ningún atributo del archivo físico. |
| documentoRef : String  Referencia identificativa del documento en el repositorio de documentos global del SGI. |
| tipoDocumentoId : Long  Clasificación del documento según su tipología. Es una FK a la tabla "TipoDocumento". Obligatorio. |
| comentarios : String  Comentario de texto libre asociado al documento. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..1] | Target: Public (Class) Documento  Cardinality:  [1] |

#### EmpresaEquipoEmprendedor

Representa a cada uno de los miembros de los equipos emprendedores de las distintas empresas de explotación de resultados.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "EmpresaEquipoEmprendedor". |
| empresaId : Long  Identificador de la empresa al que pertenece el miembro del equipo emprendedor. Clave ajena a "Empresa". Obligatorio. |
| miembroEquipoRef : String  Referencia a la persona miembro del equipo emprendedor. Es una FK al modelo del SGP. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Empresa  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaEquipoEmprendedor  Cardinality:  [0..\*] | Target: Public (Class) Persona  Cardinality:  [1] |

#### TipoDocumento

Contiene los tipos de documento disponibles para categorización de los documentos adjuntos en empresas de explotación de resultados.

El tipo de documento permitirá clasificar los documentos de acuerdo con la naturaleza de la información que contienen. Ejemplos de tipos de documento podrían ser: documentos de procedimiento, documentos corporativos, estatutos sociales, ...

| **ATTRIBUTES** |
| --- |
| id : Long  Identificador único de la tabla. Secuencia. Clave primaria. |
| nombre : String  Nombre del tipo de documento. Obligatorio. |
| descripcion : String  Descripción del tipo de documento. Obligatorio. |
| padreId : Long  Identificador del tipo padre (en caso de que sea un subtipo). FK a TipoDocumento (a sí misma). Opcional. |
| activo : Booelan    = True  Flag con el que se da cobertura al borrado lógico de los registros de esta tabla. Un tipo de documento con al flag "activo" a "false" no estará disponible para su vinculación a los documentos de la empresa de explotación de resultados. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality:  [1] | Target: Public (Class) TipoDocumento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality:  [1] | Target: Public (Class) TipoDocumento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) EmpresaDocumento  Cardinality:  [0..\*] | Target: Public (Class) TipoDocumento  Cardinality:  [0..1] |

### Enumerados

#### EstadoEmpresa

Enumerado que contiene los posibles estados de las empresas de explotación de resultados. Valores:

* En tramitación
* No aprobada
* Activa
* Sin actividad
* Disuelta

| **ATTRIBUTES** |
| --- |
| En tramitación : Long |
| No aprobada : Long |
| Activa : Long |
| Sin actividad : Long |
| Disuelta : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source:  (Class) Empresa  Cardinality:  [0..\*] | Target:  (Enumeration) EstadoEmpresa  Cardinality:  [1] |

#### TipoAdministracion

Enumerado que contiene los posibles tipos de administración de la sociedad que representa la empresa de explotación de resultados. Valores:

* Administrador único (1 persona)
* Administrador solidario (2 personas o más)
* Administrador mancomunado (2 personas o más)
* Consejo de administración (3 personas o más)

| **ATTRIBUTES** |
| --- |
| Administrador único : Long |
| Administrador solidario : Long |
| Administrador mancomunado : Long |
| Consejo de administración : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source:  (Class) EmpresaAdministracionSociedad  Cardinality:  [0..\*] | Target:  (Enumeration) TipoAdministracion  Cardinality:  [1] |

#### TipoAportacion

Enumerado que contiene los posibles tipos de aportación a la composición de la sociedad que representa la empresa de explotación de resultado por parte de los miembros de la misma. Valores:

* Dineraria
* No dineraria

| **ATTRIBUTES** |
| --- |
| Dineraria : Long |
| No dineraria : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source:  (Class) EmpresaComposicionSociedad  Cardinality:  [0..\*] | Target:  (Enumeration) TipoAportacion  Cardinality:  [1] |

#### TipoEmpresa

Enumerado que contiene los posibles tipos de empresa de explotación de resultados. Valores:

* EBT (Empresa de base tecnológica).
* EINCNT (Empresa intensiva en conocimiento no tecnológico).

| **ATTRIBUTES** |
| --- |
| EBT : Long |
| EINCNT : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source:  (Class) Empresa  Cardinality:  [0..\*] | Target:  (Enumeration) TipoEmpresa  Cardinality:  [1] |