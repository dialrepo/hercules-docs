# IU-CSP-0201-001 - Crear convocatoria - Datos generales

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0101-001 Crear convocatoria - Datos generales******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Crear convocatoria - Datos generales

La información de una convocatoria estará distribuida en los siguientes apartados:

* **Datos generales**
* Entidades convocantes
* Entidades financiadoras
* Enlaces
* Fases
* Periodos justificación
* Seguimiento científico
* Hitos
* Documentos
* Requisitos IP
* Requisitos Equipo
* Elegibilidad
* Configuración de solicitudes.

### Datos generales

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Título | Texto (1000 caracteres)  Obligatorio | Campo para introducir el título de la convocatoria.  Se le debe dar un tamaño de 1000 caracteres.  Se corresponde con el campo "título" de la tabla "convocatoria". |
| Tipo solicitud SGI | Selector  Texto corto  Obligatorio | Campo para especificar el tipo de formulario con el que se recogerán en el SGI las solicitudes asociadas a la convocatoria. Podrá tomar uno de los valores:   * Proyecto. Se utilizará este valor cuando la convocatoria se corresponda con una ayuda para el desarrollo de proyectos. Seleccionar este valor implica además de que el formulario para recoger la solicitud tenga unos campos determinados que el resultado final de la convocatoria dé lugar al registro, en el SGI, de un Proyecto. * Grupo. Se utilizará este valor cuando la convocatoria se corresponda con una convocatoria de constitución de Grupos de investigación. Seleccionar este valor implica además de que el formulario para recoger la solicitud tenga unos campos determinados que el resultado final de la convocatoria dé lugar al registro, en el SGI, de un Grupo de investigación. * RRHH. Se utilizará este valor cuando la convocatoria se corresponda con una ayuda de contratación de RRHH. Seleccionar este valor implica además de que el formulario para recoger la solicitud tenga unos campos determinados que el resultado final de la convocatoria dé lugar al registro, en el SGI, de un Proyecto.   El listado se corresponde con los valores del enumerado "Tipo formulario solicitud". Por defecto, se precargará el valor "Proyecto"  Es un campo de introducción obligatoria. Se corresponde con el campo "formulario solicitud" de la tabla "convocatoria". |
| Unidad de gestión | Selector  Texto corto  Obligatorio | Listado con los valores de la unidad de gestión (OTRI, OPE, UGI, etc.) que realiza la gestión de la convocatoria .  Las unidades de gestión disponibles en el desplegable serán solamente aquellas sobre las que el usuario que está creando la convocatoria disponga de un rol ACT-CSP-003-Gestor o ACT-CSP-004-Administrador. |
| Modelo de ejecución | Selector  Texto corto  Obligatorio si estado Registrada | Listado con los valores de modelos de ejecución activos que tenga asociados la unidad de gestión a la que se ha asociado la convocatoria a través del campo "Unidad de gestión". Ejemplos de valores: Contrato art.83, proyecto I+D, ayuda RRHH, etc. Puede consultarse [CSP - Modelo de ejecución](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-modelo-de-ejecucion) |
| Finalidad | Selector  Texto corto  Obligatorio si estado Registrada | Listado con los tipos de finalidad activos que estén asociados al Modelo de ejecución (ModeloTipoFinalidad activos) al que se haya vinculado la convocatoria en el campo anterior.  Ejemplos de valores: proyectos i+d, contratación rrhh, servicios técnicos, asesorías, movilidades, constitución grupos, infraestructuras, royalties, etc. Puede consultarse [CSP - Modelo de ejecución](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-modelo-de-ejecucion) e [IU-CSP-0020 - Gestión de tipos de finalidad](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0020-gestion-de-tipos-de-finalidad) |
| Identificación | Texto corto  Opcional | Código de identificación de la convocatoria que puede ser utilizado para recoger la referencia externa de la convocatoria. Es un campo totalmente independiente del identificador secuencial interno. El código de referencia será de introducción libre por el ACT-CSP-003-Gestor o ACT-CSP-004-Administrador y no será obligatorio.  Se corresponde con el campo "código" de la tabla "convocatoria". |
| Entidad gestora | Buscador  Texto  Opcional | Entidad u organismo que actúa como gestor de la convocatoria.  El listado de entidades disponible se obtendrá a partir del buscador de empresas será el común al SGI,  [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas), procedente del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa). |
| Fecha publicación | Fecha  Opcional | Fecha de publicación.  Se corresponde con el campo "fecha publicación" de la tabla "convocatoria". |
| Fecha provisional | Fecha  Opcional | Fecha de resolución provisional.  Se corresponde con el campo "fecha provisional" de la tabla "convocatoria". |
| Fecha concesión | Fecha  Opcional | Fecha de concesión.  Se corresponde con el campo "fecha concesión" de la tabla "convocatoria". |
| Duración de la actividad resultante (meses) | Numérico entero  Opcional | Valor numérico, expresado en meses, que indicará la duración prevista de la actividad de investigación (proyecto, contrato) resultante de la convocatoria.  Se corresponde con el campo "duración" de la tabla "convocatoria". |
| Convocatoria de excelencia | Selector (valores sí/no)  Boolean  Opcional | Indicará si la convocatoria está considerada o no como  una convocatoria de excelencia.  Podrá tomar valor Sí/No.  Se corresponde con el campo "excelencia" de la tabla "convocatoria". |
| Ámbito geográfico | Selector  Texto corto  Obligatorio si estado Registrada | El listado de valores disponibles se cargará a partir de los registros activos de la tabla "tipo ámbito geográfico". Un ejemplo de listado posible sería: propio, local, regional, autonómico, estatal, europeo, internacional no europeo. [CSP - Convocatorias - Gestión de ámbitos geográficos](/hercules/sgi-sistema-de-gestion-de-investigacion/mdu-manual-de-usuario/mdu-perfil-unidad-de-gestion/mdu-perfil-unidad-de-gestion-modulo-csp/csp-convocatorias#CSP-Convocatorias-ambitos_geograficosGesti%C3%B3nde%C3%A1mbitosgeogr%C3%A1ficos)  El valor seleccionado se almacenará en el campo "ámbito geográfico" de la tabla "convocatoria". |
| Régimen de concurrencia | Selector  Texto corto  Opcional | El listado de valores disponibles se cargará a partir de los registros activos de la tabla "Tipo régimen concurrencia". Un ejemplo de listado posible sería:   * Concurrencia competitiva * Concesión directa   El valor seleccionado se almacenará en el campo "régimen concurrencia" de la tabla "convocatoria". |
| Clasificación producción científica/CVN | Selector  Texto corto Opcional | El listado de valores disponibles se cargará a partir de un listado fijo del SGI (listado de enumerados "Apartado CVN"). Este listado se corresponderá con apartados de Producción científica y/o CVN. Si al crear la convocatoria se selecciona un valor de este listado, la actividad derivada de la convocatoria pasará automáticamente a formar parte del CVN bajo el epígrafe indicado en este campo.  El valor seleccionado se almacenará en el campo "apartado cvn" de la tabla "convocatoria". |
| Palabras clave | Componente a medida  Opcional | Lista de palabras clave asociadas a la convocatoria.  El comportamiento del componente será el descrito de manera general en [IU-GEN-0200 - Gestión de palabras clave](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/plcl-palabras-clave/gen-palabras-clave-interfaz-de-usuario/iu-gen-0200-gestion-de-palabras-clave). |
| Objeto o descripción general de la convocatoria | Texto largo  Opcional | Objetivos de la convocatoria.  Se corresponde con el campo "objeto" de la tabla "convocatoria". |
| Observaciones | Texto largo  Opcional | Observaciones de carácter interno de la convocatoria.  Se corresponde con el campo "observaciones" de la tabla "convocatoria". |
| Áreas temáticas | Tabla de listado  Opcional | Áreas temáticas a las que limita la convocatoria.  Se mostrará en formato de tabla. En la fase de creación la  tabla estará vacía.  Ver [IU-CSP-0204-001 - Modificar convocatoria - Datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-0204-modificar-convocatoria/iu-csp-0204-001-modificar-convocatoria-datos-generales) |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Buscar (entidad gestora) | Muestra la pantalla de búsqueda para seleccionar la entidad gestora. | El listado de entidades disponible se obtendrá a través del buscador de Empresas común a todo el SGI, [IU-GEN-0100-0080 - Búsqueda de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas), que hará uso para su resolución del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa). |
| Añadir área temática |  | Muestra la pantalla para añadir un área temática [IU-CSP-202-001 - Añadir área temática](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-202-001-anadir-area-tematica). |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea la Convocatoria con la información introducida en el formulario.  Al guardar una convocatoria se guardar la información de todos los apartados de definición de la convocatoria. | * Estado: El campo estado tomará por defecto el valor "Borrador". * Unidad de gestión: El listado solo contendrá la unidades de gestión sobre las que el usuario tenga rol ACT-CSP-003-Gestor o ACT-CSP-004-Administrador * Modelo ejecución: el listado proporcionado en el selector se corresponderá con los modelos de ejecución disponibles para la Unidad de gestión indicada en el campo "unidad de gestión" * Finalidad: el listado proporcionado en el selector se corresponderá con los tipos de finalidad disponibles para el modelo de ejecución indicado en el campo "modelo ejecución".   Serán obligatorios los siguientes campos:   * Estado * Título * Tipo solicitud SGI * Unidad de gestión | CSP-CON-C  CSP-CON-C\_UO |
| Cancelar | Retorna al listado de Convocatorias sin salvar los posibles cambios. | Se mostrarán los avisos de datos no guardados sobre los apartados de datos que hubieran sido introducidos. |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-CON-C, CSP-CON-C\_UO |
| ACT-CSP-003-Gestor | CSP-CON-C, CSP-CON-C\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-C, CSP-CON-C\_UO |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.