# CSP-EEC-Seguimiento justificación - Modelo lógico multiidioma - Documentación

* [Entidad Alegación de un requerimiento: “AlegacionRequerimiento"](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadAlegacióndeunrequerimiento:“AlegacionRequerimiento")
* [Entidad Observaciones de la alegación de un requerimiento: “AlegacionRequerimientoObservaciones”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadObservacionesdelaalegacióndeunrequerimiento:“AlegacionRequerimientoObservaciones”)
* [Entidad Cofinanciación de un gasto justificado: “CofinanciacionGastoJustificacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadCofinanciacióndeungastojustificado:“CofinanciacionGastoJustificacion”)
* [Entidad Documentación de un requerimiento: “DocumentoRequerimiento”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadDocumentacióndeunrequerimiento:“DocumentoRequerimiento”)
* [Entidad Gasto incluido en una justificación: “GastoJustificacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadGastoincluidoenunajustificación:“GastoJustificacion”)
* [Entidad Gasto incluido en un requerimiento de justificación: “GastoRequerimientoJustificacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadGastoincluidoenunrequerimientodejustificación:“GastoRequerimientoJustificacion”)
* [Entidad Alegación de un gasto incluido en un requerimiento: “GastoRequerimientoJustificacionAlegacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadAlegacióndeungastoincluidoenunrequerimiento:“GastoRequerimientoJustificacionAlegacion”)
* [Entidad Incidencia de un gasto incluido en un requerimiento: “GastoRequerimientoJustificacionIncidencia”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadIncidenciadeungastoincluidoenunrequerimiento:“GastoRequerimientoJustificacionIncidencia”)
* [Entidad Incidencia de documentación incluida en un requerimiento: “IncidenciaDocumentacionRequerimiento”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadIncidenciadedocumentaciónincluidaenunrequerimiento:“IncidenciaDocumentacionRequerimiento”)
* [Entidad Alegación presentada sobre una incidencia de documentación: “IncidenciaDocumentacionRequerimientoAlegacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadAlegaciónpresentadasobreunaincidenciadedocumentación:“IncidenciaDocumentacionRequerimientoAlegacion”)
* [Entidad Descripción de una incidencia de documentación: “IncidenciaDocumentacionRequerimientoIncidencia”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadDescripcióndeunaincidenciadedocumentación:“IncidenciaDocumentacionRequerimientoIncidencia”)
* [Entidad Nombre de documento de una incidencia de documentación: “IncidenciaDocumentacionRequermientoNombreDocumento”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadNombrededocumentodeunaincidenciadedocumentación:“IncidenciaDocumentacionRequermientoNombreDocumento”)
* [Entidad Seguimiento de un periodo de justificación: “ProyectoPeriodoJustificacionSeguimiento”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadSeguimientodeunperiododejustificación:“ProyectoPeriodoJustificacionSeguimiento”)
* [Entidad Seguimiento de la justificación de un proyecto: “ProyectoSeguimientoJustificacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadSeguimientodelajustificacióndeunproyecto:“ProyectoSeguimientoJustificacion”)
* [Entidad requerimiento sobre una justificación: “RequerimientoJustificacion”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-Entidadrequerimientosobreunajustificación:“RequerimientoJustificacion”)
* [Entidad Observaciones de un requerimiento: “RequerimientoJustificacionObservaciones”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadObservacionesdeunrequerimiento:“RequerimientoJustificacionObservaciones”)
* [Entidad Tipo de requerimiento: “TipoRequerimiento”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadTipoderequerimiento:“TipoRequerimiento”)
* [Entidad Nombre de un tipo de requerimiento: “TipoRequerimientoNombre”](#CSPEECSeguimientojustificaciónModelológicomultiidiomaDocumentación-EntidadNombredeuntipoderequerimiento:“TipoRequerimientoNombre”)

### Entidad Alegación de un requerimiento: “AlegacionRequerimiento"

Información relativa a la alegación presentada sobre un requerimiento recibido.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| requerimientoJustificacion : RequerimientoJustificacion  Private |
| fechaAlegacion : Timestamp  Private |
| importeAlegadoCD : BigDecimal  Private |
| importeAlegadoCI : BigDecimal  Private |
| importeReintegrado : BigDecimal  Private |
| importeReintegradoCD : BigDecimal  Private |
| importeReintegradoCI : BigDecimal  Private |
| interesesReintegrados : BigDecimal  Private |
| fechaReintegro : Timestamp  Private |
| justificanteReintegro : String  Private |
| importeAlegado : int  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) AlegacionRequerimiento  Cardinality:  [1] | Target: Public (Class) AlegacionRequerimientoObservaciones  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) AlegacionRequerimiento  Cardinality:  [0..1] |

