# PII - Modelo lógico - Documentación

* [Entidades del modelo Protección Industrial e Intelectual](#PIIModelológicoDocumentación-EntidadesdelmodeloProtecciónIndustrialeIntelectual)
  + [Invencion](#PIIModelológicoDocumentación-Invencion)
  + [TipoProteccion](#PIIModelológicoDocumentación-TipoProteccion)
  + [InvencionSectorAplicacion](#PIIModelológicoDocumentación-InvencionSectorAplicacion)
  + [SectorAplicacion](#PIIModelológicoDocumentación-SectorAplicacion)
  + [InvencionAreaConocimiento](#PIIModelológicoDocumentación-InvencionAreaConocimiento)
  + [InvencionDocumento](#PIIModelológicoDocumentación-InvencionDocumento)
  + [InvencionPalabraClave](#PIIModelológicoDocumentación-InvencionPalabraClave)
  + [InvencionInventor](#PIIModelológicoDocumentación-InvencionInventor)
  + [PeriodoTitularidad](#PIIModelológicoDocumentación-PeriodoTitularidad)
  + [PeriodoTitularidadTitular](#PIIModelológicoDocumentación-PeriodoTitularidadTitular)
  + [InformePatentabilidad](#PIIModelológicoDocumentación-InformePatentabilidad)
  + [ResultadoInformePatentabilidad](#PIIModelológicoDocumentación-ResultadoInformePatentabilidad)
  + [SolicitudProteccion](#PIIModelológicoDocumentación-SolicitudProteccion)
  + [ViaProteccion](#PIIModelológicoDocumentación-ViaProteccion)
  + [TipoCaducidad](#PIIModelológicoDocumentación-TipoCaducidad)
  + [PaisValidado](#PIIModelológicoDocumentación-PaisValidado)
  + [Procedimiento](#PIIModelológicoDocumentación-Procedimiento)
  + [TipoProcedimiento](#PIIModelológicoDocumentación-TipoProcedimiento)
  + [ProcedimientoDocumento](#PIIModelológicoDocumentación-ProcedimientoDocumento)
  + [InvencionGasto](#PIIModelológicoDocumentación-InvencionGasto)
  + [SectorLicenciado](#PIIModelológicoDocumentación-SectorLicenciado)
  + [InvencionIngreso](#PIIModelológicoDocumentación-InvencionIngreso)
  + [Reparto](#PIIModelológicoDocumentación-Reparto)
  + [TramoReparto](#PIIModelológicoDocumentación-TramoReparto)
  + [RepartoGasto](#PIIModelológicoDocumentación-RepartoGasto)
  + [RepartoIngreso](#PIIModelológicoDocumentación-RepartoIngreso)
  + [RepartoEquipoInventor](#PIIModelológicoDocumentación-RepartoEquipoInventor)
* [Enumerados](#PIIModelológicoDocumentación-Enumerados)
  + [TipoPropiedad](#PIIModelológicoDocumentación-TipoPropiedad)
  + [EstadoSolicitudProteccion](#PIIModelológicoDocumentación-EstadoSolicitudProteccion)
  + [EstadoReparto](#PIIModelológicoDocumentación-EstadoReparto)
  + [EstadoInvencionGasto](#PIIModelológicoDocumentación-EstadoInvencionGasto)
  + [EstadoInvencionIngreso](#PIIModelológicoDocumentación-EstadoInvencionIngreso)
  + [TipoTramo](#PIIModelológicoDocumentación-TipoTramo)

### Entidades del modelo Protección Industrial e Intelectual

#### Invencion

Representa cada una de las invenciones para las que alguien estima oportuno solicitar su protección a través de solicitudes de protección de diferente naturaleza.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Invencion". |
| titulo : String  Texto corto identificativo de la invención. Obligatorio. |
| fechaComunicacion : Date  Fecha en la que se comunica la solicitud para gestionar la protección de una invención por parte de un investigador o de la propia OTRI. Formato fecha sin hora. Obligatorio. |
| descripcion : String  Texto descriptivo de la invención. Obligatorio. |
| tipoProteccionId : Long  Referencia al tipo de protección bajo el cuál se decide clasificar la invención. FK a la tabla TipoProteccion. Obligatorio. |
| proyectoRef : String  Referencia al proyecto de investigación con el que opcionalmente se relaciona la invención como origen de la misma. Opcional. |
| comentarios : String  Texto abierto para aportar comentarios acerca de la invención. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[1] | Target: Public (Class) InvencionIngreso  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[0..\*] | Target: Public (Class) TipoProteccion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[0..\*] | Target: Public (Class) Proyecto  Cardinality:[0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[1] | Target: Public (Class) InvencionGasto  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionInventor  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SectorLicenciado  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeriodoTitularidad  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionDocumento  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionAreaConocimiento  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionSectorAplicacion  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) DatoEconomico  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionPalabraClave  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |

#### **TipoProteccion**

Representa las diferentes modalidades a través de las cuales se puede clasificar una invención y que marcarán además a través de qué vías se podrá solicitar su protección.

Tendrá por defecto los siguientes valores, aunque el usuario podrá modificarlos, añadir otros o dar estos de baja:

* Propiedad Industrial

  + Patente
  + Modelo de utilidad
  + Diseño industrial
  + Marca
  + Secreto industrial.
* Propiedad Intelectual

  + Software
  + Know-how

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "TipoProteccion". |
| tipoPropiedad : String  Tipo de propiedad del tipo de protección. Los tipos de protección podrán tener uno de los tipos de propiedad del enumerado TipoPropiedad. Obligatorio. |
| nombre : String  Es el nombre identificativo del tipo, con el que se listará en todos los desplegables.Clave única respecto al resto de tipos del mismo nivel. Obligatorio. |
| descripcion : String  Campo de texto de introducción libre para descripción ampliada. Obligatorio. |
| padreId : Long  Identificador al tipo de protección padre en el caso de tenerlo. Aunque el modelo soporta varios niveles, el SGI actualmente solo soportará 2 por pantalla. Opcional. |
| activo : Boolean= True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) TipoPropiedad  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoProteccion  Cardinality:[0..\*] | Target: Public (Class) TipoProteccion  Cardinality:[0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[0..\*] | Target: Public (Class) TipoProteccion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoProteccion  Cardinality:[0..\*] | Target: Public (Class) TipoProteccion  Cardinality:[0..1] |

#### InvencionSectorAplicacion

Representa la relación entre una invención y un sector de aplicación. Una invención debe tener al menos un sector de aplicación asociado.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionSectorAplicacion". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| sectorAplicacionId : Long  Sector de aplicación al que pertenece el registro. Es una FK a la tabla "SectorAplicacion". Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionSectorAplicacion  Cardinality:[0..\*] | Target: Public (Class) SectorAplicacion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionSectorAplicacion  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |

#### **SectorAplicacion**

Representa la lista de sectores empresariales que podrían estar interesados en la invención. No se utilizan los códigos CNAE porque no se dispondrá de información tan detallada, por lo que será información de más alto nivel y distinta a la que se presenta a la hora de seleccionar clasificaciones CNAE. Se pueden asociar más de uno. Será obligatorio añadir al menos uno asociado a una invención.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "SectorAplicacion". |
| nombre : String  Nombre identificativo del sector de aplicación, con el que se listará en todos los desplegables. Obligatorio. Clave única. |
| descripcion : String  Campo de texto de introducción libre para descripción ampliada. Obligatorio. |
| activo : Boolean= True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionSectorAplicacion  Cardinality:[0..\*] | Target: Public (Class) SectorAplicacion  Cardinality:[1] |

#### InvencionAreaConocimiento

Representa la relación entre una invención y un área de conocimiento. Una invención debe tener al menos un área de conocimiento asociada. A efectos del usuario final, se denominan "Áreas de procedencia". Obligatorio.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionAreaConocimiento". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| areaConocimientoRef : String  Referencia al área de conocimiento asociada a la invención. Es una FK al modelo de datos del SGO. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionAreaConocimiento  Cardinality:[0..\*] | Target: Public (Class) AreaConocimiento  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionAreaConocimiento  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |

#### InvencionDocumento

Representa la relación entre una invención y un documento. Una invención deberá tener al menos asociado el documento de "Comunicación de invención" que el investigador entrega a la OTRI para solicitar que se proteja la misma.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionDocumento". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| documentoRef : String  Referencia al documento asociado a la invención. Clave ajena a otro modelo, el del SGDOC. Obligatorio. |
| nombre : String  Nombre que se quiere usar para identificar al documento. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionDocumento  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionDocumento  Cardinality:[0..1] | Target: Public (Class) Documento  Cardinality:[1] |

#### InvencionPalabraClave

Representa la relación enter una invención y una palabra clave.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionPalabraClave". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| palabraClave : String  Valor de la palabra clave con la que se asocia la invención. Será una clave ajena al modelo del SGO. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionPalabraClave  Cardinality:[0..\*] | Target: Public (Class) PalabraClave  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionPalabraClave  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |

#### **InvencionInventor**

Representa la relación entre una invención y un autor/inventor de la misma. Cada invención debe tener reflejado en el SGI la lista completa de autores, esto es, el % de participación de todos los autores que se asocien a ella debe sumar el 100%.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InventorInvencion". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| inventorRef : String  Referencia al inventor/autor de la invención. Es una clave ajena al modelo SGP que se encuentra en otro esquema de BBDD.Obligatorio. |
| participacion : Decimal  Porcentaje de participación de autoría en la invención del miembro del equipo inventor. Podrá tener un valor mayor que 0 y menor o igual que 100. Numérico decimal con 2 decimales. Obligatorio. |
| repartoUniversidad : Boolean  Indicador de si al miembro del equipo inventor se le hará el reparto de resultados por parte de la Universidad o no. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionInventor  Cardinality:[1..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionInventor  Cardinality:[0..\*] | Target: Public (Class) Persona  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] | Target: Public (Class) InvencionInventor  Cardinality:[1] |

#### PeriodoTitularidad

Representa cada uno de los intervalos de tiempo durante los que un grupo de empresas determinado regenta la titularidad de una invención. No se podrán solapar unos períodos con otros.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "PeriodoTitularidad". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| fechaInicio : Date  Fecha de inicio del periodo de titularidad. Formato fecha sin hora. Obligatorio. |
| fechaFin : Date  Fecha de fin del periodo de titularidad. Formato fecha sin hora. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeriodoTitularidad  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeriodoTitularidadTitular  Cardinality:[0..\*] | Target: Public (Class) PeriodoTitularidad  Cardinality:[1] |

#### PeriodoTitularidadTitular

Representa la relación entre cada uno de los períodos de titularidad y cada titular de la invención.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "PeriodoTitularidadTitular". |
| periodoTitularidadId : Long  Período de titularidad al que pertenece el registro. Es una FK a la tabla "PeriodoTitularidad". Obligatorio. |
| titularRef : String  Referencia a la entidad titular de la invención. Es una FK al modelo del SGEMP. Obligatorio. |
| participacion : Decimal  Porcentaje de participación en la titularidad en la invención. Podrá tener un valor mayor o igual que 0 (indicando así que una entidad deja de ser titular por ejemplo) y menor o igual que 100. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeriodoTitularidadTitular  Cardinality:[0..\*] | Target: Public (Class) PeriodoTitularidad  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeriodoTitularidadTitular  Cardinality:[0..\*] | Target: Public (Class) Empresa  Cardinality:[1] |

#### InformePatentabilidad

Representa cada uno de los informes que se pueden emitir sobre una invención evaluando su posible "patentabilidad" o la viabilidad de que se apruebe una solicitud de protección para la misma.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InformePatentabilidad". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| fecha : Date  Fecha a dar al informe de patentabilidad asociado a la invención. Fecha sin hora. Obligatorio. |
| nombre : String  Nombre a dar al informe de patentabilidad asociado a la invención. Obligatorio. |
| documentoRef : String  Referencia al documento de informe de patentabilidad que se asocia a la invención. FK al modelo del SGDOC. Obligatorio. |
| resultadoId : Long  Resultado asociado al informe de patentabilidad. Es una FK a la tabla "ResultadoInformePatentabilidad". Obligatorio. |
| entidadCreadoraRef : String  Referencia a la entidad/empresa que ha realizado el informe. Será una FK al modelo del SGEMP. Obligatorio. |
| contactoEntidadCreadora : String  Persona de contacto de la entidad creadora del informe de patentabilidad. Obligatorio. |
| contactoExaminador : String  Contacto del examinador del informe de patentabilidad. Obligatorio. |
| comentarios : String  Comentarios acerca del informe de patentabilidad. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality: [0..\*] | Target: Public (Class) Empresa  Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality: [0..\*] | Target: Public (Class) ResultadoInformePatentabilidad  Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality: [0..1] | Target: Public (Class) Documento  Cardinality: [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality: [0..\*] | Target: Public (Class) Invencion  Cardinality: [1] |

#### **ResultadoInformePatentabilidad**

Representa cada uno de los posibles resultados que se pueden asociar a un informe de patentabilidad. Tendrá por defecto los siguientes valores: Favorable, Desfavorable, pero se podrán modificar, dar de baja o añadir otros por parte del usuario.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "ResultadoInformePatentabilidad". |
| nombre : String  Es el nombre identificativo del resultado de informe de patentabilidad, con el que se listará en todos los desplegables. Clave única. Obligatorio. |
| descripcion : String  Campo de texto de introducción libre para descripción ampliada. Obligatorio. |
| activo : Boolean= True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InformePatentabilidad  Cardinality:[0..\*] | Target: Public (Class) ResultadoInformePatentabilidad  Cardinality:[1] |

#### **SolicitudProteccion**

Representa cada una de las solicitudes para proteger una invención que se presentan tanto a organismos públicos como privados o incluso internos a la propia Universidad.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "SolicitudProteccion". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| titulo : String  Título de la solicitud de protección. Obligatorio. |
| fechaPrioridadSolicitud : Date  Fecha de la solicitud que, en caso de primera solicitud que NO sea Extensión internacional, esto es, que su vía de protección asociada sea del tipo extensión internacional = "Sí" (PCT p.ej.), será además la fecha de inicio de la prioridad. Formato fecha sin hora. Obligatorio. |
| fechaFinPriorPresFasNacRec : Date  Fecha de finalización de la prioridad de la solicitud o de fin del plazo de presentación de solicitudes en fases nacionales/regionales. Si la solicitud NO es la primera solicitud de la invención, este campo no estará informado salvo que la vía de protección sea del tipo extensión internacional = "Sí" (PCT p.ej.). Solo se podrá informar para la protección industrial y, en ese caso, será obligatorio. Formato fecha sin hora. |
| viaProteccionId : Long  Referencia a la vía de protección asociada a la solicitud de protección. FK a la tabla ViaProteccion. Obligatorio. |
| paisProteccionRef : String  Referencia al identificador del país para el que se hace la solicitud de protección en el caso de que la solicitud tenga una vía de protección asociada que tenga opción de presentarse en varios países (variosPaises = true en tabla ViaProteccion).Es una FK a la tabla "Pais" del modelo del módulo SGO. Obligatorio si se selecciona una vía de protección del tipo indicado, opcional en otro caso. |
| numeroSolicitud : String  Número de la solicitud que es comunicada por el organismo donde se solicita. Obligatorio. |
| numeroRegistro : String  Número del registro que es comunicada por el organismo que concede la protección. Solo se podrá informar para la protección intelectual y, en ese caso, será opcional. |
| estado : String  Estado de la solicitud. Las solicitudes podrán tener uno de los estados del enumerado EstadoSolicitudProteccion. Al crear la solicitud se establecerá por defecto el valor "Solicitada" para su estado de manera implícita. Solo estará informado para la protección industrial y, en ese caso, será obligatorio. |
| fechaPublicacion : Date  Fecha de publicación de la solicitud de invención. Solo se podrá informar para la propiedad industrial y, en ese caso, será opcional. Formato fecha sin hora. |
| numeroPublicacion : String  Número de la publicación que es comunicada por el organismo donde se publica. Solo se podrá informar para la propiedad industrial y, en ese caso, será opcional. |
| fechaConcesion : Date  Fecha de concesión de la solicitud de protección. Solo se podrá informar para la propiedad industrial y, en ese caso, será opcional.Formato fecha sin hora. |
| numeroConcesion : String  Número de la concesión que es comunicada por el organismo que concede la protección. Solo se podrá informar para la propiedad industrial y, en ese caso, será opcional. |
| fechaCaducidad : Date  Fecha de caducidad de la solicitud de invención. Solo estará informada para la protección industrial y si el estado es o se cambia a "Caducada" y, en ese caso, será obligatorio indicarla. Formato fecha sin hora. |
| agentePropiedad : agentePropiedadRef  Agente de la propiedad asociado a la solicitud de protección. Referencia a una entidad dentro del modelo del SGEMP. Solo podrá estar informada para la propiedad industrial y, en ese caso, será opcional. |
| tipoCaducidadId : Long  Referencia al tipo de caducidad de la solicitud de invención. FK a TipoCaducidad. Solo estará informada para la propiedad industrial y si el estado es o se cambia a "Caducada" y, en ese caso, será obligatorio indicarla. |
| comentarios : String  Campo de texto abierto con comentarios a la solicitud de protección. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoSolicitudProteccion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[1] | Target: Public (Class) PaisValidado  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) Empresa  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) Pais  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[1] | Target: Public (Class) InvencionGasto  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) TipoCaducidad  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[0..\*] | Target: Public (Class) SolicitudProteccion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ViaProteccion  Cardinality:[1] | Target: Public (Class) SolicitudProteccion  Cardinality:[0..\*] |

#### **ViaProteccion**

Representa los diferentes mecanismos o vías por las que se puede solicitar proteger / explotar una invención.Las vías de protección posibles irán acorde al tipo de propiedad asociado al tipo de protección que tenga la invención, es por ello que existirá una lista de vías de protección asociada a "Propiedad intelectual" y otra a "Propiedad industrial".

A priori esta lista tendrá los siguientes valores:

* Protecciones de tipo "Protección industrial":

  + España
  + PCT
  + Europea
  + País específico
* Protecciones de tipo "Protección intelectual":

  + Registro autonómico
  + Acta notarial
  + Registro interno

En todo caso, esta lista es configurable en el SGI.

Si se selecciona una vía de protección con el indicador de que dicha vía es por país = "Sí" (País específico p.ej.), se deberá informar además el campo pais en la solicitud de protección.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "ViaProteccion". |
| nombre : String  Es el nombre identificativo del tipo, con el que se listará en todos los desplegables. Clave única. Obligatorio. |
| descripcion : String  Campo de texto de introducción libre para descripción ampliada. Obligatorio. |
| tipoPropiedad : String  Tipo de propiedad de la vía de protección. Las vías de protección podrán tener uno de los tipos de propiedad del enumerado TipoPropiedad. Obligatorio. |
| mesesPrioridad : Integer  Meses de prioridad a aplicar cuando la solicitud es la primera de una invención o de plazo para la entrada a las fases nacionales / regionales en el caso concreto de solicitudes que sean extensión internacional (p.ej. vía PCT). Solo aplicará al Tipo de propiedad "Propiedad industrial". Numérico entero. Obligatorio. |
| paisEspecifico : Boolean  Indicador de si al ser seleccionada esta vía para una solicitud de protección ha de mostrarse el desplegable de países para elegir uno concreto. Opcional. |
| extensionInternacional : Boolean  Indicador de si al ser seleccionada esta vía para una solicitud de protección se ha de gestionar la solicitud como una extensión a varios países (p.e. como una PCT). Opcional. |
| variosPaises : Boolean  Indicador de si al asociar esta vía a una solicitud de protección se pueden informar un listado de países en los que se ha validado la invención a través de la misma. Opcional. |
| activo : Boolean= True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ViaProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) TipoPropiedad  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) ViaProteccion  Cardinality:[1] | Target: Public (Class) SolicitudProteccion  Cardinality:[0..\*] |

#### **TipoCaducidad**

Representa los diferentes tipos de caducidad por los que puede dejar de estar en proceso de tramitación pasado un tiempo una solicitud de protección. Por defecto estará precargada con los valores:

* Abandono
* Retirada
* Denegación

No será gestionada por el usuario final pero sí se podrán añadir, eliminar o modificar valores por BBDD.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "TipoCaducidad". |
| descripcion : String  Descripción identificativa del tipo de caducidad con el que se presentará en los desplegables. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Class) TipoCaducidad  Cardinality:[1] |

#### PaisValidado

Representa cada uno de los países en los que se ha validado el uso de una licencia de una invención a través de una solicitud de protección de vía Europea.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "PaisValidado". |
| fechaValidacion : Date  Fecha en la que se valida el uso de una licencia de una invención, a través de una solicitud de protección, en un país concreto. Formato fecha sin hora. Obligatorio. |
| paisRef : String  Referencia al identificador del país para el que se valida el uso de una licencia de invención a través de una solicitud de protección.Es una FK a la tabla "Pais" del modelo del módulo SGO. Obligatorio. |
| codigoInvencion : String  Código identificativo de la licencia de uso de una invención en un país. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PaisValidado  Cardinality:[0..\*] | Target: Public (Class) Pais  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[1] | Target: Public (Class) PaisValidado  Cardinality:[0..\*] |

#### **Procedimiento**

Representa cada una de las anotaciones que se quieren registrar a lo largo del tiempo relacionadas con una solicitud de protección y de las que se quiere dejar constancia de documentación, acciones a tomar y los comentarios que se consideren oportunos.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Procedimiento". |
| solicitudProteccionId : Long  Solicitud de protección a la que pertenece el registro. Es una FK a la tabla "SolicitudProteccion". Obligatorio. |
| fecha : Date  Fecha de registro del procedimiento asociado a la solicitud. Formato fecha sin hora. Obligatorio. |
| tipoId : Long  Tipo de procedimiento al que se asocia el registro. Es una FK a la tabla "TipoProcedimiento". Obligatorio. |
| accionATomar : String  Acciones a tomar en el procedimiento asociado a la solicitud. Opcional. |
| fechaLimiteAccion : Date  Fecha límite del procedimiento asociado a la solicitud. Será obligatorio únicamente si el campo aviso está a True. Esta fecha será utilizada para programar el envío de un aviso en el módulo de comunicados. Formato fecha sin hora. Opcional. |
| aviso : Boolean  Indicador de si el procedimiento ha de generar un aviso o no una vez se alcance la fecha límite para realizar la acción indicada en el procedimiento. Opcional. |
| observaciones : String  Campo de texto abierto con observaciones al procedimiento. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[1] | Target: Public (Class) ProcedimientoDocumento  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[0..\*] | Target: Public (Class) SolicitudProteccion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[0..\*] | Target: Public (Class) TipoProcedimiento  Cardinality:[1] |

#### **TipoProcedimiento**

Representa los diferentes tipos de procedimiento que se podrán asociar a los procedimientos.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "TipoProcedimiento". |
| nombre : String  Nombre identificativo del tipo de procedimiento, con el que se listará en todos los desplegables. Clave única. Obligatorio. |
| descripcion : String  Descripción del tipo de procedimiento. Obligatorio. |
| activo : Boolean= True  Indicador de si el registro está activo o no en el SGI. Obligatorio. Por defecto tendrá valor True. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[0..\*] | Target: Public (Class) TipoProcedimiento  Cardinality:[1] |

#### ProcedimientoDocumento

Representa la relación de un procedimiento con un documento en el Sistema de Gestión de Documentos (SGDOC).

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "ProcedimientoDocumento". |
| procedimientoId : Long  Procedimiento al que pertenece el registro. Es una FK a la tabla "Procedimiento". Obligatorio. |
| documentoRef : String  Referencia al documento de procedimiento al que se asocia el mismo. FK al modelo del SGDOC. Obligatorio. |
| nombre : String  Nombre identificativo del documento asociado al procedimiento. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ProcedimientoDocumento  Cardinality:[0..1] | Target: Public (Class) Documento  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Procedimiento  Cardinality:[1] | Target: Public (Class) ProcedimientoDocumento  Cardinality:[0..\*] |

#### **InvencionGasto**

Representa la relación entre una invención y cada uno de los gastos incluidos en los diferentes procesos de reparto de la misma.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionGasto". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| gastoRef : String  Referencia al gasto. FK al modelo del Sistema de Gestión Económica de la Protección Industrial e Intelectual (SGEPII). Obligatorio. |
| estado : String  Estado del gasto asociado a la invención dentro del proceso de reparto en el que se incluye. Tomará uno de los valores del enumerado EstadoInvencionGasto. Obligatorio. |
| importePendienteDeducir : Decimal  Importe que queda por deducir del gasto. Obligatorio. |
| solicitudProteccion : solicitudProteccionId  Referencia al la solicitud de protección con la que opcionalmente se relaciona el gasto por ser origen del mismo. FK a SolicitudProteccion. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[0..\*] | Target: Public (Class) TipoGasto  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoInvencionGasto  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[1] | Target: Public (Class) RepartoGasto  Cardinality:[1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[0..1] | Target: Public (Class) DatoEconomico  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[1] | Target: Public (Class) InvencionGasto  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[1] | Target: Public (Class) InvencionGasto  Cardinality:[0..\*] |

#### **SectorLicenciado**

Representa cada uno de los sectores en los que a través de contratos de regalías o de explotación de invenciones se conceden licencias de uso de una invención para un país y por un plazo de tiempo establecido.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "SectorLicenciado". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion".Obligatorio. |
| contratoRef : String  Referencia al contrato asociado a la licencia por país, sector y plazo. Es una FK a la tabla "Proyecto" del modelo del módulo CSP. |
| sectorId : Long  Sector de aplicación a la que pertenece el registro. Es una FK a la tabla "SectorAplicacion". Obligatorio. |
| paisRef : String  Referencia al identificador del país al que corresponde la licencia del sector de aplicación.Es una FK a la tabla "Pais" del modelo del módulo SGO. Obligatorio. |
| exclusividad : Boolean  Indicador de si la licencia es en exclusiva o no. Valores: true o false. Obligatorio. |
| fechaInicioLicencia : Date  Fecha de inicio de la vigencia de la licencia para el sector y país indicado. Obligatorio. |
| fechaFinLicencia : Date  Fecha de fin de la vigencia de la licencia para el sector y país indicado. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) SectorLicenciado  Cardinality:[0..\*] | Target: Public (Class) Convocatorias, Ayudas, Proyectos, Contratos :: Contrato  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SectorLicenciado  Cardinality:[0..\*] | Target: Public (Class) Invencion  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SectorLicenciado Cardinality:[0..\*] | Target: Public (Class) Pais  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) SectorLicenciado | Target: Public (Class) Clasificacion |

#### **InvencionIngreso**

Representa la relación entre una invención y cada uno de los ingresos incluidos en los diferentes procesos de reparto de la misma.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "InvencionIngreso". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| ingresoRef : String  Referencia al ingreso. FK al modelo del Sistema de Gestión Económica de la Protección Industrial e Intelectual (SGEPII). Obligatorio. |
| estado : String  Estado del ingreso asociado a la invención dentro del proceso de reparto en el que se incluye. Tomará uno de los valores del enumerado EstadoInvencionIngreso. Obligatorio. |
| importePendienteRepartir : Decimal  Importe que queda por repartir del ingreso. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[1] | Target: Public (Class) RepartoIngreso  Cardinality:[1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoInvencionIngreso  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[0..1] | Target: Public (Class) Factura  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[0..1] | Target: Public (Class) DatoEconomico  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Invencion  Cardinality:[1] | Target: Public (Class) InvencionIngreso  Cardinality:[0..\*] |

#### Reparto

Representa cada uno de los actos de reparto del beneficio de la explotación de invenciones a través de licencias que realizarán los usuarios gestores del SGI.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Reparto". |
| invencionId : Long  Invención a la que pertenece el registro. Es una FK a la tabla "Invencion". Obligatorio. |
| fecha : Date  Fecha en la que se crea el reparto. Formato fecha + hora. Obligatorio. |
| importeUniversidad : Decimal  Importe que se asigna a la universidad en el reparto. Obligatorio. |
| importeEquipoInventor : Decimal  Importe que se asigna al equipo inventor en el reparto. Obligatorio. |
| estado : String  Estado del reparto. Será uno de los posibles valores del enumerado "EstadoReparto". Mientras el reparto esté en estado "Pendiente de ejecutar" se podrán realizar modificaciones en él. En el estado "Ejecutado" ya no se podrá modificar. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[1] | Target: Public (Class) RepartoIngreso  Cardinality:[1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[1] | Target: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoReparto  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoGasto  Cardinality:[1..\*] | Target: Public (Class) Reparto  Cardinality:[1] |

#### **TramoReparto**

Representa la configuración de cómo se propondrá por defecto por parte del SGI realizar la distribución del reparto en % de beneficios de las invenciones entre Universidad e inventores, en función del tramo en el que se encuentre el valor de ese beneficio.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "TramoReparto". |
| orden : Integer  Orden del tramo entre 1 y el número de tramos siendo el 1 indicador de que es el primer tramo y el máximo de que es el último. Se utiliza para su presentación por pantalla de forma ordenada de menor a mayor valor del límite superior del tramo. Obligatorio. |
| desde : Integer  Valor inicial del intervalo entre el que debe estar el beneficio del reparto para que el reparto de % de este tramo aplique. Obligatorio. |
| hasta : Integer  Valor final del intervalo entre el que debe estar el beneficio del reparto para que el reparto de % de este tramo aplique. Obligatorio. |
| porcentajeUniversidad : Decimal  Valor del % de reparto a la Universidad que aplica cuando el beneficio esté dentro del tramo. Obligatorio. |
| porcentajeInventores : Decimal  Valor del % de reparto a los miembros del equipo inventor que aplica cuando el beneficio esté dentro del tramo. Obligatorio. |
| tipoTramo : String  Indicador de si es necesario indicar para el tramo los límites superior, inferior o ambos. Utiliza para ello los valores del enumerado TipoTramo. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TramoReparto  Cardinality:[0..\*] | Target: Public (Enumeration) TipoTramo  Cardinality:[1] |

#### RepartoGasto

Representa cada uno de los gastos que se han incluido en un reparto.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "RepartoGasto". |
| repartoId : Long  Reparto al que pertenece el registro. Es una FK a la tabla "Reparto". Obligatorio. |
| invencionGastoId : Long  Gasto de la invención concreto al que se asocia el registro. Es una FK a la tabla "InvencionGasto". Obligatorio. |
| importeADeducir : Decimal  Valor del importe del gasto a deducir. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoGasto  Cardinality:[1..\*] | Target: Public (Class) Reparto  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[1] | Target: Public (Class) RepartoGasto  Cardinality:[1..\*] |

#### RepartoIngreso

Representa cada uno de los ingresos que se han incluido en un reparto.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "RepartoIngreso". |
| repartoId : Long  Reparto al que pertenece el registro. Es una FK a la tabla "Reparto".Obligatorio. |
| invencionIngresoId : Long  Ingreso de la invención concreto al que se asocia el registro. Es una FK a la tabla "InvencionIngreso". Obligatorio. |
| importeARepartir : Decimal  Valor del importe del ingreso a repartir. Obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[1] | Target: Public (Class) RepartoIngreso  Cardinality:[1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[1] | Target: Public (Class) RepartoIngreso  Cardinality:[1..\*] |

#### **RepartoEquipoInventor**

Representa cómo se desglosa por cada inventor y concepto el importe que en el reparto asociado se ha destinado al equipo inventor.

| **ATTRIBUTES** |
| --- |
| id : Long  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "RepartoEquipoInventor". |
| repartoId : Long  Reparto al que pertenece el registro. Es una FK a la tabla "Reparto". Obligatorio. |
| invencionInventorId : Long  Miembro del equipo inventor al que pertenece el registro. Es una FK a la tabla "InvencionInventor". Obligatorio. |
| importeNomina : Decimal  Importe correspondiente al reparto para el miembro del equipo inventor que se va a realizar al miembro del equipo inventor en nómina. Opcional. |
| importeProyecto : Decimal  Importe correspondiente al reparto para el miembro del equipo inventor que se va a repercutir hacia un proyecto. Opcional. |
| importeOtros : Decimal  Importe correspondiente al reparto para el miembro del equipo inventor que se va a retribuir en cualquier otra forma que no sea en nómina o a un proyecto.  Contempla por ejemplo el caso de los repartos de regalías a miembros del equipo inventor que ya no tienen vinculación con la Universidad pero ésta sí sigue teniendo obligación de realizarles estos pagos de repartos. Opcional. |
| proyectoRef : String  Proyecto al que se asocia el registro. Es una FK a la tabla "Proyecto" perteneciente a otro esquema de BBDD, al del módulo CSP.  Será el proyecto al que destinar la parte del reparto indicado en el campo Importe a proyecto.  Este campo podrá estar informado si se indica un valor > 0 en el campo Importe a proyecto. Opcional. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] | Target: Public (Class) Proyecto  Cardinality:[0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] | Target: Public (Class) Persona  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] | Target: Public (Class) InvencionInventor  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[1] | Target: Public (Class) RepartoEquipoInventor  Cardinality:[0..\*] |

### **Enumerados**

#### TipoPropiedad

Enumerado que contiene los posibles tipos de protección con los que se puede asociar una invención. Valores:

* Propiedad industrial
* Propiedad intelectual

| **ATTRIBUTES** |
| --- |
| Propiedad industrial : Long |
| Propiedad intelectual : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ViaProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) TipoPropiedad  Cardinality:[1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) TipoPropiedad Cardinality:[1] |

#### EstadoSolicitudProteccion

Enumerado que contiene los posibles estados de las solicitudes de protección. Valores:

* Solicitada
* Publicada
* Concedida
* Caducada

| **ATTRIBUTES** |
| --- |
| Solicitada : Long |
| Publicada : Long |
| Concedida : Long |
| Caducada : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) SolicitudProteccion  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoSolicitudProteccion Cardinality:[1] |

#### EstadoReparto

Enumerado que contiene los posibles estados del reparto de beneficios de las licencias de explotación de las invenciones. Valores:

* Pendiente de ejecutar: aún no se ha realizado el pago del reparto.
* Ejecutado: ya se ha llevado a cabo el pago del reparto.

| **ATTRIBUTES** |
| --- |
| Pendiente de ejecutar : Long |
| Ejecutado : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Reparto  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoReparto  Cardinality:[1] |

#### EstadoInvencionGasto

Enumerado que contiene los posibles estados de los gastos en su relación con una invención. Valores:

* Sin deducir: aún no se ha deducido este gasto dentro de ningún proceso de reparto.
* Parcialmente deducido: se ha deducido parcialmente este gasto dentro de un proceso de reparto, aún le queda parte de importe sin deducir.
* Deducido:se ha deducido totalmente este gasto dentro de un proceso de reparto.

| **ATTRIBUTES** |
| --- |
| Sin deducir (No) : Long |
| Parcialmente deducido (Parcialmente) : Long |
| Deducido (Sí) : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionGasto  Cardinality:[0..\*] | Target: Public (Enumeration) EstadoInvencionGasto Cardinality:[1] |

#### EstadoInvencionIngreso

Enumerado que contiene los posibles estados de los ingresos en su relación con una invención. Valores:

* Sin repartir: aún no se ha repartido este ingreso dentro de ningún proceso de reparto.
* Parcialmente repartido: se ha repartido parcialmente este ingreso dentro de un proceso de reparto, aún le queda parte de importe sin repartir.
* Repartido:se ha repartido totalmente este ingreso dentro de un proceso de reparto.

| **ATTRIBUTES** |
| --- |
| Sin repartir (No) : Long |
| Parcialmente repartido (Parcialmente) : Long |
| Repartido (Sí) : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) InvencionIngreso  Cardinality:[0..\*] | Target: Public (Enumeration)  EstadoInvencionIngreso Cardinality:[1] |

#### TipoTramo

Enumerado que contiene los tipos de tramo de reparto de beneficios de las licencias de explotación de las invenciones. Valores:

* Inicial: el límite inferior se considera por defecto 1, aunque no es necesario indicarlo expresamente.
* Intermedio: tiene valor tanto en el campo desde como en hasta, ambos límites están especificados.
* Final: no tiene límite superior, aplicará a cualquier beneficio > desde

| **ATTRIBUTES** |
| --- |
| Inicial : Long |
| Intermedio : Long |
| Final : Long |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TramoReparto  Cardinality:[0..\*] | Target: Public (Enumeration) TipoTramo  Cardinality:[1] |