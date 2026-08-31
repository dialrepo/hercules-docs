# CSP-Grupo - Modelo lógico multiidioma - Documentación

* [Entidades del modelo CSP Grupo Investigación](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadesdelmodeloCSPGrupoInvestigación)

  - [Entidad grupo: "grupo"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadgrupo:"grupo")
  - [Entidad Nombre de un grupo: "GrupoNombre"](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadNombredeungrupo:"GrupoNombre")
  - [Entidad Resumen de un grupo: "GrupoResumen"](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadResumendeungrupo:"GrupoResumen")
  - [Entidad enlaces de un grupo: "GrupoEnlace"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadenlacesdeungrupo:"GrupoEnlace")
  - [Entidad equipo del grupo "GrupoEquipo"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadequipodelgrupo"GrupoEquipo")
  - [Entidad equipo instrumental del grupo: "GrupoEquipoInstrumental"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadequipoinstrumentaldelgrupo:"GrupoEquipoInstrumental")
  - [Entidad Nombre de un equipo instrumental: "GrupoEquipoInstrumentalNombre"](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadNombredeunequipoinstrumental:"GrupoEquipoInstrumentalNombre")
  - [Entidad Descripción de un equipo instrumental: "GrupoEquipoInstrumentalDescripcion"](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadDescripcióndeunequipoinstrumental:"GrupoEquipoInstrumentalDescripcion")
  - [Entidad histórico grupo especial: "GrupoEspecialInvestigacion"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadhistóricogrupoespecial:"GrupoEspecialInvestigacion")
  - [Entidad clasificación de las líneas de investigación del grupo: "GrupoLineaClasificacion"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadclasificacióndelaslíneasdeinvestigacióndelgrupo:"GrupoLineaClasificacion")
  - [Entidad línea de investigación del equipo instrumental del grupo: "GrupoLineaEquipoInstrumental"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadlíneadeinvestigacióndelequipoinstrumentaldelgrupo:"GrupoLineaEquipoInstrumental")
  - [Entidad línea de investigación del grupo: "GrupoLineaInvestigacion"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadlíneadeinvestigacióndelgrupo:"GrupoLineaInvestigacion")
  - [Entidad línea de investigación de los miembros del grupo: "GrupoLineaInvestigador"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadlíneadeinvestigacióndelosmiembrosdelgrupo:"GrupoLineaInvestigador")
  - [Entidad palabras clave del grupo: "GrupoPalabraClave"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadpalabrasclavedelgrupo:"GrupoPalabraClave")
  - [Entidad persona autorizada del grupo: "GrupoPersonaAutorizada"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadpersonaautorizadadelgrupo:"GrupoPersonaAutorizada")
  - [Entidad responsable económico del grupo: "GrupoResponsableEconomico"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadresponsableeconómicodelgrupo:"GrupoResponsableEconomico")
  - [Entidad histórico de tipos del grupo: "GrupoTipo"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadhistóricodetiposdelgrupo:"GrupoTipo")
  - [Entidad línea de investigación: "LineaInvestigacion"](#CSPGrupoModelológicomultiidiomaDocumentación-Entidadlíneadeinvestigación:"LineaInvestigacion")
  - [Entidad Nombre de una línea de investigación: "LineaInvestigacionNombre"](#CSPGrupoModelológicomultiidiomaDocumentación-EntidadNombredeunalíneadeinvestigación:"LineaInvestigacionNombre")+ [Enumerados del modelo CSP Grupo](#CSPGrupoModelológicomultiidiomaDocumentación-EnumeradosdelmodeloCSPGrupo)
    - [Enumerado tipo de dedicación: "Dedicacion"](#CSPGrupoModelológicomultiidiomaDocumentación-Enumeradotipodededicación:"Dedicacion")
    - [Enumerado tipo de grupo: "TipoGrupo"](#CSPGrupoModelológicomultiidiomaDocumentación-Enumeradotipodegrupo:"TipoGrupo")

## Entidades del modelo CSP Grupo Investigación

#### Entidad grupo: "grupo"

Entidad principal del modelo lógico de Grupos de investigación. Representa a agrupaciones estables de personal investigador que coopera en una o varias líneas de investigación. Forman equipos de trabajo específicos para realizar proyectos de investigación que pueden durar varios años.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "grupo". |
| fechaInicio : Timestamp Private  Fecha de inicio del grupo de investigación. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin del grupo de investigación. |
| proyectoSGERef : String Private  Código con el que se va a identificar el grupo de investigación en el SGE (Sistema de gestión económico). |
| solicitud : Solicitud Private  Identificador de la Solicitud concedida de la que se contituyó el grupo de investigación. Solo estará informado en caso que la solicitud esté registrada en el SGI. Es una FK a la tabla "solicitud". |
| codigo : String Private  Es un código identificativo del grupo de investigación. Debe de ser un campo único y obligatorio. |
| tipo : GrupoTipo Private  Indica el grado de madurez actual del grupo de investigación. Es una FK a la tabla "grupo tipo" |
| especialInvestigacion : GrupoEspecialInvestigacion Private  Indica si el grupo de investigación en el moment o actual es un "grupo especial de investigación". Es una FK a la tabla "grupo especial investigación" |
| departamentoOrigenRef : String Private  Identificador del departamento al que esta adscrito el investigador principal del grupo de investigación en el momento de la solicitud de constitución del grupo o creación del grupo. |
| activo : Boolean Private  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro (grupo) está activo mientras que un valor "false" será indicativo de que el registro (grupo) ha sido eliminado a nivel de usuario. Es un campo obligatorio. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoEquipo  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoPalabraClave  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumental  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoEnlace  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoTipo  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1..] | Target: Public (Class) GrupoResponsableEconomico  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoEspecialInvestigacion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1..] | Target: Public (Class) GrupoPersonaAutorizada  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality:  [1] | Target: Public (Class) Grupo  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoNombre  Cardinality:  [1..\*] | Target: Public (Class) Grupo  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoResumen  Cardinality:  [0..\*] | Target: Public (Class) Grupo  Cardinality:  [1] |

#### Entidad Nombre de un grupo: "GrupoNombre"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre de un grupo de investigación. El nombre de un grupo es un campo de texto y es de introducción obligatoria. Está disponible en la pantalla de Datos generales de un grupo.

| **ATTRIBUTES** |
| --- |
| grupo : Grupo  Private  Grupo de investigación al que pertenece el nombre. Es una FK a la tabla "Grupo" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo nombre del grupo. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo nombre del grupo de investigación. Está expresado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoNombre  Cardinality:  [1..\*] | Target: Public (Class) Grupo  Cardinality:  [1] |

#### Entidad Resumen de un grupo: "GrupoResumen"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el campo resumen de un grupo de investigación. El resumen es un campo de texto para recoger el sumario o presentación de un grupo. Es un campo opcional. Está disponible en la pantalla de Datos generales del grupo.

| **ATTRIBUTES** |
| --- |
| grupo : Grupo  Private  Grupo de investigación al que pertenece el resumen. Es una FK a la tabla "Grupo" |
| lang : String  Private  Idioma en el que está almacenado el valor del campo resumen del grupo. El idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor del campo resumen del grupo de investigación. Está expresado en el idioma indicado por el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoResumen  Cardinality:  [0..\*] | Target: Public (Class) Grupo  Cardinality:  [1] |

#### Entidad enlaces de un grupo: "GrupoEnlace"

Enlaces (en formato URL) que se considere útil y/o necesario recoger en los datos del grupo.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupo : Grupo Private  Identificador del grupo al que pertenece el enlace. Es una FK a la tabla "grupo". Es un campo obligatorio. |
| enlace : String Private  Url de la página web con la información de interés. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1] | Target: Public (Class) GrupoEnlace  Cardinality: [0..\*] |

#### Entidad equipo del grupo "GrupoEquipo"

Entidad que contiene los miembros del Grupo, tanto actuales como todo su histórico.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Identificador de la tabla. |
| grupo : Grupo Private  Identificador del Grupo al que pertenece la persona referenciada. Es una FK a la tabla "grupo". Es un campo obligatorio.  Es una FK a la tabla "grupo". Es un campo obligatorio. |
| personaRef : String Private  Identificador o Referencia de la persona miembro del equipo de grupo. Es el identificador de la persona en el sistema de personas de la Universidad. Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha de inicio de la participación del miembro del equipo con el rol seleccionado. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin de la participación del miembro del equipo con el rol seleccionado. |
| rol : RolProyecto Private  Identificador del rol con el que participa el miembro en el Grupo de investigación. Es un FK a la tabla "rol proyecto". Es un campo obligatorio. |
| dedicacion : Dedicacion Private  Tipo de dedicación del miembro en el grupo. Toma el valor del enumerado "dedicación". |
| participacion : BigDecimal Private  Porcentaje de dedicación del miembro en el equipo (de forma relativa a su participación en grupos de investigación, sin considerar su participación en otras actividades de investigación, docencia, etc.). Si el campo "dedicación" toma el valor "COMPLETA", la dedicación tomará el valor 100%.  Si el campo "dedicación" toma el valor "PARCIAL", la dedicación tomará el valor inferior al 100%. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipo | Target: Public (Enumeration) Dedicacion |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1] | Target: Public (Class) GrupoEquipo  Cardinality: [1..\*] |