### Entidad Observaciones de la alegación de un requerimiento: “AlegacionRequerimientoObservaciones”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, las observaciones recogidas en la alegación de un requerimiento. El campo observaciones de la alegación de un requerimiento es un campo de texto opcional, no es obligatorio que se introduzca en ningún idioma.

|  |
| --- |
| **ATTRIBUTES** |
| alegacionRequerimiento : AlegacionRequerimiento  Private   Alegación sobre un requerimiento a la que pertenecen las observaciones. Es una FK a la tabla "AlegacionRequerimiento" |
| lang : String  Private   Identificador del idioma en el que están expresadas las observaciones de la alegación. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private   Valor de las observaciones incluidas en la alegación de un requerimiento. Es un campo de texto opcional. El valor estará exporesado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) AlegacionRequerimiento  Cardinality:  [1] | Target: Public (Class) AlegacionRequerimientoObservaciones  Cardinality:  [0..\*] |

### Entidad Cofinanciación de un gasto justificado: “CofinanciacionGastoJustificacion”

Información de cofinanciación del gasto. Es una información no soportada por los SGE. El importe total de un gasto puede justificarse parcialmente al organismo de una convocatoria asumiendo otra parte del gasto como cofinanciación. La cofinanciación podría ser aportada por otra convocatoria y/o entidad.

Funcionalidad actualmente no implementada en el SGI.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| convocatoriaRef : String  Private |
| proyectoRef : String  Private |
| entidadRef : String  Private |
| importe : BigDecimal  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoJustificacion  Cardinality:  [1] | Target: Public (Class) CofinanciacionGastoJustificacion  Cardinality:  [0..\*] |

### Entidad Documentación de un requerimiento: “DocumentoRequerimiento”

Documentación asociada a un requerimiento. Funcionalidad no implementada actualmente.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| nombreDocumento : String  Private |
| documentoRef : String  Private |
| tipoDocumentoRef : String  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentoRequerimiento | Target: Public (Class) Documento |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) DocumentoRequerimiento  Cardinality:  [0..\*] |

### Entidad Gasto incluido en una justificación: “GastoJustificacion”

Gastos justificados dentro de un periodo de justificación. Funcionalidad no implementada actualmente en el SGI

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| gastoRef : String  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoJustificacion  Cardinality:  [1] | Target: Public (Class) CofinanciacionGastoJustificacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoJustificacion  Cardinality:  [1] | Target: Public (Class) GastoJustificacion  Cardinality:  [0..\*] |

### Entidad Gasto incluido en un requerimiento de justificación: “GastoRequerimientoJustificacion”

Información asociada a un gasto incluido en un requerimiento. En el SGI se aporta información relativa a la incidencia recibida en el requerimiento sobre el gasto, así como a la alegación que se presenta. Además se desglosan los importes aceptados y/o rechazados en la justificación, así como los alegados en la respuesta al requerimiento recibido.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| gastoRef : String  Private |
| requerimientoJustificacion : RequerimientoJustificacion  Private |
| importeAceptado : BigDecimal  Private |
| importeRechazado : BigDecimal  Private |
| importeAlegado : BigDecimal  Private |
| aceptado : Boolean  Private |
| justificacionRef : String  Private  Campo necesario para consultar al SGE un gastoRef de forma única, puesto que en el SGE un mismo gastoRef podría estar en dos justificaciones ref diferentes. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) GastoRequerimientoJustificacionIncidencia  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) GastoRequerimientoJustificacionAlegacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1..\*] | Target: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [0..\*] |

### Entidad Alegación de un gasto incluido en un requerimiento: “GastoRequerimientoJustificacionAlegacion”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción de la alegación enviada en la respuesta de un requerimiento sobre un gasto. Es un campo de texto opcional, no siendo obligatorio que sea introducido en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| gastoRequerimientoJustificacion : GastoRequerimientoJustificacion  Private  Identificador del gasto incluido en el requerimiento de justificación al que está asociada la descripción de la alegación. Es una FK a la tabla "GastoRequerimientoJustificacion". |
| lang : String  Private  Identificador del idioma en el que está expresada la descripción de la alegación presentada al requerimiento sobre un gasto. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Descripción de la alegación. Está expresada en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) GastoRequerimientoJustificacionAlegacion  Cardinality:  [0..\*] |

