# Multiidioma a nivel de contenido - Identificación de campos

Se enumeran a continuación los campos que será objeto de desdoblamiento a tabla, para dar cobertura a su internacionalización, y la pantalla en la que se encuentran:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Módulo** | **Menú** | **Pantalla** | **Campo** | **Tabla y campo en modelo actual** | **Observaciones** |
| CSP | Configuración - Roles de equipo | Datos generales | Nombre | RolProyecto.nombre |  |
| CSP | Configuración - Roles de equipo | Datos generales | Abreviatura | RolProyecto.abreviatura |  |
| CSP | Configuración - Roles de equipo | Datos generales | Descripción | RolProyecto.descripcion |  |
| CSP | Configuración - Roles de socio de proyecto |  | Nombre | RolSocio.nombre |  |
| CSP | Configuración - Roles de socio de proyecto |  | Abreviatura | RolSocio.abreviatura |  |
| CSP | Configuración - Roles de socio de proyecto |  | Descripción | RolSocio.descripcion |  |
| CSP | Configuración - Tipo de ámbito geográfico |  | Nombre | TipoAmbitoGeograficon.nombre |  |
| CSP | Configuración - Tipos de facturación |  | Nombre | TipoFacturacion.nombre |  |
| CSP | Configuración - Tipos de financiación |  | Nombre | TipoFinanciacion.nonbre |  |
| CSP | Configuración - Tipos de financiación |  | Descripción | TipoFinanciacion.descripcion |  |
| CSP | Configuración - Tipos de origen de fuente de financiación |  | Nombre | TipoOrigenFuenteFinanciacion.nombre |  |
| CSP | Configuración - Tipos régimen concurrencia |  | Nombre | TipoRegimenConcurrencia.nombre |  |
| CSP | Configuración - Tipos de fase |  | Nombre | TipoFase.nombre |  |
| CSP | Configuración - Tipos de fase |  | Descripción | TipoFase.descricpion |  |
| CSP | Configuración - Tipos de finalidad |  | Nombre | TipoFinalidad.nombre |  |
| CSP | Configuración - Tipos de finalidad |  | Descripción | TipoFinalidad.descripcion |  |
| CSP | Configuración - Tipos de documento |  | Nombre | TipoDocumento.nombre |  |
| CSP | Configuración - Tipos de documento |  | Descripción | TipoDocumento.descripcion |  |
| CSP | Configuración - Tipos de enlace |  | Nombre | TipoEnlace.nombre |  |
| CSP | Configuración - Tipos de enlace |  | Descripción | TipoEnlace.descripcion |  |
| CSP | Configuración - Tipos de hito |  | Nombre | TipoHito.nombre |  |
| CSP | Configuración - Tipos de hito |  | Descripción | TipoHito.descripcion |  |
| CSP | Configuración - Modelos de ejecución | Datos generales | Nombre | ModeloEjecucion.nombre |  |
| CSP | Configuración - Modelos de ejecución | Datos generales | Descripción | ModeloEjecucion.descripcion |  |
| CSP | Configuración - Planes de investigación | Datos generales | Nombre del plan | Programa.nombre |  |
| CSP | Configuración - Planes de investigación | Datos generales | Descripción | Programa.descripcion |  |
| CSP | Configuración - Áreas temáticas | Datos generales | Área temática | AreaTematica.nombre |  |
| CSP | Configuración - Áreas temáticas | Datos generales | Descripción | AreaTematica.descripcion |  |
| CSP | Configuración - Fuentes de financiación |  | Nombre de la fuente | FuenteFinanciacion.nombre |  |
| CSP | Configuración - Fuentes de financiación |  | Descripción | FuenteFinanciacion.descripcion |  |
| CSP | Configuración - Conceptos de gasto |  | Nombre | ConceptoGasto.nombre |  |
| CSP | Configuración - Conceptos de gasto |  | Descripción | ConcetoGasto.descripcion |  |
|  | | | | | |
| CSP | Convocatoria | Datos generales | Título | convocatoria.titulo |  |
| CSP | Convocatoria | Datos generales | Identificación (Referencia externa) | convocatoria.codigo | No aplica su internacionalización pues representa un código. |
| CSP | Convocatoria | Datos generales | Referencia interna | convocatoria.codInterno | No aplica su internacionalización pues representa un código. |
| CSP | Convocatoria | Datos generales | Palabras clave | PalabraClave.palabra | No aplica internacionalización como tal. Se listarán todas las palabras clave. |
| CSP | Convocatoria | Datos generales | Objeto o descripción general de la convocatoria | convocatoria.objeto |  |
| CSP | Convocatoria | Datos generales | Observaciones | convocatoria.observaciones |  |
| CSP | Convocatoria | Enlaces | Descripción | ConvocatoriaEnlace.descripcion |  |
| CSP | Convocatoria | Periodos Justificación | Observaciones | ConvocatoriaPeriodoJustificacion.observaciones |  |
| CSP | Convocatoria | Fases | Observaciones | ConvocatoriaFase.observaciones |  |
| CSP | Convocatoria | Fases - Avisos | Asunto | SubjectTPL.tpl | Módulo de comunicados. |
| CSP | Convocatoria | Fases - Avisos | Contenido Email | ContentTPL.html  ContentTPL.text | Módulo de comunicados. |
| CSP | Convocatoria | Seguimiento científico | Observaciones | ConvocatoriaPeriodoSeguimientoCientifico.observaciones |  |
| CSP | Convocatoria | Hitos | Observaciones | ConvocatoriaHito.comentario |  |
| CSP | Convocatoria | Hitos - Aviso | Asunto | SubjectTPL.tpl | Módulo de comunicados. |
| CSP | Convocatoria | Hitos - Aviso | Contenido Email | ContentTPL.html  ContentTPL.text | Módulo de comunicados. |
| CSP | Convocatoria | Documentos | Nombre | Documento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Convocatoria | Documentos | Observaciones | ConvocatoriaDocumento.observaciones |  |
| CSP | Convocatoria | Requisitos IP | Campo libre | RequisitoIP.otrosRequisitos |  |
| CSP | Convocatoria | Requisitos Equipo | Campo libre | RequisitoEquipo.otrosRequisitos |  |
| CSP | Convocatoria | Elegibilidad - Datos Generales | Observaciones del concepto de gasto en la convocatoria | ConvocatoriaConceptoGasto.observaciones |  |
| CSP | Convocatoria | Elegibilidad - Códigos Económicos | Observaciones | ConvocatoriaConceptoGastoCodigoEc.obsservaciones |  |
| CSP | Convocatoria | Partidas presupuestarias | Descripción | ConvocatoriaPartida.descripcion |  |
| CSP | Convocatoria | Configuración Solicitudes | Documento requerido Observaciones | DocumentoRequeridoSolicitud.observaciones |  |
|  | | | | | |
| CSP | Solicitudes | Datos generales | Identificación convocatoria (referencia externa convocatoria) | Solicitud.convocatoriaExterna | No internacionalizable. Se considera un código. |
| CSP | Solicitudes | Datos generales | Título | Solicitud.titulo |  |
| CSP | Solicitudes | Datos generales | Observaciones | Solicitud.observaciones |  |
| CSP | Solicitudes | Datos proyecto - Ficha general | Palabras clave | PalabraClave.palabra | Módulo palabras clave. No aplica internacionalización como tal, se listarían de forma común. |
| CSP | Solicitudes | Datos proyecto - Ficha general | Objetivos del proyecto | SolicitudProyecto.objetivos |  |
| CSP | Solicitudes | Datos proyecto - Ficha general | Justificación en interés | SolicitudProyecto.intereses |  |
| CSP | Solicitudes | Datos proyecto - Ficha general | Resultados esperados | SolicitudProyecto.resultadosPrevistos |  |
| CSP | Solicitudes | Datos proyecto - Socios - Periodo justificación | Observaciones | SolicitudProyectoPeriodoJustificacion.observaciones |  |
| CSP | Solicitudes | Datos proyecto - Desglose presupuesto - Partida gasto | Observaciones | SolicitudProyectoPresupuesto.observaciones |  |
| CSP | Solicitudes | Documentos | Nombre | SolicitudDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Solicitudes | Documentos | Comentarios | SolicitudDocumento.comentario |  |
| CSP | Solicitudes | Histórico Estados | Comentario | EstadoSolicitud.comentario |  |
| CSP | Solicitudes | Hitos | Observaciones | SolicitudHito.comentario |  |
| CSP | Solicitudes | Hitos - Avisos | Asunto | SubjectTPL.tpl | Módulo de comunicados. |
| CSP | Solicitudes | Hitos - Avisos | Contenido Email | ContentTPL.html  ContentTPL.text | Módulo de comunicados. |
| CSP | Solicitudes | Datos Solicitud RRHH - Memoria | Título del trabajo | SolicitudRRHH.tituloTrabajo |  |
| CSP | Solicitudes | Datos Solicitud RRHH - Memoria | Resumen | SolicitudRRHH.resumen |  |
| CSP | Solicitudes | Datos Solicitud RRHH - Memoria | Observaciones | SolicitudRRHH.observaciones |  |
|  |  |  |  |  |  |
| CSP | Proyectos | Datos generales - Ficha general | Título | Proyecto.titulo |  |
| CSP | Proyectos | Datos generales - Ficha general | Identificación convocatoria | Proyecto.convocatoriaExterna | No internacionalizable. Se considera un código. |
| CSP | Proyectos | Datos generales - Ficha general | Observaciones | Proyecto.observaciones |  |
| CSP | Proyectos | Datos generales - Ficha general | Palabras clave | PalabraClave.palabra | Módulo palabras clave. No aplica internacionalización como tal, se listarían de forma común. |
| CSP | Proyectos | Datos generales - Contexto proyecto | Objetivos del proyecto | ContextoProyecto.objetivos |  |
| CSP | Proyectos | Datos generales - Contexto proyecto | Justificación e intereses | ContextoProyecto.intereses |  |
| CSP | Proyectos | Datos generales - Contexto proyecto | Resultados esperados | ContextoProyecto.resultadosPrevistos |  |
| CSP | Proyectos | Datos generales - Histórico estados | Comentario | EstadoProyecto.comentario |  |
| CSP | Proyectos | Datos generales - Relaciones | Observaciones | Relacion.observaciones |  |
| CSP | Proyectos | Fases | Observaciones | ProyectoFase.observaciones |  |
| CSP | Proyectos | Fases - Generar aviso | Asunto | SubjectTPL.tpl | Módulo de comunicados. |
| CSP | Proyectos | Fases - Generar aviso | Contenido email | ContentTPL.html  ContentTPL.text | Módulo de comunicados. |
| CSP | Proyectos | Hitos | Observaciones |  |  |
| CSP | Proyectos | Hitos - Generar aviso | Asunto | SubjectTPL.tpl | Módulo de comunicados. |
| CSP | Proyectos | Hitos - Generar aviso | Contenido email | ContentTPL.html  ContentTPL.text | Módulo de comunicados. |
| CSP | Proyectos | Seguimiento científico - Datos generales | Observaciones | ProyectoPeriodoSeguimiento.observaciones |  |
| CSP | Proyectos | Seguimiento científico - Documentos | Nombre | ProyectoPeriodoSeguimientoDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Proyectos | Seguimiento científico - Documentos | Comentario | ProyectoPeriodoSeguimientoDocumento.comentario |  |
| CSP | Proyectos | Prórroga - Datos generales | Observaciones | ProyectoProrroga.observaciones |  |
| CSP | Proyectos | Prórroga - Documentos | Nombre | ProyectoProrrogaDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Proyectos | Prórroga - Documentos | Comentario | ProyectoProrrogaDocumento.comentario |  |
| CSP | Proyectos | Documentos | Nombre | ProyectoDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Proyectos | Documentos | Comentarios | ProyectoDocumento.comentario |  |
| CSP | Proyectos | Paquetes de trabajo | Nombre | ProyectoPaqueteTrabajo.nombre | No internacionalizable. Se considera un código. |
| CSP | Proyectos | Paquetes de trabajo | Descripción | ProyectoPaqueteTrabajo.descripción |  |
| CSP | Proyectos | Socios - Periodos justificación - Datos generales | Observaciones | ProyectoSocioPeriodoJustificacion.observaciones |  |
| CSP | Proyectos | Socios - Periodos justificación - Documentos | Nombre | SocioPeriodoJustificacionDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| CSP | Proyectos | Socios - Periodos justificación - Documentos | Comentarios | SocioPeriodoJustificacionDocumento.comentario |  |
| CSP | Proyectos | Configuración Económica - Elegibilidad - Datos generales | Observaciones | ProyectoConceptoGasto.observaciones |  |
| CSP | Proyectos | Configuración Económica - Elegibilidad - Códigos económicos | Observaciones | ProyectoConceptoGastoCodigoEc.observaciones |  |
| CSP | Proyectos | Configuración Económica - Partida presupuestaria | Descripción | ProyectoPartida.descripcion |  |
| CSP | Proyectos | Configuración Económica - Calendario facturación | Comentario | ProyectoFacturacion.comentario |  |
| CSP | Proyectos | Configuración Económica - Calendario facturación - Validación IP | Comentario | EstadoValidacionIP.comentario |  |
| CSP | Proyectos | Configuración Económica - Calendario Justificación | Observaciones | ProyectoPeriodoJustificacion.observaciones |  |
| CSP | Proyectos | Configuración Económica -Amortización de fondos |  |  | El SGI notifica los periodos de amortización creados. En los datos del periodo se envían valores internacionalizados. El servicio externo debe de dar cobertura a la internacionalización  El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. [Amortización fondos](/hercules/apis-de-integracion/sgi-servicios-de-terceros-que-expone/sistema-de-gestion-economica/amortizacion-fondos) |
|  | | | | | |
| CSP | Participación Proyectos Externos - Autorización | Datos generales | Título proyecto | Autorizacion.tituloProyecto |  |
| CSP | Participación Proyectos Externos - Autorización | Datos generales | Datos de la convocatoria | Autorizacion.datosConvocatoria |  |
| CSP | Participación Proyectos Externos - Autorización | Datos generales | Datos de la entidad con la que participa | Autorizacion.datosEntidad | No se aplicará internacionalización a este campo. Es un nombre de empresa/entidad que se supone que será único y que ya será introducido en el idioma correspondiente. No aplica traducción sobre un "nombre propio". Además el nombre introducido deberá ser mapeado posteriormente a una empresa/entidad del SGEMP a través del buscador de empresas disponible en la pantalla. |
| CSP | Participación Proyectos Externos - Autorización | Datos generales | Observaciones | Autorizacion.observaciones |  |
| CSP | Participación Proyectos Externos - Autorización | Autorización Cambiar estado | Comentario | EstadoAutorizacion.comentario |  |
| CSP | Participación Proyectos Externos - Autorización | Certificación autorización | Nombre | CertificadoAutorizacion.nombre |  |
| CSP | Participación Proyectos Externos - Notificaciones CVN | Datos generales | Título | NotificacionProyectoExternoCVN.tituloProyecto | Procede del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización.  Es un campo que es susceptible de copiar a los datos de un proyecto, por tanto, se internacionalizará.  Procede del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. [Autorizaciones y notificaciones de proyectos externos#NotificacionProyecto](/hercules/apis-de-integracion/sgi-servicios-propios-que-expone/autorizaciones-y-notificaciones-de-proyectos-externos#Autorizacionesynotificacionesdeproyectosexternos-NotificacionProyecto) |
| CSP | Participación Proyectos Externos - Notificaciones CVN | Datos generales | Ámbito geográfico | NotificacionProyectoExternoCVN.ambitoGeografico | No será objeto de internacionalización.  Es un campo procedente del servicio de integración del ESB. Se persisten en el SGI pero no se realiza ninguna operación con este valor. Sería un campo que procedería de CVN y que estaría tipificado según sistema origen.  La funcionalidad de Notificaciones de CVN para proyectos externos aún no cuenta con un uso extendido en el SGI y sería dependiente de una toma de decisión en el tratamiento de los campos procedentes de CVN por lo que se opta por no introducirlo en la internacionalización a la espera de una posible re-definición de esta funcionalidad. |
| CSP | Participación Proyectos Externos - Notificaciones CVN | Datos generales | Grado contribución | NotificacionProyectoExternoCVN.gradoContribucion | No será objeto de internacionalización.  Es un campo procedente del servicio de integración del ESB. Se persisten en el SGI pero no se realiza ninguna operación con este valor. Sería un campo que procedería de CVN y que estaría tipificado según sistema origen.  La funcionalidad de Notificaciones de CVN para proyectos externos aún no cuenta con un uso extendido en el SGI y sería dependiente de una toma de decisión en el tratamiento de los campos procedentes de CVN por lo que se opta por no introducirlo en la internacionalización a la espera de una posible re-definición de esta funcionalidad. |
| CSP | Participación Proyectos Externos - Notificaciones CVN | Datos generales | Nombre programa asociado al proyecto | NotificacionProyectoExternoCVN.nombrePrograma | No será objeto de internacionalización.  Es un campo procedente del servicio de integración del ESB. Se persisten en el SGI pero no se realiza ninguna operación con este valor. Sería un campo que procedería de CVN y que estaría tipificado según sistema origen.  La funcionalidad de Notificaciones de CVN para proyectos externos aún no cuenta con un uso extendido en el SGI y sería dependiente de una toma de decisión en el tratamiento de los campos procedentes de CVN por lo que se opta por no introducirlo en la internacionalización a la espera de una posible re-definición de esta funcionalidad. |
|  | | | | | |
| CSP | Grupo investigación | Datos generales | Nombre | Grupo.nombre |  |
| CSP | Grupo investigación | Datos generales | Resumen | Grupo.resumen |  |
| CSP | Grupo investigación | Datos generales | Palabras clave | PalabraClave.palabra | Módulo palabras clave. No aplica internacionalización como tal, se listarían de forma común. |
| CSP | Grupo investigación | Equipo instrumental | Nombre | GrupoEquipoInstrumental.nombre |  |
| CSP | Grupo investigación | Equipo instrumental | Descripción | GrupoEquipoInstrumental.descripción |  |
|  | | | | | |
| CSP | Ejecución económica - Ejecución presupuestaria | Resumen actual |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Ejecución presupuestaria | Gastos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Ejecución presupuestaria | Ingresos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Detalle operaciones | Gastos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Detalle operaciones | Ingresos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Detalle operaciones | Modificaciones |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Facturas y justificantes | Facturas y gastos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Facturas y justificantes | Viajes y dietas |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Facturas y justificantes | Viajes y dietas | Observaciones | GastoProyecto.observaciones |  |
| CSP | Ejecución económica - Facturas y justificantes | Personal contratado |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Clasificación gastos | Clasificación de gastos |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Facturas emitidas | Facturas emitidas |  |  | Valores procedente del ESB - servicio de integración. El SGI consultará al servicio de integración en el idioma seleccionado en cada momento. El servicio de integración externo deberá dar cobertura a la internacionalización. |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Datos generales | Nombre del documento de justificación | TipoRequerimiento.nombre | Tabla de datos maestros sin configuración por interface. |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Datos generales | Observaciones | RequerimientoJustificacion.observaciones |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Datos generales -Incidencias documentación | Nombre del documento de justificación | IncidenciaDocumentacionRequerimiento.nombreDocumento |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Datos generales -Incidencias documentación | Incidencia motivo rechazo | IncidenciaDocumentacionRequerimiento.incidencia |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Respuesta alegación | Observaciones | AlegacionRequerimiento.observaciones |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Respuesta alegación - Incidencias documentación | Alegación presentada | IncidenciaDocumentacionRequerimiento.alegacion |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Gastos - Detalle gasto | Incidencia en el gasto o motivo de rechazo | GastoRequerimientoJustificacion.incidencia |  |
| CSP | Ejecución económica - Seguimiento justificación | Requerimientos - Gastos - Detalle gasto | Alegación | GastoRequerimientoJustificacion.alegacion |  |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Módulo** | **Menú** | **Pantalla** | **Campo** | **Tabla y campo actual** | **Observaciones** |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Título | PeticionEvaluacion.titulo |  |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Resumen (texto enriquecido) | PeticionEvaluacion.resumen |  |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Otro valor social | PeticionEvaluacion.otroValorSocial |  |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Objetivos científicos (texto enriquecido) | PeticionEvaluacion.objetivos |  |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Diseño metodológico (texto enriquecido) | PeticionEvaluacion.disMetodologico |  |
| ETI - INV | Solicitud evaluación proyecto | Datos generales | Órgano financiador (Fuente financiación) | PeticionEvaluacion.fuenteFinanciacion |  |
| ETI - INV | Memoria | Asignación tareas | Tarea | Tarea.tarea |  |
| ETI - INV | Memoria | Asignación tareas | Formación específica | Tarea.formacion |  |
| ETI - INV | Memoria | Asignación tareas | Organismo | Tarea.organismo |  |
| ETI - INV | Memoria | Documentación | Nombre | DocumentacionMemoria.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| ETI - INV | Memoria | Documentación - Seguimiento anual | Nombre | DocumentacionMemoria.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| ETI - INV | Memoria | Documentación - Seguimiento final | Nombre | DocumentacionMemoria.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| ETI | Convocatorias de reunión | Datos generales | Lugar | ConvocatoriaReunion.lugar |  |
| ETI | Convocatorias de reunión | Datos generales | Orden del día (texto enriquecido) | ConvocatoriaReunion.ordenDia |  |
| ETI | Evaluación | Comentario | Comentario | Comentario.texto |  |
| ETI | Evaluación |  | Motivo (no procede evaluar) | Evaluacion.comentario |  |
| ETI | Actas | Datos generales | Resumen | Acta.resumen |  |
| ETI | Actas | Asistentes - Editar asistencia | Motivo | Asistentes.motivo |  |
| ETI | Actas | Comentarios | Comentario | Comentario.texto |  |
| ETI | Evaluadores | Datos generales | Resumen | Evaluador.resumen |  |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Módulo** | **Menú** | **Pantalla** | **Campo** | **Tabla y campo** | **Observaciones** |
| PII | Configuración - Tipos de protección | Datos generales | Nombre | TipoProteccion.nombre |  |
| PII | Configuración - Tipos de protección | Datos generales | Descripción | TipoProteccion.descripcion |  |
| PII | Configuración - Tipos de protección | Subtipos de protección | Nombre | TipoProteccion.nombre |  |
| PII | Configuración - Tipos de protección | Subtipos de protección | Descripción | TipoProteccion.descripcion |  |
| PII | Configuración - Sectores de aplicación |  | Nombre | SectorAplicacion.nombre |  |
| PII | Configuración - Sectores de aplicación |  | Descripción | SectorAplicacion.descripcion |  |
| PII | Configuración - Resultados informe patentabilidad |  | Nombre | ResultadoInformePatentabilidiad.nombre |  |
| PII | Configuración - Resultados informe patentabilidad |  | Descripción | ResultadoInformePatentabilidiad.descripcion |  |
| PII | Configuración - Tipos de procedimiento |  | Nombre | TipoProcedimiento.nombre |  |
| PII | Configuración - Tipos de procedimiento |  | Descripción | TipoProcedimiento.descripcion |  |
| PII | Configuración - Vías de protección |  | Nombre | ViaProteccion.nombre |  |
| PII | Configuración - Vías de protección |  | Descripción | ViaProteccion.descripcion |  |
| PII | Invenciones | Datos generales | Título | Invencion.titulo |  |
| PII | Invenciones | Datos generales | Descripción | Invencion.descricpion |  |
| PII | Invenciones | Datos generales | Comentarios | Invencion.comentarios |  |
| PII | Invenciones | Datos generales | Palabras clave | PalabraClave.palabra | Módulo palabras clave. No aplica internacionalización como tal, se listarían de forma común. |
| PII | Invenciones | Documentos | Nombre | InvencionDocumento.nombre |  |
| PII | Invenciones | Informes de patentabilidad | Nombre | InformePatentabilidad.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| PII | Invenciones | Informes de patentabilidad | Comentarios | InformePatentabilidad.comentarios |  |
| PII | Invención - Solicitud de protección | Datos generales | Título | SolicitudProteccion.titulo |  |
| PII | Invención - Solicitud de protección | Datos generales | Comentarios | SolicitudProteccion.comentarios |  |
| PII | Invención - Solicitud de protección | Datos generales (con estado = "caducada") | Tipo caducidad | TipoCaducidad.descripcion |  |
| PII | Invención - Solicitud de protección | Procedimientos | Acciones a tomar | Procedimiento.accionATomar |  |
| PII | Invención - Solicitud de protección | Procedimientos | Comentarios | Procedimiento.observaciones |  |
| PII | Invención - Solicitud de protección | Procedimientos - Documentos | Nombre | ProcedimientoDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Módulo** | **Menú** | **Pantalla** | **Campo** | **Tabla y campo** | **Observaciones** |
| EER | Empresas de explotación de resultados | Datos generales | Nombre/Razón social | Empresa.nombreRazonSocial |  |
| EER | Empresas de explotación de resultados | Datos generales | Objeto social | Empresa.objetoSocial |  |
| EER | Empresas de explotación de resultados | Datos generales | Tecnología/Conocimiento | Empresa.conocimientoTecnologia |  |
| EER | Empresas de explotación de resultados | Datos generales | Notario | Empresa.notario |  |
| EER | Empresas de explotación de resultados | Datos generales | Observaciones | Empresa.observaciones |  |
| EER | Empresas de explotación de resultados | Documentos | Nombre | EmpresaDocumento.nombre | Se aplica internacionalización al considerar el nombre como un "título" del contenido del fichero |
| EER | Empresas de explotación de resultados | Documentos | Comentario | EmpresaDocumento.comentarios |  |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Módulo** | **Menú** | **Pantalla** | **Campo** | **Tabla y campo** | **Observaciones** |
| ADM | Configuración CSP |  | Texto acceso a sistema corporativo secundario de gestión de la investigación | cnf\_sgi.config | Es el registro de la tabla cnf\_sgi.config para el que el atributo “name” toma el valor “nombre-sistema-gestion-externo” |
| ADM | Configuración CSP |  | URL sistema corporativo secundario de gestión de la investigación | cnf\_sgi.config | Es el registro de la tabla cnf\_sgi.config para el que el atributo “name” toma el valor “url-sistema-gestion-externo” |

#### Listados no configurables

Se listan a continuación los listados que no son configurables y que serían objeto de traducción

|  |  |  |  |
| --- | --- | --- | --- |
| **Módulo** |  | **Listado** |  |
| CSP | Configuración - Roles de equipo | Equipo |  |
| CSP | Configuración - Roles de equipo | Rol principal (Sí/No) |  |
| CSP | Configuración - Roles de equipo | Orden |  |
| CSP | Configuración - Roles de equipo | BaremablePRC (Sí/No) |  |
| CSP | Configuración - Roles de equipo | Colectivo |  |
| CSP | Configuración - Roles de socio de proyecto | Coordinador (Sí/No) |  |
| CSP | Configuración - Modelos de ejecución | Unidades de gestión |  |
| CSP | Configuración - Fuentes de financiación | Origen |  |
| CSP | Configuración - Fuentes de financiación | Fondo Estructural (Sí/No) |  |
| CSP | Configuración - Conceptos de gasto | Costes indirectos (Sí/No) |  |
| CSP | Configuración - Líneas investigación | Nombre |  |
| CSP | Convocatoria | Tipo solicitud SGI |  |
| CSP | Convocatoria | Unidad de gestión |  |
| CSP | Convocatoria | Convocatoria de excelencia (Sí/No) |  |
| CSP | Convocatoria | Clasificación producción científica CVN |  |
| CSP | Convocatoria | Tipo Justificación |  |
| CSP | Convocatoria | Tipo Seguimiento |  |
| CSP | Convocatoria | Documento - Publico (Sí/No) |  |
| CSP | Convocatoria | Sexo (ESB - SGP) |  |
| CSP | Convocatoria | Nivel Académico (ESB - SGP) |  |
| CSP | Convocatoria | Requisitos IP - Vinculación universidad (Sí/No) |  |
| CSP | Convocatoria | Categoría Profesional (ESB) |  |
| CSP | Convocatoria | Elegibilidad - Costes indirectos (Sí/No) |  |
| CSP | Convocatoria | Códigos Económicos (ESB - SGE) |  |
| CSP | Convocatoria | Partidas presupuestarias - Tipo Partida |  |
| CSP | Convocatoria | Configuración solicitudes  - Habilitar presentación SGI (Sí/No) |  |
| CSP | Convocatoria | Tipo Estado Convocatoria |  |
| CSP | Solicitudes | Tipo Estado Solicitud |  |
| CSP | Solicitudes | Tipo Solicitud Grupo |  |
| CSP | Solicitudes | Proyecto coordinado (Sí/No) |  |
| CSP | Solicitudes | Proyecto colaborativo (Sí/No) |  |
| CSP | Solicitudes | Tipo desglose presupuesto |  |
| CSP | Solicitudes | Áreas conocimiento (ESB - SGO) |  |
| CSP | Solicitudes | Clasificaciones (ESB - SGO) |  |
| CSP | Solicitudes RRHH | Tipo documento (ESB - SGP) |  |
| CSP | Solicitudes RRHH | País nacimiento (ESB - SGO) |  |
| CSP | Solicitudes RRHH | País (ESB - SGO) |  |
| CSP | Solicitudes RRHH | Comunidad Autónoma (ESB - SGO) |  |
| CSP | Solicitudes RRHH | Provincia (ESB - SGO) |  |
| CSP | Solicitudes RRHH | Área ANEP (ESB - SGO) |  |
| CSP | Proyectos | Tipo estado proyecto |  |
| CSP | Proyectos | Confidencial (Sí/No) |  |
| CSP | Proyectos | Paquetes trabajo (sí/no) |  |
| CSP | Proyectos | IVA deducible (Sí/No) |  |
| CSP | Proyectos | Causa exención |  |
| CSP | Proyecto - Contexto proyecto | Tipo propiedad resultados |  |
| CSP | Proyecto - Relaciones | Tipo entidad |  |
| CSP | Proyecto - Seguimiento científico - Documentos | Documento Visible (Sí/No) |  |
| CSP | Proyecto - Prórroga | Tipo prórroga |  |
| CSP | Proyecto - Prórroga - Documentos | Documento Visible (Sí/No) |  |
| CSP | Proyecto - Documentos | Documento Visible (Sí/No) |  |
| CSP | Proyecto - Configuración Económica - Presupuesto | ¿Desglosar en anualidades? (Sí/No) |  |
| CSP | Proyecto - Configuración Económica - Presupuesto - Datos generales | Presupuestar (Sí/No) |  |
| CSP | Proyecto - Configuración Económica - Facturación | Tipo Estado Validación IP |  |
| CSP | Proyecto - Socios - Periodos justificación - Documentos | Documento Visible (Sí/No) |  |
| CSP | Participación proyectos externos - Autorización | Tipo estado autorización |  |
| CSP | Participación proyectos externos - Autorización - Certificados autorización | Documento Visible (Sí/No) |  |
| CSP | Grupos investigación | Tipo Grupo |  |
| CSP | Grupos investigación | Grupo especial investigación (Sí/No) |  |
| CSP | Ejecución Económica - Seguimiento justificación | Tipo requerimiento.nombre | Está implementado como tabla |
| CSP | Ejecución Económica - Seguimiento justificación | Recurso estimado (Sí/No) |  |
|  |  |  |  |  |  |  |
| ETI | Solicitud evaluación proyectos | Tipo actividad |  |
| ETI | Solicitud evaluación proyectos | Tipo investigación tutelada |  |
| ETI | Solicitud evaluación proyectos | ¿Se dispone de financiación? (Sí/No) |  |
| ETI | Solicitud evaluación proyectos | Valor social |  |
| ETI | Solicitud evaluación proyectos | Estado financiación |  |
| ETI | Asignación tareas | Tipo Tarea |  |
| ETI | Asignación tareas | Formación específica |  |
| ETI | Memoria | Comité |  |
| ETI | Memoria | Listado de formularios (M10, M20, ...) | En principio sin internacionalización al considerarse códigos internos |
| ETI | Memoria | Estado memoria |  |
| ETI | Memoria | Estado retrospectiva |  |
| ETI | Memoria | Bloques |  |
| ETI | Memoria | Apartados |  |
| ETI | Memoria - Datos generales | Tipo Memoria |  |
| ETI | Memoria - Documentación | Tipo documento |  |
| ETI | Convocatorias de reunión | Tipo convocatoria reunión |  |
| ETI | Evaluaciones | Tipo dictamen |  |
| ETI | Actas | Tipo estado acta |  |
| ETI | Evaluadores | Tipo cargo comité |  |
|  |  |  |  |  |  |  |
| PII |  | Tipos de propiedad |  |
| PII | Configuración - Tramos reparto | Tipo de tramo |  |
| PII | Solicitud protección | Estado solicitud protección |  |
| PII | Ejecución económica - Contratos | Exclusividad (Sí/No) |  |
| PII | Ejecución económica - Ingresos | Estado invención ingreso |  |
| PII | Ejecución económica - Gastos | Estado invención gasto |  |
| PII | Ejecución económica - Reparto | Estado reparto |  |
|  |  |  |  |  |  |  |
| EER | Datos generales | Tipo empresa |  |
|  | Datos generales | Estado empresa |  |
|  | Documentos | Tipo documento.nombre | Listado implementado como tabla sin configuración |
|  | Documentos | Tipo documento.descripcion | Listado implementado como tabla sin configuración |
|  | Equipo empresarial - Composición sociedad | Tipo aportación |  |
|  | Equipo empresarial - Administración sociedad | Tipo administración |  |
|  |  |  |  |  |  |  |