#### Entidad equipo instrumental del grupo: "GrupoEquipoInstrumental"

Equipos instrumentales de los que dispone el grupo de investigación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupo : Grupo Private  Identificador del grupo al que pertenece el equipo instrumental Es una FK a la tabla "grupo". Es un campo obligatorio. |
| numRegistro : String Private  Identificador del equipo instrumental en la Universidad, en caso que se desee informar de dicho campo. |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipoInstrumental  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumentalDescripcion  Cardinality:  [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipoInstrumental  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumentalNombre  Cardinality:  [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaEquipoInstrumental  Cardinality:  [0..\*] | Target: Public (Class) GrupoEquipoInstrumental  Cardinality:  [1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumental  Cardinality:  [0..\*] |

#### Entidad Nombre de un equipo instrumental: "GrupoEquipoInstrumentalNombre"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, el nombre de un equipo instrumental perteneciente a un grupo de investigación. El nombre del equipo es un campo de texto y es de introducción obligatoria. Ha de introducirse en al menos uno de los idiomas habilitados. Está disponible en e apartado Equipos instrumentales de Grupo de investigación.

| **ATTRIBUTES** |
| --- |
| grupoEquipoInstrumental : GrupoEquipoInstrumental  Private  Equipo instrumental al que pertenece el nombre. Es una FK a la tabla "GrupoEquipoInstrumental" |
| lang : String  Private  Idioma en el que está almacenado el nombre del equipo instrumental. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor que toma el campo "nombre" de un equipo instrumental de un grupo de investigación. Está expresado en el idioma recogido en el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipoInstrumental  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumentalNombre  Cardinality:  [1..\*] |

#### Entidad Descripción de un equipo instrumental: "GrupoEquipoInstrumentalDescripcion"

Entidad para almacenar, en todos los idiomas soportados por la aplicación, la descripción de un equipo instrumental perteneciente a un grupo de investigación. La descripción del equipo es un campo de texto y es opcional. No es obligatorio introducirla en ninguno de los idiomas habilitados. Está disponible en e apartado Equipos instrumentales de Grupo de investigación.

| **ATTRIBUTES** |
| --- |
| grupoEquipoInstrumental : GrupoEquipoInstrumental  Private  Equipo instrumental al que pertenece la descripción. Es una FK a la tabla "GrupoEquipoInstrumental" |
| lang : String  Private  Idioma en el que está almacenada la descripción del equipo instrumental. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String  Private  Valor que toma el campo "descripción" de un equipo instrumental de un grupo de investigación. Está expresado en el idioma recogido en el campo "lang". |

| **ASSOCIATIONS** | |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipoInstrumental  Cardinality:  [1] | Target: Public (Class) GrupoEquipoInstrumentalDescripcion  Cardinality:  [0..\*] |

#### Entidad histórico grupo especial: "GrupoEspecialInvestigacion"

Un Grupo podrá pasar o dejar de tener la consideración de "Grupo especial" en diferentes ocasiones a lo largo de su trayectoria. En esta tabla se almacena tanto el dato actual como el histórico.  Por defecto, un grupo se crea con la configuración de Grupo especial = No.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| especialInvestigacion : Boolean Private  Indica si el grupo es un "Grupo especial de investigación". Podrá tomar los valores true o false. En un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha de fin en la que empieza a aplicarse el valor indicado en el campo "especial investigación" al que se refiere el registro. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin en la que deja de aplicarse el valor indicado en el campo "especial investigación" al que se refiere el registro. |
| grupoId : Long Private  Grupo al que pertenece el registro. Es una FK a la tabla "grupo". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1] | Target: Public (Class) GrupoEspecialInvestigacion  Cardinality: [0..\*] |

#### Entidad clasificación de las líneas de investigación del grupo: "GrupoLineaClasificacion"

Tabla que recoge todas las clasificaciones de una línea de investigación de un grupo. El SGI dispone de una estructura genérica "clasificación" , en

forma de árbol, que permite, en tiempo de implantación, configurar los listados bajo los que resulte de interés clasificar la línea de investigación. No se establecen límites al respecto. En cada implantación se definirán las clasificaciones a utilizar. Esta estructura clasificación reside en el ESB, de forma que cada uno de los listados asociados a cada clasificación podrá ser alimentado desde un sistema de gestión corporativo (de forma genérica en el SGI se hace referencia a este posible sistema como SGO, sistema de gestión de la organización), a través del servicio de integración correspondiente, o bien ser configurados en tiempo de implantación.

Algunas clasificaciones tipo serían:

* Clasificación de códigos UNESCO.
* Clasificación de códigos NABS.
* Clasificación de códigos CNAE

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupoLinea : GrupoLineaInvestigacion Private  Línea de investigación al que pertenece el registro. Es una FK a la tabla "grupo línea investigación". Es un campo obligatorio. |
| codClasificacionRef : String Private  Elemento dentro de una clasificación con el que se vincula la línea de investigación. La referencia es el identificador del elemento dentro de la tabla "clasificación" incluida en modelo lógico del SGO (sistema de gestión de la organización). Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaClasificacion  Cardinality: [0..\*] | Target: Public (Class) GrupoLineaInvestigacion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaClasificacion  Cardinality: [0..\*] | Target: Public (Class) Clasificacion  Cardinality: [1] |

#### Entidad línea de investigación del equipo instrumental del grupo: "GrupoLineaEquipoInstrumental"

Relaciona un equipo instrumental definido en un grupo con la línea de investigación (perteneciente también al mismo grupo) que va a hacer uso del equipo.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupoLinea : GrupoLineaInvestigacion Private  Identificador de la línea de investigación del grupo. Es una FK a la tabla "grupo línea investigación". Es un campo obligatorio. |
| equipoInstrumental : GrupoEquipoInstrumental Private  Identificador del equipo instrumental del grupo. Es una FK a la tabla "grupo equipo instrumental". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaEquipoInstrumental  Cardinality: [0..\*] | Target: Public (Class) GrupoEquipoInstrumental  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality: [1] | Target: Public (Class) GrupoLineaEquipoInstrumental  Cardinality: [0..\*] |

#### Entidad línea de investigación del grupo: "GrupoLineaInvestigacion"

Líneas de investigación en las que trabaja un grupo de investigación.

Una línea de investigación quedará constituida por:

* Nombre: nombre o descripción de la línea de investigación
* Fecha de inicio y fecha de fin de duración de la línea en el grupo
* Miembros adscritos. Investigadores/as que forman parte del grupo de investigación se pueden adscribir a una o varias líneas de investigación del grupo.
* Clasificaciones. Una línea de investigación podrá clasificarse por medio de los códigos UNESCO, códigos CNAE, etc..
* Equipos instrumentales adscritos. Una línea de investigación podrá hacer uso de uno o varios equipos instrumentales definidos en el grupo.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupo : Grupo Private  Identificador del grupo al que pertenece la línea de investigación. Es una FK a la tabla "grupo". Es un campo obligatorio. |
| lineaInvestigacion : LineaInvestigacion Private  Identificador de la línea de investigación. Es una FK a la tabla "línea investigación". Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha de inicio de actuación de la línea de investigación en el grupo. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin de de actuación de la línea de investigación en el grupo |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality: [1..] | Target: Public (Class) GrupoLineaInvestigador  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality: [1] | Target: Public (Class) GrupoLineaEquipoInstrumental  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality: [1] | Target: Public (Class) Grupo  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaClasificacion  Cardinality: [0..\*] | Target: Public (Class) GrupoLineaInvestigacion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) LineaInvestigacion  Cardinality: [1] | Target: Public (Class) GrupoLineaInvestigacion  Cardinality: [0..\*] |

#### Entidad línea de investigación de los miembros del grupo: "GrupoLineaInvestigador"

Listado de miembros del equipo de grupo vinculados a la línea de investigación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupoLinea : GrupoLineaInvestigacion Private  Línea de investigación al que pertenece el registro. Es una FK a la tabla "grupo línea investigación". Es un campo obligatorio. |
| personaRef : String Private  Referencia de la persona que forma parte del equipo del grupo y esta adscrita a la línea de investigación. Es el identificador de la persona en el sistema de gestión de personas corporativo. Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha de inicio del miembro del equipo adscrito a la línea de investigación. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin del miembro del equipo adscrito a la línea de investigación. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoLineaInvestigacion  Cardinality: [1..] | Target: Public (Class) GrupoLineaInvestigador  Cardinality: [0..\*] |

#### Entidad palabras clave del grupo: "GrupoPalabraClave"

Palabras clave asociadas al grupo. El catálogo de palabras clave común al SGI se implementa en la tabla "palabra clave" del ESB (modelo SGO).

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| palabraClave : String Private  Palabra clave asociada al grupo. Es una FK a la tabla "palabra clave" del modelo ESB-SGO. Es un campo obligatorio. |
| grupo : Grupo Private  Grupo al que pertenece la palabra clave. Es una FK a la tabla "grupo". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoPalabraClave | Target: Public (Class) PalabraClave |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1] | Target: Public (Class) GrupoPalabraClave  Cardinality: [0..\*] |