### Entidad Incidencia de un gasto incluido en un requerimiento: “GastoRequerimientoJustificacionIncidencia”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción de la incidencia remitida sobre un gasto dentro de un requerimiento de justificación. Es un campo de texto opcional, no siendo obligatorio que sea introducido en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| gastoRequerimientoJustificacion : GastoRequerimientoJustificacion  Private  Identificador del gasto incluido en el requerimiento de justificación al que está asociada la descripción de la incidencia. Es una FK a la tabla "GastoRequerimientoJustificacion". |
| lang : String  Private  Identificador del idioma en el que está expresada la descripción de la incidencia sobre el gasto. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  PrivateDescripción de la incidencia. Está expresada en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) GastoRequerimientoJustificacionIncidencia  Cardinality:  [0..\*] |

### Entidad Incidencia de documentación incluida en un requerimiento: “IncidenciaDocumentacionRequerimiento”

Incidencia incluida en um requerimiento de justificación que hace referencia a un documento aportado en la justificación.

El SGI no da cobertura a registrar los documentos aportados en la justificación, puesto que actualmente no se cubre la justificación en el SGI (se parte del requisito de UMU que supone que la justificación se realiza en el SGE). Se permitirá indicar el nombre del documento al que hace referencia la incidencia, la descripción de la incidencia, y la alegación posteriormente presentada en la alegación del requerimiento.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| requerimientoJustificacion : RequerimientoJustificacion  Private |
| nombreDocumento : String  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimientoAlegacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimientoIncidencia  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequermientoNombreDocumento  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [0..\*] |

### Entidad Alegación presentada sobre una incidencia de documentación: “IncidenciaDocumentacionRequerimientoAlegacion”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción asociada a la alegación aportada sobre una incidencia relativa a un documento entregado en la justificación. La incidencia sobre el documento se recibe a través de un requerimiento sobre la justificación y la alegación se realiza sobre el requerimiento.

|  |
| --- |
| **ATTRIBUTES** |
| incidenciaDocumentacionRequerimiento : IncidenciaDocumentacionRequerimiento  Private  Incidencia sobre la documentación con la que se corresponde la alegación. Es una FK a la tabla "IncidenciaDocumentacionRequerimiento" |
| lang : String  Private  Identificador del idioma en el que está expresada la alegación con la que se responde a la incidencia de documentación. Cada idioma se representa por un código de 2 caracteres:   * es * es * eu |
| value\_ : String  Private  Descripción de la alegación con la que se responde a la incidencia de documentación. Está expresada en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimientoAlegacion  Cardinality:  [0..\*] |

### Entidad Descripción de una incidencia de documentación: “IncidenciaDocumentacionRequerimientoIncidencia”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción asociada a una incidencia recibida relativa a un documento entregado en la justificación. La incidencia sobre el documento se recibe a través de un requerimiento sobre la justificación

|  |
| --- |
| **ATTRIBUTES** |
| incidenciaDocumentacionRequerimiento : IncidenciaDocumentacionRequerimiento  Private  Incidencia sobre la documentación con la que se corresponde la descripción. Es una FK a la tabla "IncidenciaDocumentacionRequerimiento" |
| lang : String  Private  Identificador del idioma en el que está expresada la incidencia de documentación recibida en el requerimiento. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Descripción de la incidencia recibida sobre la documentación. Está expresada en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimientoIncidencia  Cardinality:  [0..\*] |

### Entidad Nombre de documento de una incidencia de documentación: “IncidenciaDocumentacionRequermientoNombreDocumento”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre del documento sobre el que se recibe una incidencia en un requerimiento. El nombre del documento es obligatorio, ha de introducirse al menos en un idioma

|  |
| --- |
| **ATTRIBUTES** |
| incidenciaDocumentacionRequerimiento : IncidenciaDocumentacionRequerimiento  Private  Incidencia sobre la documentación a la que hace referencia el nombre del documento. Es una FK a la tabla "IncidenciaDocumentacionRequerimiento" |
| lang : String  Private  Identificador del idioma en el que está expresado el nombre del documento sobre el que se recibe incidencia. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del nombre del documento al que hace referencia la incidencia reportada en el requerimiento. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequermientoNombreDocumento  Cardinality:  [1..\*] |

