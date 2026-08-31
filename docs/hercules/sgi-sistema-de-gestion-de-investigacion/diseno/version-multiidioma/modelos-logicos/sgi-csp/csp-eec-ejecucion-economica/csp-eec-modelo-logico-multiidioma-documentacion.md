# CSP-EEC - Modelo lógico multiidioma - Documentación

* [Entidades del modelo lógico de Ejecución Económica - Validación de gasto](#CSPEECModelológicomultiidiomaDocumentación-EntidadesdelmodelológicodeEjecuciónEconómica-Validacióndegasto)
  + [Entidad Gasto de un proyecto: “GastoProyecto"](#CSPEECModelológicomultiidiomaDocumentación-EntidadGastodeunproyecto:“GastoProyecto")
  + [Entidad Observaciones de un gasto de proyecto: “GastoProyectoObservaciones"](#CSPEECModelológicomultiidiomaDocumentación-EntidadObservacionesdeungastodeproyecto:“GastoProyectoObservaciones")
  + [Entidad Estado de un gasto de proyecto: “EstadoGastoProyecto”](#CSPEECModelológicomultiidiomaDocumentación-EntidadEstadodeungastodeproyecto:“EstadoGastoProyecto”)
  + [Entidad Comentario de un estado de gasto: “EstadoGastoProyectoComentario”](#CSPEECModelológicomultiidiomaDocumentación-EntidadComentariodeunestadodegasto:“EstadoGastoProyectoComentario”)
* [Enumerados del modelo lógico de Ejecución Económica - Validación de gastos](#CSPEECModelológicomultiidiomaDocumentación-EnumeradosdelmodelológicodeEjecuciónEconómica-Validacióndegastos)
  + [Enumerado Estado de validación de un gasto: ”TipoEstadoGasto”](#CSPEECModelológicomultiidiomaDocumentación-EnumeradoEstadodevalidacióndeungasto:”TipoEstadoGasto”)

### Entidades del modelo lógico de Ejecución Económica - Validación de gasto

#### Entidad Gasto de un proyecto: “GastoProyecto"

Entidad para almacenar en el SGI información de los gastos. Es una información adicional a la existente en el SGE. Son datos propios del SGI. No se duplica información del gasto existente en el SGE. Se aporta desde la vista de detalle de gasto de Ejecución Económica - Facturas y justificantes:

* Viajes y dietas: Se aportan datos relativos a los congresos. Campos "fecha congreso", "importe inscripción" y "observaciones".
* Facturas y gastos/Viajes y dietas: validación y clasificación de gastos. La activación de la validación o clasificación de gastos queda establecida por el parámetro de configuración "validacion\_clasificacion\_gastos" de la tabla "configuracion" del modelo lógico de CSP. Los posibles valores de este parámetro son:

  + Validación de gastos
  + Clasificación de gastos
  + Elegibilidad

La configuración "validación de gastos" supone la creación de la tabla "estado gasto proyecto" a partir de la información introducida en el detalle del gasto y la cumplimentación del campo "concepto de gasto" de esta tabla "gasto proyecto". La configuración "clasificación de gastos" supone la cumplimentación del campo "concepto de gasto" en esta tabla "gasto proyecto". La configuración " elegibilidad", supone la clasificación automática del concepto de gasto en base a la elegibilidad del proyecto (no se inserta ningún registro en esta tabla "gasto proyecto").

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private  Identificador único del gasto en la tabla "gasto proyecto" del SGI. Es clave primaria. Secuencia |
| proyectoId : Long  Private  Proyecto del SGI al que está vinculado el gasto. Es una FK a la tabla "proyecto". |
| gastoRef : String  Private   Referencia del gasto en el SGE.  En esta tabla "gasto proyecto" del SGI no se duplica información del gasto que ya exista en el SGE. |
| conceptoGasto : ConceptoGasto  Private  Concepto de gasto del SGI bajo el que se clasifica el gasto. Es una FK a la tabla "concepto gasto".  El campos concepto de gasto estará informado con la configuración "validación clasificación gastos" establecida a:   * clasificación gastos * validación gastos |
| estado : EstadoGastoProyecto  Private  Estado actual del gasto, relativo a la validación del gasto. Es una FK a la tabla "estado gasto proyecto".  Para que el campo estado de los gastos esté informado deberá estar activada la configuración "validación gastos" sobre el parámetro " validación clasificación gastos".  El estado se informa desde la entrada de menú Ejecución económica - Validación de gastos |
| fechaCongreso : Date  Private   Campo para almacenar la fecha en que se realiza el congreso al que hace referencia el gasto. Es un dato no disponible en el SGE por eso se almacena en el SGI. Solo afecta a los gastos de tipo "viajes y dietas". Se informa desde la vista de detalle de un gasto listado en el apartado ejecución económica - facturas y justificantes - viajes y dietas. |
| importeInscripcion : BigDecimal  Private  Campo para almacenar el importe de la inscripción al congreso al que hace referencia el gasto. Es un dato no disponible en el SGE por eso se almacena en el SGI. Solo afecta a los gastos de tipo "viajes y dietas". Se informa desde la vista de detalle de un gasto listado en el apartado ejecución económica - facturas y justificantes - viajes y dietas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoProyecto  Cardinality:  [0..\*] | Target: Public (Class) ProyectoConceptoGastoCodigoEc  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoProyecto  Cardinality:  [1] | Target: Public (Class) EstadoGastoProyecto  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoProyecto  Cardinality:  [1] | Target: Public (Class) GastoProyectoObservaciones  Cardinality:  [0..\*] |

#### Entidad Observaciones de un gasto de proyecto: “GastoProyectoObservaciones"

Entidad para almacenar, en todos los idiomas soportados por el sistema, las observaciones que se añaden a los gastos editados desde el apartado Ejecución Económica - Facturas y justificantes - Viajes y dietas. Estas observaciones hacen referencia al congreso al que hace referencia el gasto. Es información no disponible en el SGE.

|  |
| --- |
| **ATTRIBUTES** |
| gastoProyecto : GastoProyecto  Private  Gasto de un proyecto al que pertenece el campo observaciones. Es una FK a la tabal "gasto proyecto" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo observaciones del gasto. El idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "observaciones" del gasto de proyecto, que estará almacenado en el idioma indicado por el campo "lang". El campo "observaciones" es opcional, no es obligatorio que se introduzca en ninguno de lo idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoProyecto  Cardinality:  [1] | Target: Public (Class) GastoProyectoObservaciones  Cardinality:  [0..\*] |

#### Entidad Estado de un gasto de proyecto: “EstadoGastoProyecto”

Entidad para almacenar el estado relativo a la validación de gastos. La activación o no del proceso de validación está regulado por el parámetro de configuración "validacion\_clasificacion\_gastos" de la tabla "configuración" del modelo lógico de CSP. Para activar la validación de gastos, este parámetro debe de estar establecido al valor "validación gastos".

Los estados de validación en el que puede estar un gasto quedan definidos en el enumerado "tipo estado gasto" .

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private  Identificador único de la tabla "estado gasto proyecto". Secuencia. Clave primaria. |
| estado : TipoEstadoGasto  Private   Estado del gasto. Es un valor del enumerado "tipo estado gasto" |
| fechaEstado : Timestamp  Private  Fecha en la que el gasto adquiere el estado. |
| gastoProyectoId : Long  Private  Identificador del gasto al que está asociado el estado. Es una FK a la tabla "gasto proyecto" |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoGastoProyecto  Cardinality:  [1] | Target: Public (Class) EstadoGastoProyectoComentario  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GastoProyecto  Cardinality:  [1] | Target: Public (Class) EstadoGastoProyecto  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoGasto | Target: Public (Class) EstadoGastoProyecto |

#### Entidad Comentario de un estado de gasto: “EstadoGastoProyectoComentario”

Entidad para almacenar, en todos los idiomas soportados por el sistema, el comentario asociado al estado de validación de un gasto de proyecto. El comentario asociado al estado de validación está disponible en el detalle de un gasto de Ejecución Económica - Validación de gastos, cuando la configuración del parámetro "validacion\_clasificacion\_gastos" está establecida a "Validación de gastos"

El comentario en el proceso de validación es un campo opcional, no es obligatorio que sea introducido en ninguno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| estadoGastoProyecto : EstadoGastoProyecto  Private  Estado de la validación de un gasto al que pertenece el comentario. Es una FK a la tabla "estado gasto proyecto". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo comentario asociado a la validación del gasto. El idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo comentario asociado a la validación de un gasto. Está expresado en el idioma indicado por el campo "lang" |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoGastoProyecto  Cardinality:  [1] | Target: Public (Class) EstadoGastoProyectoComentario  Cardinality:  [0..\*] |

### Enumerados del modelo lógico de Ejecución Económica - Validación de gastos

#### Enumerado Estado de validación de un gasto: ”TipoEstadoGasto”

Enumerado con los estados en los que puede estar la validación de un gasto de un proyecto.

|  |
| --- |
| **ATTRIBUTES** |
| Validado :   Public |
| Bloqueado :   Public |
| Rechazado :   Public |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoGasto | Target: Public (Class) EstadoGastoProyecto |