#### Entidad persona autorizada del grupo: "GrupoPersonaAutorizada"

Persona delegada a la tarea de validar/rechazar items de producción científica y a la tarea de solicitud de modificación del grupo. La tabla almacena la persona autorizada ctual del grupo e histórico de las mismas. Cada grupo solo puede una persona autorizada en un momento determinado.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupo : Grupo Private  Identificador del grupo al que pertenece el registro persona autorizada. Es una FK a la tabla "grupo". Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha en la que comienza la participación en el grupo como persona autorizada. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha en la que finaliza la participación en el grupo como persona autorizada. |
| personaRef : iString Private  Referencia de la persona que actúa como persona autorizada del grupo. Es el identificador de la persona en el sistema de gestión de personas corporativo. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1..] | Target: Public (Class) GrupoPersonaAutorizada  Cardinality: [0..\*] |

#### Entidad responsable económico del grupo: "GrupoResponsableEconomico"

Responsable económico actual del grupo e histórico de los mismos. Cada grupo solo puede un responsable económico en un momento determinado.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| grupo : Grupo Private  Identificador del grupo al que pertenece el registro responsable económico. Es una FK a la tabla "grupo". Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha en la que comienza la participación en el grupo como responsable económico. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha en la que finaliza la participación en el grupo como responsable económico. |
| personaRef : String Private  Referencia de la persona que actúa como responsable económico del grupo. Es el identificador de la persona en el sistema de gestión de personas corporativo. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1..] | Target: Public (Class) GrupoResponsableEconomico  Cardinality: [0..\*] |