### Entidad Seguimiento de un periodo de justificación: “ProyectoPeriodoJustificacionSeguimiento”

Información relativa al seguimiento de un periodo de justificación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| proyectoPeriodoJustificacion : ProyectoPeriodoJustificacion  Private |
| importeJustificado : BigDecimal  Private |
| importeJustificadoCD : BigDecimal  Private |
| importeJustificadoCI : BigDecimal  Private |
| importeAceptado : BigDecimal  Private |
| importeAceptadoCD : BigDecimal  Private |
| importeAceptadoCI : BigDecimal  Private |
| importeRechazado : BigDecimal  Private |
| importeRechazadoCD : BigDecimal  Private |
| importeRechazadoCI : BigDecimal  Private |
| importeAlegado : BigDecimal  Private |
| importeAlegadoCD : BigDecimal  Private |
| importeAlegadoCI : BigDecimal  Private |
| importeReintegrar : BigDecimal  Private |
| importeReintegrarCD : BigDecimal  Private |
| importeReintegrarCI : BigDecimal  Private |
| importeReintegrado : BigDecimal  Private |
| importeReintegradoCD : BigDecimal  Private |
| importeReintegradoCI : BigDecimal  Private |
| interesesReintegrados : BigDecimal  Private |
| interesesReintegrar : BigDecimal  Private |
| fechaReintegro : TimeStamp  Private |
| justificanteReintegro : String  Private |
| proyectoAnualidad : ProyectoAnualidad  Private |
| importeNoEjecutado : BigDecimal  Private |
| importeNoEjecutadoCD : BigDecimal  Private |
| importeNoEjecutadoCI : BigDecimal  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoJustificacionSeguimiento  Cardinality:  [0..1 | Target: Public (Class) ProyectoAnualidad  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoJustificacion  Cardinality:  [1] | Target: Public (Class) ProyectoPeriodoJustificacionSeguimiento  Cardinality:  [0..1] |

### Entidad Seguimiento de la justificación de un proyecto: “ProyectoSeguimientoJustificacion”

Estado actual de la justificación de un proyecto. Como el planteamiento implementado en el SGI parte de que la justificación se realiza en el SGE (definición del requisito de UMU), la relación se establece con "ProyectoProyectoSGE", en lugar de establecerse con "proyecto"

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| proyectoProyectoSGE : ProyectoProyectoSGE  Private |
| importeJustificado : BigDecimal  Private |
| importeJustificadoCD : BigDecimal  Private |
| importeJustificadoCI : BigDecimal  Private |
| importeAceptado : BigDecimal  Private |
| importeAceptadoCD : BigDecimal  Private |
| importeAceptadoCI : BigDecimal  Private |
| importeRechazado : BigDecimal  Private |
| importeRechazadoCD : BigDecimal  Private |
| importeRechazadoCI : BigDecimal  Private |
| importeAlegado : BigDecimal  Private |
| importeAlegadoCD : BigDecimal  Private |
| importeAlegadoCostesCI : BigDecimal  Private |
| importeReintegrar : BigDecimal  Private |
| importeReintegrarCD : BigDecimal  Private |
| importeReintegrarCI : BigDecimal  Private |
| importeReintegrado : BigDecimal  Private |
| importeReintegradoCD : BigDecimal  Private |
| importeReintegradoCI : BigDecimal  Private |
| interesesReintegrados : BigDecimal  Private |
| interesesReintegrar : BigDecimal  Private |
| fechaReintegro : Timestamp  Private |
| justificanteReintegro : String  Private |
| importeNoEjecutado : BigDecimal  Private |
| importeNoEjecutadoCD : BigDecimal  Private |
| importeNoEjecutadoCI : BigDecimal  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoProyectoSGE  Cardinality:  [1] | Target: Public (Class) ProyectoSeguimientoJustificacion  Cardinality:  [1] |

### Entidad requerimiento sobre una justificación: “RequerimientoJustificacion”

Requerimientos remitidos por el organismo al que va dirigido la justificación económica de un proyecto. Un requerimiento puede estar asociado a un periodo de justificación concreto o puede ser general.

La implementación realizada parte de los requisitos de UMU, organización en la que se dispone de una herramienta para realizar la justificación económica desde el SGE. De acuerdo a esto, un requerimiento está vinculado a la relación "ProyectoProyectoSGE", y no directamente a la tabal "Proyecto".

La posible relación del requerimiento con un periodo de justificación se establece a través del campo "identificador de justificación" de la tabla "proyecto periodo justificacion". Este identificador hace referencia al SGE. Es el identificador en el SGE con el que corresponde el periodo de justificación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private |
| proyectoPeriodoJustificacion : ProyectoPeriodoJustificacion  Private |
| proyectoProyectoSGE : ProyectoProyectoSGE  Private |
| requerimientoPrevio : RequerimientoJustificacion  Private |
| fechaNotificacion : Timstamp  Private |
| fechaFinAlegacion : Timestamp  Private |
| importeAceptadoCD : BigDecimal  Private |
| importeAceptadoCI : BigDecimal  Private |
| importeRechazadoCD : BigDecimal  Private |
| importeRechazadoCI : BigDecimal  Private |
| importeReintegrar : BigDecimal  Private |
| importeReintegrarCD : BigDecimal  Private |
| importeReintegrarCI : BigDecimal  Private |
| interesesReintegrar : BigDecimal  Private |
| importeAceptado : BigDecimal  Private |
| importeRechazado : BigDecimal  Private |
| numRequerimiento : Integer  Private |
| subvencionJustificada : BigDecimal  Private |
| defectoSubvencion : BigDecimal  Private |
| anticipoJustificado : BigDecimal  Private |
| defectoAnticipo : BigDecimal  Private |
| recursoEstimado : Boolean  Private |
| tipoRequerimiento : TipoRequerimiento  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) RequerimientoJustificacionObservaciones  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) AlegacionRequerimiento  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) IncidenciaDocumentacionRequerimiento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [0..\*] | Target: Public (Class) TipoRequerimiento  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1..\*] | Target: Public (Class) GastoRequerimientoJustificacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) DocumentoRequerimiento  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) RequerimientoJustificacion  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoJustificacion  Cardinality:  [0..1] | Target: Public (Class) RequerimientoJustificacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) RequerimientoJustificacion  Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoProyectoSGE  Cardinality:  [1] | Target: Public (Class) RequerimientoJustificacion  Cardinality:  [0..\*] |

