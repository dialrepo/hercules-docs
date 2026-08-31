# CSP-Convocatoria - Modelo lógico multiidioma - Documentación

* [Entidad Convocatoria](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConvocatoria)
* [Entidad Título de una convocatoria: "ConvocatoriaTitulo"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadTítulodeunaconvocatoria:"ConvocatoriaTitulo")
* [Entidad Observaciones de una convocatoria: "ConvocatoriaObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeunaconvocatoria:"ConvocatoriaObservaciones")
* [Entidad Objeto de una convocatoria: "ConvocatoriaObjeto"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObjetodeunaconvocatoria:"ConvocatoriaObjeto")
* [Entidad Listados de áreas temáticas: "AreaTematica"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadListadosdeáreastemáticas:"AreaTematica")
* [Entidad Nombre del área temática: "AreaTematicaNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredeláreatemática:"AreaTematicaNombre")
* [Entidad Descripción del área temática: "AreaTematicaDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndeláreatemática:"AreaTematicaDescripción")
* [Entidad Conceptos de gasto de investigación: "ConceptoGasto"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConceptosdegastodeinvestigación:"ConceptoGasto")
* [Entidad Nombre del concepto de gasto: "ConceptoGastoNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredelconceptodegasto:"ConceptoGastoNombre")
* [Entidad Descripción del concepto de gasto "ConceptoGastoDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndelconceptodegasto"ConceptoGastoDescripción")
* [Entidad Configuración de solicitudes de una convocatoria: "ConfiguracionSolicitud"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConfiguracióndesolicitudesdeunaconvocatoria:"ConfiguracionSolicitud")
* [Entidad Áreas temáticas de una convocatoria: "ConvocatoriaAreaTematica"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadÁreastemáticasdeunaconvocatoria:"ConvocatoriaAreaTematica")
* [Entidad Conceptos de gasto de una convocatoria: "ConvocatoriaConceptoGasto"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConceptosdegastodeunaconvocatoria:"ConvocatoriaConceptoGasto")
* [Entidad Observaciones de un concepto de gasto de una convocatoria: "ConvocatoriaConceptoGastoObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeunconceptodegastodeunaconvocatoria:"ConvocatoriaConceptoGastoObservaciones")
* [Entidad Correspondencia entre códigos económicos del SGE y conceptos de gasto para una convocatoria: "ConvocatoriaConceptoGastoCodigoEc"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadCorrespondenciaentrecódigoseconómicosdelSGEyconceptosdegastoparaunaconvocatoria:"ConvocatoriaConceptoGastoCodigoEc")
* [Entidad Observaciones de la correspondencia entre códigos económicos del SGE y conceptos de gasto para una convocatoria: "ConvocatoriaConceptoGastoCodigoEcObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdelacorrespondenciaentrecódigoseconómicosdelSGEyconceptosdegastoparaunaconvocatoria:"ConvocatoriaConceptoGastoCodigoEcObservaciones")
* [Entidad Documentos de una convocatoria: "ConvocatoriaDocumento"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDocumentosdeunaconvocatoria:"ConvocatoriaDocumento")
* [Entidad Nombre de un documento de una convocatoria: "ConvocatoriaDocumentoNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredeundocumentodeunaconvocatoria:"ConvocatoriaDocumentoNombre")
* [Entidad Observaciones de un documento de una convocatoria: "ConvocatoriaDocumentoObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeundocumentodeunaconvocatoria:"ConvocatoriaDocumentoObservaciones")
* [Entidad Enlaces de una convocatoria: "ConvocatoriaEnlace"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadEnlacesdeunaconvocatoria:"ConvocatoriaEnlace")
* [Entidad Descripción del enlace de una convocatoria: "ConvocatoriaEnlaceDescripcion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndelenlacedeunaconvocatoria:"ConvocatoriaEnlaceDescripcion")
* [Entidad Entidades convocantes de una convocatoria: "ConvocatoriaEntidadConvocante"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadEntidadesconvocantesdeunaconvocatoria:"ConvocatoriaEntidadConvocante")
* [Entidad Entidades financiadoras de una convocatoria: "ConvocatoriaEntidadFinanciadora"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadEntidadesfinanciadorasdeunaconvocatoria:"ConvocatoriaEntidadFinanciadora")
* [Entidad Entidad gestora de una convocatoria: "ConvocatoriaEntidadGestora"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadEntidadgestoradeunaconvocatoria:"ConvocatoriaEntidadGestora")
* [Entidad Fases de una convocatoria: "ConvocatoriaFase"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadFasesdeunaconvocatoria:"ConvocatoriaFase")
* [Entidad Observaciones de la fase de una convocatoria: "ConvocatoriaFasesObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdelafasedeunaconvocatoria:"ConvocatoriaFasesObservaciones")
* [Entidad Hitos de una convocatoria: "ConvocatoriaHito"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadHitosdeunaconvocatoria:"ConvocatoriaHito")
* [Entidad Comentario de un hito de una convocatoria: "ConvocatoriaHitoComentario"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadComentariodeunhitodeunaconvocatoria:"ConvocatoriaHitoComentario")
* [Entidad Avisos de un hito de convocatoria: "ConvocatoriaHitoAviso"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadAvisosdeunhitodeconvocatoria:"ConvocatoriaHitoAviso")
* [Entidad Partidas presupuestarias de una convocatoria: "ConvocatoriaPartida"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadPartidaspresupuestariasdeunaconvocatoria:"ConvocatoriaPartida")
* [Entidad Descripción de una partida de una convocatoria: "ConvocatoriaPartidaDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndeunapartidadeunaconvocatoria:"ConvocatoriaPartidaDescripción")
* [Entidad Calendario de periodos de justificación de una convocatoria: "ConvocatoriaPeriodoJustificacion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadCalendariodeperiodosdejustificacióndeunaconvocatoria:"ConvocatoriaPeriodoJustificacion")
* [Entidad Observaciones de un periodo de justificación de una convocatoria: "ConvocatoriaPeriodoJustificacionObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeunperiododejustificacióndeunaconvocatoria:"ConvocatoriaPeriodoJustificacionObservaciones")
* [Entidad Calendario de periodos de seguimiento científico de una convocatoria: "ConvocatoriaPeriodoSeguimientoCientifico"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadCalendariodeperiodosdeseguimientocientíficodeunaconvocatoria:"ConvocatoriaPeriodoSeguimientoCientifico")
* [Entidad Observaciones de un periodo de seguimiento científico de una convocatoria: "ConvocatoriaPeriodoSeguimientoCientificoObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeunperiododeseguimientocientíficodeunaconvocatoria:"ConvocatoriaPeriodoSeguimientoCientificoObservaciones")
* [Entidad Configuración de documentos requeridos en las solicitudes de una convocatoria: "DocumentoRequeridoSolicitud"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConfiguracióndedocumentosrequeridosenlassolicitudesdeunaconvocatoria:"DocumentoRequeridoSolicitud")
* [Entidad Observaciones de un documento requerido de una solicitud de convocatoria: "DocumentoRequeridoSolicitudObservaciones"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadObservacionesdeundocumentorequeridodeunasolicituddeconvocatoria:"DocumentoRequeridoSolicitudObservaciones")
* [Entidad Fuentes de financiación: "FuenteFinanciacion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadFuentesdefinanciación:"FuenteFinanciacion")
* [Entidad Nombre de la fuente de financiación: "FuenteFinanciacionNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredelafuentedefinanciación:"FuenteFinanciacionNombre")
* [Entidad Descripción de la fuente de financiación: "FuenteFinanciaciónDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndelafuentedefinanciación:"FuenteFinanciaciónDescripción")
* [Entidad Planes o programas de investigación: "Programa"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadPlanesoprogramasdeinvestigación:"Programa")
* [Entidad Nombre del programa: "ProgramaNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredelprograma:"ProgramaNombre")
* [Entidad Descripción del programa: "ProgramaDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndelprograma:"ProgramaDescripción")
* [Entidad Requisitos de convocatoria para los miembros de equipo: "RequisitoEquipo"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadRequisitosdeconvocatoriaparalosmiembrosdeequipo:"RequisitoEquipo")
* [Entidad Otros requisitos de convocatoria para los miembros de equipo: "RequisitoEquipoOtrosRequisitos"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadOtrosrequisitosdeconvocatoriaparalosmiembrosdeequipo:"RequisitoEquipoOtrosRequisitos")
* [Entidad Categorías en convocatoria para los miembros de equipo: "RequisitoEquipoCategoria"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadCategoríasenconvocatoriaparalosmiembrosdeequipo:"RequisitoEquipoCategoria")
* [Entidad Niveles académicos en convocatoria para los miembros de equipo: "RequisitoEquipoNivelAcademico"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNivelesacadémicosenconvocatoriaparalosmiembrosdeequipo:"RequisitoEquipoNivelAcademico")
* [Entidad Requisitos de convocatoria para el rol IP: "RequisitoIP"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadRequisitosdeconvocatoriaparaelrolIP:"RequisitoIP")
* [Entidad Otros requisitos de convocatoria para el rol IP: "RequisitoIPOtrosRequisitos"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadOtrosrequisitosdeconvocatoriaparaelrolIP:"RequisitoIPOtrosRequisitos")
* [Entidad Categorías en convocatoria para el rol IP: "RequisitoIPCategoria"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadCategoríasenconvocatoriaparaelrolIP:"RequisitoIPCategoria")
* [Entidad Nivel académico en convocatoria para el rol IP: "RequisitoIPNivelAcademico"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNivelacadémicoenconvocatoriaparaelrolIP:"RequisitoIPNivelAcademico")
* [Entidad Listado de ámbitos geográfico: "TipoAmbitoGeografico"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadListadodeámbitosgeográfico:"TipoAmbitoGeografico")
* [Entidad Nombre del ámbito geográfico: "TipoAmbitoGeograficoNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredelámbitogeográfico:"TipoAmbitoGeograficoNombre")
* [Entidad Tipos de financiación: "TipoFinanciación"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadTiposdefinanciación:"TipoFinanciación")
* [Entidad Nombre del tipo de financiación: "TipoFinanciaciónNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredeltipodefinanciación:"TipoFinanciaciónNombre")
* [Entidad Descripción del tipo de financiación: "TipoFinanciaciónDescripción"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadDescripcióndeltipodefinanciación:"TipoFinanciaciónDescripción")
* [Entidad Tipos de origen para una fuente de financiación: "TipoOrigenFuenteFinanciacion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadTiposdeorigenparaunafuentedefinanciación:"TipoOrigenFuenteFinanciacion")
* [Entidad Nombre de los tipos de origen para una fuente de financiación: "TipoOrigenFuenteFinanciacionNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredelostiposdeorigenparaunafuentedefinanciación:"TipoOrigenFuenteFinanciacionNombre")
* [Entidad Tipos de régimen de concurrencia: "TipoRegimenConcurrencia"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadTiposderégimendeconcurrencia:"TipoRegimenConcurrencia")
* [Entidad Nombre del los tipos de régimen de concurrencia: "TipoRegimenConcurrenciaNombre"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadNombredellostiposderégimendeconcurrencia:"TipoRegimenConcurrenciaNombre")
* [Entidad Palabras clave de una convocatoria: "ConvocatoriaPalabraClave"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadPalabrasclavedeunaconvocatoria:"ConvocatoriaPalabraClave")
* [Entidad Configuración: "Configuracion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EntidadConfiguración:"Configuracion")
* [Enumerados del modelo CSP Convocatoria](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradosdelmodeloCSPConvocatoria)
  + [Enumerado Clasificación de items para CVN: "ClasificacionCVN"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoClasificacióndeitemsparaCVN:"ClasificacionCVN")
  + [Enumerado Tipo estado de convocatoria: "TipoEstadoConvocatoria"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoTipoestadodeconvocatoria:"TipoEstadoConvocatoria")
  + [Enumerado Tipo formulario de solicitud: "TipoFormularioSolicitud"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoTipoformulariodesolicitud:"TipoFormularioSolicitud")
  + [Enumerado Tipo de periodo de justificación: "TipoJustificacion"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoTipodeperiododejustificación:"TipoJustificacion")
  + [Enumerado Tipo de partida presupuestaria: "TipoPartida"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoTipodepartidapresupuestaria:"TipoPartida")
  + [Enumerado Tipo de periodo de seguimiento científico:"TipoSeguimiento"](#CSPConvocatoriaModelológicomultiidiomaDocumentación-EnumeradoTipodeperiododeseguimientocientífico:"TipoSeguimiento")

### Entidad Convocatoria

Entidad principal que representa una convocatoria de ayuda a la investigación. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private  = True   Flag que da cobertura al borrado lógico de las convocatorias. No es posible realizar un borrado físico de una convocatoria a través del interface de usuario. |
| ambitoGeografico : TipoAmbitoGeografico  Private   Identificador del ámbito geográfico que se asocia a la convocatoria. Es una FK a la tabla "tipo ámbito geográfico". |
| clasificacionCVN : ClasificacionCVN  Private   Identifica el apartado del CVN en el que deberán figurar los proyectos resultados de la convocatoria. Es un valor del enumerado "clasificación CVN". |
| codigo : String  Private   Referencia o identificación externa de la convocatoria. Es un campo totalmente independiente del identificador secuencial interno. Este código de referencia será de introducción libre por la unidad de gestión. |
| duracion : Integer  Private   Valor numérico, expresado en meses, que indicará la duración prevista de la actividad de investigación (proyecto) resultante de la convocatoria. |
| estadoActual : TipoEstadoConvocatoria  Private   Estado actual de la convocatoria. Es un valor del enumerado "tipo estado convocatoria". |
| excelencia : Boolean  Private   Flag que determina si la convocatoria es considerada como una convocatoria de excelencia. |
| fechaConcesion : Timestamp  Private   Fecha en la que se resuelve la concesión de la convocatoria. |
| fechaProvisional : Timestamp  Private   Fecha de resolución provisional de la convocatoria |
| fechaPublicacion : Timestamp  Private   Fecha de publicación de la convocatoria |
| finalidad : TipoFinalidad  Private   Identificador del tipo de finalidad. Los tipos de finalidad disponibles para una convocatoria vienen determinados por el modelo de ejecución al que se asocia. Es una FK a la tabla "tipo finalidad". |
| formularioSolicitud : TipoFormularioSolicitud  Private   Valor que determina el tratamiento que se dará en el SGI a las solicitudes asociadas a la convocatoria. Es el tipo de solicitud, de las disponibles en el SGI, en base a la que se recogerá la información de las solicitudes derivadas de la convocatoria. Es un campo obligatorio. Por defecto, a nivel de interface de usuario tomará el valor "proyecto".    Es un valor del enumerado "tipo formulario solicitud". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| modeloEjecucion : ModeloEjecucion  Private   Identificador del modelo de ejecución al que se asocia la convocatoria. Es una FK a la tabla "modelo ejecución". |
| regimenConcurrencia : TipoRegimenConcurrencia  Private   Identificador del tipo de régimen de concurrencia con el que se asocia la convocatoria. Es una FK a la tabla "tipo régimen concurrencia". |
| unidadGestionRef : String  Private   Identificador de la unidad de gestión a la que se asocia la convocatoria. La unidad de gestión va a delimitar la visibilidad de la convocatoria, de forma que solo los/las usuarios/as que tengan permisos para esta unidad de gestión tendrán acceso a la convocatoria (ya sea con permisos de lectura o de escritura).    Es un campo obligatorio. Es una FK a la tabla "unidad" incluida en el modelo lógico USR. |
| anio : Integer Private  Año natural en el que enmarca la convocatoria. En ocasiones no tiene por qué coincidir con el año de la fecha de publicación por eso se recoge este campo independiente. |
| codInterno : String Private  Referencia o identificación interna de la convocatoria. Especie de nombre corto utilizado en el ámbito interno de la unidad de gestión para referirse a la convocatoria. Es un campo totalmente independiente del identificador secuencial  interno. Este código de referencia será de introducción libre por la  unidad de gestión, aunque en algunas implantaciones podría llegar a generarse automáticamente. En cada implantación podrá tener un formato particular. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) TipoAmbitoGeografico    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoSeguimientoCientifico    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEnlace    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaFase    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaHito    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) Solicitud    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaDocumento    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) Unidad    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) TipoRegimenConcurrencia    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadGestora    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPartida    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadConvocante    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) ModeloTipoFinalidad    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) TipoFinalidad    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoJustificacion    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Enumeration) ClasificacionCVN    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPalabraClave    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Autorizacion    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Entidad    Cardinality:  [1..\*] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo Investigación    Cardinality:  [1..] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Proyecto    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoConvocatoria    Cardinality:  [1] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoFormularioSolicitud    Cardinality:  [1] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Relacion    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |

### Entidad Título de una convocatoria: "ConvocatoriaTitulo"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el campo "título" de una convocatoria. El campo "título" es un campo obligatorio sobre la entidad convocatoria.

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria: Convocatoria Private  Identificador de la convocatoria a la que pertenece el título. Es una FK a la tabla "convocatoria". |
| lang : String  Private   Idioma en el que está almacenado el valor del  campo título de la convocatoria. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private     Valor del campo "título". Es un texto libre. Estará almacenado en el idioma indicado por el campo "lang". La convocatoria ha de tener  un título al menos en un idioma. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaTitulo  Cardinality:  [1..\*] | Target: Public (Class) Convocatoria  Cardinality:  [1] |

### Entidad Observaciones de una convocatoria: "ConvocatoriaObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados, el campo "observaciones" de una convocatoria. El campo "observaciones" es un campo opcional, un texto de libre introducción, que permite dejar recogido cualquier comentario.

| **ATTRIBUTES** |
| --- |
| convocatoria : Convocatoria  Private  Identificador de la convocatoria a la que pertenece el valor. Es una FK a la tabla "convocatoria". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo observaciones de la convocatoria. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "observaciones". Es un texto libre. Estará almacenado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaObservaciones  Cardinality:  [0..\*] | Target: Public (Class) Convocatoria  Cardinality:  [1] |

### Entidad Objeto de una convocatoria: "ConvocatoriaObjeto"

Entidad para almacenar, en cada uno de los idiomas habilitados, el campo "objeto" de una convocatoria. El campo "objeto" es un campo de texto libre para recoger los objetivos de la convocatoria. Su introducción es opcional.

| **ATTRIBUTES** |
| --- |
| convocatoria : Convocatoria  Private  Identificador de la convocatoria a la que pertenece el valor. Es una FK a la tabla "convocatoria". |
| lang : String  Private  Idioma en el que está almacenado el valor del campo título de la convocatoria. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "objeto". Es un texto libre. Estará almacenado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaObjeto  Cardinality:  [0..\*] | Target: Public (Class) Convocatoria  Cardinality:  [1] |

### Entidad Listados de áreas temáticas: "AreaTematica"

Representa los listados de áreas temáticas utilizados en convocatorias, solicitudes y proyectos. Responde a una estructura jerárquica en forma árbol, por lo que dispone de una FK a la propia tabla. Las convocatorias estarán (opcionalmente) asociadas un listado de áreas temáticas (que puede ser particular para esa convocatoria o compartido con otras). Dentro de este listado, las convocatorias pueden restringir las áreas temáticas que se admitirán para el desarrollo de los proyectos derivados, es decir, una convocatoria puede estar vinculada a uno o varios nodos del árbol de áreas temáticas. Las solicitudes y proyectos derivados deberán estar vinculados a un nodo hijo a partir de los establecidos por la convocatoria. 

Los listados de áreas temáticas son configurables a través del interface de usuario. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private   Flag a través del que se implementa el borrado lógico de los registros de esta tabla. Un elemento con el flag "activo" a "false" no estará disponible para su vinculación a las convocatorias, solicitudes y proyectos. Si el elemento que no está activo es el nodo raíz del árbol será el listado completo que no esté visible. Si el elemento que no está activo es un nodo interno, será este nodo y todos sus descendientes los que no estén disponibles. |
| id : Long  Private   Identificador único del registro. Secuencia. Clave primaria. |
| padre : AreaTematica  Private   El listado de áreas temáticas se implementa con una estructura de árbol jerárquico. Este campo establece la jerarquía del registro actual con su superior. El registro para el que este campo tome el valor "null" será el nodo raíz y será el que otorgue el nombre al listado de áreas temáticas.   Es una FK hacia esta misma tabla para implementar la estructura jerárquica. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Source -> Destination) | |
| Source: Public (Class) AreaTematica    Cardinality:  [1] | Target: Public (Class) AreaTematica    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..\*] | Target: Public (Class) AreaTematica    Cardinality:  [1] |
| AssociationClass (direction: Unspecified) | |
| Source: Public (Class) SolicitudProyecto    Cardinality:  [0..\*] | Target: Public (Class) AreaTematica    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) AreaTematicaNombre  Cardinality: [1..\*] | Target: Public (Class) AreaTematica   Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) AreaTematicaDescripcion  Cardinality: [0..\*] | Target: Public (Class) AreaTematica   Cardinality: [1] |

### Entidad Nombre del área temática: "AreaTematicaNombre"

Entidad para almacenar el nombre del área temática en los idiomas soportados por la aplicación. Las áreas temáticas se almacenan en una estructura de árbol. El nombre del nodo raíz del árbol da el nombre al listado de áreas temáticas. El nombre es un campo de texto obligatorio

|  |
| --- |
| **ATTRIBUTES** |
| areaTematica : AreaTematica Private  Identificador del área temática a la que pertenece el nombre. Es una FK a la tabla "area temática". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del área temática en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del área temática en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) AreaTematicaNombre  Cardinality: [1..\*] | Target: Public (Class) AreaTematica   Cardinality: [1] |

### Entidad Descripción del área temática: "AreaTematicaDescripción"

Entidad para almacenar la descripción del área temática en cada uno de los idiomas soportados por la aplicación. La descripción de las áreas temáticas es un campo de texto y es opcional.

|  |
| --- |
| **ATTRIBUTES** |
| areaTematica : AreaTematica Private  Identificador del área temática a la que pertenece la descripción. Es una FK a la tabla "area temática". |
| lang : String Private  Identifica el idioma en el que está almacenado la descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del área temática en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) AreaTematicaDescripcion  Cardinality: [0..\*] | Target: Public (Class) AreaTematica   Cardinality: [1] |

### Entidad Conceptos de gasto de investigación: "ConceptoGasto"

Conceptos de gastos configurados en el SGI de uso propio para este sistema, con independencia de los códigos económicos o tipos de gasto del sistema de gestión económica corporativo. 

Son utilizados para la configuración de la elegibilidad de los gastos en convocatorias y proyectos, para realizar el desglose del presupuesto en solicitudes y proyectos y para la validación de los gastos en los proyectos. Se podrán mapear, a nivel de convocatoria y/o proyectos, con los códigos económicos (tipos de gasto) del SGE. El SGI admite que un concepto de gasto del SGI se pueda corresponder con más de un código económico del SGE y viceversa. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private   Flag a través del que se implementa el borrado lógico de los registros de esta tabla. Los conceptos de gasto con el flag activo a "false" no estarán disponibles en los desplegables de las diferentes pantallas de convocatorias y proyectos. |
| costesIndirectos : Boolean  Private   Flag que determina si el concepto de gasto se utilizará para representar los costes indirectos. Puede haber varios conceptos de gastos que se utilicen como para costes indirectos. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [0..\*] | Target: Public (Class) ConceptoGasto    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProyectoPresupuesto    Cardinality:  [0..\*] | Target: Public (Class) ConceptoGasto    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConceptoGastoNombre  Cardinality: [1..\*] | Target: Public (Class) ConceptoGasto   Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConceptoGastoDescripcion  Cardinality: [0..\*] | Target: Public (Class) ConceptoGasto   Cardinality: [1] |

### Entidad Nombre del concepto de gasto: "ConceptoGastoNombre"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre identificativo del concepto de gasto (interno al SGI). El nombre del concepto de gasto es un campo de texto y es de introducción obligatoria.

|  |
| --- |
| **ATTRIBUTES** |
| conceptoGasto : ConceptoGasto Private  Identificador del concepto de gasto a la que pertenece el nombre. Es una FK a la tabla "concepto gasto". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del concepto de gasto en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del concepto de gasto en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConceptoGastoNombre  Cardinality: [1..\*] | Target: Public (Class) ConceptoGasto   Cardinality: [1] |

### Entidad Descripción del concepto de gasto "ConceptoGastoDescripción"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción del concepto gasto. Esta descripción es opcional y se introduce a través de un campo de texto libre.

|  |
| --- |
| **ATTRIBUTES** |
| conceptoGasto : ConceptoGasto Private  Identificador del concepto de gasto a la que pertenece la descripción. Es una FK a la tabla "concepto gasto". |
| lang : String Private  Identifica el idioma en el que está almacenada la descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del concepto de gasto en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConceptoGastoDescripcion  Cardinality: [0..\*] | Target: Public (Class) ConceptoGasto   Cardinality: [1] |

### Entidad Configuración de solicitudes de una convocatoria: "ConfiguracionSolicitud"

Determina la habilitación o no de la presentación de las solicitudes a través del SGI por parte del personal investigador para la convocatoria correspondiente. Recoge, además, los parámetros necesarios para que el SGI realice determinadas validaciones relacionadas con este proceso de tramitación de solicitudes por parte del personal investigador. Estos parámetros están disponibles para su configuración a través del interface de usuario. 

Solamente existe un registro en la tabla "configuración solicitud" para cada convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el registro. Es una FK a la tabla "convocatoria". |
| fasePresentacionSolicitudes : ConvocatoriaFase  Private   Identificador de la fase configurada en la convocatoria cuyas fechas de inicio y fin utilizará el SGI para habilitar o no el registro de nuevas solicitudes sobre la convocatoria por parte del personal investigador. Es una FK a la tabla "convocatoria fase". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| importeMaximoSolicitud : BigDecimal  Private   Importe máximo que establece la convocatoria para cada solicitud. |
| tramitacionSGI : Boolean  Private   Flag utilizado por el SGI para habilitar o no al personal investigador la posibilidad de registrar solicitudes sobre la convocatoria. Si este campo toma el valor "false", la convocatoria no tendrá habilitada la opción "tramitar" para el personal investigador, quedando en este caso, restringida a la unidad de gestión la posibilidad de crear solicitudes sobre la convocatoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [1] | Target: Public (Class) ConvocatoriaFase    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [1] | Target: Public (Class) DocumentoRequeridoSolicitud    Cardinality:  [0..\*] |

### Entidad Áreas temáticas de una convocatoria: "ConvocatoriaAreaTematica"

Relación de áreas temáticas de la convocatoria. Una convocatoria puede estar asociada a elementos de un único listado de áreas. Puede estar asociada directamente al nodo raíz de ese listado o puede estar asociada a uno o varios nodos de cualquier nivel del árbol que compone el listado. 

De acuerdo al nivel que ocupen los nodos a los que está vinculada la convocatoria, las solicitudes y proyectos derivados solo podrán estar vinculados a nodos hijos de los marcados por la convocatoria. Es decir, la convocatoria restringe el área temática al que se pueden asociar sus solicitudes y proyectos derivados. 

|  |
| --- |
| **ATTRIBUTES** |
| areaTematica : AreaTematicaArbol  Private   Identificador del área temática al que se asocia la convocatoria. Es una FK a la tabla "área temática". |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el registro. Es una FK a la tabla "área temática" |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..\*] | Target: Public (Class) AreaTematica    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProyecto    Cardinality:  [0..\*] | Target: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ContextoProyecto    Cardinality:  [0..\*] | Target: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaAreaTematica    Cardinality:  [0..\*] |

### Entidad Conceptos de gasto de una convocatoria: "ConvocatoriaConceptoGasto"

Elegibilidad de gastos de los proyectos determinada por la convocatoria. La elegibilidad se configura en base a los conceptos de gastos. El listado de conceptos de gasto disponible para configurar la elegibilidad de las convocatorias es propio del SGI y puede ser creado por las unidades de gestión. el flag "permitido" determina si el concepto de gasto es aceptado o no en la justificación de proyectos de la convocatoria. La elegibilidad del concepto de gasto puede definirse para un periodo de tiempo determinado. 

|  |
| --- |
| **ATTRIBUTES** |
| conceptoGasto : ConceptoGasto  Private   Identificador del concepto de gasto del SGI. Es una FK a la tabla "concepto de gasto". |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el registro de elegibilidad. Es un FK a la tabla "convocatoria". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| importeMaximo : BigDecimal  Private   Tomará valor en caso que la convocatoria limite el importe justificable sobre el concepto de gasto. |
| porcentajeMaximo : BigDecimal Private  Tomará valor en caso que la convocatoria especifique un porcentaje máximo para el concepto de gasto sobre el importe total de la convocatoria. |
| mesFinal : Integer  Private   Mes final del periodo en el que el concepto de gasto está o no permitido (flag "permitido"). Este mes se traducirá sobre una fecha determinada en los proyectos derivados de la convocatoria en función de la duración de los mismos. |
| mesInicial : Integer  Private    Mes inicial del periodo en el que el concepto de gasto está o no permitido (flag "permitido"). Este mes se traducirá sobre una fecha determinada en los proyectos derivados de la convocatoria de acuerdo a la duración de los mismos. |
| permitido : Boolean  Private   Flag que determina si el concepto de gasto está o no permitido. Un valor "true" indica que el concepto de gasto es admitido por la convocatoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [1] | Target: Public (Class) ConvocatoriaConceptoGastoCodigoEc    Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [0..\*] | Target: Public (Class) ConceptoGasto    Cardinality:  [1] |

### Entidad Observaciones de un concepto de gasto de una convocatoria: "ConvocatoriaConceptoGastoObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones indicadas sobre un concepto de gasto de una convocatoria. Las observaciones en los conceptos de gasto de convocatoria son opcionales. Se recogen a través de un campo de texto.

| **ATTRIBUTES** |
| --- |
| convocatoriaConceptoGasto : ConvocatoriaConceptoGasto  Private  Identificador del concepto de gasto al que se corresponden las observaciones. Es una FK a la tabla "ConvocatoriaConceptoGasto" |
| lang : String  Private  Identificador del idioma en el que se expresan las observaciones. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones expresado en el idioma indicado por el campo "lang". Las observaciones de un cocepto de gasto dentro de una convocatoria son opcionales y se recogen como un campo de texto. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGastoObservaciones  Cardinality:  [0..\*] | Target: Public (Class) ConvocatoriaConceptoGasto  Cardinality:  [1] |

### Entidad Correspondencia entre códigos económicos del SGE y conceptos de gasto para una convocatoria: "ConvocatoriaConceptoGastoCodigoEc"

Mapeo de los conceptos de gasto del SGI con los códigos económicos del SGE (identificadores de los tipos de gasto del SGE) para una convocatoria concreta. El SGI permite que la relación entre los conceptos de gasto del SGI y los códigos económicos del SGE sea de "muchos" a "muchos". Se contempla, además, que los códigos económicos del SGI puedan tener un periodo de validez. 

|  |
| --- |
| **ATTRIBUTES** |
| codigoEconomicoRef : String  Private   Referencia o Identificador del código económico (tipo de gasto) proveniente del SGE (sistema de gestión económica). |
| convocatoriaGasto : ConvocatoriaGasto  Private    Concepto de gasto concreto para una convocatoria concreta qoe que se vincula el código económico. Es una FK a la tabla "convocatoria concepto gasto". |
| fechaFin : date  Private   Fecha de fin del periodo de correspondencia entre el concepto de gasto del SGI y el código económico del SGE. Se establece este periodo porque pudieran darse el caso de que en el SGE se realicen modificaciones de los códigos económicos vigentes, lo que implicaría realizar un nuevo mapeo de los conceptos de gasto del SGI de acuerdo a la nueva configuración de códigos económicos del SGE. |
| fechaInicio : date  Private   Fecha de inicio del periodo de correspondencia entre el concepto de gasto del SGI y el código económico del SGE. Se establece este periodo porque pudiera darse el caso de que en el SGE se realicen modificaciones de los códigos económicos vigentes, lo que implicaría realizar un nuevo mapeo de los conceptos de gasto del SGI de acuerdo a la nueva configuración de códigos económicos del SGE. |
| id : int  Private   Identificador único de la tabla. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGasto    Cardinality:  [1] | Target: Public (Class) ConvocatoriaConceptoGastoCodigoEc    Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) CodigoEconomicoGasto    Cardinality:  [1] | Target: Public (Class) ConvocatoriaConceptoGastoCodigoEc    Cardinality:  [0..\*] |

### Entidad Observaciones de la correspondencia entre códigos económicos del SGE y conceptos de gasto para una convocatoria: "ConvocatoriaConceptoGastoCodigoEcObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones indicadas sobre la correspondencia de un concepto de gasto de una convocatoria con el código económico del SGE. Estas observaciones se recogen a través de un campo de texto y son opcionales.

| **ATTRIBUTES** |
| --- |
| convocatoriaConceptoGastoCodigoEc : ConvocatoriaConceptoGastoCodigoEc  Private  Código económico del concepto de gasto de una convocatoria con el que se corresponden las observaciones. Es una FK a la tabla "ConvocatoriaConceptoGastoCodigoEc" |
| lang : String  Private  Identifica el idioma en el que se expresa el valor de las observaciones. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones expresado en el idioma indicado por el campo "lang". Las observaciones asociadas a la correspondencia de un concepto de gasto con un código económico del SGE para una convocatoria, son opcionales. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaConceptoGastoCodigoEc  Cardinality:  [1] | Target: Public (Class) ConvocatoriaConceptoGastoCodigoEcObservaciones  Cardinality:  [0..\*] |

### Entidad Documentos de una convocatoria: "ConvocatoriaDocumento"

Documentos asociados a una convocatoria. Los documentos quedarán registrados en el repositorio de documentos global del SGI. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el documento. Es una FK a la tabla convocatoria. |
| ficheroRef : String  Private   Referencia o identificador del documento almacenado en el repositorio de documentos global del SGI |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| publico : Boolean  Private   Indica si el documento va a ser visible para el perfil de investigación a través de su acceso al SGI. |
| tipoDocumento : TipoDocumento  Private   Clasificación del documento según tipología del SGI. Es una FK a la tabla "tipo documento" incluida en l modelo lógico "CSP modelo de ejecución". |
| tipoFase : TipoFase  Private   Fase a la que pertenece el documento. Es una FK a la tabla "tipo fase" incluida en el modelo lógico CSP modelo de ejecución. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaDocumento | Target: Public (Class) Documento |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaDocumento    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ModeloTipoDocumento    Cardinality:  [0..1] | Target: Public (Class) ConvocatoriaDocumento    Cardinality:  [0..\*] |

### Entidad Nombre de un documento de una convocatoria: "ConvocatoriaDocumentoNombre"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el nombre que representa a un documento de una convocatoria. Es obligatorio que cada documento tenga un nombre recogido al menos en un idioma de los habilitados. Es un campo de texto.

| **ATTRIBUTES** |
| --- |
| convocatoriaDocumento : ConvocatoriaDocumento  Private  Identificador del documento de la convocatoria al que corresponde el nombre. Es una FK a la tabla "ConvocatoriaDocumento" |
| lang : String  Private  Identificador del idioma en el que está recogido el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del nombre del documento expresado en el idioma indicado por el campo "lang".  El nombre de un documento es un campo de texto y es obligatorio indicarlo para, al menos, uno de los idiomas habilitados |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaDocumento  Cardinality:  [1] | Target: Public (Class) ConvocatoriaDocumentoNombre  Cardinality:  [1..\*] |

### Entidad Observaciones de un documento de una convocatoria: "ConvocatoriaDocumentoObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones que se aportan sobre los documentos de las convocatorias. Las observaciones de un documento se introducen de manera opcional a través de un campo de texto.

| **ATTRIBUTES** |
| --- |
| convocatoriaDocumento : ConvocatoriaDocumento  Private  Identificador del documento de la convocatoria con el que se corresponden las observaciones.  Es una FK a la tabla "ConvocatoriaDocumento". |
| lang : String  Private  Identificador del idioma en el que está almacenado el registro. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones de un documento de una convocatoria, expresado en el idioma representado por el campo "lang".  Las observaciones de un documento se introducen a través de un campo de texto, siendo su introducción opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaDocumento  Cardinality:  [1] | Target: Public (Class) ConvocatoriaDocumentoObservaciones  Cardinality:  [0..\*] |

### Entidad Enlaces de una convocatoria: "ConvocatoriaEnlace"

Enlaces (en formato URL) que complementan la información de la convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el registro. Es una FK a la tabla "convocatoria". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoEnlace : TipoEnlace  Private   Identificador del tipo de enlace que permite asociar un tipo al enlace. Los tipos de enlace disponibles para la convocatoria vienen determinados por el modelo de ejecución al que se asocia la misma. Es una FK a la tabla "tipo enlace" |
| url : String  Private   Dirección en formato url del enlace. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEnlace    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEnlace    Cardinality:  [0..1] | Target: Public (Class) ConvocatoriaEnlace    Cardinality:  [0..\*] |

### Entidad Descripción del enlace de una convocatoria: "ConvocatoriaEnlaceDescripcion"

Entidad para almacenar,  en cada uno de los idiomas soportados por la aplicación, la descripción de los enlaces de la convocatoria.  La descripción de los enlaces es un campo de texto libre y opcional

| **ATTRIBUTES** |
| --- |
| convocatoriaEnlace : ConvocatoriaEnlace  Private  Identificador de la relación convocatoria-enlace (enlace de la convocatoria) a la que pertenece la descripción. Es una FK a la tabla "convocatoria enlace". |
| lang : String  Private  Identificador del idioma en el que está almacenado el valor. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "descripción" del enlace de la convocatoria. Estará almacenado en el idioma indicado por el campo "lang". Es un texto libre y es opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEnlace  Cardinality:  [1] | Target: Public (Class) ConvocatoriaEnlaceDescripcion  Cardinality:  [0..\*] |

### Entidad Entidades convocantes de una convocatoria: "ConvocatoriaEntidadConvocante"

Entidades convocantes de la convocatoria. El SGI no dispone de un repositorio de entidades, las entidades (empresas) siempre deberán ser referencias al sistema de gestión de empresas corporativo con el que se integra el SGI. 

Las entidades convocantes participan en la convocatoria bajo un determinado plan de investigación (nodo raíz de una de las estructuras árbol almacenada en la tabla "programa"). Una entidad puede participar en una convocatoria cubriendo cualquier programa del plan, en este caso la entidad convocante estaría vinculada al nodo raíz del árbol que represente al plan. Una entidad también podría estar asociada a un programa, subprograma o modalidad concretos dentro del plan de investigación. En este caso la entidad se vinculará a un nodo de un nivel interior del árbol del plan de investigación. Las solicitudes y proyectos derivados de la convocatoria deberán estar vinculados a un nodo hijo a partir de los establecidos por la convocatoria para cada entidad convocante. Es decir, la convocatoria restringe los programas, subprogramas, modalidades, topics, etc. que estarán disponibles para las solicitudes y proyectos derivados de la convocatoria. 

|  |
| --- |
| **OUTGOING STRUCTURAL RELATIONSHIPS** |
| Generalization from  ConvocatoriaEntidadConvocante to  Entidad   [ Direction is 'Source -> Destination'. ] |
| Aggregation from  ConvocatoriaEntidadConvocante to  EmpresaEconomica   [ Direction is 'Source -> Destination'. ] |
| Aggregation from  ConvocatoriaEntidadConvocante to  Empresa   [ Direction is 'Source -> Destination'. ] |

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria con la que se asocia la entidad convocante. Es una FK a la tabla "entidad". |
| empresaRef : String  Private   Referencia o identificador de la entidad (empresa) en el sistema de gestión de empresas corporativo. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| programa : Programa  Private   Identificador del programa bajo el que la entidad convocante participa en la convocatoria. Es una FK a la tabla "programa". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadConvocante    Cardinality:  [0..\*] | Target: Public (Class) Programa    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadConvocante    Cardinality:  [0..\*] |

### Entidad Entidades financiadoras de una convocatoria: "ConvocatoriaEntidadFinanciadora"

Entidades que participan en la financiación de la convocatoria. El SGI no dispone de un repositorio de entidades, las entidades (empresas) siempre deberán ser referencias al sistema de gestión de empresas corporativo con el que se integra el SGI. 

Una entidad participa en la financiación de una convocatoria a través de una fuente de financiación y un tipo de financiación. Las entidades financiadoras de las convocatorias son heredadas por las solicitudes y proyectos derivados de la misma. 

|  |
| --- |
| **OUTGOING STRUCTURAL RELATIONSHIPS** |
| Aggregation from  ConvocatoriaEntidadFinanciadora to  Empresa   [ Direction is 'Source -> Destination'. ] |
| Aggregation from  ConvocatoriaEntidadFinanciadora to  EmpresaEconomica   [ Direction is 'Source -> Destination'. ] |
| Generalization from  ConvocatoriaEntidadFinanciadora to  Entidad   [ Direction is 'Source -> Destination'. ] |

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el registro. Es una FK a la tabla "convocatoria". |
| empresaRef : String  Private  Referencia o identificador de la entidad (empresa) en el sistema de gestión de empresas corporativo. |
| fuenteFinanciacion : FuenteFinanciacion  Private   Identificador de la fuente de financiación a través de la que la entidad financia la convocatoria. Es una FK a la tabla "fuente financiación". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| importeFinanciacion : BigDecimal  Private   Importe de financiación aportado por la entidad. |
| porcentajeFinanciacion : BigDecimal  Private   Porcentaje que la entidad aporta a la convocatoria respecto al total de financiación de la misma. |
| tipoFinanciacion : tipoFinanciacion  Private   Tipología de financiación utilizada por la entidad en la convocatoria. Es una FK a la tabla "tipo financiación". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [0..\*] | Target: Public (Class) TipoFinanciación    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [0..\*] | Target: Public (Class) FuenteFinanciacion    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProyectoPresupuesto    Cardinality:  [0..\*] | Target: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [1..\*] |

### Entidad Entidad gestora de una convocatoria: "ConvocatoriaEntidadGestora"

Entidad gestora de la convocatoria.  Se dispone de una tabla si bien a nivel de interface solo se permite añadir una única entidad gestora a la convocatoria.  El SGI no dispone de un repositorio de entidades, las entidades (empresas) siempre deberán ser referencias al sistema de gestión de empresas corporativo con el que se integra el SGI. 

|  |
| --- |
| **UTGOING STRUCTURAL RELATIONSHIPS** |
| Aggregation from  ConvocatoriaEntidadGestora to  Empresa   [ Direction is 'Source -> Destination'. ] |
| Aggregation from  ConvocatoriaEntidadGestora to  EmpresaEconomica   [ Direction is 'Source -> Destination'. ] |
| Generalization from  ConvocatoriaEntidadGestora to  Entidad   [ Direction is 'Source -> Destination'. ] |

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece la entidad gestora. Es una FK a la tabla "convocatoria". |
| empresaRef : String  Private   Referencia o Identificador de la entidad (empresa) en el sistema de gestión de empresas corporativo. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaEntidadGestora    Cardinality:  [0..1] |

### Entidad Fases de una convocatoria: "ConvocatoriaFase"

Fases o plazos generales de la convocatoria (teniendo en cuenta que los periodos de justificación y de seguimiento científico tendrán sus propias tablas). La disponibilidad de los tipos de fase es dependiente del modelo de ejecución al que se vincula la convocatoria. Las fases pueden registrarse a pasado o a futuro. Si se registran a futuro podrán conllevar la generación de un comunicado 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Convocatoria a la que pertenece la fase. Es una FK a la tabla "convocatoria". |
| fechaFin : Timestamp  Private   Fecha de fin de la fase definida para la convocatoria. Se expresa en formato fecha + hora. |
| fechaInicio : Timestamp  Private   Fecha de inicio de la fase definida para la convocatoria. Se expresa en formato fecha + hora. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoFase : TipoFase  Private   Identificador del tipo de fase. Es una FK a la tabla "tipo fase" incluida en el modelo lógico "CSP Modelo ejecución". Los tipos de fase disponibles para la convocatoria son dependientes del modelo de ejecución bajo el que se crea. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaFase    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [1] | Target: Public (Class) ConvocatoriaFase    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoFase    Cardinality:  [1] | Target: Public (Class) ConvocatoriaFase    Cardinality:  [0..\*] |

### Entidad Observaciones de la fase de una convocatoria: "ConvocatoriaFasesObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones asociadas a una fase de una convocatoria. Es un dato opcional y se introduce a través de un campo de texto libre.

| **ATTRIBUTES** |
| --- |
| convocatoriaFase : ConvocatoriaFase  Private  Fase de la convocatoria con la que se corresponden las observaciones. Es una FK a la tabla "ConvocatoriaFase". |
| lang : String  Private  Identificador del idioma en el que está almacenado el registro. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones de una fase de una convocatoria, recogido en el idioma indicado por el campo "lang". Las observaciones sobre una fase de una convocatoria es una información opcional y se introduce a través de una campo de texto libre |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaFaseObservaciones  Cardinality:  [0..\*] | Target: Public (Class) ConvocatoriaFase  Cardinality:  [1] |

### Entidad Hitos de una convocatoria: "ConvocatoriaHito"

Hitos de la convocatoria. Se define hito de forma genérica como cualquier acontecimiento/evento que resulte de interés mantener identificado en el historial de la convocatoria. La disponibilidad de los tipos de hito es dependiente del modelo de ejecución al que se vincula la convocatoria. Los hitos pueden registrarse a pasado o a futuro. Si se registran a futuro podrán conllevar la generación de un comunicado. 

|  |
| --- |
| **ATTRIBUTES** |
| aviso : ConvocatoriaHitoAviso  Private   Flag que indica si el hito lleva asociado la generación de un comunicado (que se remitiría vía mail de forma automática por el SGI). |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el hito. Es un FK a la tabla "convocatoria". |
| fecha : date  Private   Fecha en la que se produce el hito. Podrá ser una fecha a pasado o a futuro. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoHito : tipoHito  Private   Identificador del tipo de hito vinculado a la convocatoria. Es una FK a la tabla "tipo hito". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaHito    Cardinality:  [1] | Target: Public (Class) ConvocatoriaHitoAviso    Cardinality:  [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaHito    Cardinality:  [0..\*] | Target: Public (Class) TipoHito    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaHito    Cardinality:  [0..\*] |

### Entidad Comentario de un hito de una convocatoria: "ConvocatoriaHitoComentario"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el comentario de un hito de una convocatoria. El comentario de un hito es un campo opcional y se recoge a través de un campo de texto libre.

| **ATTRIBUTES** |
| --- |
| convocatoriaHito : ConvocatoriaHito  Private  Identificador del hito de convocatoria al que pertenece el comentario. Es una FK a la tabla "convocatoria hito". |
| lang : String  Private  Identificador del idioma en el que se almacena el comentario. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : Strig  Private  Valor del comentario recogido en el idioma indicado por el campo "lang". El cometario se recoge a través de un campo de texto y es de libre introducción. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaHito  Cardinality:  [1] | Target: Public (Class) ConvocatoriaHitoComentario  Cardinality:  [0..\*] |

### Entidad Avisos de un hito de convocatoria: "ConvocatoriaHitoAviso"

Configuración del aviso asociado a un hito de una convocatoria. Solo los hitos creados sobre una fecha futura podrán originar comunicado. Los comunicados se generan automáticamente mediante tarea programada (modelo lógico SGI TP) y se remiten vía mail. En el caso de los hitos de convocatorias se permite configurar, a nivel de comunicado, si éste se debe remitir a los/as IP de las solicitudes y proyectos derivados de la convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| comunicadoRef : String  Private   Referencia o identificador del comunicado que se generará asociado al hito de convocatoria. La tabla "comunicado" está incluida en el modelo lógico SGI COM. Al ser una tabla de otro servicio no se establece FK. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| incluirIPsProyecto : boolean  Private   Flag que indica si el comunicado debe remitirse a los/las IP de lor proeyctos asociados a la convocatoria. El valor de este flag lo establece la unidad de gestión a través del interface de usuario en la propia pantalla de creación/modificación del hito. |
| incluirIPsSolicitud : boolean  Private   Flag que indica si el comunicado debe remitirse a los/las IP de las solicitudes asociadas a la convocatoria. El valor de este flag lo establece la unidad de gestión a través del interface de usuario en la propia pantalla de creación/modificación del hito. |
| tareaProgramadaRef : String  Private   Referencia o identificador de la tarea programada que gestionará el envío de los mails asociados al comunicado. La entidad asociada ("bean method task") está incluida en el modelo lógico SGI TP. Al ser una entidad de un servicio independiente a CSP no se establece una FK. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaHito    Cardinality:  [1] | Target: Public (Class) ConvocatoriaHitoAviso    Cardinality:  [0..1] |

### Entidad Partidas presupuestarias de una convocatoria: "ConvocatoriaPartida"

Partidas o aplicaciones presupuestarias de la convocatoria. Si bien el SGI permite su definición a nivel de convocatoria será en los proyectos finalmente derivados de la convocatoria donde tengan utilidad. Las partidas introducidas a nivel de convocatoria son heredadas por los proyectos derivados de la misma. 

|  |
| --- |
| **ATTRIBUTES** |
| codigo : String  Private   Código alfanumérico que identifica a la partida o aplicación presupuestaria. A nivel de interface de usuario se implementa un patrón para validar su formato (tabla "configuración" campo "plantilla partida presupuestaria").   Se informará de este campo cuando la variable de configuración "partida\_presupuestaria\_SGE" tenga valor "False" lo que significa que las partidas presupuestarias se van a dar de alta en el SGI y no se van a leer del SGE. |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece la partida. Es una FK a la tabla "convocatoria". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoPartida : TipoPartida  Private   Tipo de la partida de acuerdo al enumerado "tipo partida". |
| partidaRef: String Private  Identificador de la partida presupuestaria del SGE. Se informará de este campo cuando la variable de configuración "partida\_presupuestaria\_SGE" tenga valor "True" lo que significa que las partidas presupuestarias no se van a dar de alta en el SGI sino que vendrán informadas de la integración con el SGE. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPartida | Target: Public (Enumeration) TipoPartida |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPartida    Cardinality:  [0..\*] |

### Entidad Descripción de una partida de una convocatoria: "ConvocatoriaPartidaDescripción"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, la descripción de las partidas de las convocatorias. La posibilidad de introducir la descripción de las partidas de la convocatoria es dependiente del valor del parámetro de configuración "partida\_presupuestaria\_SGE". Si este parámetro toma el valor "false", las partidas se introducirán manualmente en el SGI, pasando a poder informarse el campo descripción. Aún así será un campo opcional.

| **ATTRIBUTES** |
| --- |
| convocatoriaPartida : ConvocatoriaPartida  Private  Identificador de la partida de una convocatoria con la que está asociada la descripción. Es una FK a la tabla "ConvocatoriaPartidaDescripcion". |
| lang : String  Private  Identificador del idioma con el que se corresponde el valor del campo descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo descripción, almacenado en el idioma indicado por el campo "lang". El campo descripción es un campo de texto libre y su introducción es opcional |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPartida  Cardinality:  [1] | Target: Public (Class) ConvocatoriaPartidaDescripcion  Cardinality:  [0..\*] |

### Entidad Calendario de periodos de justificación de una convocatoria: "ConvocatoriaPeriodoJustificacion"

Periodos de justificación económica establecidos por la convocatoria. Son heredados por los proyectos derivados de la convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el periodo de justificación. Es una FK a la tabla "convocatoria". |
| fechaFinPresentacion : Timestamp  Private   Fecha en la que finaliza el plazo disponible para presentar a la entidad la documentación de justificación económica correspondiente al periodo. Se recoge en formato fecha + hora. |
| fechaInicioPresentacion : Timestamp  Private   Fecha en la que comienza el plazo disponible para presentar a la entidad la documentación de justificación económica correspondiente al periodo. Se recoge en formato fecha + hora. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| mesFinal : Integer  Private   Mes final del periodo para el que se deben justificar los gastos ejecutados en los proyectos derivados de la convocatoria. Al estar en fase de convocatoria aún no es posible establecer fechas pues no se han iniciado los proyectos. Los periodos se expresan en meses siendo el mes inicial y el final de los mismos relativos a la duración que tengan los proyectos finalmente derivados de la convocatoria. |
| mesInicial : Integer  Private   Mes inicial del periodo para el que se deben justificar los gastos ejecutados en los proyectos derivados de la convocatoria. Al estar en fase de convocatoria aún no es posible establecer fechas pues no se han iniciado los proyectos. Los periodos se expresan en meses siendo el mes inicial y el final de los mismos relativos a la duración que tengan los proyectos finalmente derivados de la convocatoria. |
| numPeriodo : Integer  Private    Número del periodo de acuerdo a un orden secuencial establecido en función del mes de inicio de los periodos de seguimiento recogidos para la convocatoria. Es asignado de manera automática por el sistema. |
| tipoJustificacion : TipoJustificacion  Private   Tipo del periodo de justificación de acuerdo al enumerado "tipo justificación". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoJustificacion | Target: Public (Enumeration) TipoJustificacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoJustificacion    Cardinality:  [0..\*] |

### Entidad Observaciones de un periodo de justificación de una convocatoria: "ConvocatoriaPeriodoJustificacionObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones de un periodo de justificación de una convocatoria. Las observaciones son un campo opcional y se recoge a través de un campo de texto libre.

| **ATTRIBUTES** |
| --- |
| convocatoriaPeriodoJustificacion : ConvocatoriaPeriodoJustificacion  Private  Identificador del perido de justificación con el que se corresponden las observaciones. Es una FK a la tabla "ConvocatorioPeriodoJustificacion" |
| lang : String  Private  Identificador del idioma en el que está recogido el valor del campo observaciones. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones. Las observaciones de un periodo de seguimiento son opcionales. El valor está expresado en el idioma indicado por el campo "lang" |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoJustificacion  Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoJustificacionObservaciones  Cardinality:  [0..\*] |

### Entidad Calendario de periodos de seguimiento científico de una convocatoria: "ConvocatoriaPeriodoSeguimientoCientifico"

Periodos de seguimiento científico establecidos para la convocatoria. Son heredados por los proyectos derivados de la convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private   Identificador de la convocatoria a la que pertenece el periodo de seguimiento. Es una FK a la tabla convocatoria. |
| fechaFinPresentacion : Timestamp  Private   Fecha en la que finaliza el plazo disponible para presentar a la entidad la documentación de justificación científico-técnica correspondiente al periodo de seguimiento. Se recoge en formato fecha + hora. |
| fechaInicioPresentacion : Timestamp  Private   Fecha en la que comienza el plazo disponible para presentar a la entidad la documentación de justificación científico-técnica correspondiente al periodo de seguimiento. Se recoge en formato fecha + hora. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| mesFinal : Integer  Private   Mes final del periodo de seguimiento, entendiendo éste como el periodo dentro de la duración total de los proyectos derivados de la convocatoria cuya ejecución se debe justificar en este periodo de seguimiento. Al estar en fase de convocatoria aún no es posible establecer fechas pues no se han iniciado los proyectos. Los periodos se expresan en meses siendo el mes inicial y el final de los mismos relativos a la duración que tengan los proyectos finalmente derivados de la convocatoria. |
| mesInicial : Integer  Private   Mes inicial del periodo de seguimiento, entendiendo éste como el periodo dentro de la duración total de los proyectos derivados de la convocatoria cuya ejecución se debe justificar en este periodo de seguimiento. Al estar en fase de convocatoria aún no es posible establecer fechas pues no se han iniciado los proyectos. Los periodos se expresan en meses siendo el mes inicial y el final de los mismos relativos a la duración que tengan los proyectos finalmente derivados de la convocatoria. |
| numPeriodo : Integer  Private   Número del periodo de acuerdo a un orden secuencial establecido en función del mes de inicio de los periodos de seguimiento recogidos para la convocatoria. Es asignado de manera automática por el sistema. |
| tipoSeguimiento : TipoSeguimiento  Private   Tipo del periodo de seguimiento de acuerdo al enumerado "tipo seguimiento" |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoSeguimientoCientifico | Target: Public (Enumeration) TipoSeguimiento |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoSeguimientoCientifico    Cardinality:  [0..\*] |

### Entidad Observaciones de un periodo de seguimiento científico de una convocatoria: "ConvocatoriaPeriodoSeguimientoCientificoObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones de los periodos de seguimiento científico de una convocatoria. Las observaciones de los periodos de seguimiento científico es un campo de texto libre y opcional.

| **TTRIBUTES** |
| --- |
| convocatoriaPeriodoSeguimientoCientifico : ConvocatoriaPeriodoSeguimientoCientifico  Private  Identificador de la relación convocatoria-periodo de seguimiento científico a la que pertenece la descripción. Es una FK a la tabla "ConvocatoriaPeriodoSeguimientoCientifico" |
| lang : String  Private  Identificador del idioma con el que se corresponde el valor del campo observaciones. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones de un periodo de seguimiento científico de una convocatoria. Está almacenado en el idioma indicado por el campo lang. El campo observaciones es un texto libre y opcional |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoSeguimientoCientifico  Cardinality:  [1] | Target: Public (Class) ConvocatoriaPeriodoSeguimientoCientificoObservaciones  Cardinality:  [0..\*] |

### Entidad Configuración de documentos requeridos en las solicitudes de una convocatoria: "DocumentoRequeridoSolicitud"

Documentos que serán requeridos por el SGI para que el personal investigador puede pasar una solicitud a estado "solicitada". 

Los documentos requeridos son configurados por la unidad de gestión sobre cada convocatoria (apartado configuración solicitudes). Los documentos requeridos se especifican en base a los tipos de documentos definidos en el modelo de ejecución. 

|  |
| --- |
| **ATTRIBUTES** |
| configuracionSolicitud : ConfiguracionSolicitud  Private   Identificador de la configuración de solicitud, que a su vez contiene el identificador de la convocatoria, con la que se corresponde el documento requerido. Es una FK sobre la tabla "configuración solicitud". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoDocumento : TipoDocumento  Private   Identificador del tipo de documento que se requerirá en las solicitudes presentadas por el personal investigador. Los tipos de documento disponibles para marcar como requeridos deben estar asociados al tipo de fase configurada como fase de presentación de solicitudes para la convocatoria (campo "fase presentación solicitudes" de la tabla "configuración solicitud"). Es una FK a la tabla "tipo documento". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConfiguracionSolicitud    Cardinality:  [1] | Target: Public (Class) DocumentoRequeridoSolicitud    Cardinality:  [0..\*] |

### Entidad Observaciones de un documento requerido de una solicitud de convocatoria: "DocumentoRequeridoSolicitudObservaciones"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, las observaciones asociadas a un documento requerido en las solicitudes de una convocatoria. Estas observaciones se recogen a través de un campo de texto y son opcionales.

| **ATTRIBUTES** |
| --- |
| documentoRequeridoSolicitud : DocumentoRequeridoSolicitud  Private  Identificador del documento requerido en la configuración de solicitudes de una convocatoria con el que se corresponden las observaciones. Es una FK a la tabla "DocumentoRequeridoSolicitud" |
| lang : String  Private  Identificador del idioma en el que se expresan las observaciones acerca del documento requerido. Es un código de dos caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo observaciones, expresado en el idioma indicado por el campo "lang". Las observaciones del documento requerido son opcionales |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentoRequeridoSolicitud  Cardinality:  [1] | Target: Public (Class) DocumentoRequeridoSolicitudObservaciones  Cardinality:  [0..\*] |

### Entidad Fuentes de financiación: "FuenteFinanciacion"

Listado de fuentes de financiación. las fuentes de financiación se asocian a las entidades financiadoras de convocatorias y proyectos/contratos para clasificar la procedencia de los fondos. Una misma fuente de financiación podría ser compartida por la misma o varias entidades financiadoras en más de una convocatoria/proyecto/contrato. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private   Flag con el que se da cobertura al borrado lógico de los registros de esta tabla. Una fuente de financiación con el campo "activo" a "false" no estará disponible para ser asociada a ninguna entidad financiadora en convocatorias/proyectos. |
| fondoEstructural : Boolean  Private   Flag que identifica si la fuente de financiación procede o no de fondos estructurales europeos. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| tipoAmbitoGeografico : TipoAmbitoGeografico  Private   Campo que permite indicar el ámbito geográfico de la fuente de financiación. Es una FK a la tabla "tipo ámbito geográfico". |
| tipoOrigenFuenteFinanciacion : TipoOrigenFuenteFinanciacion  Private  Clasificación de la fuente de financiación de acuerdo a su origen. Es una FK a la tabla "tipo origen fuente financiación". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacion    Cardinality:  [0..\*] | Target: Public (Class) TipoOrigenFuenteFinanciacion    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion | Target: Public (Class) FuenteFinanciacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [0..\*] | Target: Public (Class) FuenteFinanciacion    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoAmbitoGeografico    Cardinality:  [1] | Target: Public (Class) FuenteFinanciacion    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) FuenteFinanciacion   Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacionDescripcion  Cardinality: [0..\*] | Target: Public (Class) FuenteFinanciacion   Cardinality: [1] |

### Entidad Nombre de la fuente de financiación: "FuenteFinanciacionNombre"

Entidad para almacenar el nombre identificativo de la fuente de financiación en todos los idiomas soportados por la aplicación. Es obligatorio que una fuente de financiación tenga un nombre, al menos en uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| fuenteFinanciacion : FuenteFinanciacion Private  Identificador de la fuente de financiación a la que pertenece el nombre. Es una FK a la tabla "fuente financiación". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre identificativo de la fuente de financiación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio de la fuente de financiación en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) FuenteFinanciacion   Cardinality: [1] |

### Entidad Descripción de la fuente de financiación: "FuenteFinanciaciónDescripción"

Entidad para almacenar la descripción de la fuente de financiación en todos los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| fuenteFinanciacion : FuenteFinanciacion Private  Identificador de la fuente de financiación a la que pertenece la descripción. Es una FK a la tabla "fuente financiación". |
| lang : String Private  Identifica el idioma en el que está almacenada la descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción de la fuente de financiación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacionDescripcion  Cardinality: [0..\*] | Target: Public (Class) FuenteFinanciacion   Cardinality: [1] |

### Entidad Planes o programas de investigación: "Programa"

Listado de planes de investigación disponibles para la gestión de convocatorias y proyectos. Los planes de investigación se implementan con una estructura jerárquica de árbol, por lo que esta tabla dispone de una FK a la propia tabla. Cada plan de investigación estará formado por un árbol de programas y subprogramas de forma libre. El elemento raíz del árbol es el que da nombre al plan de investigación. Con el objetivo de ofrecer la mayor versatilidad posible en la definición de los posibles planes de investigación, no existe ninguna limitación en el número de niveles de cada uno de los planes creados. El árbol de programas del plan podrá tener todos los niveles necesarios (programas, subprogramas, modalidad, submodalidad, topic, etc.), sin limitar ni el número de elementos de cada nivel ni que todos los elementos hayan de tener el mismo número subniveles. 

Una entidad puede participar en una convocatoria cubriendo cualquier programa del plan, en este caso la entidad convocante estaría vinculada al nodo raíz del árbol que represente al plan. Una entidad también podría estar asociada a un programa, subprograma o modalidad concretos dentro del plan de investigación. En este caso la entidad se vinculará a un nodo de un nivel interior del árbol del plan de investigación. Las solicitudes y proyectos derivados de la convocatoria deberán estar vinculados a un nodo hijo a partir de los establecidos por la convocatoria para cada entidad convocante. Es decir, la convocatoria restringe los programas, subprogramas, modalidades, topics, etc. que estarán disponibles para las solicitudes y proyectos derivados de la convocatoria. 

Los planes de investigación son configurables a través del interface de usuario. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private   Flag con el que se da cobertura al borrado lógico de los registros de esta tabla. Un programa con el flag "activo" a "false" no estará disponible para ser seleccionado en convocatorias/proyectos. Si un elemento del árbol no está activo no estará disponible ni el propio elemento ni ninguno de sus descendientes. Si el elemento no activo es el nodo raíz del árbol el será el plan de investigación al completo el que no esté disponible. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| padre : Programa  Private   Los planes de investigación se implementan con una estructura de árbol jerárquico. Este campo establece la jerarquía del registro actual con su superior. El registro para el que este campo tome el valor "null" será el nodo raíz y será el que otorgue el nombre al plan de investigación.   Es una FK hacia esta misma tabla para implementar la estructura jerárquica. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Source -> Destination)     Un programa se podrá descomponer en cuantos niveles sea necesario. A nivel de IU se deberá implementar con una estructura de tipo árbol | |
| Source: Public (Class) Programa    Cardinality:  [1] | Target: Public (Class) Programa    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoEntidadConvocante    Cardinality:  [0..\*] | Target: Public (Class) Programa    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Solicitud | Target: Public (Class) Programa |
| Association (direction: Source -> Destination)     Un programa se podrá descomponer en cuantos niveles sea necesario. A nivel de IU se deberá implementar con una estructura de tipo árbol | |
| Source: Public (Class) Programa    Cardinality:  [1] | Target: Public (Class) Programa    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadConvocante    Cardinality:  [0..\*] | Target: Public (Class) Programa    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProgramaNombre  Cardinality: [1..\*] | Target: Public (Class) Programa   Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProgramaDescripcion  Cardinality: [0..\*] | Target: Public (Class) Programa   Cardinality: [1] |

### Entidad Nombre del programa: "ProgramaNombre"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el nombre identificativo del programa, el que se mostrará en la visualización del árbol del plan de investigación en la gestión de convocatorias y proyectos en los idiomas soportados por la aplicación. El nombre es un campo de texto y es de obligada cumplimentación en la creación de un nuevo programa.

|  |
| --- |
| **ATTRIBUTES** |
| programa : Programa Private  Identificador del elemento del árbol de programas a la que pertenece el nombre. Es una FK a la tabla "programa". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del plan investigación/programa/subprograma/modalidad en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 200 caracteres. Es un campo obligatorio del elemento en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProgramaNombre  Cardinality: [1..\*] | Target: Public (Class) Programa   Cardinality: [1] |

### Entidad Descripción del programa: "ProgramaDescripción"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, la descripción de un programa de investigación. Esta descripción es un campo de texto y es opcional.

|  |
| --- |
| **ATTRIBUTES** |
| programa : Programa Private  Identificador del elemento del árbol de programas a la que pertenece la descripción. Es una FK a la tabla "programa". |
| lang : String Private  Identifica el idioma en el que está almacenada la descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del plan investigación/programa/subprograma/modalidad en el idioma indicado por el campo "lang". Es un campo de tipo CLOB. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProgramaDescripcion  Cardinality: [0..\*] | Target: Public (Class) Programa   Cardinality: [1] |

### Entidad Requisitos de convocatoria para los miembros de equipo: "RequisitoEquipo"

Requisitos que establece la convocatoria para cualquier persona que participe en el equipo de proyecto (que no desempeñe un rol principal, IP, cuyos requisitos se establecen en la tabla "requisitos IP"). Los requisitos aquí establecidos se aplicarán sobre todos los miembros del equipo de proyecto de las solicitudes y proyectos derivados de la convocatoria (que no tengan un rol catalogado como "principal"). 

Solamente existirá un registro en esta tabla por cada convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private    Convocatoria con la que se corresponden los requisitos. Es una FK a la tabla "convocatoria" |
| edadMaxima : Integer  Private    Edad máxima que pudiera requerir la convocatoria y que aplicará para cualquier miembro del equipo (que no tenga un rol catalogado como "principal", IP). |
| fechaMaximaCategoriaProfesional : Timestamp  Private   Fecha tope máxima en la que se debe haber alcanzado cualquiera de las categorías profesionales admitidas/exigidas por la convocatoria. Las categorías sobre las que aplica esta fecha están recogidas en la tabla "requisito equipo categoría".   Esta fecha solo se podrá establecer si el flag "vinculación universidad" está marcado a "true". |
| fechaMaximaNivelAcademico : Timestamp  Private    Fecha tope máxima en la que se debe haber obtenido cualquiera de los niveles académicos admitidos por la convocatoria. Los niveles académicos sobre los que aplica esta fecha están recogidos en la tabla "requisito equipo nivel académico". |
| fechaMinimaCategoriaProfesional : Timestamp  Private   Fecha tope mínima en la que se debe haber alcanzado cualquiera de las categorías profesionales admitidas/exigidas por la convocatoria. Las categorías sobre las que aplica esta fecha están recogidas en la tabla "requisito equipo categoría".   Esta fecha solo se podrá establecer si el flag "vinculación universidad" está marcado a "true". |
| fechaMinimaNivelAcademico : Timestamp  Private   Fecha tope mínima en la que se debe haber obtenido cualquiera de los niveles académicos admitidos por la convocatoria. Los niveles académicos sobre los que aplica esta fecha están recogidos en la tabla "requisito equipo nivel académico". |
| id : Long  Private    Identificador único de la tabla. Secuencia. Clave primaria. |
| numMaximoCompetitivosActivos : Integer  Private   Recoge el límite máximo de proyectos competitivos con participación actual que establece la convocatoria para poder optar a la misma. Esta restricción aplicará sobre el total de los proyectos acumulados por todos los miembros del equipo que no tengan un rol principal (IP). |
| numMaximoNoCompetitivosActivos : Integer  Private   Recoge el límite máximo de proyectos no competitivos con participación actual que establece la convocatoria para poder optar a la misma. Esta restricción aplicará sobre el total de los proyectos acumulados por todos los miembros del equipo que no tengan un rol principal (IP). |
| numMinimoCompetitivos : Integer  Private   Recoge el número mínimo de proyectos competitivos en los que se ha debido participar, con independencia de las fechas, para poder optar a la misma. Esta restricción aplicará sobre el total de los proyectos acumulados por todos los miembros del equipo que no tengan un rol principal (IP). |
| numMinimoNoCompetitivos : Integer  Private   Recoge el número mínimo de proyectos no competitivos en los que se ha debido participar, con independencia de las fechas, para poder optar a la misma. Esta restricción aplicará sobre el total de los proyectos acumulados por todos los miembros del equipo que no tengan un rol principal (IP). |
| ratioSexo : Integer  Private    Junto con el campo "sexo" permitirá recoger las limitaciones que establezca la convocatoria respecto a la composición, en términos de igualdad, del equipo. En este campo se recogerá el porcentaje de miembros exigido que deben tener el sexo especificado en el campo "sexo". |
| sexoRef : String  Private   Junto con el campo "ratio sexo" permitirá recoger las limitaciones que establezca la convocatoria respecto a la composición, en términos de igualdad, del equipo. En este campo se recogerá el sexo en base al que se expresa el ratio mínimo exigido. El valor a almacenar en este campo será la referencia al tipo de sexo utilizado en el sistema de gestión de personas corporativo (modelo SGP Personas). |
| vinculacionUniversidad : Boolean  Private    Flag que identifica si la convocatoria exige que los miembros de equipo deban tener o nor contrato profesional con la Universidad.    Si este flag toma valor "true" se deberán especificar la/s categoría/s exigidas (tabla "requisito equipo categoría"). |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [1] | Target: Public (Class) RequisitoEquipoNivelAcademido    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [1] | Target: Public (Class) RequisitoEquipoCategoria    Cardinality:  [0..\*] |

### Entidad Otros requisitos de convocatoria para los miembros de equipo: "RequisitoEquipoOtrosRequisitos"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, los requisitos adicionales que deba cumplir el equipo de proyecto, de acuerdo a la convocatoria. Estos requisitos se recogen a través de un campo de texto y son de libre introducción. Es un dato informativo, el SGI no realiza ninguna comprobación automática sobre el cumplimiento por parte del equipo de los requisitos aquí descritos.

| **ATTRIBUTES** |
| --- |
| requisitoEquipo : RequisitoEquipo  Private  Identificador de los requisitos equipo a los que se vincula el campo "otros requisitos".  Es una FK a la tabla "RequisitoEquipo". |
| lang : String  Private  Identificador del idioma en el que está almacenado el registro. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "otros requisitos" en el idioma indicado por el campo "lang".  El campo "otros requisitos" para el equipo es un campo de texto y su introducción es opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipoOtrosRequisitos  Cardinality:  [0..\*] | Target: Public (Class) RequisitoEquipo  Cardinality:  [1..] |

### Entidad Categorías en convocatoria para los miembros de equipo: "RequisitoEquipoCategoria"

Categorías profesionales admitidas por una convocatoria determinada para cualquier persona que participe en el equipo de proyecto y que no ocupe un rol principal (IP) (los requisitos de IP se recogen en la tabla "requisitos IP"). 

|  |
| --- |
| **ATTRIBUTES** |
| categoriaProfesionalRef : String  Private    Referencia o identificador de la categoría profesional exigida por la convocatoria. El listado de categorías disponibles procede de la integración con el sistema de gestión corporativo correspondiente. En este campo se almacena el identificador de la categoría profesional en el sistema de gestión corporativo (modelado incluido en el ESB SGP). |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| requisitoEquipo : RequisitoEquipo  Private    Identificador de la tabla requisito equipo, que a su vez contiene la convocatoria, a la que se acoja la categoría profesional. Es una FK a la tabla "requisito equipo". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [1] | Target: Public (Class) RequisitoEquipoCategoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) CategoriaProfesional | Target: Public (Class) RequisitoEquipoCategoria |

### Entidad Niveles académicos en convocatoria para los miembros de equipo: "RequisitoEquipoNivelAcademico"

Niveles académicos admitidos por una convocatoria determinada que debe tener cualquier persona que participe en el equipo de proyecto y que no ocupe un rol principal (IP)(los requisitos de IP se recogen en la tabla "requisitos IP"). 

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| nivelAcademicoRef : String  Private   Referencia o identificador del nivel académico exigido por la convocatoria. El listado de niveles académicos disponibles procede de la integración con el sistema de gestión corporativo correspondiente. En este campo se almacena el identificador del nivel académico en el sistema de gestión corporativo (modelado incluido en el ESB SGP). |
| requisitoEquipo : RequisitoEquipo  Private    Identificador de la tabla requisito equipo, que a su vez contiene la convocatoria, a la que se acoja el nivel académico. Es una FK a la tabla "requisito equipo". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipoNivelAcademido | Target: Public (Class) NivelAcademico |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoEquipo    Cardinality:  [1] | Target: Public (Class) RequisitoEquipoNivelAcademido    Cardinality:  [0..\*] |

### Entidad Requisitos de convocatoria para el rol IP: "RequisitoIP"

Requisitos que establece la convocatoria para la persona solicitante. Los requisitos aquí establecidos se aplicarán sobre la el/la solicitante de las solicitudes asociadas a la convocatoria y sobre el/la IP de los proyectos derivados. Solamente existirá un registro en esta tabla por cada convocatoria. 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoria : Convocatoria  Private    Identificador de la convocatoria para la que establecen los requisitos IP. Es una FK a la tabla "convocatoria" |
| edadMaxima : Integer  Private   Edad máxima que pudiera exigir la convocatoria para poder optar a la misma. |
| fechaMaximaCategoriaProfesional : Timestamp  Private   Fecha tope máxima en la que se debe haber alcanzado cualquiera de las categorías profesionales admitidas/exigidas por la convocatoria. Las categorías sobre las que aplica esta fecha están recogidas en la tabla "requisito IP categoría".   Esta fecha solo se podrá establecer si el flag "vinculación universidad" está marcado a "true". |
| fechaMaximaNivelAcademico : Timestamp  Private   Fecha tope máxima en la que se debe haber obtenido cualquiera de los niveles académicos admitidos por la convocatoria. Los niveles académicos sobre los que aplica esta fecha están recogidas en la tabla "requisito IP nivel académico". |
| fechaMinimaCategoriaProfesional : Timestamp  Private   Fecha tope mínima en la que se debe haber alcanzado cualquiera de las categorías profesionales admitidas/exigidas por la convocatoria. Las categorías sobre las que aplica esta fecha están recogidas en la tabla "requisito IP categoría".   Esta fecha solo se podrá establecer si el flag "vinculación universidad" está marcado a "true". |
| fechaMinimaNivelAcademico : Timestamp  Private   Fecha tope mínima en la que se debe haber obtenido cualquiera de los niveles académicos admitidos por la convocatoria. Los niveles académicos sobre los que aplica esta fecha están recogidas en la tabla "requisito IP nivel académico". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| numMaximoCompetitivosActivos : Integer  Private   Recoge el límite máximo de proyectos competitivos con participación como IP a fecha actual que establece la convocatoria para poder optar a la misma. |
| numMaximoIP : Integer  Private    Número máximo de investigadores principales que pudiera requerir la convocatoria. |
| numMaximoNoCompetitivosActivos : Integer  Private   Recoge el límite máximo de proyectos no competitivos con participación como IP a fecha actual que establece la convocatoria para poder optar a la misma. |
| numMinimoCompetitivos : Integer  Private    Recoge el número mínimo de proyectos competitivos con participación como IP, independientemente de las fechas de participación, que establece la convocatoria para poder optar a la misma. |
| numMinimoNoCompetitivos : Integer  Private    Recoge el número mínimo de proyectos no competitivos con participación como IP, independientemente de las fechas de participación, que establece la convocatoria para poder optar a la misma. |
| sexoRef : String  Private   Sexo de la persona solicitante (IP de los proyectos derivados) al que pudiera estar limitado la convocatoria.   El valor que se almacena en este campo es una referencia al tipo de sexo utilizado en el sistema de gestión de personas corporativo (modelo lógico ESB SGP). |
| vinculacionUniversidad : Boolean  Private   Flag que identifica si la convocatoria exige que la persona solicitante/IP deba o no tener contrato profesional con la Universidad.    Si este flag toma valor "true" se deberán especificar la/s categoría/s exigidas (tabla "requisito IP categoría"). |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [1] | Target: Public (Class) RequisitoIPCategoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [1] | Target: Public (Class) RequisitoIPNivelAcademico    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [0..1] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP | Target: Public (Class) Sexo |

### Entidad Otros requisitos de convocatoria para el rol IP: "RequisitoIPOtrosRequisitos"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, los requisitos adicionales que deba cumplir la persona que actúe como IP, de acuerdo a la convocatoria. Estos requisitos se recogen a través de un campo de texto y son de libre introducción. Es un dato informativo, el SGI no realiza ninguna comprobación automática sobre el cumplimiento por parte de las personas solicitantes de los requisitos aquí descritos.

| **ATTRIBUTES** |
| --- |
| requisitoIP : RequisitoIP  Private  Identificador de los requisitos IP a los que se vincula el campo "otros requisitos".  Es una FK a la tabla "RequisitoIP". |
| lang : String  Private  Identificador del idioma en el que está almacenado el registro. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo "otros requisitos" en el idioma indicado por el campo "lang".  El campo "otros requisitos" para IP es un campo de texto y su introducción es opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP  Cardinality:  [1] | Target: Public (Class) RequisitoIPOtrosRequisitos  Cardinality:  [0..\*] |

### Entidad Categorías en convocatoria para el rol IP: "RequisitoIPCategoria"

 Categorías profesionales admitidas por una convocatoria determinada que debe tener la persona solicitante (IP del proyecto resultante) para poder optar a la misma. 

|  |
| --- |
| **ATTRIBUTES** |
| categoriaProfesionalRef : String  Private    Referencia o identificador de la categoría profesional exigida por la convocatoria. El listado de categorías disponibles procede de la integración con el sistema de gestión corporativo correspondiente. En este campo se almacena el identificador de la categoría profesional en el sistema de gestión corporativo (modelado incluido en el ESB SGP). |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| requisitoIP : RequisitoIP  Private   Identificador de la tabla requisito IP, que a su vez contiene la convocatoria, a la que se acocia la categoría profesional. Es una FK a la tabla "requisito IP". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIPCategoria    Cardinality:  [0..\*] | Target: Public (Class) CategoriaProfesional    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [1] | Target: Public (Class) RequisitoIPCategoria    Cardinality:  [0..\*] |

### Entidad Nivel académico en convocatoria para el rol IP: "RequisitoIPNivelAcademico"

Niveles académicos admitidos por una convocatoria determinada que debe tener la persona solicitante (IP del proyecto resultante) para poder optar a la misma. 

|  |
| --- |
| **ATTRIBUTES** |
| id : Long  Private   Identificador único de la tabla. Secuencia. Claver primaria. |
| nivelAcademicoRef : String  Private   Referencia o identificador del nivel académico exigido por la convocatoria. El listado de niveles académicos disponibles procede de la integración con el sistema de gestión corporativo correspondiente. En este campo se almacena el identificador del nivel académico en el sistema de gestión corporativo (modelado incluido en el ESB SGP). |
| requisitoIP : RequisitoIP  Private   Identificador de la tabla requisito IP, que a su vez contiene la convocatoria, a la que se acocia el nivel académico. Es una FK a la tabla "requisito IP". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIPNivelAcademico    Cardinality:  [0..\*] | Target: Public (Class) NivelAcademico    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RequisitoIP    Cardinality:  [1] | Target: Public (Class) RequisitoIPNivelAcademico    Cardinality:  [0..\*] |

### Entidad Listado de ámbitos geográfico: "TipoAmbitoGeografico"

Listado de ámbitos geográficos. Fuentes de financiación, convocatorias y proyectos se asocian a un ámbito geográfico. No dispone de configuración a través del interface de usuario. El listado de ámbitos geográficos debe ser definido en tiempo de implantación.  

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private  = True   Campo utilizado para dar soporte al borrado lógico de los registros de esta entidad. Un ámbito geográfico no activo no se está disponible para su selección a nivel de interface de usuario. |
| id : Long  Private   Identificador único del registro. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoAmbitoGeografico    Cardinality:  [1] | Target: Public (Class) FuenteFinanciacion    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) TipoAmbitoGeografico    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Proyecto    Cardinality:  [0..\*] | Target: Public (Class) TipoAmbitoGeografico    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoAmbitoGeograficoNombre  Cardinality: [1..\*] | Target: Public (Class) TipoAmbitoGeografico   Cardinality: [1] |

### Entidad Nombre del ámbito geográfico: "TipoAmbitoGeograficoNombre"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el nombre del tipo de ámbito geográfico. El tipo de ámbito geográfico es una  clasificación asociada a las fuentes de financiación, convocatorias y proyectos.  El nombre es un campo de texto y es obligatorio, al menos en un idioma.

|  |
| --- |
| **ATTRIBUTES** |
| tipoAmbitoGeografico : TipoAmbitoGeografico Private  Identificador del tipo de ámbito geográfico a la que pertenece el nombre. Es una FK a la tabla "tipo ámbito geográfico". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del tipo de ámbito geográfico en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del tipo de ámbito geográfico en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoAmbitoGeograficoNombre  Cardinality: [1..\*] | Target: Public (Class) TipoAmbitoGeografico   Cardinality: [1] |

### Entidad Tipos de financiación: "TipoFinanciación"

Listado de tipos de financiación. Los tipos de financiación se corresponden con los diferentes mecanismos a través de los que las entidades aportarán la financiación sobre convocatorias, proyectos/contratos. Posibles ejemplos de valores son subvención, préstamo, anticipo reembolsable. 

La configuración de los valores de esta tabla está disponible a través del interface de usuario. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private   Flag a través del que se implementa el borrado lógico de los registros de esta tabla. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaEntidadFinanciadora    Cardinality:  [0..\*] | Target: Public (Class) TipoFinanciación    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) TipoFinanciacion   Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoFinanciacionDescripcion  Cardinality: [0..\*] | Target: Public (Class) TipoFinanciacion   Cardinality: [1] |

### Entidad Nombre del tipo de financiación: "TipoFinanciaciónNombre"

Entidad para almacenar, en cada uno de los idiomas  soportados por la aplicación, el nombre del tipo de financiación. Los tipos de financiación permiten clasificar los diferentes mecanismos a través de los que las entidades/organismos  aportan la financiación para la ejecución de las actividades de investigación (proyectos/contratos). El nombre de los tipos de financiación es un campo de texto y es de introducción obligatoria en la creación de un nuevo tipo de financiación

|  |
| --- |
| **ATTRIBUTES** |
| tipoFinanciacion : TipoFinanciacion Private  Identificador del tipo de financiación a la que pertenece el nombre. Es una FK a la tabla "tipo financiación". |
| lang : String Private  Identifica el idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del tipo de financiación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del tipo de financiación en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) TipoFinanciacion   Cardinality: [1] |

### Entidad Descripción del tipo de financiación: "TipoFinanciaciónDescripción"

Entidad para almacenar, en cada uno de los idiomas  soportados por la aplicación, la descripción del tipo de financiación. Los tipos de financiación permiten clasificar los diferentes mecanismos a través de los que las entidades/organismos aportan la financiación para la ejecución de las actividades de investigación (proyectos/contratos). La descripción de los tipos de financiación es un campo opcional.

|  |
| --- |
| **ATTRIBUTES** |
| tipoFinanciacion : TipoFinanciacion Private  Identificador del tipo de financiación a la que pertenece la descripción. Es una FK a la tabla "tipo financiación". |
| lang : String Private  Identifica el idioma en el que está almacenada la descripción. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del tipo de financiación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoFinanciacionDescripcion  Cardinality: [0..\*] | Target: Public (Class) TipoFinanciacion   Cardinality: [1] |

### Entidad Tipos de origen para una fuente de financiación: "TipoOrigenFuenteFinanciacion"

Listado de tipos de origen para tipificación de las fuentes de financiación. La naturaleza de esta tipificación queda a elección de la Universidad de implantación. Un ejemplo de valores podría ser: público, privado. 

Es un listado configurable en tiempo de implantación para el que no se dispone de interface de usuario. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private    Flag a través del que se implementa el borrado lógico de los registros de esta tabla. Un tipo de origen de fuente de financiación con el campo "activo" a "false" no estará disponible para la creación/modificación de las fuentes de financiación. |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) FuenteFinanciacion    Cardinality:  [0..\*] | Target: Public (Class) TipoOrigenFuenteFinanciacion    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoOrigenFuenteFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) TipoOrigenFuenteFinanciacion   Cardinality: [1] |

### Entidad Nombre de los tipos de origen para una fuente de financiación: "TipoOrigenFuenteFinanciacionNombre"

Entidad para almacenar, en cada uno de los idiomas soportados por la aplicación, el nombre del tipo de origen de las fuentes de financiación. Este nombre identifica al tipo de origen y será el que se muestre en los listados en los que se utilice de tipo de origen de fuente de financiación. El nombre del tipo de origen es un campo de texto y debe de introducirse obligatoriamente para crear un nuevo tipo de origen de fuente de financiación.

|  |
| --- |
| **ATTRIBUTES** |
| tipoOrigenFuenteFinanciacion : TipoOrigenFuenteFinanciacion Private  Identificador  del tipo de origen de las fuentes de financiación a la que pertenece el nombre. Es una FK a la tabla "tipo origen fuente financiación". |
| lang : String Private  Identifica al idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del tipo de origen de las fuentes de financiación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del tipo de origen de las fuentes de financiación en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoOrigenFuenteFinanciacionNombre  Cardinality: [1..\*] | Target: Public (Class) TipoOrigenFuenteFinanciacion   Cardinality: [1] |

### Entidad Tipos de régimen de concurrencia: "TipoRegimenConcurrencia"

 Listado de los tipos de regímenes de concurrencia disponibles para clasificación de las convocatorias. La configuración de este listado no está disponible a través de interface gráfico. El listado debe ser definido en tiempo de implantación. 

|  |
| --- |
| **ATTRIBUTES** |
| activo : Boolean  Private  = True   Flag a través del que se implementa el borrado lógico de los registros de esta tabla. |
| id : Long  Private   Identificador único de la tabla.  Secuencia. Clave primaria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoRegimenConcurrencia    Cardinality:  [1] | Target: Public (Class) Proyecto    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Class) TipoRegimenConcurrencia    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoRegimenConcurrenciaNombre  Cardinality: [1..\*] | Target: Public (Class) TipoRegimenConcurrencia   Cardinality: [1] |

### Entidad Nombre del los tipos de régimen de concurrencia: "TipoRegimenConcurrenciaNombre"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre del tipo de régimen de concurrencia. Los tipos de régimen de concurrencia es una clasificación de las convocatorias.

|  |
| --- |
| **ATTRIBUTES** |
| tipoRegimenConcurrencia : TipoRegimenConcurrencia Private  Identificador del tipo de régimen de concurrencia a la que pertenece el nombre. Es una FK a la tabla "tipo regimen concurrencia". |
| lang : String Private  Identifica al idioma en el que está almacenado el nombre. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre identificativo del tipo de regimen de concurrencia en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 50 caracteres. Es un campo obligatorio del tipo de regimen de concurrencia en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoRegimenConcurrenciaNombre  Cardinality: [1..\*] | Target: Public (Class) TipoRegimenConcurrencia   Cardinality: [1] |

### Entidad Palabras clave de una convocatoria: "ConvocatoriaPalabraClave"

Palabras clave asociadas a la convocatoria. El catálogo de palabras clave común al SGI se implementa en la tabla "palabra clave" del ESB (modelo SGO) 

|  |
| --- |
| **ATTRIBUTES** |
| convocatoriaId : Long  Private   Identificador de la convocatoria a la que pertenece la palabra clave. Es una FK a la tabla "convocatoria". |
| id : Long  Private   Identificador único de la tabla. Secuencia. Clave primaria. |
| palabraClave : String  Private   Es una referencia a la tabla "palabra clave" del modelo ESB SGO. Al ser una tabla de un módulo independiente a CSP no se establece una FK. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPalabraClave    Cardinality:  [0..\*] | Target: Public (Class) Convocatoria    Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPalabraClave    Cardinality:  [0..\*] | Target: Public (Class) PalabraClave    Cardinality:  [1] |

### Entidad Configuración: "Configuracion"

 Tabla genérica para almacenar variables de configuración del SGI referentes al módulo de CSP. Cada campo representa un parámetro de configuración. 

|  |
| --- |
| **ATTRIBUTES** |
| formato\_partida\_presupuestaria : String  Private   Contiene la expresión regular que indica el formato de la partida presupuestaria. Se utiliza para aplicar la validación en el formulario de introducción de datos. |
| id : Long  Private   Clave primaria. Identificador de la tabla |
| plantilla\_partida\_presupuestaria : String  Private    Cadena de texto que representa el patrón con el que se debe introducir la partida presupuestaria  (ya que puede variar en cada implantación). Se utiliza para mostrar un tooltip informativo al usuario. |
| validacion\_\_clasificaciñon\_gastos : String  Private    Permite configurar el mecanismo que se utiliza en el apartado Ejecución económica para clasificar los gastos del SGE de acuerdo a los conceptos económicos del SGI.  Posibles valores:   * VALIDACION * CLASIFICACION * ELEGIBILIDAD |
| plantilla\_identificador\_justificacion : String  Private    Cadena de texto que representa el patrón con el que se debe introducir el identificador de la justificación (ya que puede variar en cada implantación). Se utiliza para mostrar un tooltip informativo al usuario. |
| formato\_identificador\_justificacion : String  Private   Contiene la expresión regular que indica el formato del identificador de justificación. Se utiliza para aplicar la validación en el formulario de introducción de datos. |
| dedicacion\_minima\_grupo : Integer Private  Contiene el valor que se utilizará para comprobar la dedicación parcial de un miembro a un grupo. Se validará que la dedicación parcial asignada a cualquier miembro sea mayor o igual que el valor indicado por este parámetro (salvo que el valor del parámetro sea 0 o null que se validará que la dedicación sea mayor que 0). |
| plantilla\_codInterno\_proyecto : String  Private    Cadena de texto que representa el patrón con el que se debe introducir el código interno de proyecto (ya que puede variar en cada implantación). Se utiliza para mostrar un tooltip informativo al usuario. |
| formato\_codInterno\_proyecto : String  Private   Contiene la expresión regular que indica el formato del código interno de proyecto. Se utiliza para aplicar la validación en el formulario de introducción de datos. |
| cardinalidad\_relacion\_sgi\_sge: Integer Private  Permite configurar la cardinalidad de la relación entre proyecto SGI y proyecto SGE.  Posibles valores:   * SGI\_1\_SGE\_1 * SGI\_1\_SGE\_N * SGI\_N\_SGE\_1 * SGI\_N\_SGE\_N   El valor "SGI\_1\_SGE\_1" se corresponde con el texto "Un proyecto SGI sólo puede asociarse a un identificador SGE (1:1)"  El valor "SGI\_1\_SGE\_N" se corresponde con el texto "Un proyecto SGI puede asociarse a diferentes identificadores SGE (1:n)"  El valor "SGI\_N\_SGE\_1" se corresponde con el texto "Diferentes proyectos SGI pueden estar asociados a un mismo identificador SGE (n:1)"  El valor "SGI\_N\_SGE\_N" se corresponde con el texto "Diferentes proyectos SGI pueden estar asociados a diferentes identificadores SGE (n:n)" |
| sge\_sincronizacion\_alta\_proyecto: Integer Private  Permite configurar si el alta del proyecto en el SGE se realiza de forma sincrona o de forma asíncrona.  Posibles valores:   * Sincrona * Asíncrona   El valor "SINCRONA" se corresponde con el texto "Sincrona"  El valor "ASINCRONA" se corresponde con el texto "Asíncrona" |
| sge\_sincronizacion\_modificacion\_proyecto: Integer Private  Permite configurar si la modificción del proyecto en el SGE se realiza de forma sincrona o de forma asíncrona.  Posibles valores:   * Sincrona * Asíncrona   El valor "SINCRONA" se corresponde con el texto "Sincrona"  El valor "ASINCRONA" se corresponde con el texto "Asíncrona" |
| gin\_ejecucion\_economica: Boolean Private = True  Permite habilitar la Ejecución económica de Grupos de investigación.  Posibles valores:   * False * True   El valor "False" se corresponde con el texto "No"  El valor "True" se corresponde con el texto "Sí" |
| partidas\_presupuestarias\_SGE: Boolean Private = False  Permite habilitar si la partidas presupuestarias se introducen manualmente o se listan a través de una función del ESB que las lee del SGE.  Posibles valores:   * False * True   El valor "False" se corresponde con el texto "No" y significará  que no hay integración con el SGE por lo tanto las partidas se crean en el SGI.  El valor "True" se corresponde con el texto "Sí" y significará que si hay integración con el SGE para recuperar el listado de partidas presupuestarias, por lo tanto no se crean en el SGI. |
| sge\_modificacion: Boolean Private = False  Permite habilitar la acción de solicitar modificación de datos del proyecto al SGE.  Posibles valores:   * Sí * No   El valor "Sí" significará  que se permite la modificación del proyecto SGE desde el SGI (volver a enviarle los datos del SGI y actualizar los datos propios del formly del proyecto SGE).  El valor "No" significará  que no se permite la modificación del proyecto SGE desde el SGI. |
| sge\_alta\_buscador: Boolean Private = False  Permite habilitar la visualización del buscador de proyectos económicos al añadir un nuevo identificador SGE para permitir relacionar el proyecto SGI con un proyecto SGE existente.  Posibles valores:   * Sí * No   El valor "Sí" significará  que se mostrará el buscador de proyectos económicos lo que permitirá seleccionar un proyecto SGE existente para relacionarlo con un proyecto SGI.  El valor "No" significará que se no mostrará el buscador de proyectos económicos lo que no permitirá relacionar un proyecto SGI con un proyecto SGE existente. |
| sge\_sector\_iva: Boolean Private = False  Permite habilitar la visualización del campo "Sector IVA" proveniente de la integración con el SGE en el SGI.  Posibles valores:   * Sí * No   El valor "Sí" significará  que se mostrará el campo "Sector IVA" en el SGI. Su valor es recuperado del SGE a través de una integración con el SGE.  El valor "No" significará que no se mostrará el campo "Sector IVA" en el SGI. |
| sge\_amortizacion\_fondos: Boolean Private = False  Permite habilitar o no la integración de los periodos de amortización con el SGE.  Posibles valores:   * Sí * No   El valor "Sí" significará que al crear, modificar o eliminar un periodo de amortización en el SGI se le notificará al SGE a través de los servicios de integración definidos para ello.  El valor "No" significará que al crear, modificar o eliminar un periodo de amortización en el SGI no se le notificará  nada al SGE. No existirá integración. |
| sge\_calendario\_facturacion: Boolean Private = False  Permite habilitar o no la integración del calendario de facturación con el SGE.  Posibles valores:   * Sí * No   El valor "Sí" significará que al crear y modificar facturas previstas del calendario de facturación en el SGI se le notificará al SGE a través de los servicios de integración definidos para ello.  El valor "No" significará que al crear y  modificar facturas previstas del calendario de facturación en el SGI no se le notificará  nada al SGE. No existirá integración. |
| sge\_modificaciones: Boolean Private = False  Permite habilitar o no mostrar la opción de menú de "Modificaciones" de dentro del apartado "Ejecución económcia - Detalle de operaciones". En caso de que no este habilitada no existirá dicha integración con el SGE.  Posibles valores:   * Sí * No   El valor "Sí" significará que se mostrará la opción de menú "Modificaciones" de dentro del apartado "Ejecución económcia - Detalle de operaciones" y que existirá integración con el SGE para obtener los datos a mostrar.  El valor "Sí" significará que no se mostrará la opción de menú "Modificaciones" de dentro del apartado "Ejecución económcia - Detalle de operaciones" y por lo tanto no existirá integración con el SGE. |
| sge\_gastos\_justificados: Boolean Private = False  Permite activar/desactivar la integración de gastos justificados (apartado seguimiento de justificación)  Posibles valores:   * Sí * No   El valor "Sí" significará que existirá integración con un módulo de justificación que pudiera existir en la Universidad para obtener los gastos justificados (usados en el seguimiento justificación). .  El valor "No" significará que no existirá integración con un sistema externo para obtener los gastos justificados (usados en el seguimiento justificación). |
| inv\_solicitudes\_sin\_convocatoria: Boolean Private = False  Permite habilitar la opción de Añadir Solicitud al perfil de investigación. Con esta opción habilitada se permitirá la creación de solicitudes que no tengan vinculación a una convocatoria. Con esta opción se dará cobertura al escenario de uso en el que el personal de investigación propone a la unidad de gestión, a través de una solicitud, la realización de un proyecto a través de un contrato/convenio sin convocatoria. |
| sge\_facturas\_columnas\_visibles: String Private  Permite indicar que columnas de las columnas fijas se desean mostrar en Facturas y gastos. Sólo se muestran aquellas columnas que  se pueden eliminar, el resto de columnas fijas que no se muestran en el desplegable es porque siempre se van a mostrar, no se da opción de hacerlas configurables.  Posibles valores:   * Partidas Presupuestarias * Clasificación SGE   Si se desmarca una de las dos columnas o las dos, dichas columnas no se mostrarán en la pantalla de Ejecución económica - Facturas y Justificantes - Facturas y gastos ni en la exportación ni en el detalle del gasto. |
| sge\_viajes\_columnas\_visibles: String Private  Permite indicar que columnas de las columnas fijas se desean mostrar en Viajes y dietas. Sólo se muestran aquellas columnas que  se pueden eliminar, el resto de columnas fijas que no se muestran en el desplegable es porque siempre se van a mostrar, no se da opción de hacerlas configurables.  Posibles valores:   * Partidas Presupuestarias * Clasificación SGE   Si se desmarca una de las dos columnas o las dos, dichas columnas no se mostrarán en la pantalla de Ejecución económica - Facturas y Justificantes - Viajes y dietas ni en la exportación ni en el detalle del gasto. |
| sge\_personal\_columnas\_visibles: String Private  Permite indicar que columnas de las columnas fijas se desean mostrar en Pesonal contratado. Sólo se muestran aquellas columnas que  se pueden eliminar, el resto de columnas fijas que no se muestran en el desplegable es porque siempre se van a mostrar, no se da opción de hacerlas configurables.  Posibles valores:   * Partidas Presupuestarias * Clasificación SGE   Si se desmarca una de las dos columnas o las dos, dichas columnas no se mostrarán en la pantalla de Ejecución económica - Facturas y Justificantes - Pesonal contratado ni en la exportación ni en el detalle del gasto. |
| csp\_pro\_socio\_pais\_filter\_enabled: Boolean Private  Habilita el filtro de búsqueda por país socio en el buscador ampliado de proyectos. Se requiere que el requisito de integración de búsqueda de empresas del SGEMP implemente la búsqueda por "pais ID" |

### Enumerados del modelo  CSP Convocatoria

#### **Enumerado Clasificación de items para CVN: "ClasificacionCVN"**

Enumerado que representa los apartados del CVN. A partir de este enumerado se identifica el apartado del CVN en el que se deberían mostrar los proyectos registrados en el SGI. Valores: 

* AYUDAS (los proyectos catalogados con este tipo se deberían incluir en el apartado CVN "Ayudas y becas obtenidas")
* COMPETITIVOS (los proyectos catalogados con este tipo se deberían incluir en el apartado CVN "Proyectos competitivos")
* NO\_COMPETITIVOS (los proyectos catalogados con este tipo se deberían incluir en el apartado CVN "Contratos, convenios y proyectos no competitivos")
* INSTITUCIONAL\_AYUDAS (los proyectos catalogados con este tipo no se mostrarán en CVN)
* INSTITUCIONAL\_COMPETITIVOS (los proyectos catalogados con este tipo no se mostrarán en CVN)
* INSTITUCIONAL\_NO\_COMPETITIVOS (los proyectos catalogados con este tipo no se mostrarán en CVN)

|  |
| --- |
| **ATTRIBUTES** |
| Ayudas y becas :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Proyectos competitivos :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Contratos, convenios, proyectos no competitivos :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Proyectos institucionales. Ayudas y becas :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Proyectos institucionales. Proyectos competitivos :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Proyectos institucionales. Contratos, convenios, proyectos no competitivos :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) ClasificacionCVN    Cardinality:  [1] | Target: Public (Class) Proyecto    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Convocatoria    Cardinality:  [0..\*] | Target: Public (Enumeration) ClasificacionCVN    Cardinality:  [1] |

#### **Enumerado Tipo estado de convocatoria: "TipoEstadoConvocatoria"**

Enumerado que representa los estados por lo que puede pasar una convocatoria. Valores: 

* BORRADOR
* REGISTRADA

|  |
| --- |
| **ATTRIBUTES** |
| Borrador :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Registrada :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoConvocatoria    Cardinality:  [1] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |

#### **Enumerado Tipo formulario de solicitud: "TipoFormularioSolicitud"**

Listado con los distintos tipos de solicitud posibles. Enumerado con los siguientes valores: 

* PROYECTO
* GRUPO
* RRHH

|  |
| --- |
| **ATTRIBUTES** |
| Proyecto :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Grupo :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoFormularioSolicitud    Cardinality:  [1] | Target: Public (Class) Convocatoria    Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Solicitud | Target: Public (Enumeration) TipoFormularioSolicitud |

#### **Enumerado Tipo de periodo de justificación: "TipoJustificacion"**

Enumerado que contiene los tipos de los periodos de justificación económica disponibles en convocatorias y proyectos. Valores: 

* FINAL
* INTERMEDIO
* PERIODICO

|  |
| --- |
| **ATTRIBUTES** |
| Periódica :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Intermedia :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Final :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoJustificacion | Target: Public (Enumeration) TipoJustificacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoJustificacion | Target: Public (Enumeration) TipoJustificacion |

#### **Enumerado Tipo de partida presupuestaria: "TipoPartida"**

Enumerado para identificar el tipo de las partidas o aplicaciones presupuestarias. Toma los valores: 

* GASTO
* INGRESO

|  |
| --- |
| **ATTRIBUTES** |
| Gasto :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Ingresos :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPartida | Target: Public (Enumeration) TipoPartida |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPartida | Target: Public (Enumeration) TipoPartida |

#### **Enumerado Tipo de periodo de seguimiento científico:"TipoSeguimiento"**

Enumerado que contiene los tipos de los periodos de seguimiento científico disponibles en convocatorias y proyectos. Valores: 

* FINAL
* INTERMEDIO
* PERIODICO

|  |
| --- |
| **ATTRIBUTES** |
| Periódico :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Intermedio :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |
| Final :   Public   [ Stereotype is «enum». Is static False. Containment is Not Specified. ] |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProyectoPeriodoSeguimiento | Target: Public (Enumeration) TipoSeguimiento |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaPeriodoSeguimientoCientifico | Target: Public (Enumeration) TipoSeguimiento |