# ETI-Modelo lógico - Documentación Multiidioma

* Entidades
  + [Entidad: Acta](#)
  + [Entidad: ActaDocumento](#)
  + [Entidad: ActaResumen](#)
  + [Entidad: Apartado](#)
  + [Entidad: ApartadoDenificion](#)
  + [Entidad: Asistentes](#)
  + [Entidad: AsitentesMotivo](#)
  + [Entidad: Bloque](#)
  + [Entidad: BloqueNombre](#)
  + [Entidad: CargoComite](#)
  + [Entidad: Checklist](#)
  + [Entidad: Comentario](#)
  + [Entidad: ComentarioTexto](#)
  + [Entidad: Comite](#)
  + [Entidad: ComiteNombre](#)
  + [Entidad: Configuracion](#)
  + [Entidad: ConflictoInteres](#)
  + [Entidad: ConvocatoriaReunion](#)
  + [Entidad: ConvocatoriaReunionLugar](#)
  + [Entidad: ConvocatoriaReunionOrdenDia](#)
  + [Entidad: Dictamen](#)
  + [Entidad: DocumentacionConvocatoriaReunion](#)
  + [Entidad: DocumentacionConvocatoriaReunionNombre](#)
  + [Entidad: DocumentacionMemoria](#)
  + [Entidad: DocumentacionMemoriaNombre](#)
  + [Entidad: EquipoTrabajo](#)
  + [Entidad: EstadoActa](#)
  + [Entidad: EstadoMemoria](#)
  + [Entidad: EstadoMemoriaComentario](#)
  + [Entidad: EstadoRetrospectiva](#)
  + [Entidad: Evaluacion](#)
  + [Entidad: EvaluacionComentario](#)
  + [Entidad: Evaluador](#)
  + [Entidad: EvaluadorResumen](#)
  + [Entidad: FormacionEspecifica](#)
  + [Entidad: FormacionEspecificaNombre](#)
  + [Entidad: Formly](#)
  + [Entidad: FormlyDefinicion](#)
  + [Entidad: Formulario](#)
  + [Entidad: FormularioReport](#)
  + [Entidad: Informe](#)
  + [Entidad: InformeDocumento](#)
  + [Entidad: Memoria](#)
  + [Entidad: MemoriaTitulo](#)
  + [Entidad: PeticionEvaluacion](#)
  + [Entidad: PeticionEvaluacionDisMetodologico](#)
  + [Entidad: PeticionEvaluacionObjetivos](#)
  + [Entidad: PeticionEvaluacionOtroValorSocial](#)
  + [Entidad: PeticionEvaluacionResumen](#)
  + [Entidad: PeticionEvaluacionTitulo](#)
  + [Entidad: PeticionEvaluacionFuenteFinanciacion](#)
  + [Entidad: Respuesta](#)
  + [Entidad: Retrospectiva](#)
  + [Entidad: Tarea](#)
  + [Entidad: TareaFormacion](#)
  + [Entidad: TareaNombre](#)
  + [Entidad: TareaOrganismo](#)
  + [Entidad: TipoActividad](#)
  + [Entidad: TipoComentario](#)
  + [Entidad: TipoConvocatoriaReunion](#)
  + [Entidad: TipoDocumento](#)
  + [Entidad: TipoDocumentoNombre](#)
  + [Entidad: TipoEstadoActa](#)
  + [Entidad: TipoEstadoMemoria](#)
  + [Entidad: TipoEvaluacion](#)
  + [Entidad: TipoInvestigacionTutelada](#)
  + [Entidad: TipoTarea](#)
  + [Entidad: TipoTareaNombre](#)
* Enumerados
  + TipoValorSocial
  + EstadoFinanciacion
  + EstadoRetrospectiva
  + Genero
  + SeguimientoAnualDocumentacionTitle
  + TipoActividad
  + TipoComentario
  + TipoConvocatoriaReunion
  + TipoDictamen
  + TipoEstadoActa
  + TipoEstadoComentario
  + TipoEstadoMemoria
  + TipoEvaluacion
  + TipoFormulario
  + TipoInvestigacionTutelada
  + TipoMemoria
  + TpoCargoComite

## Entidades

### Entidad: Acta

Tabla para almacenar la información de las actas asociadas las convocatorias de reunión. Cada convocatoria de reunión tiene que tener asociada una única acta.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "acta". |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión al que pertenece el acta. Es una FK a la tabla "convocatoria reunión". Es un campo obligatorio. |
| horaInicio : String Private  Hora del inicio de la reunión de la convocatoria de reunión. Es un dato obligatorio. |
| minutoInicio : Integer Private  Minutos de inicio de la reunión de la convocatoria de reunión. Es un dato obligatorio. |
| minutoFin : Integer Private  Minutos de finalización de la reunión de la convocatoria de reunión. Es un dato obligatorio. |
| horaFin : String PrivateHora de finalización de la reunión de la convocatoria de reunión. Es un dato obligatorio. |
| numero : Integer Private  Es el número del acta. Se le asigna el mismo valor que el campo "número acta" de convocatoria de reunión asociada. Es un campo obligatorio. |
| estadoActual : TipoEstadoActa Private  Valor del estado actual del acta. Es una FK a la tabla "tipo estado acta". Es un campo obligatorio. |
| inactiva : Boolean Private = True  Indica si el acta esta finalizada (valor "true") o en elaboración (valor "false"). |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ActaResumen  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ActaDocumento  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoActa  Cardinality: [1] | Target: Public (Class) Acta  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoActa  Cardinality: [0..\*] | Target: Public (Class) Acta  Cardinality: [1] |

### Entidad: ActaDocumento

Almacena el documento generado a partir de la plantilla del acta cuando se finaliza la misma. Habrá un documento por cada uno de los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| documentoRef : String Private  Referencia o Identificador del documento almacenado en el repositorio de documentos global del SGI. |
| transaccionRef : String Private  Identificador de la transacción devuelta por el servicio para sellar el documento en blockchain. Sólo se almacenará esta transacción cuando la variable de configuración "blockchain\_enable" este a true. |
| lang : String Private  Identifica al idioma en el que esta almacenado el documento del acta. Es un código de 2 caracteres:   * es * en * eu |
| acta : Acta Private  Identificador del acta a la que pertenece el documento. Es una FK a la tabla "acta". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ActaDocumento  Cardinality: [0..\*] |

### Entidad: ActaResumen

Entidad para poder almacenar el resumen del acta de evaluación en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| acta : Acta Private  Identificador del acta a la que pertenece el resumen. Es una FK a la tabla "acta". |
| lang : String Private  Identifica al idioma en el que esta almacenado el resumen del acta. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Resumen del acta de la reunión de evaluación almacenado en  el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 4000 caracteres que dispone del componente para introducción de texto con formato enriquecido. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ActaResumen  Cardinality: [1..\*] |

### Entidad: Apartado

Contiene la definición de los apartados de cada uno de los formularios definidos en la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| padre : Apartado Private  Identificador del "apartado" del que es hijo (subpartado) en caso de que se trate de un apartado incluido en otro. En una FK a la propia tabla "apartado". |
| bloque : BloqueFormulario Private  Identifciador del bloque del formulario al que pertenece. Es un FK a la tabla "bloque". |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "apartado". |
| orden : int Private  Indica el orden que ocupa el apartado dentro del bloque |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Apartado  Cardinality: [1] | Target: Public (Class) Apartado  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified | |
| Source: Public (Class) Apartado  Cardinality: [1] | Target: Public (Class) ApartadoDenificion  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Apartado  Cardinality: [1] | Target: Public (Class) Apartado  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario  Cardinality: [1..\*] | Target: Public (Class) Apartado  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ComponenteFormulario  Cardinality: [1] | Target: Public (Class) Apartado  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Bloque  Cardinality: [1] | Target: Public (Class) Apartado  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Respuesta  Cardinality: [0..\*] | Target: Public (Class) Apartado  Cardinality: [1] |

### Entidad: ApartadoDenificion

Tabla con esquema de definición del apartado en cada uno de los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| nombre : String Private  Nombre del apartado en el idioma definido en el campo "lang". Es un campo de texto de 250 caracteres |
| esquema : String Private  Definición del esquema del apartado en el idioma indicado por el campo "lang". Es un campo de tipo CLOB. |
| lang : String Private  Identifica al idioma en el que esta almacenado el esquema del apartado. Es un código de 2 caracteres:   * es * en * eu |
| apartado : Apartado Private  Identificador del apartado al que pertenece el esquema del apartado. Es una FK a la tabla "apartado". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Apartado  Cardinality: [1] | Target: Public (Class) ApartadoDenificion  Cardinality: [1..\*] |

### Entidad: Asistentes

Listado de miembros activos del comité que tienen que asistir a la reunión de convocatoria.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "asistentes". |
| evaluador : Evaluador Private  Identificador del miembro del comité. Es una FK a la tabla "evaluador". Es un campo obligatorio. |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión. Es una FK a la tabla "convocatoria reunión". Es un campo obligatorio. |
| asistencia : Boolean Private  Indica si el miembro del comité (evaluador) ha podido o no asistir a la convocatoria de reunión. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Asistentes  Cardinality: [1] | Target: Public (Class) AsitentesMotivo  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Asistentes  Cardinality: [1..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) Asistentes  Cardinality: [1..\*] |

### Entidad: AsitentesMotivo

Entidad para poder almacenar el motivo de la no asistencia de un evaluador a la convocatoria de reunión de un comité en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas cuando el evaluador no asiste.

|  |
| --- |
| **ATTRIBUTES** |
| asistentes : Asistentes Private  Identificador del asistente a la que pertenece el motivo de la ausencia. Es una FK a la tabla "asistentes". |
| lang : String Private  Identifica al idioma en el que esta almacenado el motivo de la no asistencia del evaluador a la reunión de evaluación. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Motivo de la no asistencia del evaluador a la reunión de evaluación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Asistentes  Cardinality: [1] | Target: Public (Class) AsitentesMotivo  Cardinality: [0..\*] |

### Entidad: Bloque

Contiene el nombre de los bloques de información en los que se engloban los apartados de los formularios soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "bloque". |
| formulario : Formulario Private  Identificador del formulario al que pertenece el bloque. Es una FK a la tabla "formulario". |
| orden : Integer Private  Indica el orden de cada uno de los bloques, para saber cual es el primero, el segundo, etc. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Bloque  Cardinality: [1] | Target: Public (Class) BloqueNombre  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Bloque  Cardinality: [1] | Target: Public (Class) Apartado  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) Bloque  Cardinality: [0..\*] |

### Entidad: BloqueNombre

Tabla con el nombre de los bloques en los que se agrupan los apartados de los formularios en cada uno de los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| value\_ : String Private  Nombre del bloque en el idioma definido en el campo "lang". Es un campo de texto de 2000 caracteres |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del bloque. Es un código de 2 caracteres:   * es * en * eu |
| bloque : Bloque Private  Identificador del bloque al que pertenece. Es una FK a la tabla "bloque". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Bloque  Cardinality: [1] | Target: Public (Class) BloqueNombre  Cardinality: [1..\*] |

### Entidad: CargoComite

Tabla con los distintos cargos que puede tener cada uno de los miembros de un comité.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "cargo comite". |
| nombre : String Private  Nombre de los distintos cargos que pueden existir dentro de un comité. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) CargoComite  Cardinality: [1] | Target: Public (Class) Evaluador  Cardinality: [0..\*] |

### Entidad: Checklist

Entidad para almacenar las respuestas del formulario checklist realizado por el usuario previo al proyecto de investigación que dio lugar a la solicitud de evaluación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "checklist". |
| formly : Formly Private  Identificador del formulario formly con las preguntas del checklist. Es una FK a la tabla "Formly". |
| respuesta : String Private  Contiene las respuestas del usuario al formulario Formly del checklist. Es un campo de tipo CLOB, |
| personaRef : String Private  Identificador o Referencia de la persona que ha realizado el checklist Es el identificador de la persona en el sistema de personas de la Universidad (SGP). |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Checklist  Cardinality: [0..\*] | Target: Public (Class) Formly  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [0..1] | Target: Public (Class) Checklist  Cardinality: [0..1] |

### Entidad: Comentario

Tabla con los distintos comentarios contemplados en la aplicación:

* comentarios realizados por los evaluadores en su revisión de la evaluación de una memoria
* comentarios realizados por el gestor/evaluadores a la hora de asignar el dictamen a la evaluación de una memoria
* comentarios realizados por los evaluadores al acta de la convocatoria de reunión
* comentarios realizados por los gestores al acta de la convocatoria de reunión

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "comentario". |
| apartadoFormulario : apartadoFormulario Private  Identificador del apartado del formulario al que hace referencia el comentario. Es una FK a la tabla "apartado". Es un campo obligatorio. |
| evaluacion : Evaluacion Private  Identificador de la evaluación a la que se esta añadiendo el comentario. Es una FK a la tabla "evaluación". Es un campo obligatorio. |
| tipo : TipoComentario Private  Identificador del tipo de comentario. Es una FK a la tabla "tipo comentario". Es un campo obligatorio. |
| estado : TipoEstadoÇomentario Private  Estado del comentario. Es un campo obligatorio. Se trata en el SGI como un enumerado con los siguientes posibles valoras:   * CERRADO * ABIERTO |
| fechaEstado : Timestamp Private  Fecha en la que los comentarios realizados por el evaluador tanto a una evaluación como a un acta se enviaron a secreataría, se pusieron en estado CERRADO. |
| createdBy(personaRef) : String Private  Identificador o Referencia de la persona que ha creado el comentario. Es el identificador de la persona en el sistema de personas de la Universidad (SGP). |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario | Target: Public (Enumeration) TipoEstadoComentario |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario  Cardinality: [1..\*] | Target: Public (Class) Apartado  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario  Cardinality: [1] | Target: Public (Class) ComentarioTexto  Cardinality: [1..\* |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario  Cardinality: [0..\*] | Target: Public (Class) ApartadoFormulario  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoComentario  Cardinality: [1] | Target: Public (Class) Comentario  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormularioMemoria  Cardinality: [1] | Target: Public (Class) Comentario  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [1] | Target: Public (Class) Comentario  Cardinality: [0..\*] |

### Entidad: ComentarioTexto

Entidad para poder almacenar el texto del comentario de la evaluación de los evaluadores y/o del gestor en los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| comentario : Comentario Private  Identificador del comentario al que pertenece el texto. Es una FK a la tabla "comentario". |
| lang : String Private  Identifica al idioma en el que esta almacenado el texto del comentario. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Texto del comentario en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario  Cardinality: [1] | Target: Public (Class) ComentarioTexto  Cardinality: [1..\*] |

### Entidad: Comite

Representa cada uno de los posibles comités éticos de la Universidad, responsables de realizar las convocatorias de reunión para llevar a cabo la evaluación de las solicitudes de proyectos de investigación o prácticas docentes con datos de carácter personal, seres humanos, animales o agentes biológicos.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "comite". |
| codigo : String Private  Abreviatura o acrónimo del nombre del comité. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| formularioMemoria : Formulario Private  Identificador de la última versión del formulario de memoria disponible. Es una FK a la tabla "formulario". |
| formularioSeguimientoAnual : Formulario Private  Identificador de la última versión del formulario de seguimiento anual disponible. Es una FK a la tabla "formulario". |
| formularioSeguimientoFinal : Formulario Private  Identificador de la última versión del formulario de seguimiento final disponible. Es una FK a la tabla "formulario". |
| formularioRetrospectiva : Formulario Private  Identificador de la última versión del formulario de retrospectiva disponible. Es una FK a la tabla "formulario". |
| requiereRetrospectiva : Boolean Private = False  Indica si el comité tendrá formulario de retrospectiva o no. A priori sólo el comité CEEA tendrá este campo a true. |
| prefijoReferencia : String Private  Cadena de texto que servirá para contruir de forma automática el campo "número de referencia" al crear una nueva memoria. Se concatenará con el año y con un secuencial. |
| permitirRatificacion : Boolean Private = False  Indica si se permite crear o no una memoria para este comité del tipo "ratificación". A priori sólo el comité CEISH tendrá este campo a true. |
| tareaNombreLibre : Boolean Private = False  Indica si en la pantalla de asignación de tareas al miembro del equipo de una solicitud de evaluación el campo "tarea" se va a introducir de forma manual por el usuario dejando que pueda escribir libremente la descripcón de la tarea o bien tendrá que seleccionar la tarea de las propuestas en un desplegable. Si este campo esta a true, será un campo de texto libre. Si este campo esta a false será un campo desplegable. A priori los comités CEISH y CBE tendrán este campo a true. |
| tareaExperienciaLibre : Boolean Private = False  Indica si en la pantalla de asignación de tareas al miembro del equipo de una solicitud de evaluación el campo "experiencia/formación" se va a introducir de forma manual por el usuario dejando que pueda escribir libremente lo que desee o bien tendrá que seleccionar la formación de las propuestas en un desplegable. Si este campo esta a true, será un campo de texto libre. Si este campo esta a false será un campo desplegable. A priori los comités CEISH y CBE tendrán este campo a true. |
| tareaExperienciaDetalle : Boolean Private = False  Indica si en la pantalla de asignación de tareas al miembro del equipo de una solicitud de evaluación se deben de mostrar o no los campos "año" y "organismo" para detallar más la información de la formación. Si este campo esta a true, se mostrarán los campos y deberán de informarse. Si este campo esta a false no se mostrarán dichos campos. A priori los comités CEEA y CBE tendrán este campo a true. |
| memoriaTituloLibre : Boolean Private = False  Indica si en la pantalla de creación de memoria se debe de introducir el título de la memoria. Si este campo esta a true, se mostrará el campo y deberá de informarse. Si este campo esta a false no se mostrará dicho campo. A priori sólo el comité CEEA y CBE tendrá este campo a true. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [1] | Target: Public (Class) ComiteNombre  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [1] | Target: Public (Class) ComiteFormulario  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [1] | Target: Public (Class) TipoMemoriaComite  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [0..1] | Target: Public (Class) Formulario  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |

### Entidad: ComiteNombre

Entidad para poder almacenar el nombre comité en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| comite : Comite Private  Identificador del comité al que representa. Es una FK a la tabla "comite". |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del comité. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del comité en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |
| genero : Genero Private  Identificador del género con el que se debe hacer referencia al comité. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [1] | Target: Public (Class) ComiteNombre  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) Genero | Target: Public (Class) ComiteNombre |

### Entidad: Configuracion

Tabla genérica para almacenar variables de configuración del SGI referentes al módulo de ETI. Cada campo representa un parámetro de configuración.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "comite". |
| diasArchivadaInactivo : Integer Private  Variable que marca el paso automático a estado "archivada" de las memorias con estado "Favorable Pendiente de Modificaciones Mínimas" o "No procede evaluar" o "Solicitud modificación". Comunicado Memoria con dictamen "Favorable Pendiente de Modificaciones Mínimas" archivada automáticamente y proceso batch "Paso a archivado por inactividad (modificaciones mínimas)" |
| mesesArchivadaPendienteCorrecciones : Integer Private  Variable que marca el paso automático a estado "archivada" de las memorias con estado "Pendiente de correcciones". Comunicado Memoria con dictamen "Pendiente de correcciones" archivada automáticamente y proceso batch "Paso a archivado por no presentar de nuevo el informe" |
| diasLimiteEvaluador : Integer Private  Número de días previos a la fecha de la reunión de evaluación que disponen los evaluadores para evaluar la memoria |
| diasAvisoRetrospectiva : Integer Private  Número de días con antelación a la fecha indicada de retrospectiva (memorias CEEA) con el que se envía el comunicado "Informe de retrospectiva de memoria tipo CEEA pendiente" |
| duracionPoryectoEvaluacion : Integer Private  Expresada en años. El valor indicado se utilizará para realizar comprobación entre las fechas de inicio y fin indicadas en la solicitud de evaluación (tabla petición evaluación). No se permitirá que la diferencia entre fecha de fin y fecha de inicio supere, en años, al valor establecido en este parámetro. |

### Entidad: ConflictoInteres

Tabla con el listado de personas con las que los evaluadores tienen conflicto de interés, por lo que no podrán evaluar una memoria en la que esa persona este asignada a una de las tareas de la memoria.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "conflicto interés". |
| evaluador : Evaluador Private  Identificador del evaluador el cual tiene conflicto de interés con una persona. Es una FK a la tabla "evaluador". |
| personaConflictoRef : String Private  Identificador o Referencia de la persona con la que el evaluador tiene un conflicto de interés, por lo que no le podrá evaluar ninguna memoria en la que aparece asignada a una tarea de ka misma.Es el identificador de la persona en el sistema de personas de la Universidad (SGP). |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1] | Target: Public (Class) ConflictoInteres  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Persona  Cardinality: [1] | Target: Public (Class) ConflictoInteres  Cardinality: [0..\*] |

### Entidad: ConvocatoriaReunion

Tabla con las convocatorias de reunión de evaluación para los distintos comités. Una convocatoria de reunión esta asignada a un único comité de evaluación y valorará una o varias memorias (evaluaciones).

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "convocatoria reunión". |
| comite : Comite Private  Identificador del comité al que pertenece la convocatoria de reunión. Es una FK a la tabla "comité". Es un campo obligatorio. |
| tipoConvocatoriaReunion : TipoConvocatoriaReunion Private  Identificador del tipo de convocatoria de reunión (ordinaria, extraordinaria o de seguimiento). Es una FK a la tabla "tipo convocatoria reunión". Es un campo obligatorio. |
| fechaEvaluacion : Date Private  Fecha en la que se va a realizar la convocatoria de reunión. Es un campo obligatorio. |
| horaInicio : Integer Private  Almacena la hora del inicio de la reunión de primera convocatoria. Es un campo obligatorio. |
| minutoInicio : Integer Private  Almacena los minutos del inicio de la reunión de primera convocatoria. Es un campo obligatorio. |
| fechaLimite : Date Private  Fecha hasta la cual se van a tener en cuenta las memorias enviadas a secretaría por el personal de investigación, a partir de esta fecha las memorias que lleguen no se tendrá en cuenta para la convocatoria, entrarían para la siguiente. Es un campo obligatorio. |
| numActa : Integer Private  Almacena internamente el número del acta que le corresponde a la convocatoria de reunión. Se calcula de forma automática por la aplicación cuando se crea una nueva convocatoria de reunión. Se contará el número de convocatorias de reunión existentes para el comité asociado y se sumará uno. Existen tres secuenciales, uno por cada comité (el secuencial es único, no se inicia por año). |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| fechaEnvio : Date Private  Fecha en la que se envió la notificación a los miembros activos del comité para informarles de que existe una nueva convocatoria programada en la que son citados. |
| horaInicioSegunda : Integer Private  Almacena la hora del inicio de la reunión de segunda convocatoria. |
| minutoInicioSegunda : Integer Private  Almacena los minutos del inicio de la reunión de segunda convocatoria. |
| anio : Integer Private  Es un dato interno de la aplicación. Indica el año de la fecha de evaluación indicada en la conocatoria de reunión. Se usa para formar el campo "código" de la convocatoria de reunión. |
| videoconferencia : Boolean Private = False  Indica si la convocatoria de reunión se va a realizar a través de una videoconferencia o no. En caso de que tenga el valor "false", se deberá de almacenar el lugar de la convocatoria de reunión en la tabla "convocatoria reunión lugar". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunionLugar  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunionOrdenDia  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) Asistentes  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionConvocatoriaReunion  Cardinality: [0..\*] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Acta  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [1..\*] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |

### Entidad: ConvocatoriaReunionLugar

Entidad para poder almacenar el lugar de la reunión del comité en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas si el campo "videoconferencia" tiene el valor "false"

|  |
| --- |
| **ATTRIBUTES** |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión a la que pertenece el lugar de la reunión. Es una FK a la tabla "convocatoria reunión". |
| lang : String Private  Identifica al idioma en el que esta almacenado el lugar de la reunión. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Lugar de la reunión en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunionLugar  Cardinality: [0..\*] |

### Entidad: ConvocatoriaReunionOrdenDia

Entidad para poder almacenar el orden del día de la reunión del comité en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión a la que pertenece el orden del día de la reunión. Es una FK a la tabla "convocatoria reunión". |
| lang : String Private  Identifica al idioma en el que esta almacenado el orden del día de la reunión. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Orden del día de la reunión en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunionOrdenDia  Cardinality: [1..\*] |

### Entidad: Dictamen

Tabla con los distintos valores de dictamen que puede tener un tipo de evaluación concreto. Dependiendo del tipo de evaluación los valores del dictamen serán distintos.

* Los valores  para las evaluaciones de memoria (nueva, modificación o ratificación) son:
  + Favorable
  + Favorable pendiente de revisión mínima
  + Pendiente de correcciones
  + Desfavorable
  + No procede evaluar
  + Los valores  para el tipo de evaluación de Retrospectiva son:
  + Favorable
  + Desfavorable
* Los valores para las memorias de tipo seguimiento anual son:
  + Favorable
  + Solicitud de modificación
* Los valores para las memorias de tipo seguimiento final son:
  + Favorable
  + Solicitud de aclaraciones

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "dictamen". |
| nombre : String Private  Nombre del dictamen. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| tipoEvaluacion : TipoEvaluacion Private = True  Identificador del tipo de evaluación. Es una FK a la tabla "tipo evaluación". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Dictamen  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEvaluacion  Cardinality: [1] | Target: Public (Class) Dictamen  Cardinality: [0..\*] |

### Entidad: DocumentacionConvocatoriaReunion

Tabla para almacenar la documentación adjuntada a una convocatoria de reunión.

|  |
| --- |
| **ATTRIBUTES** |
| id : Integer Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "documentación convocatoria reunión". |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión a la que pertenece el documento. Es una FK a la tabla "convocatoria reunión". |
| documentoRef : String Private  Referencia identificativa del documento en el repositorio de documentos global del SGI. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionConvocatoriaReunion  Cardinality: [0..\*] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) DocumentacionConvocatoriaReunionNombre  Cardinality: [1..\*] |

### Entidad: DocumentacionConvocatoriaReunionNombre

Entidad para poder almacenar el nombre del documento aportado en una convocatoria de reunión en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| documentacionConvocatoriaReunion : DocumentacionConvocatoria Private  Identificador del documento de la convocatoria de reunión al que describe. Es una FK a la tabla "documentación convocatoria reunión". |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del documento. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del documento de la convocatoria de reunión en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) DocumentacionConvocatoriaReunionNombre  Cardinality: [1..\*] |

### Entidad: DocumentacionMemoria

Entidad que guarda las referencias al SGDOC de los documentos aportados por el usuario para cada una de las memorias.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "documentación memoria". |
| memoria : Memoria Private  Identificador a la que pertenece el documento adjuntado. Es una FK a la tabla Memoria. |
| tipoDocumento : TipoDocumento Private  Identificador del tipo de documento. Es una FK a la tabla "tipo documento". Habrá distintos tipos de documento según el formulario. |
| documentoRef : String Private  Identificador del documento en el sistema de gestión de documentación de la Universidad. Es el identificador con el que se va a ir recuperar el documento en el SGDOC. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionMemoria  Cardinality: [0..\*] | Target: Public (Class) TipoDocumento  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionMemoria  Cardinality: [1.. | Target: Public (Class) DocumentacionMemoriaNombre  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Documento | Target: Public (Class) DocumentacionMemoria |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1] | Target: Public (Class) DocumentacionMemoria  Cardinality: [0..\*] |

### Entidad: DocumentacionMemoriaNombre

Entidad para poder almacenar el nombre del documento en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| documentacionMemoria : DocumentacionMemoria Private  Identificador del documento de la memoria al que describe. Es una FK a la tabla "documentación memoria". |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del documento. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del documento de la memoria en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionMemoria  Cardinality: [1..] | Target: Public (Class) DocumentacionMemoriaNombre  Cardinality: [1..\*] |

### Entidad: EquipoTrabajo

Contiene el conjunto de personas que forman parte del equipo de trabajo de un proyecto de investigación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "equipo trabajo. |
| personaRef : String Private  Identificador o Referencia de la persona que forma parte del equipo de trabajo. Es el identificador de la persona en el sistema de personas de la Universidad (SGP). Es un campo obligatorio. |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación que representa el proyecto de investigación que se va a evaluar por una Comisión de ética. Es una FK a la tabla "peticion evaluacion". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EquipoTrabajo  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) EquipoTrabajo  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Persona | Target: Public (Class) EquipoTrabajo |

### Entidad: EstadoActa

Histórico de estados por los pasa el acta. El estado actual será el registro más reciente.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "estado acta". |
| acta : Acta Private  Identifciador del acta al que pertenece el estado. Es un FK a la tabla "acta". Es un campo obligatorio. |
| tipoEstadoActa : TipoEstadoActa Private  Identificador del tipo de estado del acta. Es una FK a la tabla "tipo estado acta". Es un campo obligatorio. |
| fechaEstado : Datetime Private  Fecha en la que se alcanzó el estado. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoActa  Cardinality: [0..\*] | Target: Public (Class) Acta  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoActa  Cardinality: [1] | Target: Public (Class) EstadoActa  Cardinality: [0..\*] |

### Entidad: EstadoMemoria

Histórico de estados por los pasa la memoria. El estado actual será el registro más reciente.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "estado memoria". |
| memoria : Memoria Private  Memoria al que pertenece el registro. Es una FK a la tabla "memoria". Es un campo obligatorio. |
| tipoEstadoMemoria : TipoEstadoMemoria Private  Indica el tipo de estado de la memoria. Es una FK a la tabla "tipo estado memoria". Es un campo obligatorio. |
| fechaEstado : Datetime Private  Fecha en la que se alcanzó el estado. Es un campo obligatorio. |
| comentario : String Private  Campo para añadir comentario global a la memoria al pasar a estado "Subsanación" (previo a la inclusión de la memoria en convocatoria de reunión de evaluación) |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoMemoria  Cardinality: [1..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoMemoria  Cardinality: [0..\*] | Target: Public (Class) EstadoMemoria  Cardinality: [1] |

### Entidad: EstadoMemoriaComentario

Entidad para poder almacenar el comentario global a la memoria al pasar a estado "Subsanación" (previo a la inclusión de la memoria en convocatoria de reunión de evaluación) en los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| estadoMemoria : EstadoMemoria Private  Identificador del estado de la memoria a la que pertenece el comentario. Es una FK a la tabla "estado memoria". Es un campo obligatorio. |
| lang : String Private  Identifica al idioma en el que esta almacenado el comentario. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Comentario de la evaluación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoMemoriaComentario  Cardinality: [1..\*] | Target: Public (Class) EstadoMemoria  Cardinality: [1] |

### Entidad: EstadoRetrospectiva

Tabla con los estados de una retrospectiva.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "estado retrospectiva". |
| nombre : String Private  Nombre del tipo de estado de la retrospectiva. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoRetrospectiva  Cardinality: [1] | Target: Public (Class) Retrospectiva  Cardinality: [0..\*] |

### Entidad: Evaluacion

Tabla con las evaluaciones por las que ha pasado una memoria y sus seguimientos. Cada vez que el personal de investigación envíe a secretaría una memoria o un seguimiento para su evaluación y ésta sea asignada a una convocatoria de reunión se creará una evaluación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "evaluación". |
| memoria : Memoria Private  Identificador de la memoria a la que pertenece la evaluación. Es una FK a la tabla "memoria". Es un campo obligatorio. |
| convocatoriaReunion : ConvocatoriaReunion Private  Identificador de la convocatoria de reunión a la que pertenece la evaluación. Es una FK a la tabla "convocatoria reunión". Es un campo obligatorio. |
| tipoEvaluacion : TipoEvaluacion Private  Identificador que representa el tipo de la evaluación del que se trata. Es una FK a la tabla "tipo evaluación". Es un campo obligatorio. |
| version : Integer Private  Número de versión de la evaluación para un tipo concreto de evaluación. Es un campo de tipo numérico. Es un campo obligatorio. |
| dictamen : Dictamen Private  Identificador del dictamen obtenido en la evaluación. Es una FK a la tabla "dictamen". |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| fechaDictamen : Date Private  Fecha en la que se ha dado el dictamen a la evaluación. |
| esRevMinima : Boolean Private  Indica si la evaluación es de revisión mínima o no, es decir, si previamente ha tenido otra evaluación en las que haya sacado un dictamen de "Favorable pendiente de revisión mínima". En caso de ser una evaluación de revisión mínima estará asignada a la misma convocatoria de reunión que su antecesora. |
| evaluador1 : Evaluador Private  Identificador del evaluador 1 asignado a la memoria a evaluar por el gestor entre los miembros del comité evauador. Es una FK a la tabla "evaluador". |
| evaluador2 : Evaluador Private  Identificador del evaluador 2 asignado a la memoria a evaluar por el gestor entre los miembros del comité evauador. Es una FK a la tabla "evaluador". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified | |
| Source: Public (Class) Evaluacion  Cardinality: [1] | Target: Public (Class) Comentario  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [1..\*] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EvaluacionComentario  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\* |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEvaluacion  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Dictamen  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EvaluadorEvaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluacion  Cardinality: [1] |

### Entidad: EvaluacionComentario

Entidad para poder almacenar el motivo por el que la evaluación ha tenido un dictamen "No procede evaluar" en los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| evaluacion : Evaluacion Private  Identificador de la evaluación a la que pertenece el comentario. Es una FK a la tabla "evaluacion". |
| lang : String Private  Identifica al idioma en el que esta almacenado el comentario. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Comentario de la evaluación en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EvaluacionComentario  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\*] |

### Entidad: Evaluador

Tabla con la lista de miembros de cada uno de los comités de ética.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "evaluador". |
| comite : Comite Private  Identificador del comité al que pertenece el evaluador. Es una FK a la tabla "comite". Es un campo obligatorio. |
| cargoComite : CargoComite Private  Identificador del cargo que ocupa el evaluador dentro del comité. Es una FK de la tabla "cargo comité". Es un campo obligatorio. |
| fechaAlta : Date Private  Fecha de incorporación del evaluador al comité en el cargo indicado. Es un campo obligatorio. |
| fechaBaja : Date Private  Fecha en la que se da de baja el evaluador en el comité en el cargo indicado. |
| personaRef : String Private  Identificador o Referencia de la persona evaluadora. Es el identificador de la persona en el sistema de personas de la Universidad (SGP). Es un campo obligatorio. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1] | Target: Public (Class) ConflictoInteres  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1] | Target: Public (Class) EvaluadorResumen  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Persona | Target: Public (Class) Evaluador |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) CargoComite  Cardinality: [1] | Target: Public (Class) Evaluador  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EvaluadorEvaluacion  Cardinality: [0..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Asistentes  Cardinality: [1..\*] | Target: Public (Class) Evaluador  Cardinality: [1] |

### Entidad: EvaluadorResumen

Entidad para poder almacenar los datos relativos al personal evaluador en los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| evaluador : Evaluador Private  Identificador del evaluador al que pertenece las anotaciones. Es una FK a la tabla "evaluador". |
| lang : String Private  Identifica al idioma en el que esta almacenado el resumen. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Resumen del evaluador en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 4000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Evaluador  Cardinality: [1] | Target: Public (Class) EvaluadorResumen  Cardinality: [0..\*] |

### Entidad: FormacionEspecifica

Entidad con los tipos de formación que puede tener una persona para aquellas memorias que pertenezcan a un comité cuya variable de configuración "tarea experiencia libre" tenga el valor "false". Normalmente será el comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "formación específica". |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormacionEspecifica  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormacionEspecifica  Cardinality: [1] | Target: Public (Class) FormacionEspecificaNombre  Cardinality: [1..\*] |

### Entidad: FormacionEspecificaNombre

Entidad para almacenar los tipos de formación en los distintos idiomas para memorias que tienen configurado el comité con la variable "tarea formacion libre" con valor "false". Normalmente será el comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| formacionEspecifica : FormacionEspecifica Private  Identificador de la formación específica. Es una FK a la tabla "formación específica. |
| lang : String Private  Identifica al idioma en el que esta almacenado el tipo de formación. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Tipo de la formación en un idioma concreto. Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormacionEspecifica  Cardinality: [1] | Target: Public (Class) FormacionEspecificaNombre  Cardinality: [1..\*] |

### Entidad: Formly

Entidad que indica la versión del formulario usado en el checklist mostrado al usuario antes de su solicitud de evaluación ante una Comisión de ética.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "Formly". |
| nombre : String Private  Nombre del formulario checklist. Es un campo de texto libre con un máximo de 50 caracteres. |
| version : Integer Private  Indica la versión del fomulario Formly que representa las preguntas del Checklist. Es un campo numérico. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formly  Cardinality: [1] | Target: Public (Class) FormlyDefinicion  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Checklist  Cardinality: [0..\*] | Target: Public (Class) Formly  Cardinality: [1] |

### Entidad: FormlyDefinicion

Definición del formulario del checklist que contiene las preguntas para valorar si un proyecto asociado a una solicitud deberá ser evaluado por la Comisión de ética.

|  |
| --- |
| **ATTRIBUTES** |
| formly : Formly Private  Identificador del fomulario cheklist. Es una FK a la tabla "Formly". |
| esquema : String Private  Esquema del formulario con la definición de las preguntas del cheklist. Es un campo de tipo CLOB. |
| lang : String Private  Identifica al idioma en el que esta almacenado el formulario. Es un código de 2 caracteres:   * es * en * eu |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formly  Cardinality: [1] | Target: Public (Class) FormlyDefinicion  Cardinality: [1..\*] |

### Entidad: Formulario

Entidad que representa cada uno de los formularios soportados por la aplicación. Se incluyen los formularios de memoria, de seguimiento anual, de seguimiento final y los de retrospectivas. Para un mismo tipo de formulario podrá existir mas de uno, serán identificadores distintos (distintas versiones del formulario). Cuando se crea una memoria se asocia al formulario que este activo en ese momento, el indicado en la tabla "comite".

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "formulario". |
| tipo : TipoFormulario Private  Identifica el tipo de formulario:   * Memoria * Seguimiento anual * Seguimiento final * Retrospectiva |
| codigo : String Private  Código identificativo de cada uno de los formularios y de sus versiones. Ejemplos:   * M10/2024/001 * M10/2024/002 * M20/2024/001 * M20/2024/002 * M30/2024/001 * M30/2024/002 * SA/2024/001 * SF/2024/001 * R/2024/001 |
| seguimientoAnualDocumentacionTitle : SeguimientoAnualDocument Private  Texto a mostrar en la pantalla de documentación aportada del formulario en el apartado de "Seguimiento anual". Dependiendo del formulario (m10,m20 o m30) se muestra un título u otro. Los valores vendrán dados por un enumerado. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) FormularioReport  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario | Target: Public (Enumeration) SeguimientoAnualDocumentacionTitle |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) Bloque  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) ComiteFormulario  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario | Target: Public (Enumeration) TipoFormulario |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) FormularioMemoria  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality: [0..\*] | Target: Public (Class) Formulario  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comite  Cardinality: [0..1] | Target: Public (Class) Formulario  Cardinality: [1] |

### Entidad: FormularioReport

Entidad para poder almacenar las plantillas de los documentos en base a los que se genera el documento/informe de exportación de los distintos formularios de memoria. Los documentos de memoria se generan en las acción " enviar a Secretaría".  
Existe una plantilla para cada uno de los idiomas habilitados en la implantación.

|  |
| --- |
| **ATTRIBUTES** |
| formulario : Formulario Private  Identificador del formulario al que pertenece la plantilla. Es una FK a la tabla "formulario". |
| lang : String Private  Identifica al idioma con el que se corresponde cada plantilla. Cada idioma se representa por un código de 2 caracteres:   * es * en * eu |
| value\_ : Blob Private  Es un campo de tipo BLOB en el que se almacena el documento de plantilla. Existe una plantilla por cada idioma habilitado en la aplicación. La plantilla se corresponde con el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario  Cardinality: [1] | Target: Public (Class) FormularioReport  Cardinality: [1..\*] |

### Entidad: Informe

Tabla con los de informes(pdf) generados a partir de los formularios de memoria, seguimiento anual, seguimiento final o retrospectiva enviados a secretaria. Cada vez que el personal de investigación envía a secretaría una memoria o un seguimiento para su evaluación se generará su informe con la información recogida en el formulario hasta ese momento.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "informe". |
| version : int Private  Versión del documento de informe. Coincide con el valor que tenía el campo "versión" de la tabla "memoria" en el momento en que el usuario envió a secretaría la memoria. Es un campo obligatorio. |
| memoria : Memoria Private  Identificador de la memoria a la que pertenece el informe. Es una FK a la tabla "memoria". Es un campo obligatorio. |
| tipoEvaluacion : TipoEvaluacion Private  Identificador del tipo de evaluación, para distinguir si se trata de un informe de memoria, de seguimiento anual, seguimiento final o retrospectiva. Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Informe  Cardinality: [1] | Target: Public (Class) InformeDocumento  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Informe | Target: Public (Class) Documento |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Informe  Cardinality: [0..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormularioMemoria  Cardinality: [1] | Target: Public (Class) Informe  Cardinality: [0..\*] |

### Entidad: InformeDocumento

Almacena el documento generado a partir de la plantilla del informe de memoria o de seguimiento cuando se envía a secretaría. Habrá un documento por cada uno de los idiomas soportados por la aplicación

|  |
| --- |
| **ATTRIBUTES** |
| documentoRef : String Private  Referencia o Identificador del documento almacenado en el repositorio de documentos global del SGI. |
| lang : String Private  Identifica al idioma en el que esta almacenado el documento. Es un código de 2 caracteres:   * es * en * eu |
| informe : Informe Private  Identificador del informe. Es una FK a la tabla "informe". Es un campo obligatorio. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Informe  Cardinality: [1] | Target: Public (Class) InformeDocumento  Cardinality: [1..\*] |

### Entidad: Memoria

Entidad que representa a las memorias que se van a evaluar enlas solicitudes de evaluación de proyectos.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "memoria". |
| numReferencia : String Private  Código que representa a la memoria, es un dato generado automáticamente y tiene el formato Mxx/YYYY/secuencia donde xx sera 10, 20 o 30 (tipo de formulario), YYYY será el año, secuencia será un código secuencial que empieza en 000 cada año y comité y va hasta 999 si es de tipo "Nueva", si es de tipo "Ratificación" lleva una R al final (Mxx/YYYY/secuenciaR), y si es de tipo "Modificación" se copia la referencia de la memoria original y se pone al final MRX donde X es un secuencial de las modificaciones que haya tenido la memoria. Es un campo obligatorio. |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece la memoria. Es una FK a la tabla "petición evaluación". |
| comite : Comite Private  Identificador del comité de ética que va a evaluar a la memoria. Es una FK a la tabla "comité". |
| personaRef : String Private  Persona designada como responsable de la memoria por la persona que realiza la solicitud de evaluación. Tiene que ser un miembro del equipo de trabajo. Se guardar el identificador o referencia de la persona en el sistema de gestión de personas de la Universidad (SGP). |
| tipo : TipoMemoria Private  Determina el tipo de memoria, es decir, si es "nueva", "modficicación" sobre una prevía dada de alta en el SGI o si se trata de una "ratificación" del equipo de investigación. Hace referencia al enumerado del SGI "tipoMemoria". |
| estadoActual : TipoEstadoMemoria Private  Estado actual en el que se encuentra la solicitud de evaluación. Es una FK a la tabla "estado memoria". |
| fechaEnvioSecretaria : Date Private  Fecha en la que el solicitante la ha enviado a "Secreataría" para su evaluación. |
| idMemoriaOriginal : Memoria Private  Identificador de la memoria la cual se toma como origen para copiarle sus respuestas del formulario cuando se trata de una memoria de tipo "modificación". Es un FK a la propia tabla "memoria". |
| requiereRetrospectiva : Boolean Private = False  Indica si la memoria requiere informar del formulario de "Retrospeciva" y enviarlo a "Secreataría para su evaluación una vez se haya conseguido el informe favorable del proyecto |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| retrospectiva : Retrospectiva Private  Identificador de la entidad que contiene el estado y la fecha de retrospecitiva. Es una FK a la tabla "retrospeciva". Sólo existirá si en el campo "requiere retrospectiva" tiene el valor "true". |
| version : Integer Private  Versión de la memoria. Cada vez que se envía la memoria a secretaría se incrementa la versión (bien sea el formulario de memoria, el formulario de seguimiento anual, el formulario de retrospectiva o el formulario de seguimiento final). Se inicializa a 0. Cuando se envía la primera vez a secretaría se sumará uno quedando el valor de la versión a 1 y así sucesivamente |
| formulario : Formulario Private  Identificador del formulario de memoria asociado. Será el formulario activo en el comité a la hora de crear la memoria. |
| formularioSeguimientoAnual : Formulario Private  Identificador del formulario de seguimiento anual asociado. Será el formulario activo en el comité a la hora de crear la memoria. |
| formularioSeguimientoFinal : Formulario Private  Identificador del formulario de seguimiento final asociado. Será el formulario activo en el comité a la hora de crear la memoria. |
| formularioRetrospectiva : Formulario Private  Identificador del formulario de retrospectiva asociado. Será el formulario activo en el comité a la hora de crear la memoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [0] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1..\*] | Target: Public (Class) Comite  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1] | Target: Public (Class) FormularioMemoria  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1] | Target: Public (Class) DocumentacionMemoria  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria | Target: Public (Class) MemoriaTitulo |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria | Target: Public (Enumeration) TipoMemoria |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [1..\*] | Target: Public (Class) TipoMemoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria  Cardinality: [0] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Informe  Cardinality: [0..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoMemoria  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Retrospectiva  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoMemoria  Cardinality: [1..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Persona | Target: Public (Class) Memoria |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Respuesta  Cardinality: [0..\*] | Target: Public (Class) Memoria  Cardinality: [1] |

### Entidad: MemoriaTitulo

Entidad para poder almacenar el título de la memoria en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas para los comités que tiene marcado que dicho campo es necesario. Normalmente el comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| memoria : Memoria Private  Identificador de la memoria a la que pertenece el resumen. Es una FK a la tabla "memoria". |
| lang : String Private  Identifica al idioma en el que esta almacenado el título. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Título de la memoria en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria | Target: Public (Class) MemoriaTitulo |

### Entidad: PeticionEvaluacion

Entidad principal del modelo lógico de Ética. Representa a la solicitud de evaluación de un proyecto de investigación ante una comisión de ética debido a que en el proyecto se trabaja con seres humanos, con animales o con agentes biológicos.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "petición evaluación". |
| solicitudConvocatoriaRef : String Private  Referencia de la solicitud del módulo CSP en el caso que la solicitud de evaluación de ética se haya creado a partir de ella.  Se corresponde con el campo "código registro interno" de la tabla "solicitud" (del módulo de CSP). |
| codigo : String Private  Código con formato YYYY/secuencia , donde YYYY es el año y secuencia en un código secuencial desde 000 hasta 999 del año. Es un campo obligatorio. |
| tipoActividad : TipoActividad Private  Clasificación de la actividad investigadora del proyecto. Es una FK a la tabla "tipo actividad". Es un campo obligatorio. |
| tipoInvestigacionTutelada : TipoInvestigacionTutelada Private  Subclasificación de la actividad investigadora del proyecto cuando en el campo "tipo actividad" se ha seleccionado el valor de "investigación tutelada". Es una FK a la tabla "tipo investigación tutelada". Es un campo obligatorio dependiendo del valor del campo "tipo actividad". |
| existeFinanciacion : Boolean Private  Indica si el solicitante dispone de financiación para realizar el proyecto. Es un campo obligatorio. |
| estadoFinanciacion : EstadoFinanciacion Private  Estado de la financiación. Es un campo obligatorio si el solicitante dispone de financiación del proyecto, es decir, cuando el "existe financiación" tiene el valor "true". Se trata en el SGI como un enumerado, con los siguientes valores:   * SOLICITADO * CONCEDIDO * DENEGADO |
| importeFinanciacion : BigDecimal Private  Importe de financiación del proyecto. Es un campo obligatorio si el solicitante dispone de financiación del proyecto, es decir, cuando el "existe financiación" tiene el valor "true". |
| fechaInicio : Date Private  Fecha de inicio del proyecto. Es un campo obligatorio. |
| fechaFin : Date Private  Fecha fin del proyecto. Es un campo obligatorio. |
| valorSocial : TipoValorSocial Private  Este campo corresponderá con el apartado 1.1 VALOR SOCIAL DEL PROYECTO del formulario de la memoria. Es un campo obligatorio. Se trata en el SGI como un enumerado con los siguientes posibles valoras:   * INVESTIGACION\_FUNDAMENTAL * INVESTIGACION\_JURIDICA * INVESTIGACION\_EVALUACION * INVESTIGACION\_DESARROLLO * INVESTIGACION\_PROTECCION * INVESTIGACION\_BIENESTAR * INVESTIGACION\_CONSERVACION * ENSENIANZA\_SUPERIOR * INVESTIGACION\_JURIDICA * OTRA\_FINALIDAD |
| tieneFondosPropios : Boolean Private = False  Campo a cumplimentar solamente cuando la petición de evaluación se inicia desde el módulo CSP. Permite indicar si, a pesar de no tener financiación, el proyecto se va a realizar con fondos propios |
| personaRef : String Private  Identificador o Referencia de la persona solicitante del proyecto. Es el identificador de la persona en el sistema de personas de la Universidad (SGP). |
| checklistId : String Private  Identificador del formulario del checklist con que contiene las preguntas y respuestas para valorar si el futuro proyecto asociado a la solicitud deberá ser evaluado por la Comisión de ética. Es una FK a la tabla "checklist" |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario |
| tutorRef : String Private  Referencia a la persona que actúa como director/a o tutor/a del trabajo. Campo solo cumplimentado en caso de que el tipo de actividad sea "investigación tutelada". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1..] | Target: Public (Class) PeticionEvaluacionObjetivos  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) EquipoTrabajo  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion | Target: Public (Class) FuenteFinanciacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionResumen  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [0..1] | Target: Public (Class) Checklist  Cardinality: [0..1] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionTitulo  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionOtroValorSocial  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionDisMetodologico  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion | Target: Public (Enumeration) TipoValorSocial |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoInvestigacionTutelada  Cardinality: [1..\*] | Target: Public (Class) PeticionEvaluacion  Cardinality: [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) EstadoFinanciacion | Target: Public (Class) PeticionEvaluacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoActividad  Cardinality: [1] | Target: Public (Class) PeticionEvaluacion  Cardinality: [0..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) Persona | Target: Public (Class) PeticionEvaluacion |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoValorSocial  Cardinality: [1] | Target: Public (Class) PeticionEvaluacion  Cardinality: [1..\*] |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionFuenteFinanciacion  Cardinality: [0..\*] |

### Entidad: PeticionEvaluacionDisMetodologico

Entidad para poder almacenar una descripción del diseño metodológico del proyecto en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece la descripción del diseño metodológico del proyecto Es una FK a la tabla "petición evaluación". |
| lang : String Private  Identifica al idioma en el que esta almacenada la descripción del diseño metodológico del proyecto . Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del diseño metodológico del proyecto en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 4000 caracteres y que dispone del componente de texto enriquecido. El campo se corresponderá con el apartado 3.2 DISEÑO METODOLÓGICO DEL PROYECTO del formulario de la memoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionDisMetodologico  Cardinality: [1..\*] |

### Entidad: PeticionEvaluacionObjetivos

Entidad para poder almacenar los principales objetivos científicos del proyecto en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenecen los principales objetivos científicos del proyecto Es una FK a la tabla "petición evaluación" |
| lang : String Private  Identifica al idioma en el que estan almacenados los principales objetivos científicos del proyecto . Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Objetivos científicos del proyecto en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 4000 caracteres y que dispone del componente de texto enriquecido. El campo se corresponderá con el apartado 3.1 OBJETIVOS CIENTÍFICOS DEL PROYECTO del formulario de la memoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1..] | Target: Public (Class) PeticionEvaluacionObjetivos  Cardinality: [1..\*] |

### Entidad: PeticionEvaluacionOtroValorSocial

Entidad para poder almacenar el valor social en el caso de que en el campo "valor social" se haya seleccionado el valor "OTRA\_FINALIDAD" en los idiomas soportados por la aplicación. En este caso es un campo obligatorio en al menos uno de los idiomas

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece la descripción de otro valor social. Es una FK a la tabla "petición evaluación". |
| lang : String Private  Identifica al idioma en el que esta almacenado el valor social. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción del valor social en el caso de que en el campo "valor social" se haya seleccionado el valor "OTRA\_FINALIDAD" en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 2000 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionOtroValorSocial  Cardinality: [1..\*] |

### Entidad: PeticionEvaluacionResumen

Entidad para poder almacenar el resumen del proyecto en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece el resumen. Es una FK a la tabla "petición evaluación". |
| lang : String Private  Identifica al idioma en el que esta almacenado el resumen. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Resumen del proyecto en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 4000 caracteres y que dispone del componente de texto enriquecido. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionResumen  Cardinality: [1..\*] |

### Entidad: PeticionEvaluacionTitulo

Entidad para poder almacenar el título del proyecto en los idiomas soportados por la aplicación. Es un campo obligatorio en al menos uno de los idiomas.

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece el título. Es una FK a la tabla "petición evaluación". |
| lang : String Private  Identifica al idioma en el que esta almacenado el título. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Título del proyecto en el idioma indicado por el campo "lang". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionTitulo  Cardinality: [1..\*] |

### Entidad: PeticionEvaluacionFuenteFinanciacion

Entidad para poder almacenar el nombre del órgano financiador del proyecto en los idiomas soportados por la aplicación. Es un campo de texto libre con un máximo de 250 caracteres. Es un campo obligatorio en al menos uno de los idiomas si el solicitante dispone de financiación del proyecto, es decir, cuando el "existe financiación" tiene el valor "true".

|  |
| --- |
| **ATTRIBUTES** |
| peticionEvaluacion : PeticionEvaluacion Private  Identificador de la solicitud de evaluación a la que pertenece el el nombre del órgano financiador del proyecto. Es una FK a la tabla "petición evaluación". |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del órgano financiador. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del órgano financiador del proyecto. en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) PeticionEvaluacion  Cardinality: [1] | Target: Public (Class) PeticionEvaluacionFuenteFinanciacion  Cardinality: [0..\*] |

### Entidad: Respuesta

Tabla con las respuestas del usuario a cada uno de los apartados de los formularios.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "respuesta". |
| memoria : Memoria Private  Identificador de la memoria a la que pertenece la respuesta del apartado del formulario. Es una FK a la tabla "memoria". |
| apartado : Apartado Private  Identificador del apartado del formulario al que pertenece la respuesta. Es una FK a la tabla "apartado". |
| valor : String Private  Respuesta del usuario al apartado del formulario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Respuesta  Cardinality: [0..\*] | Target: Public (Class) Apartado  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Respuesta  Cardinality: [0..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) ComponenteFormulario  Cardinality: [1] | Target: Public (Class) Respuesta  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormularioMemoria  Cardinality: [1] | Target: Public (Class) Respuesta  Cardinality: [1..\*] |

### Entidad: Retrospectiva

Almacena los datos de una retrospectiva para aquellas memorias que pertenecen a un comité que tiene configurado que es obligatorio introducir este apartado en su formulario. Actualmente ocurre para las memorias del comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "retrospectiva". |
| estadoRetrospectiva : EstadoRetrospectiva Private  Estado actual de la retrospectiva. Es una FK a la tabla "estado retrospectiva". Es un campo obligatorio. |
| fechaRetrospectiva : Date Private  Fecha en la que se debe de realizar la retrospectiva de la memoria. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Retrospectiva  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EstadoRetrospectiva  Cardinality: [1] | Target: Public (Class) Retrospectiva  Cardinality: [0..\*] |

### Entidad: Tarea

Entidad que define la tarea o actividad asignada a cada una de las personas del equipo del trabajo en una memoria del proyecto.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tarea". |
| equipoTrabajo : EquipoTrabajo Private  Identificador de la persona del equipo de trabajo al que se refiere la tarea. Es una FK a la tabla "equipo trabajo". |
| memoria : Memoria Private  Identificador de la memoria para la que se esta realizando la taera. Es una FK a la tabla "memoria". |
| formacionEspecifica : FormacionEspecifica Private  Identificador del tipo de formación que tiene la persona para aquellas memorias que pertenezcan a un comité cuya variable de configuración "tarea experiencia libre" tenga el valor "false". Normalmente será el comité CEEA. Para estos casos es un campo obligatorio. Es una FK a la tabla "formación específica". |
| anio : Integer Private  Entidad para almacenar el año de obtención de la formación de la persona la persona cuando la asignación de la tarea es para una memoria que tiene configurado el comité con la variable "tarea experiencia detalle" con valor "true". Normalmente los comités CEEA y CBE. Para estos casos es un campo obligatorio. |
| tipoTarea : TipoTarea Private  Identificador del tipo de tarea que va a realizar la persona cuando la asignación de la tarea es para una memoria que tiene configurado el comité con la variable "tarea nombre libre" con valor "false". Normalmente el comité CEEA. Para estos casos es un campo obligatorio y se deberá seleccionar uno de los valores de la tabla "tipo tarea". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaOrganismo  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1..\*] | Target: Public (Class) Memoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaFormacion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaNombre  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoTarea  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) EquipoTrabajo  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) FormacionEspecifica  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [0..\*] |

### Entidad: TareaFormacion

Entidad para almacenar en un campo de texto la experiencia que tiene la persona haciendo la tarea encomendada o la formación de la persona para aquellas memorias que pertenezcan a un comité cuya variable de configuración "tarea experiencia libre" tenga el valor "true". Normalmente los comités CEI y CBE. Para estos casos es un campo obligatorio en al menos uno de los idiomas

|  |
| --- |
| **ATTRIBUTES** |
| tarea : Tarea Private  Identificador de la tarea a la que pertenece la descripción de la experiencia o formación. Es una FK a la tabla "tarea. |
| lang : String Private  Identifica al idioma en el que esta almacenada la descripción de la experiencia o formación. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción de la experiencia en la tarea encomendada a la persona o su formación en la tarea. Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaFormacion  Cardinality: [0..\*] |

### Entidad: TareaNombre

Entidad para almacenar la descripción de la tarea que va a realizar la persona cuando la asignación de la tarea es para una memoria que tiene configurado el comité con la variable "tarea nombre libre" con valor "true". Normalmente los comités CEI y CBE. Para estos casos es un campo obligatorio en al menos uno de los idiomas

|  |
| --- |
| **ATTRIBUTES** |
| tarea : Tarea Private  Identificador de la tarea a la que pertenece la descripción. Es una FK a la tabla "tarea. |
| lang : String Private  Identifica al idioma en el que esta almacenada la descripción de la tarea. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Descripción de la tarea que va a realizar la persona. Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaNombre  Cardinality: [0..\*] |

### Entidad: TareaOrganismo

Entidad para almacenar el organismo donde se ha formado la persona cuando la asignación de la tarea es para una memoria que tiene configurado el comité con la variable "tarea experiencia detalle" con valor "true". Normalmente los comités CEEA y CBE. Para estos casos es un campo obligatorio en al menos uno de los idiomas

|  |
| --- |
| **ATTRIBUTES** |
| tarea : Tarea Private  Identificador de la tarea a la que pertenece el organismo donde se ha formado. Es una FK a la tabla "tarea. |
| lang : String Private  Identifica al idioma en el que esta almacenado el organismo donde se ha formado la persona. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del organismo donde se ha formado la persona. Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Tarea  Cardinality: [1] | Target: Public (Class) TareaOrganismo  Cardinality: [0..\*] |

### Entidad: TipoActividad

Tabla con los tipos de actividad investigadora de una solicitud de evaluación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo actividad". |
| nombre : String Private  Nombre del tipo de actividad investigadora. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoActividad  Cardinality: [1] | Target: Public (Class) PeticionEvaluacion  Cardinality: [0..\*] |

### Entidad: TipoComentario

Tabla con los distintos tipos de comentarios soportados en la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo comentario". |
| nombre : String Private  Nombre del tipo de comentario. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoComentario  Cardinality: [1] | Target: Public (Class) Comentario  Cardinality: [0..\*] |

### Entidad: TipoConvocatoriaReunion

Tabla con los tipos de convocatoria de reunión.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo convocatoria reunión". |
| nombre : String Private  Nombre del tipo de convocatoria de reunión. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoConvocatoriaReunion  Cardinality: [1] | Target: Public (Class) ConvocatoriaReunion  Cardinality: [0..\*] |

### Entidad: TipoDocumento

Tabla con los tipos de documento que puede tener cada uno de los formularios de memorias. Los tipos de documento que se les pedirá en el bloque 5 del formulario de memoria.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo documento". |
| formulario : Formulario Private  Identificador del formulario donde se pedirá el tipo de documento. Es una FK a la tabla "formulario". |
| codigo : String Private  Campo de texto que identifica al documento dentro del formulario. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |
| adicional : Boolean Private = False  Campo para indicar si el tipo de documento es el tipo "adicional" o no. Se necesita identificar al documento adicional porque será el tipo que puedan los gestores adjuntar documento y el que se pueda adjuntar en las memorias de tipo "ratificación". |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality: [0..\*] | Target: Public (Class) Formulario  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality: [1] | Target: Public (Class) TipoDocumentoNombre  Cardinality: [1..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) DocumentacionMemoria  Cardinality: [0..\*] | Target: Public (Class) TipoDocumento  Cardinality: [1] |

### Entidad: TipoDocumentoNombre

Entidad para poder almacenar el nombre del tipo de documento en los idiomas soportados por la aplicación.

|  |
| --- |
| **ATTRIBUTES** |
| tipoDocumento : TipoDocumento Private  Identificador del documento de la memoria al que describe. Es una FK a la tabla "documentación memoria". |
| lang : String Private  Identifica al idioma en el que esta almacenado el nombre del documento. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Nombre del documento de la memoria en el idioma indicado por el campo "lang". Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoDocumento  Cardinality: [1] | Target: Public (Class) TipoDocumentoNombre  Cardinality: [1..\*] |

### Entidad: TipoEstadoActa

Tabla con los distintos estados por lo que puede pasar un acta.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo estado acta". |
| nombre : String Private  Nombre del estado por los que puede pasar una acta. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = Boolean  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoActa  Cardinality: [1] | Target: Public (Class) Acta  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoActa  Cardinality: [1] | Target: Public (Class) EstadoActa  Cardinality: [0..\*] |

### Entidad: TipoEstadoMemoria

Tabla con los tipos de estado por los que pasa una memoria desde que es creado por el solicitante hasta que obtiene un dictamen favorable y pasa por el ciclo de seguimiento anual y seguimiento final.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo estado memoria". |
| nombre : String Private  Nombre del tipo de estado de la memoria. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoMemoria  Cardinality: [1] | Target: Public (Class) Memoria  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEstadoMemoria  Cardinality: [0..\*] | Target: Public (Class) EstadoMemoria  Cardinality: [1] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoMemoria | Target: Public (Class) TipoEstadoMemoria |

### Entidad: TipoEvaluacion

Tabla con los distintos tipos de evaluación.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo evaluación". |
| nombre : String Private  Nombre del tipo de evaluación. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEvaluacion  Cardinality: [1] | Target: Public (Class) Evaluacion  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoEvaluacion  Cardinality: [1] | Target: Public (Class) Dictamen  Cardinality: [0..\*] |

### Entidad: TipoInvestigacionTutelada

Tabla con los tipos de investigación tutelada. Se hace uso de ella cuando el tipo de actividad es de tipo "Investigación tutelada".

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo investigación tutelada". |
| nombre : String Private  Nombre del tipo de investigación tutelada. Es un campo de texto libre con un máximo de 250 caracteres. |
| activo : Boolean Private  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoInvestigacionTutelada  Cardinality: [1..\*] | Target: Public (Class) PeticionEvaluacion  Cardinality: [0..\*] |

### Entidad: TipoTarea

Tabla con los tipos de tarea que puede realizar una persona para aquellas memorias que pertenezcan a un comité cuya variable de configuración "tarea nombre libre" tenga el valor "false". Normalmente será el comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| id : Long Private  Clave primaria. Secuencia. Identificador único del registro dentro de la tabla "tipo tarea". |
| activo : Boolean Private = True  Campo interno al SGI con el que se da cobertura al borrado lógico. El valor "true" será indicativo de que el registro está activo mientras que un valor "false" será indicativo de que el registro ha sido eliminado a nivel de usuario. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoTarea  Cardinality: [1] | Target: Public (Class) Tarea  Cardinality: [0..\*] |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoTareaNombre  Cardinality: [1] | Target: Public (Class) TipoTarea  Cardinality: [1..\*] |

### Entidad: TipoTareaNombre

Entidad para almacenar los tipos de tarea en los distintos idiomas para memorias que tienen configurado el comité con la variable "tarea nombre libre" con valor "false". Normalmente el comité CEEA.

|  |
| --- |
| **ATTRIBUTES** |
| tipoTarea : TipoTarea Private  Identificador del tipo de tarea. Es una FK a la tabla "tipo tarea. |
| lang : String Private  Identifica al idioma en el que esta almacenado el tipo de tarea. Es un código de 2 caracteres:   * es * en * eu |
| value\_ : String Private  Tipo de la tarea en un idioma concreto. Es un campo de texto libre con un máximo de 250 caracteres. |

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoTareaNombre  Cardinality: [1] | Target: Public (Class) TipoTarea  Cardinality: [1..\*] |

## Enumerados

### TipoValorSocial

Enumerado que representa los tipos de valor social que puede tener una solicitud de evaluación. Valores:

* INVESTIGACION\_FUNDAMENTAL
* INVESTIGACION\_JURIDICA
* INVESTIGACION\_EVALUACION
* INVESTIGACION\_DESARROLLO
* INVESTIGACION\_PROTECCION
* INVESTIGACION\_BIENESTAR
* INVESTIGACION\_CONSERVACION
* ENSENIANZA\_SUPERIOR
* INVESTIGACION\_JURIDICA
* OTRA\_FINALIDAD

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) TipoValorSocial  Cardinality: [1] | Target: Public (Class) PeticionEvaluacion  Cardinality: [1..\*] |

### EstadoFinanciacion

Enumerado que representa los estados de financiación que puede tener una solicitud de evaluación. Valores:

* SOLICITADO
* CONCEDIDO
* DENEGADO

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) EstadoFinanciacion | Target: Public (Class) PeticionEvaluacion |

### EstadoRetrospectiva

Enumerado que representa los estados de una retrospectiva. Valores:

* 1: El valor 1 representa el estado "Pendiente".
* 2: El valor 2 representa el estado "Completada".
* 3: El valor 3 representa el estado "En secretaría".
* 4: El valor 4 representa el estado "En evaluación".
* 5: El valor 5 representa el estado "Fin evaluación".

### Genero

Enumerado que representa el tratamiento con el que se debe de hacer referencia al comité. Valores:

* F: El valor F representa que se debe de usar el género femenino para referirse al comité (la).
* M: El valor M representa que se debe de usar el género masculino para referirse al comité (el).

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) Genero | Target: Public (Class) ComiteNombre |

### SeguimientoAnualDocumentacionTitle

Enumerado que representa los distintos títulos que se puede mostrar en el apartado de Documentación del seguimiento anul. Valores:

* TITULO\_1: El valor TITULO\_1 representa el texto " Adjuntar pdf de las publicaciones si se hubiesen generado con el proyecto, así como aquella documentación cuyo modelo fue aprobado por el comité (IF) y que requería firmas (por ejemplo: Autorización de Centros escolares, residenciales, deportivos, Convenios, etc.):"
* TITULO\_2: El valor TITULO\_2 representa el texto "Adjuntar pdf de las publicaciones si se hubiesen generado con el proyecto durante el primer año:"
* TITULO\_3: El valor TITULO\_2 representa el texto "Adjuntar pdf de las publicaciones si se hubiesen generado con el proyecto, así como aquella documentación cuyo modelo fue aprobado por el comité (IF) y que requería firmas (por ejemplo: MTA, Convenios, etc.):"

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario | Target: Public (Enumeration) SeguimientoAnualDocumentacionTitle |

### TipoActividad

Enumerado que representa los tipos de actividad investigadora de una solicitud de evaluación. Valores:

* 1: El valor 1 representa una Proyecto de investigación
* 2: El valor 2 representa un Práctica docente
* 3: El valor 3 representa un Investigación tutelada

### TipoComentario

Enumerado que representa los tipos de comentarios. Valores:

* 1: El valor 1 representa un comentario de tipo "GESTOR".
* 2: El valor 2 representa un comentario de tipo "EVALUADOR".
* 3: El valor 3 representa un comentario de tipo "ACTA\_GESTOR".
* 4: El valor 4 representa un comentario de tipo "ACTA\_EVALUADOR".

### TipoConvocatoriaReunion

Enumerado que representa los tipos de convocatoria de reunión. Valores:

* 1: El valor 1 representa un comentario de tipo "ORDINARIA".
* 2: El valor 2 representa un comentario de tipo "EXTRAORDINARIA".
* 3: El valor 3 representa un comentario de tipo "SEGUIMIENTO".

### TipoDictamen

Enumerado que representa los tipos de dictamen existentes para cada tipo de evaluación. Valores:

* 1: El valor 1 representa el dictamen "Favorable" del tipo de evaluación "Memoria"
* 2: El valor 2 representa el dictamen "Favorable pendiente de revisión mínima" del tipo de evaluación "Memoria"
* 3: El valor 3 representa el dictamen "Pendiente de correcciones" del tipo de evaluación "Memoria"
* 4: El valor 4 representa el dictamen "No procede evaluar" del tipo de evaluación "Memoria"
* 5: El valor 5 representa el dictamen "Favorable" del tipo de evaluación "Seguimiento anual"
* 6: El valor 6 representa el dictamen "Solicitud de modificaciones" del tipo de evaluación "Seguimiento anual"
* 7: El valor 7 representa el dictamen "Favorable" del tipo de evaluación "Seguimiento final"
* 8: El valor 8 representa el dictamen "Solicitud de aclaraciones" del tipo de evaluación "Seguimiento final"
* 9: El valor 9 representa el dictamen "Favorable" del tipo de evaluación "Retrospectiva"
* 10: El valor 10 representa el dictamen "Desfavorable" del tipo de evaluación "Retrospectiva"
* 11: El valor 11representa el dictamen "Desfavorable" del tipo de evaluación "Memoria"

### TipoEstadoActa

Enumerado que representa los tipos de estado por lo que pasa una acta. Valores:

* 1: El valor 1 representa una memoria en estado "En elaboración".
* 2: El valor 2 representa una memoria en estado "Finalizada".

### TipoEstadoComentario

Enumerado que representa los tipos de estado de un comentario. Valores:

* CERRADO
* ABIERTO

Los comentarios mostrados en la ficha del evaluador o los mostrados en el acta serán los comentarios cerrados, es decir, los que han sido envíados por el evaluador a secretaría. Los abiertos no se considerarán.

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Comentario | Target: Public (Enumeration) TipoEstadoComentario |

### TipoEstadoMemoria

Enumerado que representa los tipos de estado por lo que pasa una memoria. Valores:

* 1: El valor 1 representa una memoria en estado "En elaboración".
* 2: El valor 2 representa una memoria en estado "Completada".
* 3: El valor 3 representa una memoria en estado "En secretaría".
* 4: El valor 4 representa una memoria en estado "En secretaría revisión mínima".
* 5: El valor 5 representa una memoria en estado "En evaluación".
* 6: El valor 6 representa una memoria en estado "Favorable Pendiente de Modificaciones Mínimas".
* 7: El valor 7 representa una memoria en estado "Pendiente de correcciones".
* 8: El valor 8 representa una memoria en estado "No procede evaluar".
* 9: El valor 9 representa una memoria en estado "Fin evaluación".
* 10: El valor 10 representa una memoria en estado "Archivado".
* 11: El valor 11 representa una memoria en estado "Completada seguimiento anual".
* 12: El valor 12 representa una memoria en estado "En secretaría seguimiento anual".
* 13: El valor 13 representa una memoria en estado "En evaluación seguimiento anual".
* 14: El valor 14 representa una memoria en estado "Fin evaluación seguimiento anual".
* 15: El valor 15 representa una memoria en estado "Solicitud modificación".
* 16: El valor 16 representa una memoria en estado "Completada seguimiento final".
* 17: El valor 17 representa una memoria en estado "En secretaría seguimiento final".
* 18: El valor 18 representa una memoria en estado "En secretaría seguimiento final aclaraciones".
* 19: El valor 19 representa una memoria en estado "En evaluación seguimiento final".
* 20: El valor 20 representa una memoria en estado "Fin evaluación seguimiento final".
* 21: El valor 21 representa una memoria en estado "En aclaración seguimiento final".
* 22: El valor 22 representa una memoria en estado "Subsanación".
* 23: El valor 23 representa una memoria en estado "Desfavorable".
* 24: El valor 24 representa una memoria en estado "Solicitud modificación seguimiento anual".
* 25: El valor 25 representa una memoria en estado "En secretaría seguimiento anual modificación".
* 26: El valor 26 representa una memoria en estado "En evaluación revisión mínima".

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Enumeration) TipoEstadoMemoria | Target: Public (Class) TipoEstadoMemoria |

### TipoEvaluacion

Enumerado que representa los tipos de evaluación. Valores:

* 1: El valor 1 representa una evaluación de tipo "Retrospectiva". Se evalúa el formulario de Restrospectiva.
* 2: El valor 2 representa una evaluación de tipo "Memoria". Se evalúa el formulario de "Memoria" (pestaña Formulario).
* 3: El valor 3 representa una evaluación de tipo "Seguimiento anual". Se evalúa el formulario de "Seguimiento anual".
* 4: El valor 4 representa una evaluación de tipo "Seguimiento final". Se evalúa el formulario de "Seguimiento final".

### TipoFormulario

Enumerado que representa los tipos de formulario. Valores:

* MEMORIA
* SEGUIMIENTO\_ANUAL
* SEGUIMIENTO\_FINAL
* RETROSPECTIVA

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Formulario | Target: Public (Enumeration) TipoFormulario |

### TipoInvestigacionTutelada

Enumerado que representa los tipos de investigación tutelada. Valores:

* 1: El valor 1 representa una Tesis Doctotal
* 2: El valor 2 representa un Trabajo Fin de Máster
* 3: El valor 3 representa un Trabajo Fin de Grado

### TipoMemoria

Enumerado que representa los tipos de memoria. Valores:

* NUEVA
* MODIFICACION
* RATIFICACION

|  |  |
| --- | --- |
| **ASSOCIATIONS** | |
|  |  |
| --- | --- |
| Association (direction: Unspecified) | |
| Source: Public (Class) Memoria | Target: Public (Enumeration) TipoMemoria |

### TpoCargoComite

Enumerado que representa los tipos de cargo de un comité. Valores:

* 1: El valor 1 representa el cargo "PRESIDENTE".
* 2: El valor 2 representa el cargo "VOCAL".
* 3: El valor 3 representa el el cargo "SECRETARIO".