#### Entidad histórico de tipos del grupo: "GrupoTipo"

Histórico de los diferentes valores del campo "tipo grupo" durante toda la duración del grupo de investigación.

Indica el grado de madurez del grupo de investigación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| tipoGrupo : TipoGrupo Private  Indica el grado de madurez del grupo de investigación. Toma el valor del enumerado "tipo grupo". Es un campo obligatorio. |
| fechaInicio : Timestamp Private  Fecha de inicio en la que empieza a aplicarse el valor indicado en el campo "tipo grupo" al que se refiere el registro. Es un campo obligatorio. |
| fechaFin : Timestamp Private  Fecha de fin en la que deja de aplicarse el valor indicado en el campo "tipo grupo" al que se refiere el registro. |
| grupoId : Long Private  Grupo al que pertenece el registro. Es una FK a la tabla "grupo". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoTipo | Target: Public (Enumeration) TipoGrupo |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Grupo  Cardinality: [1] | Target: Public (Class) GrupoTipo  Cardinality: [0..\*] |

#### Entidad línea de investigación: "LineaInvestigacion"

Entidad para almacenar las líneas de investigación. Es una entidad de datos maestros del SGI. Las líneas de investigación se vinculan a los Grupos de investigación. Una línea de investigación puede estar vinculada a uno o varios grupos de investigación. La configuración de las líneas de investigación se realiza desde el menú CSP - Configuración  y están disponibles en el apartado Líneas de Investigación dentro de  Grupos Investigación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Identificador único del registro. Secuencia. Clave primaria. |
| activo : Boolean Private  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro (línea de investigación) está activa mientras que un valor "false" será indicativo de que el registro (línea de investigación) ha sido eliminada a nivel de usuario. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) LineaInvestigacion  Cardinality: [1] | Target: Public (Class) GrupoLineaInvestigacion  Cardinality: [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) LineaInvestigacionNombre  Cardinality: [1..\*] | Target: Public (Class) LineaInvestigacion  Cardinality: [1] |

