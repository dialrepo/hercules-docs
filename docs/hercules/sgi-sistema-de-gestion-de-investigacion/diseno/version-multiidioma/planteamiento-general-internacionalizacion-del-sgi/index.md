# Planteamiento general internacionalización del SGI

* [Internacionalización (multilingüismo) a nivel de front-end](#PlanteamientogeneralinternacionalizacióndelSGI-Internacionalización(multilingüismo)aniveldefront-end)
  + [Etiquetas y mensajes](#PlanteamientogeneralinternacionalizacióndelSGI-Etiquetasymensajes)
  + [Informes](#PlanteamientogeneralinternacionalizacióndelSGI-Informes)
  + [Formly (formularios de memorias de Ética)](#PlanteamientogeneralinternacionalizacióndelSGI-Formly(formulariosdememoriasdeÉtica))
  + [Selección de idioma](#PlanteamientogeneralinternacionalizacióndelSGI-Seleccióndeidioma)
* [Internacionalización (multilingüismo) a nivel de contenido](#PlanteamientogeneralinternacionalizacióndelSGI-Internacionalización(multilingüismo)aniveldecontenido)
* [Especificación del requisito](#PlanteamientogeneralinternacionalizacióndelSGI-Especificacióndelrequisito)
  + [Idioma por defecto/priorización de idiomas](#PlanteamientogeneralinternacionalizacióndelSGI-Idiomapordefecto/priorizacióndeidiomas)
  + [Comportamiento de los listados](#PlanteamientogeneralinternacionalizacióndelSGI-Comportamientodeloslistados)
  + [Comportamiento de los buscadores](#PlanteamientogeneralinternacionalizacióndelSGI-Comportamientodelosbuscadores)
  + [Cambios en modelo de datos](#PlanteamientogeneralinternacionalizacióndelSGI-Cambiosenmodelodedatos)
  + [Cambios en interface de la aplicación](#PlanteamientogeneralinternacionalizacióndelSGI-Cambioseninterfacedelaaplicación)
  + [Cambios en servicios del API del SGI](#PlanteamientogeneralinternacionalizacióndelSGI-CambiosenserviciosdelAPIdelSGI)
  + [Gestión de documentos](#PlanteamientogeneralinternacionalizacióndelSGI-Gestióndedocumentos)
  + [Comunicados](#PlanteamientogeneralinternacionalizacióndelSGI-Comunicados)
  + [Traducciones de los textos](#PlanteamientogeneralinternacionalizacióndelSGI-Traduccionesdelostextos)
  + [Particularidades módulo PRC. Algoritmo de baremación](#PlanteamientogeneralinternacionalizacióndelSGI-ParticularidadesmóduloPRC.Algoritmodebaremación)

El SGI será una aplicación multilingüe tanto a nivel de front (etiquetas, botones, mensajes ...) como a nivel de contenido.

### Internacionalización (multilingüismo) a nivel de front-end

El sistema SGI dispondrá de todas sus etiquetas y mensajes traducidos a varios idiomas. Inicialmente se dará cobertura a los idiomas:

* Español
* Euskera
* Inglés

Las traducciones a nuevos idiomas se irán incorporando progresivamente de acuerdo a la necesidad marcada por el ritmo de implantación del SGI. Para dar cobertura a un nuevo idioma se deberán cargar los diferentes ficheros de propiedades y mensajes, así como introducir la configuración para el nuevo idioma en las estructuras internas de enumerados correspondientes. Tras la introducción de la configuración para el nuevo idioma, será necesario generar una nueva versión de la aplicación y realizar el despliegue/redespliegue de la misma.  
Una vez desplegada la versión incluyendo la configuración de los idiomas, éstos se podrán activar/ocultar a través del módulo de Administración. Se dispondrá de una variable de configuración que permitirá seleccionar los idiomas, de entre los disponibles, que van a estar habilitados. Lo idiomas habilitados estarán disponibles en el selector de idiomas situado en la cabecera de la aplicación web.  
El multiidioma se aplicará a:

* Etiquetas
* Mensajes
* Formly (formularios de memorias de Ética)
* Informes

#### Etiquetas y mensajes

Se dispondrá de un fichero de recursos por cada uno de los idiomas configurados en la aplicación. Cada fichero contendrá la traducción de las etiquetas y mensajes usados en la aplicación.

#### Informes

Se hará uso de un objeto "lenguaje" donde se incluirán los n idiomas disponibles. Cada informe deberá estar disponible de forma individual en cada uno de los idiomas para los que está disponible la aplicación. Deberá de existir una plantilla por informe e idioma. Ejemplo:  
rep-eti-mxx-en.docx  
rep-eti-mxx-es.docx  
rep-eti-mxx-eu.docx  
Los informes que se almacenan en el SGDOC, como son los documentos asociados a las memorias de Ética (que se generan en el acción "enviar a secretaría") y los documentos de acta de reunión de Ética (que se generan en la acción "finalizar acta"), se generarán en cada uno de los idiomas disponibles en la configuración.  
Los informes que se generan en el momento de la descarga, se generarán de acuerdo a la plantilla correspondiente al idioma seleccionado en cada momento.  
La descarga de cualquier  informe se realizará en el idioma en uso de la aplicación en cada momento.

#### Formly (formularios de memorias de Ética)

Actualmente  existen formularios desarrollados con tecnología Formly en el módulo de ética (M10, M20, M30, seguimiento anual, seguimiento final y retrospectiva). Estos formularios deberán ser internacionalizados para que las preguntas y textos de ayuda se muestren en el idioma seleccionado en cada momento. Los formularios están estructurados en bloques y apartados. Cada uno de ellos deberá quedar vinculado con un idioma.  
Los apartados de estos formularios se deben de refrescar automáticamente al idioma seleccionado, tras seleccionar el idioma correspondiente, sin necesidad de recargar la página. Para ello se pedirán al servidor todos los apartados de los formly en los "n" idiomas del sistema y será la vista la que filtre estas preguntas al seleccionar el idioma correspondiente. Se evitará así que se haga un refresco de la petición al servidor ya que se tendrán todos los datos necesarios recuperados previamente. Esta misma solución se aplicará a cualquier pantalla de la aplicación en la que intervengan las estructuras formly, como son  las pantallas de introducción de comentarios sobre evaluaciones y actas.

#### Selección de idioma

Los idiomas habilitados en la implantación estarán disponibles en la cabecera de la aplicación. El cambio de idioma se realizará a través del desplegable disponible. Los idiomas se muestra por su código ISO de tres caracteres.  
![](/attachments/1205862474/1205862475.png)   
![](/attachments/1205862474/1205862476.png)

### Internacionalización (multilingüismo) a nivel de contenido

El SGI Hércules en su versión piloto inicial, desarrollada bajo el liderazgo de la Universidad de Murcia, no daba cobertura al multilingüismo, ni a nivel de interface de uso (menús, etiquetas, mensajes, ...) ni a nivel de introducción de datos.    
Iniciado el plan de expansión del SGI Hércules surge, de la mano de la Universidad del País Vasco/Euskal Herriko Unibertsitatea (UPV/EHU),  la necesidad de dar cobertura al multilingüismo.   
Como parte de los servicios contratados para la implantación del SGI Hércules en la UPV/EHU se incluyeron los trabajos evolutivos necesarios para que el sistema fuese una aplicación multilingüe a nivel de interface de uso: menús, formularios, mensajes de aplicación; en líneas generales será una aplicación multilingüe a nivel de front-end. Como resultado se libera una versión del SGI Hércules con un interface de uso disponible en tres idiomas: castellano, euskera e inglés. Esta versión, sin embargo, no abarca el multilingüismo en los contenidos generados por el/la usuario/a. Es decir, en esta primera versión multilingüe, los/las usuarios/as seguían limitados a la introducción de sus datos en un único idioma. Cualquier dato/contenido que sea introducido por el/la usuario/a se almacena en las bases de datos internas en un único idioma. Del mismo modo, el diseño de las bases de datos del SGI Hércules continua dando cobertura a un único idioma.  
Sin embargo, las necesidades coyunturales de la UPV/EHU determinan la necesidad de implantación de una versión multilingüe no sólo a nivel de interface de uso, sino también a nivel de contenido. Para ello se requiere la construcción de una nueva versión del SGI. Se describe a continuación la solución técnica/funcional de los trabajos a realizar. Estos trabajos se desarrollan bajo el marco de una nueva contratación de servicios.

### Especificación del requisito

Se debe de evolucionar el SGI Hércules a una aplicación multi-idioma a nivel de contenido. Esto requiere un conjunto de cambios que se pueden catalogar como de alto impacto puesto que implican la reestructuración prácticamente por completo del modelo de datos. También es necesario aplicar cambios a nivel de interface de uso. A continuación se detallan los cambios a realizar así como se hace una explicación general del tratamiento de los idiomas configurados.

#### Idioma por defecto/priorización de idiomas

Una vez realizado el desarrollo de la versión multilingüe, el SGI quedará diseñado para que el sistema pueda estar disponible en un número variable de idiomas, de manera que los trabajos de inclusión de un nuevo idioma quedarán reducidos a la adecuada configuración de los ficheros de traducción correspondientes. La inclusión de nuevos idiomas se podrá hacer progresivamente, a medida que sean requeridos. De acuerdo a sus necesidades particulares, en cada implantación del SGI se podrá habilitar un número diferente de idiomas de entre los que estén disponibles.  
Los idiomas habilitados en cada implantación, contarán con una priorización que también será de configuración libre en cada implantación. El primero de los idiomas, de acuerdo a esta priorización, actuará como idioma por defecto, que no será sinónimo de obligatorio. La persona usuaria decidirá en qué idioma o idiomas introduce su contenido, teniendo la libertad además de introducir cada campo en un número diferente de idiomas. Los campos marcados como obligatorios en las diferentes pantallas de la aplicación deberán ser introducidos en, al menos, un idioma. Será de nuevo la persona usuaria quien decida en qué idioma introducirlo.  El orden de priorización de los idiomas será considerado para la representación del contenido de los campos multilingües sobre pantalla o en la generación de los informes, de forma que si el valor del campo no se encuentra disponible en el idioma seleccionado sobre la aplicación en ese momento o en el idioma en que se ha de generar un informe, se mostrará el contenido del campo en el primer idioma en el que esté disponible siguiendo el orden de priorización establecido en la configuración.   
Destacar que los formularios a través de los que se implementan las memorias del módulo de Ética (tecnología formly) tienen unas necesidades particulares, ya que el almacenamiento de las respuestas se realiza por bloques completos según la visualización de los mismos en pantalla. Para iniciar el proceso de evaluación de las memorias no se obligará a la cumplimentación de la misma en todos los idiomas, pero sí será necesario que esté cumplimentada por completo en uno de los idiomas.   
Cuando se accede al detalle de una entidad para modificar sus datos se mostrará el valor de sus campos tomando como idioma de referencia el seleccionado en la cabecera, pero dando prioridad a mostrar el valor del campo cuando éste no esté cumplimentado en el idioma seleccionado y sí en algún otro de los idiomas disponibles. Se mostrará el valor de los campos en el idioma seleccionado en la cabecera y si algún campo no estuviera cumplimentado en ese idioma, se mostrará el valor en cualquier otro idioma en el que sí estuviera cumplimentado, siguiente el orden de idiomas definido en la priorización. Es decir, al mostrar una entidad en modo edición podrán verse campos en diferentes idiomas, según estén o no cumplimentados en el idioma seleccionado en la cabecera. Se da prioridad a mostrar el valor de los campos en algún idioma, frente a mostrarlos vacíos cuando no están cumplimentados en el idioma seleccionado.

#### Comportamiento de los listados

Al mostrar los listados también se dará prioridad a mostrar el valor informado de los campos cuando éstos estén cumplimentados en algún idioma. Si los campos que se muestran en el listado están cumplimentados en el idioma seleccionado en la cabecera, se mostrarán en ese idioma. Cuando algún campo incluido en el listado no esté cumplimentado en el idioma seleccionado en la cabecera, pero sí lo esté en algún otro idioma, se mostrará su contenido en el idioma disponible, siguiendo el orden de prioridad establecido en la configuración. En estos casos se identificará el idioma en el que se está mostrando. Para ello, se utilizará le código ISO representativo del idioma.  
![](/attachments/1205862474/1205862477.png)

#### Comportamiento de los buscadores

Cuando se realicen búsquedas utilizando como filtro campos multi-idioma incluidos en los buscadores, se aplicarán sobre el valor del campo en cualquiera de los idiomas. Los elementos que cumplan el filtro establecido se mostrarán en el listado de resultados siguiendo el criterio indicado en el punto anterior, es decir:

* Los campos que tengan valor en el idioma de cabecera se mostrarán en este idioma (aunque no contengan el valor buscado en ese idioma)
* Los campos cuyo valor no hayan sido introducido en el idioma de cabecera se mostrarán en el idioma para el que contengan valor siguiendo el orden de prioridad establecido (aunque no contengan el valor buscado en ese idioma). Se identificará el idioma en el que se están mostrando.

En la imagen siguiente puede verse el caso en el que el término por el que se aplica la búsqueda no se corresponde con el valor del campo en el idioma seleccionado, pero sí coincidiría para otro idioma en el que fue introducido el valor del campo "nombre".  
![](/attachments/1205862474/1205862478.png)   
El término de búsqueda tiene coincidencias sobre el valor introducido en el idioma euskera  
![](/attachments/1205862474/1205862479.png)   
![](/attachments/1205862474/1205862480.png)

#### Cambios en modelo de datos

La construcción de la versión multilingüe supone el completo rediseño del modelo de datos del SGI. Por cada uno de los campos cuyo tipo dé lugar a poder estar disponible en diferentes idiomas, es decir, como norma general aquellos campos con formato tipo alfanumérico, será extraídos de su tabla original a una nueva tabla aislada. El campo en la tabla original se convertirá en una referencia a la nueva tabla.   
El esquema de las tablas que darán cobertura al multi-idioma de los campos alfanuméricos será: identificador del registro, idioma, valor que toma el campo en ese idioma. El idioma estará codificado de acuerdo a la norma ISO639.  
Ejemplo, tabla para almacenar el campo "título" de la tabla "memoria" del módulo de ética.  
![](/attachments/1205862474/1205862481.png)

En [Multiidioma a nivel de contenido - Identificación de campos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/version-multiidioma/planteamiento-general-internacionalizacion-del-sgi/multiidioma-a-nivel-de-contenido-identificacion-de-campos) se enumeran todos los campos que dispondrán de internacionalización.

#### Cambios en interface de la aplicación

Como se ha recogido anteriormente la persona usuaria decidirá en qué idioma y en cuántos introduce cada campo. Para ello dispondrá de una utilidad que le permitirá alternar el idioma. A efectos prácticos, se proporcionará un icono  que le permitirá indicar el idioma en que está introduciendo el contenido, que será independiente del idioma en el que esté visualizando la aplicación. Este icono estará disponible sobre cada uno del los campos que incluyan multi-idioma, de forma que la introducción del contenido en uno u otro idioma será independiente sobre cada campo. De acuerdo al idioma indicado, el contenido introducido para el campo será almacenado en la tabla correspondiente y asociado al idioma.   
![](/attachments/1205862474/1205862482.png)

#### Cambios en servicios del API del SGI

La implementación de los servicios del API del SGI también se verá afectada para dar cobertura al multilingüismo. Los servicios del API deben pasar a contemplar la posibilidad de que aquellos campos que representen nombres, descripciones, etc. puedan ser publicados/recibidos en los diferentes idiomas configurado en la implantación. Esto implica que tanto los objetos de entrada como los de salida se verán afectados, de modo que aquellos campos con soporte multilingüe pasen de contener un único valor a una lista de valores, siendo cada elemento de la lista una dupla de código de idioma y valor del campo en ese idioma.  
Este cambio tendrá impacto en las aplicaciones de terceros que consuman las API del SGI, pero no se mantendrá soporte a las API anteriores. En caso de ser necesario, en un momento dado, se deberá de realizar un análisis de impacto y esfuerzo de forma separada.  
El API de los servicios de integración, personas, empresas, económico y orgánico, no se ven afectados en cuanto a cambios en los objetos de entrada o salida, pero sí que sería necesario que en las integraciones se tenga en cuenta la cabecera "Accept-Language" para retornar valores en el idioma solicitado, si así lo requiere la implantación. Cualquier adaptación que sea necesario realizar en los servicios de integración de la Universidad, en caso de querer dar cobertura a la internacionalización, deberá ser realizada de manera ajena e independiente al SGI.

#### Gestión de documentos

El servicio de gestión documental facilitado en el SGI no experimentará cambios respecto a la internacionalización a nivel de front, de forma que los documentos aportados al sistema en diferentes idiomas se mantienen separados de forma física y lógica. La relación de los mismos será gestionada en los servicios propios del SGI de forma similar al soporte multilingüe de los campos, relacionando la referencia de un documento del sistema documental con un idioma asociado y una descripción.

#### Comunicados

El servicio de gestión de comunicados, envío de emails, se modificará para dar soporte a la recepción y registro de valores de  parámetro por idioma. De esta forma, en el caso de las plantillas genéricas o multilingües, la misma podrá contener textos en múltiples idiomas y asociarlos a los valores correspondientes en el idioma adecuado. En el caso de que el email fuese a ser enviado en un único idioma, la plantilla podrá optar por seleccionar los valores adecuados al idioma solicitado.  
Al contexto de las  plantillas se  incluirán funciones auxiliares para la determinación automática de la prioridad del idioma de modo que en  las plantillas existirá una función común a todo el sistema de comunicados, que permitirá obtener el valor de un campo en el idioma deseado y si este no estuviera rellenado retornaría el valor adecuado en función de la priorización de idiomas.

#### Traducciones de los textos

A partir de esta versión multilingüe el SGI quedará abierto a la inclusión de nuevos idiomas. Esto no obviará la necesidad de realizar las labores de configuración necesarias para incluir los ficheros de traducción necesarios para el front-end (etiquetas, mensajes, formularios de ética). Los textos a traducir deberán ser extraídos de la versión del SGI en curso.  Seguirá siendo necesario generar una nueva versión y realizar un nuevo despliegue cuando se introduzca la configuración de un nuevo idioma.

#### Particularidades módulo PRC. Algoritmo de baremación

La solución técnica propuesta abarcaría todos los módulos del SGI, sin embargo, se deben mencionar las particularidades del módulo de producción científica (PRC). La funcionalidad disponible en este módulo gira en torno a la baremación de la producción científica de los grupos de investigación. Los criterios de baremación disponibles en este módulo del SGI están basados en la estructura de CVN (norma FECYT). El SGI no cubre la gestión, propiamente dicha,  de los items de producción científica que son baremados (a excepción de proyectos, contratos, propiedad industrial e intelectual)  sino que provee de un API de integración para que los items a baremar puedan ser inyectados desde el sistema de gestión de CVN corporativo.  
El requisito elemental para dar cobertura a la internacionalización del módulo de PRC es que todos los servicios del API sean internacionalizables, lo que permitiría recibir los items a baremar en los diferentes idiomas en los que esté disponible cada CVN, siempre que estos hayan sido habilitados en la implantación particular del SGI. Además de esto, la internacionalización del módulo de PRC supondría adaptar el algoritmo de baremación para que tenga en cuenta los diferentes idiomas del CVN. Es decir, la aplicación de los baremos debería poder realizarse de acuerdo a la información que se recoge en cada versión por idioma del CVN. Las diferentes versiones de un mismo CVN en los diferentes idiomas no tiene por qué contener ni los mismos ítems ni estos contener la misma información, por lo que la baremación debiera de realizarse de forma independiente para cada idioma. Esto supone una reestructuración interna del algoritmo que debiera de ir acompañada de determinadas tomas de decisión funcionales, tales como, priorización de puntuación o posibilidad de selección del idioma prioritario por el personal investigador.  Si bien la instalación del módulo de PRC forma parte de los trabajos del pliego de implantación del SGI en la UPV/EHU no se contempla la integración del mismo con el sistema de gestión de CVN corporativo. Se realizarán los trabajos imprescindibles en el módulo de PRC para que éste quede operativo tras todos los cambios a realizar en el modelo de datos para dar cobertura al multilingüismo, pero no se cubrirá la adaptación del módulo para realizar la baremación en función del idioma o idiomas en que esté disponible cada CVN.