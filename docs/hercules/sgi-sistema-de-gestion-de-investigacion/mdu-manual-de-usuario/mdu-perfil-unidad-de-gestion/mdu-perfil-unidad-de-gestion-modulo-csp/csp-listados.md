# CSP-Listados

* [Introducción](#CSPListados-Introducción)
* [Listado de las facturas previstas pendientes de emitir](#CSPListados-Listadodelasfacturasprevistaspendientesdeemitir)
* [Listado de miembros de grupos de investigación](#CSPListados-Listadodemiembrosdegruposdeinvestigación)
* [Exportación de listados](#CSPListados-Exportacióndelistados)

### Introducción

Opción de menú del módulo de CSP para agrupar los informes o listados desarrollados a medida a partir de los datos almacenados en el módulo de CSP porque los listados generados a partir de los buscadores de las diferentes entidades del módulo CSP (convocatorias, solicitudes, proyectos y grupos de investigación) no cubre las necesidades buscadas en estos listados.

Los informes a medida incluidos en este bloque de Listados son:

* Facturas prevista pendientes de emitir
* Miembros de grupos de investigación

Sólo el personal de gestión tiene acceso a esta opción de menú.

### Listado de las facturas previstas pendientes de emitir

Listado de las facturas previstas pendientes de emitir por el SGE y cuya fecha prevista de emisión esté entre las fechas seleccionadas por el usuario en los campos de filtro del buscador.

Se  mostrará una formulario de búsqueda con los campos:

* Fecha desde: campo de tipo fecha. Dispone de un control calendario a través del que se podrá seleccionar la fecha deseada. La fecha introducida será la fecha prevista de emisión desde la que se quiere hacer la búsqueda.
* Fecha hasta: campo de tipo fecha. Dispone de un control calendario a través del que se podrá seleccionar la fecha deseada. La fecha introducida será la fecha prevista de emisión hasta la que se quiere hacer la búsqueda.

![](/attachments/1152811192/1160577066.png)

Una vez introducidos los filtros de búsqueda se debe pulsar el botón "Buscar". Los resultados coincidentes se mostrarán en el listado de resultados. Todos los filtros de búsqueda actuarán como una conjunción "y", es decir, las facturas previstas pendientes de emitir que se muestren en el listado de resultados deberán cumplir todos los filtros especificados.

Se puede utilizar el botón "Limpiar" para vaciar cualquier valor introducido en cualquiera de los campos y eliminar los resultados de la búsqueda.

Una vez que se pulse al botón "Buscar" se mostrará una tabla con las siguientes columnas:

![](/attachments/1152811192/1160577067.png)

* Identificador interno: Identificador interno del proyecto en el SGI.
* Código SGE: Identificador del proyecto económico en el SGE.
* Entidades financiadoras: Nombre de cada una de las entidades financiadoras del proyecto separadas por el carácter ",". Si la concatenación de los nombres supera el espacio reservado para la columna se mostrará cortada la cadena con el carácter "..." y el contenido completo pasará a mostrarse a través de un tooltip que se mostrará al pasar el ratón por el campo.
* Número previsión: Identificador de la factura pendiente de emitir dentro del proyecto SGI. Es un número secuencial dentro del proyecto.
* Fecha emisión: Es la fecha prevista de emisión de la factura.
* Importe base: Importe base de la factura.
* IVA: Porcentaje de IVA a aplicar en la factura.
* Importe total: Valor calculado a partir del importe base y el porcentaje de IVA.
* Comentario: Texto libre con el comentario que se considere que debe de ser tenido en cuenta por los gestores económicos.
* Tipo facturación: Indica el hito a cumplir o el trabajo que hay que realizar para que se pueda emitir la factura, por ejemplo realizar un informe, un trabajo , un análisis, etc... Desplegable con los valores introducidos en la configuración de los tipos de facturación.
* Fecha conformidad: Fecha en la que se ha validado la factura.
* Validación IP: Es el estado de validación en el que se encuentra la factura. Consultar [el ciclo de gestión de un ítem de facturación](/hercules/sgi-sistema-de-gestion-de-investigacion/mdu-manual-de-usuario/mdu-perfil-unidad-de-gestion/mdu-perfil-unidad-de-gestion-modulo-csp/csp-proyectos/csp-proyectos-configuracion-economica).

### Listado de miembros de grupos de investigación

Listado de participantes de grupos de investigación que cumplen con los criterios de la búsqueda.

Se  mostrará una formulario de búsqueda con los campos:

* Nombre grupo:  Si se introduce una cadena en este filtro, se mostrarán los miembros de los grupos de investigación que contengan la cadena introducida en cualquier parte del campo "nombre" del grupo de investigación.
* Código grupo. Si se introduce una cadena en este filtro, se mostrarán los miembros de los grupos de investigación que contengan la cadena introducida en cualquier parte del campo "código" del grupo de investigación.
* Miembro equipo: Este campo permite especificar una persona. Se realizará la búsqueda de los miembros de los grupos de investigación que contengan a la persona indicada como miembro del equipo de investigación. Para indicar la persona se utilizará el buscador común de personas [MDU-Manual de usuario - 8.1 Personas](/hercules/sgi-sistema-de-gestion-de-investigacion/mdu-manual-de-usuario#MDUManualdeusuario-8.1Personas)
* Código identificación SGE: Si se introduce una cadena en este filtro, se mostrarán los miembros de los grupos de investigación que contengan la cadena introducida en cualquier parte del campo "código identificación SGE" del grupo de investigación. Este campo sólo se mostrará si la variable de configuración de CSP "[Ejecución económica de Grupos de investigación](/hercules/sgi-sistema-de-gestion-de-investigacion/mdu-manual-de-usuario/mdu-perfil-de-administracion-del-sistema#MDUPerfildeAdministraci%C3%B3ndelsistema-1.2Configuraci%C3%B3nCSP)" tiene el valor "Sí".
* Listado de miembros: Es un desplegable con los valores "Todos", "Activos en SGI", y "No activos". Por defecto el filtro está precargado con el valor "Todos".
  + "Todos": se muestran todos los miembros de los grupos de investigación tanto si su participación en los grupos de investigación sea vigente o no
  + "Activos en SGI": se muestran los miembros de grupos de investigación cuya participación en los grupos esté vigente.
  + "No activos": se muestran los miembros de grupos de investigación cuya participación en los grupos no esté vigente.Fecha inicio grupo desde - hasta: Con los campos "desde" y "hasta", ambos del tipo fecha, se puede establecer un periodo que permitirá buscar los miembros de los grupos de investigación cuya fecha de inicio del grupo de investigación esté comprendida en el mismo. Ambos campos disponen de un control calendario a través del que se podrá seleccionar la fecha deseada.
* Línea investigación: Con este filtro se limita la búsqueda de los miembros de los grupos de investigación que trabajen en una determinada línea de investigación, es decir, que estén adscritos a dicha línea de investigación. La línea de investigación deberá seleccionarse a partir del desplegable disponible en este campo, que contendrá todas las líneas de investigación configuradas en el SGI. Para más información sobre la configuración de las líneas de investigación se puede consultar [CSP-Configuración - 13 Líneas de investigación](https://confluence.um.es/confluence/pages/viewpage.action?pageId=134296892#CSPConfiguraci%C3%B3n-13.L%C3%ADneasdeinvestigaci%C3%B3n).

![](/attachments/1152811192/1163919566.png)

Una vez introducidos los filtros de búsqueda se debe pulsar el botón "Buscar". Los resultados coincidentes se mostrarán en el listado de resultados. Todos los filtros de búsqueda actuarán como una conjunción "y", es decir, los participantes de grupos de investigación que se muestren en el listado de resultados deberán cumplir todos los filtros especificados. Se mostrará una persona por cada periodo de participación diferente en los diferentes grupos .

Se puede utilizar el botón "Limpiar" para vaciar cualquier valor introducido en cualquiera de los campos y eliminar los resultados de la búsqueda.

Una vez que se pulse al botón "Buscar" se mostrará una tabla con las siguientes columnas:

![](/attachments/1152811192/1163919567.png)

* Nombre:Nombre del miembro del grupo de investigación. Datos recuperados de los datos almacenados en la Universidad.
* Apellidos:Apellidos del miembro del grupo de investigación. Datos recuperados de los datos almacenados en la Universidad.
* E-mail: Correo electrónico del miembro del grupo de investigación. Dato recuperado de los datos almacenados en la Universidad.
* Rol: Rol con el que participará el miembro en el grupo.
* Activo en grupo: Indica si la participación del miembro del grupo de investigación esta vigente o no.
* Fecha inicio participación: Fecha de inicio del miembro en el grupo con el rol indicado en el campo "Rol".
* Fecha fin participación: Fecha de fin del miembro en el grupo con el rol indicado en el campo "Rol".
* Dedicación: Tiempo de dedicación del miembro en el grupo.
* % Participación: El porcentaje de dedicación del miembro en el grupo.
* Nombre grupo: Nombre del grupo de investigación.
* Código grupo: Código del grupo, formado por el código del departamento al que esta adscrito el investigador/a principal y un secuencial o bien el código que hay querido ponerle el personal de gestión.

### Exportación de listados

Cada uno de los listados mostrados en el menú de "Listados" pueden ser exportados a los formatos:

* XLSX
* CSV

Para ello se dispondrá de dos iconos situados debajo de la tabla de resultados de cada uno de los listados que permitirán generar el documento asociado bien en formato XLSX o CSV dependiendo del icono pulsado. Dicho documento podrá ser nombrado y descargado a la unidad de disco deseada.

A continuación se muestra una captura del listado de facturas previstas pendiente de emitir  donde se puede apreciar la situación de los dos iconos:

![](/attachments/1152811192/1160577069.png)