#### Entidad Nombre de una línea de investigación: "LineaInvestigacionNombre"

Entidad para almacenar el nombre o título de la línea de investigación en cada uno de los idiomas soportados por la aplicación. El campo nombre de una línea de investigación es un campo obligatorio. Ha de introducirse al menos en un idioma.

|  |
| --- |
| **ATTRIBUTES** |
| lineaInvestigacion : LineaInvestigacion Private  Identificador de la línea de investigación a la que pertenece el nombre. Es una FK a la tabla "línea investigación". |
| lang : String Private  Idioma en el que está almacenado el nombre de la línea de investigación. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre o descripción de la línea de investigación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 1000 caracteres. Es un campo obligatorio de la línea de investigación en al menos uno de los idiomas. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) LineaInvestigacionNombre  Cardinality: [1..\*] | Target: Public (Class) LineaInvestigacion  Cardinality: [1] |

### Enumerados del modelo CSP Grupo

#### Enumerado tipo de dedicación: "Dedicacion"

Tiempo de dedicación del miembro en el grupo.

Enumerado con los siguientes valores:

* COMPLETA
* PARCIAL

|  |
| --- |
| **ATTRIBUTES** |
| COMPLETA : Public |
| PARCIAL : Public |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoEquipo | Target: Public (Enumeration) Dedicacion |

#### Enumerado tipo de grupo: "TipoGrupo"

Grado de madurez del grupo de investigación.

Enumerado con los siguientes valores:

* EMERGENTE
* CONSOLIDADO
* PRECOMPETITIVO
* ALTO\_RENDIMIENTO

|  |
| --- |
| **ATTRIBUTES** |
| EMERGENTE : Public |
| CONSOLIDADO : Public |
| PRECOMPETITIVO : Public |
| ALTO\_RENDIMIENTO : Public |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) GrupoTipo | Target: Public (Enumeration) TipoGrupo |