### Entidad Observaciones de un requerimiento: “RequerimientoJustificacionObservaciones”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el campo observaciones de un requerimiento recibido para una justificación. El campo observaciones es un campo de texto y es opcional, no es obligatorio que se introduzca en ninguno de los idiomas

|  |
| --- |
| **ATTRIBUTES** |
| requerimientoJustificacion : RequerimientoJustificacion  Private  Requerimiento de justificación al que pertenecen las observaciones. Es una FK a la tabla RequerimientoJustificacion. |
| lang : String  Private   Identificador del idioma en el que está expresadas las observaciones del requerimiento. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones de un requerimiento de justificación. Es un texto expresado en el idioma indicado por el campo "lang" |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [1] | Target: Public (Class) RequerimientoJustificacionObservaciones  Cardinality:  [0..\*] |

### Entidad Tipo de requerimiento: “TipoRequerimiento”

Entidad para almacenar los tipos de requerimiento de justificación disponibles en el SGI. Es una tabla que actualmente no dispone de gestión a través de la aplicación. Su mantenimiento debe realizarse directamente sobre BD.

|  |
| --- |
| **ATTRIBUTES** |
| id : String  Private |
| activo : Booelan  Private |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoRequerimiento  Cardinality:  [1] | Target: Public (Class) TipoRequerimientoNombre  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequerimientoJustificacion  Cardinality:  [0..\*] | Target: Public (Class) TipoRequerimiento  Cardinality:  [1] |

### Entidad Nombre de un tipo de requerimiento: “TipoRequerimientoNombre”

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre de los tipos de requerimientos de justificación disponibles. El nombre de un tipo de requerimiento es obligatorio.

|  |
| --- |
| **ATTRIBUTES** |
| tipoRequerimiento : TipoRequerimiento  Private  Tipo de requerimiento al que está asociado el nombre. Es una FK a la tabla "TipoRequerimiento". |
| lang : String  Private  Identificador del idioma en el que está expresado el nombre del tipo de requerimiento. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Nombre del tipo de requerimiento. Está expresado en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoRequerimiento  Cardinality:  [1] | Target: Public (Class) TipoRequerimientoNombre  Cardinality:  [1..\*] |