# ETI - Permisos - Actores

## Catálogo de Permisos

Listado con todos los permisos del módulo ETI y la descripción de sus abreviaturas así como los criterios seguidos en el diseño para el nombrado de dichos permisos.

---

Ver Catálogo de permisos

## Diseño de permisos

Se siguen los criterios generales descritos en [Permisos](/confluence/pages/createpage.action?spaceKey=HERCULES&title=Permisos&linkCreation=true&fromPageId=597852683).

---

Ver detalle de criterios de diseño de permisos

**Error al renderizar el macro 'excerpt-include'**

No link could be created for 'Permisos'.

---

## Abreviaturas

### Entidades

| Abreviatura | Nombre |
| --- | --- |
| ETI | Ética |
| CNV | Convocatoria |
| EVC | Evaluación |
| ACT | Acta |
| EVR | Evaluadores |
| PEV | Petición de evaluación |
| INV | Investigador |
| MEM | Memoria |
| CHK | Checklist |
| CNF | Configuración |
| PER | Persona |
| EMP | Empresa |

### Acciones particularizadas

| Abreviatura | Nombre |
| --- | --- |
| ENV | Enviar |
| EVAL | Evaluar |
| FIN | Finalizar |
| DES | Descargar |
| ESCR | Enviar a secretaría |
| ERTR | Enviar retrospectiva a secretaría. |
| CEST | Cambiar de estado. |

## Catálogo de permisos

| Nombre abreviado | Descripción |
| --- | --- |
| ETI-CNV-V | Visualización.  Acceso al listado y utilización de su filtro. |
| ETI-CNV-C | Creación.  Habilita el botón de creación. |
| ETI-CNV-E | Edición.  Habilita el botón de acceso al detalle en modo edición. |
| ETI-CNV-B | Borrado.  Habilita el botón de borrado (lógico). |
| ETI-CNV-ENV | Enviar convocatoria.  Habilita el botón de envío de la convocatoria. |
| ETI-EVC-V | Visualización.  Acceso al listado y utilización de su filtro. |
| ETI-EVC-EVAL | Evaluar.  Habilita el botón de acceso a la evaluación. |
| ETI-ACT-V | Visualización.  Acceso al listado y utilización de su filtro.  Habilita el botón de acceso al detalle en modo consulta. |
| ETI-ACT-C | Creación.  Habilita el botón de creación. |
| ETI-ACT-E | Edición.  Habilita el botón de acceso al detalle en modo edición. |
| ETI-ACT-FIN | Finalizar.  Habilita el botón de finalizar el acta. |
| ETI-ACT-DES | Descargar.  Habilita el acceso a ver el informe del acta (la descarga del documento). |
| ETI-EVR-V | Visualización.  Acceso al listado y utilización de su filtro. |
| ETI-EVR-C | Creación.  Habilita el botón de creación. |
| ETI-EVR-E | Edición.  Habilita el botón de acceso al detalle en modo edición. |
| ETI-EVR-B | Borrado.  Habilita el botón de borrado (lógico). |
| ETI-EVC-INV-VR | Visualización restringida (investigador).  Acceso al listado y utilización de su filtro. |
| ETI-EVC-INV-EVALR | Evaluar restringido (investigador).  Acceso a evaluar la memoria (añadir comentarios). |
| ETI-EVC-VR | Visualización restringida (técnico).  Acceso al listado y utilización de su filtro. |
| ETI-EVC-EVALR | Evaluar restringido (técnico). |
| ETI-EVC-V | Visualización.  Acceso al listado y utilización de su filtro. |
| ETI-EVC-EVAL | Evaluar.  Habilita el botón de acceso a la evaluación. |
| ETI-PEV-INV-VR | Visualización restringida  Acceso al listado y utilización de su filtro. |
| ETI-PEV-INV-C | Creación  Habilita el botón de creación. |
| ETI-PEV-INV-ER | Edición restringida.  Habilita el botón de acceso al detalle en modo edición. |
| ETI-PEV-INV-BR | Borrado restringido.  Habilita el botón de borrado (lógico). |
| ETI-PEV-V | Visualización.  Acceso al listado y utilización de su filtro.  Habilita el botón de acceso al detalle en modo consulta. |
| ETI-MEM-INV-CR | Creación restringida. |
| ETI-MEM-INV-ER | Edición restringida.  Habilita el botón de acceso al detalle en modo edición.  Tanto el creador como el responsable de memoria puede modificar la memoria.  Siempre se podrá editar, luego serán los propias pantallas las que dependiendo del estado de la memoria se puede o no hacer algo en la pantalla. |
| ETI-MEM-INV-BR | Borrado restringido.  Solo para el creador de la petición de evaluación. El responsable de memoria no puede eliminar memorias. |
| ETI-MEM-INV-VR | Visualización restringida  Acceso al listado y utilización de su filtro. |
| ETI-MEM-INV-ESCR | Enviar a secretaría.  Solo para el creador de la petición de evaluación. El responsable de memoria no puede enviar a secretaría. |
| ETI-MEM-INV-ERTR | Enviar retrospectiva a secretaría.  Solo para el creador de la petición de evaluación. El responsable de memoria no puede enviar retrospectiva a secretaría. |
| ETI-MEM-V | Visualización.  Habilita el botón de acceso al detalle en modo consulta.  Permite ver los informes.  Todos los campos estarán en modo consulta y los botones de acción deshabilitados. |
| ETI-MEM-CEST | Cambio de estado.  Permite volver a un estado anterior dependiendo que que estado se encuentre. |
| ETI-MEM-EDOC | Edición documentación.  Habilita el botón de acceso al detalle en modo edición de la pantalla de Documentación de la memoria. |
| ETI-CHK-INV-E | Completar checklist de autoevaluación por un investigador. |
| ETI-CNF-E | Edición de configuración. |
| ETI-ACT-INV-ER | Edición restringida (evaluador - investigador)  Habilita el botón de acceso al detalle en modo edición. |
| ETI-ACT-INV-DESR | Descarga restringida (evaluador - investigador)  Habilita el acceso a ver el informe del acta (la descarga del documento). |
| ETI-ACT-ER | Edición restringida (evaluador - técnico)  Habilita el botón de acceso al detalle en modo edición. |
| ETI-ACT-DESR | Descarga restringida (evaluador - técnico)  Habilita el acceso a ver el informe del acta (la descarga del documento). |
| ESB-PER-V | Visualización del detalle.  Habilita el botón de acceso al detalle en modo consulta.  El acceso al listado y utilización de su filtro estará determinado por los permisos de acceso a la pantalla que abre la ventana emergente del buscador, esto es, el buscador y listado en sí no se restringirá por ningún permiso específico. |
| ESB-PER-E | Solicitud de modificación.  Habilita el botón de acceso al detalle en modo solicitud de edición. |
| ESB-PER-C | Solicitud de creación.  Habilita el botón de solicitud de creación. |
| ESB-EMP-V | Visualización del detalle.  Habilita el botón de acceso al detalle en modo consulta.  El acceso al listado y utilización de su filtro estará determinado por los permisos de acceso a la pantalla que abre la ventana emergente del buscador, esto es, el buscador y listado en sí no se restringirá por ningún permiso específico. |
| ESB-EMP-E | Solicitud de modificación.  Habilita el botón de acceso al detalle en modo solicitud de edición. |
| ESB-EMP-C | Solicitud de creación.  Habilita el botón de solicitud de creación. |
| CSP-SOL-ETI-V | Visualización datos solicitud desde Ética  Permite acceso a la consulta del código interno de las solicitudes desde el módulo de ética |

---

## Permisos de Acciones y/o Accesos por Actor

| Actor | Permisos |
| --- | --- |
| [ACT-ETI-006-Responsable memoria](/confluence/spaces/HERCULES/pages/597852692/ACT-ETI-006-Responsable+memoria) | ETI-PEV-INV-VR, ETI-PEV-INV-ER  ETI-MEM-INV-ER  ESB-PER-V  CSP-SOL-ETI-V |
| [ACT-ETI-003-Solicitante](/confluence/spaces/HERCULES/pages/597852688/ACT-ETI-003-Solicitante) | ETI-PEV-INV-VR, ETI-PEV-INV-C, ETI-PEV-INV-ER, ETI-PEV-INV-BR  ETI-MEM-INV-CR, ETI-MEM-INV-ER, ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR, ETI-MEM-INV-BR  ETI-CHK-INV-E  ESB-PER-V  ETI-ACT-INV-ER, ETI-ACT-INV-DESR  CSP-SOL-ETI-V |
| [ACT-ETI-002-Investigador](/confluence/spaces/HERCULES/pages/597852685/ACT-ETI-002-Investigador) | ETI-PEV-INV-VR, ETI-PEV-INV-C, ETI-PEV-INV-ER, ETI-PEV-INV-BR  ETI-MEM-INV-CR, ETI-MEM-INV-ER,  ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR, ETI-MEM-INV-BR  ETI-CHK-INV-E  ESB-PER-V  ETI-EVC-INV-VR, ETI-EVC-INV-EVALR  ETI-ACT-INV-ER, ETI-ACT-INV-DESR  CSP-SOL-ETI-V |
| [ACT-ETI-001-Gestor](/confluence/spaces/HERCULES/pages/597852686/ACT-ETI-001-Gestor) | ETI-CNV-C, ETI-CNV-E, ETI-CNV-B, ETI-CNV-ENV  ETI-EVC-EVAL  ETI-ACT-C, ETI-ACT-E, ETI-ACT-DES, ETI-ACT-FIN  ETI-EVR-C, ETI-EVR-E, ETI-EVR-B  ETI-PEV-V  ETI-MEM-V, ETI-MEM-CEST, ETI-MEM-EDOC  ESB-PER-E, ESB-PER-C  CSP-SOL-ETI-V |
| [ACT-ETI-005-Técnico](/confluence/spaces/HERCULES/pages/597852690/ACT-ETI-005-T%C3%A9cnico) | ETI-EVC-VR, ETI-EVC-EVALR  ETI-ACT-ER,ETI-ACT-DESR |
| [ACT-ETI-004-Evaluador](/confluence/spaces/HERCULES/pages/597852689/ACT-ETI-004-Evaluador) | ETI-EVC-INV-VR, ETI-EVC-INV-EVALR  ETI-ACT-INV-ER, ETI-ACT-INV-DESR |
| [ACT-ETI-007-Administrador](/confluence/spaces/HERCULES/pages/597852693/ACT-ETI-007-Administrador) | ETI-CNF-E |

## Permisos de Acceso a Pantallas (IU)

| Título | Permisos |
| --- | --- |
| [IU-ETI-0020-001 Búsqueda y listado de evaluaciones](/confluence/spaces/HERCULES/pages/597853582/IU-ETI-0020-001+B%C3%BAsqueda+y+listado+de+evaluaciones) | ETI-EVC-V, ETI-EVC-EVAL |
| [IU-ETI-0060-005 Modificación petición de evaluación](/confluence/spaces/HERCULES/pages/597852350/IU-ETI-0060-005+Modificaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n) | ETI-PEV-INV-ER, ETI-MEM-INV-CR, ETI-MEM-INV-ER,  ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR, ETI-MEM-INV-BR |
| [IU-ETI-0060-004 - Creación petición de evaluación - Equipo investigador](/confluence/spaces/HERCULES/pages/734462031/IU-ETI-0060-004+-+Creaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n+-+Equipo+investigador) | ETI-PEV-INV-C |
| [IU-ETI-0060-003 - Creación petición de evaluación - Datos generales](/confluence/spaces/HERCULES/pages/597852343/IU-ETI-0060-003+-+Creaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n+-+Datos+generales) | ETI-PEV-INV-C |
| [IU-ETI-0050-008 Evaluar memoria seguimiento- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853385/IU-ETI-0050-008+Evaluar+memoria+seguimiento-+Comentarios+-+A%C3%B1adir) | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |
| [IU-ETI-0050-004 Evaluar memoria- Comentarios - Modificar](/confluence/spaces/HERCULES/pages/597853820/IU-ETI-0050-004+Evaluar+memoria-+Comentarios+-+Modificar) | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |
| [IU-ETI-0050-003 Evaluar memoria- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853824/IU-ETI-0050-003+Evaluar+memoria-+Comentarios+-+A%C3%B1adir) | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |
| [IU-ETI-0100-003 Evaluar memoria seguimiento- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853354/IU-ETI-0100-003+Evaluar+memoria+seguimiento-+Comentarios+-+A%C3%B1adir) | ETI-EVC-EVAL |
| [IU-ETI-0020-004 Evaluar memoria- Comentarios - Modificar](/confluence/spaces/HERCULES/pages/597853587/IU-ETI-0020-004+Evaluar+memoria-+Comentarios+-+Modificar) | ETI-EVC-EVAL |
| [IU-ETI-0020-003 Evaluar memoria- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853591/IU-ETI-0020-003+Evaluar+memoria-+Comentarios+-+A%C3%B1adir) | ETI-EVC-EVAL |
| [IU-ETI-0050-002 Evaluar memoria](/confluence/spaces/HERCULES/pages/597853823/IU-ETI-0050-002+Evaluar+memoria) | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |
| [IU-ETI-0020-002 Evaluar memoria](/confluence/spaces/HERCULES/pages/597853590/IU-ETI-0020-002+Evaluar+memoria) | ETI-EVC-EVAL |
| [IU-ETI-0090-001 Búsqueda y listado de peticiones de evaluación](/confluence/spaces/HERCULES/pages/597852506/IU-ETI-0090-001+B%C3%BAsqueda+y+listado+de+peticiones+de+evaluaci%C3%B3n) | ETI-PEV-V |
| [IU-ETI-0060-014 Memorias - Edición evaluaciones](/confluence/spaces/HERCULES/pages/597852323/IU-ETI-0060-014+Memorias+-+Edici%C3%B3n+evaluaciones) | ETI-MEM-INV-ER |
| [IU-ETI-0060-010 Memorias - Edición formulario](/confluence/spaces/HERCULES/pages/597852317/IU-ETI-0060-010+Memorias+-+Edici%C3%B3n+formulario) | ETI-*MEM-INV*-ER |
| [IU-ETI-0060-009 Memorias - Edición datos generales](/confluence/spaces/HERCULES/pages/597852313/IU-ETI-0060-009+Memorias+-+Edici%C3%B3n+datos+generales) | ETI-MEM-INV-ER |
| [IU-ETI-0060-002 Búsqueda y listado de mis peticiones de evaluación - Responsable](/confluence/spaces/HERCULES/pages/597852341/IU-ETI-0060-002+B%C3%BAsqueda+y+listado+de+mis+peticiones+de+evaluaci%C3%B3n+-+Responsable) | ETI-PEV-INV-VR, ETI-PEV-INV-ER |
| [IU-ETI-0060-001 Búsqueda y listado de mis peticiones de evaluación - Creador](/confluence/spaces/HERCULES/pages/597852342/IU-ETI-0060-001+B%C3%BAsqueda+y+listado+de+mis+peticiones+de+evaluaci%C3%B3n+-+Creador) | ETI-PEV-INV-C, ETI-PEV-INV-ER, ETI-PEV-INV-BR |
| [IU-ETI-0050-001 Búsqueda y listado de evaluaciones](/confluence/spaces/HERCULES/pages/597853825/IU-ETI-0050-001+B%C3%BAsqueda+y+listado+de+evaluaciones) | ETI-EVC-INV-VR, ETI-EVC-INV-EVALR, ETI-EVC-VR, ETI-EVC-EVALR |
| [IU-ETI-0030-001 Búsqueda y listado de actas](/confluence/spaces/HERCULES/pages/597853793/IU-ETI-0030-001+B%C3%BAsqueda+y+listado+de+actas) | ETI-ACT-V, ETI-ACT-C, ETI-ACT-E, ETI-ACT-DES, ETI-ACT-FIN, ETI-ACT-INV-ER, ETI-ACT-ER,ETI-ACT-INV-DESR,ETI-ACT-DESR |
| [IU-ETI-0010-001 Búsqueda y listado de convocatorias reunión](/confluence/spaces/HERCULES/pages/597853546/IU-ETI-0010-001+B%C3%BAsqueda+y+listado+de+convocatorias+reuni%C3%B3n) | ETI-CNV-V, ETI-CNV-C, ETI-CNV-E, ETI-CNV-B, ETI-CNV-ENV |
| [IU-ETI-0050-006 Búsqueda y listado de seguimientos](/confluence/spaces/HERCULES/pages/597853377/IU-ETI-0050-006+B%C3%BAsqueda+y+listado+de+seguimientos) | ETI-EVC-INV-VR, ETI-EVC-INV-EVALR, ETI-EVC-VR, ETI-EVC-EVALR |
| [IU-ETI-0100-001 Búsqueda y listado de evaluaciones de seguimiento](/confluence/spaces/HERCULES/pages/597853457/IU-ETI-0100-001+B%C3%BAsqueda+y+listado+de+evaluaciones+de+seguimiento) | ETI-EVC-V, ETI-EVC-EVAL |
| [IU-ETI-0040-003 Modificar evaluador](/confluence/spaces/HERCULES/pages/597853813/IU-ETI-0040-003+Modificar+evaluador) | ETI-ACT-V, ETI-ACT-E |
| [IU-ETI-0040-002 Alta evaluador](/confluence/spaces/HERCULES/pages/597853802/IU-ETI-0040-002+Alta+evaluador) | ETI-ACT-C |
| [IU-ETI-0040-001 Búsqueda y listado de evaluadores](/confluence/spaces/HERCULES/pages/597853801/IU-ETI-0040-001+B%C3%BAsqueda+y+listado+de+evaluadores) | ETI-EVR-V, ETI-EVR-C, ETI-EVR-E, ETI-EVR-B |
| [IU-ETI-0010-003 Modificar convocatoria reunión](/confluence/spaces/HERCULES/pages/597853552/IU-ETI-0010-003+Modificar+convocatoria+reuni%C3%B3n) | ETI-CNV-E |
| [IU-ETI-0050-007 Evaluar memoria seguimiento](/confluence/spaces/HERCULES/pages/597853383/IU-ETI-0050-007+Evaluar+memoria+seguimiento) | ETI-EVC-INV-EVALR, ETI-EVC-EVALR |
| [IU-ETI-0130 Conflicto de interés](/confluence/spaces/HERCULES/pages/597852417/IU-ETI-0130+Conflicto+de+inter%C3%A9s) | ETI-COI-INV-ER, ETI-COI-ER |
| [IU-ETI-0110-001 Búsqueda y listado de memorias](/confluence/spaces/HERCULES/pages/597852404/IU-ETI-0110-001+B%C3%BAsqueda+y+listado+de+memorias) | ETI-MEM-INV-VR, ETI-MEM-INV-ER, ETI-MEM-INV-BR, ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR |
| [IU-ETI-0120-001 Búsqueda y listado de memorias](/confluence/spaces/HERCULES/pages/597852373/IU-ETI-0120-001+B%C3%BAsqueda+y+listado+de+memorias) | ETI-MEM-V, ETI-MEM-CEST |
| [IU-ETI-0090-002 Consulta petición de evaluación](/confluence/spaces/HERCULES/pages/597852556/IU-ETI-0090-002+Consulta+petici%C3%B3n+de+evaluaci%C3%B3n) | ETI-MEM-V, ETI-MEM-CEST |
| [IU-ETI-0080- Configuración](/confluence/spaces/HERCULES/pages/597852515/IU-ETI-0080-+Configuraci%C3%B3n) | ETI-CNF-E |
| [IU-ETI-0100-002 Evaluar memoria seguimiento](/confluence/spaces/HERCULES/pages/597853352/IU-ETI-0100-002+Evaluar+memoria+seguimiento) | ETI-EVC-EVAL |
| [IU-ETI-0070- Formulario Checklist](/confluence/spaces/HERCULES/pages/597852380/IU-ETI-0070-+Formulario+Checklist) | ETI-CHK-INV-E |
| [IU-ETI-0030-003 Modificar acta](/confluence/spaces/HERCULES/pages/597853799/IU-ETI-0030-003+Modificar+acta) | ETI-ACT-V, ETI-ACT-E, ETI-ACT-DES,ETI-ACT-INV-ER, ETI-ACT-ER,ETI-ACT-INV-DESR,ETI-ACT-DESR |
| [IU-ETI-0120-002 Consulta memoria](/confluence/spaces/HERCULES/pages/597852465/IU-ETI-0120-002+Consulta+memoria) | ETI-MEM-V,ETI-MEM-EDOC |
| [IU-ETI-0090-003 Consulta memoria - Adjuntar Documentación](/confluence/spaces/HERCULES/pages/597852478/IU-ETI-0090-003+Consulta+memoria+-+Adjuntar+Documentaci%C3%B3n) | ETI-MEM-EDOC |
| [IU-ETI-0090-004 Consultar Memoria - Edición documentación - Aportar documento](/confluence/spaces/HERCULES/pages/597852484/IU-ETI-0090-004+Consultar+Memoria+-+Edici%C3%B3n+documentaci%C3%B3n+-+Aportar+documento) | ETI-MEM-EDOC |
| [IU-ETI-0060-012 Memorias - Edición documentación - Aportar documento](/confluence/spaces/HERCULES/pages/597852423/IU-ETI-0060-012+Memorias+-+Edici%C3%B3n+documentaci%C3%B3n+-+Aportar+documento) | ETI-MEM-INV-ER |
| [IU-ETI-0060-011 Memorias - Edición documentación](/confluence/spaces/HERCULES/pages/597852320/IU-ETI-0060-011+Memorias+-+Edici%C3%B3n+documentaci%C3%B3n) | ETI-MEM-INV-ER |
| [IU-ETI-0010-002 Alta convocatoria reunión](/confluence/spaces/HERCULES/pages/597853545/IU-ETI-0010-002+Alta+convocatoria+reuni%C3%B3n) | ETI-CNV-C |
| [IU-ETI-0030-005 Modificar acta - Comentarios - Añadir/modificar](/confluence/spaces/HERCULES/pages/597852518/IU-ETI-0030-005+Modificar+acta+-+Comentarios+-+A%C3%B1adir+modificar) | ETI-ACT-E,ETI-ACT-INV-ER,ETI-ACT-ER |
| [IU-ETI-0060-019 Memorias - Edición retrospectiva](/confluence/spaces/HERCULES/pages/597853436/IU-ETI-0060-019+Memorias+-+Edici%C3%B3n+retrospectiva) | ETI-MEM-INV-ER |
| [IU-ETI-0040-004 Conflicto de intereses - Añadir](/confluence/spaces/HERCULES/pages/597852415/IU-ETI-0040-004+Conflicto+de+intereses+-+A%C3%B1adir) | ETI-ACT-C, ETI-ACT-E |
| [IU-ETI-0060-006 Equipo investigador - Alta](/confluence/spaces/HERCULES/pages/597852301/IU-ETI-0060-006+Equipo+investigador+-+Alta) | ETI-PEV-INV-C, ETI-PEV-INV-ER |
| [IU-ETI-0060-007 Asignación de tareas - Alta-modificación](/confluence/spaces/HERCULES/pages/597852307/IU-ETI-0060-007+Asignaci%C3%B3n+de+tareas+-+Alta-modificaci%C3%B3n) | ETI-PEV-INV-ER |
| [IU-ETI-0060-020 Memorias - Edición retrospectiva - Aportar documento](/confluence/spaces/HERCULES/pages/597853427/IU-ETI-0060-020+Memorias+-+Edici%C3%B3n+retrospectiva+-+Aportar+documento) | ETI-MEM-INV-ER |
| [IU-ETI-0060-018 Memorias - Edición seguimiento final - Aportar documento](/confluence/spaces/HERCULES/pages/597853392/IU-ETI-0060-018+Memorias+-+Edici%C3%B3n+seguimiento+final+-+Aportar+documento) | ETI-MEM-INV-ER |
| [IU-ETI-0060-017 Memorias - Edición seguimiento final](/confluence/spaces/HERCULES/pages/597853401/IU-ETI-0060-017+Memorias+-+Edici%C3%B3n+seguimiento+final) | ETI-MEM-INV-ER |
| [IU-ETI-0060-016 Memorias - Edición seguimiento anual - Aportar documento](/confluence/spaces/HERCULES/pages/597853313/IU-ETI-0060-016+Memorias+-+Edici%C3%B3n+seguimiento+anual+-+Aportar+documento) | ETI-MEM-INV-ER |
| [IU-ETI-0060-015 Memorias - Edición seguimiento anual](/confluence/spaces/HERCULES/pages/597853306/IU-ETI-0060-015+Memorias+-+Edici%C3%B3n+seguimiento+anual) | ETI-MEM-INV-ER |
| [IU-ETI-0060-013 Memorias - Edición informes](/confluence/spaces/HERCULES/pages/597852322/IU-ETI-0060-013+Memorias+-+Edici%C3%B3n+informes) | ETI-MEM-INV-ER |
| [IU-ETI-0060-008 Memorias - Alta datos generales](/confluence/spaces/HERCULES/pages/597852311/IU-ETI-0060-008+Memorias+-+Alta+datos+generales) | ETI-MEM-INV-CR |
| [IU-ETI-0030-004 Editar asistencia](/confluence/spaces/HERCULES/pages/597853800/IU-ETI-0030-004+Editar+asistencia) | ETI-ACT-C, ETI-ACT-E |
| [IU-ETI-0030-002 Alta acta](/confluence/spaces/HERCULES/pages/597853794/IU-ETI-0030-002+Alta+acta) | ETI-ACT-C |
| [IU-ETI-0010-006 Asignación memorias - Modificar](/confluence/spaces/HERCULES/pages/597853607/IU-ETI-0010-006+Asignaci%C3%B3n+memorias+-+Modificar) | ETI-CNV-C, ETI-CNV-E |
| [IU-ETI-0010-005 Asignación memorias - Añadir](/confluence/spaces/HERCULES/pages/597853609/IU-ETI-0010-005+Asignaci%C3%B3n+memorias+-+A%C3%B1adir) | ETI-CNV-C, ETI-CNV-E |

## Agrupación Pantallas (IU) - Actores - Permisos de acciones

| Título | ACT-ETI-001-Gestor | ACT-ETI-002-Investigador | ACT-ETI-003-Solicitante | ACT-ETI-004-Evaluador | ACT-ETI-005-Técnico | ACT-ETI-006-Responsable memoria | ACT-ETI-007-Administrador |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [IU-ETI-0020-001 Búsqueda y listado de evaluaciones](/confluence/spaces/HERCULES/pages/597853582/IU-ETI-0020-001+B%C3%BAsqueda+y+listado+de+evaluaciones) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0060-005 Modificación petición de evaluación](/confluence/spaces/HERCULES/pages/597852350/IU-ETI-0060-005+Modificaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n) |  | ETI-PEV-INV-ER, ETI-MEM-INV-CR, ETI-MEM-INV-ER,  ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR, ETI-MEM-INV-BR, CSP-SOL-ETI-V | ETI-PEV-INV-ER, ETI-MEM-INV-CR, ETI-MEM-INV-ER, ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR, ETI-MEM-INV-BR, CCSP-SOL-ETI-V |  |  | ETI-PEV-INV-ER, ETI-MEM-INV-ER, CSP-SOL-ETI-V |  |
| [IU-ETI-0060-004 - Creación petición de evaluación - Equipo investigador](/confluence/spaces/HERCULES/pages/734462031/IU-ETI-0060-004+-+Creaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n+-+Equipo+investigador) |  | ETI-PEV-INV-C | ETI-PEV-INV-C |  |  |  |  |
| [IU-ETI-0060-003 - Creación petición de evaluación - Datos generales](/confluence/spaces/HERCULES/pages/597852343/IU-ETI-0060-003+-+Creaci%C3%B3n+petici%C3%B3n+de+evaluaci%C3%B3n+-+Datos+generales) |  | ETI-PEV-INV-C | ETI-PEV-INV-C |  |  |  |  |
| [IU-ETI-0050-008 Evaluar memoria seguimiento- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853385/IU-ETI-0050-008+Evaluar+memoria+seguimiento-+Comentarios+-+A%C3%B1adir) |  |  |  | ETI-EVC-INV-EVALR | ETI-EVC-EVALR |  |  |
| [IU-ETI-0050-004 Evaluar memoria- Comentarios - Modificar](/confluence/spaces/HERCULES/pages/597853820/IU-ETI-0050-004+Evaluar+memoria-+Comentarios+-+Modificar) |  |  |  | ETI-EVC-INV-EVALR | ETI-EVC-EVALR |  |  |
| [IU-ETI-0050-003 Evaluar memoria- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853824/IU-ETI-0050-003+Evaluar+memoria-+Comentarios+-+A%C3%B1adir) |  |  |  | ETI-EVC-INV-EVALR | ETI-EVC-EVALR |  |  |
| [IU-ETI-0100-003 Evaluar memoria seguimiento- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853354/IU-ETI-0100-003+Evaluar+memoria+seguimiento-+Comentarios+-+A%C3%B1adir) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0020-004 Evaluar memoria- Comentarios - Modificar](/confluence/spaces/HERCULES/pages/597853587/IU-ETI-0020-004+Evaluar+memoria-+Comentarios+-+Modificar) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0020-003 Evaluar memoria- Comentarios - Añadir](/confluence/spaces/HERCULES/pages/597853591/IU-ETI-0020-003+Evaluar+memoria-+Comentarios+-+A%C3%B1adir) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0050-002 Evaluar memoria](/confluence/spaces/HERCULES/pages/597853823/IU-ETI-0050-002+Evaluar+memoria) |  |  |  | ETI-EVC-INV-EVALR | ETI-EVC-EVALR |  |  |
| [IU-ETI-0020-002 Evaluar memoria](/confluence/spaces/HERCULES/pages/597853590/IU-ETI-0020-002+Evaluar+memoria) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0090-001 Búsqueda y listado de peticiones de evaluación](/confluence/spaces/HERCULES/pages/597852506/IU-ETI-0090-001+B%C3%BAsqueda+y+listado+de+peticiones+de+evaluaci%C3%B3n) | ETI-PEV-V |  |  |  |  |  |  |
| [IU-ETI-0060-014 Memorias - Edición evaluaciones](/confluence/spaces/HERCULES/pages/597852323/IU-ETI-0060-014+Memorias+-+Edici%C3%B3n+evaluaciones) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-010 Memorias - Edición formulario](/confluence/spaces/HERCULES/pages/597852317/IU-ETI-0060-010+Memorias+-+Edici%C3%B3n+formulario) |  | ETI-*MEM-INV*-ER | ETI-*MEM-INV*-ER |  |  | ETI-*MEM-INV*-ER |  |
| [IU-ETI-0060-009 Memorias - Edición datos generales](/confluence/spaces/HERCULES/pages/597852313/IU-ETI-0060-009+Memorias+-+Edici%C3%B3n+datos+generales) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-002 Búsqueda y listado de mis peticiones de evaluación - Responsable](/confluence/spaces/HERCULES/pages/597852341/IU-ETI-0060-002+B%C3%BAsqueda+y+listado+de+mis+peticiones+de+evaluaci%C3%B3n+-+Responsable) |  |  |  |  |  | ETI-PEV-INV-VR, ETI-PEV-INV-ER |  |
| [IU-ETI-0060-001 Búsqueda y listado de mis peticiones de evaluación - Creador](/confluence/spaces/HERCULES/pages/597852342/IU-ETI-0060-001+B%C3%BAsqueda+y+listado+de+mis+peticiones+de+evaluaci%C3%B3n+-+Creador) |  | ETI-PEV-INV-C, ETI-PEV-INV-ER, ETI-PEV-INV-BR | ETI-PEV-INV-C, ETI-PEV-INV-ER, ETI-PEV-INV-BR |  |  |  |  |
| [IU-ETI-0050-001 Búsqueda y listado de evaluaciones](/confluence/spaces/HERCULES/pages/597853825/IU-ETI-0050-001+B%C3%BAsqueda+y+listado+de+evaluaciones) |  |  |  | ETI-EVC-INV-VR, ETI-EVC-INV-EVALR | ETI-EVC-VR, ETI-EVC-EVALR |  |  |
| [IU-ETI-0030-001 Búsqueda y listado de actas](/confluence/spaces/HERCULES/pages/597853793/IU-ETI-0030-001+B%C3%BAsqueda+y+listado+de+actas) | ETI-ACT-C, ETI-ACT-E, ETI-ACT-DES, ETI-ACT-FIN |  |  | ETI-ACT-INV-ER,ETI-ACT-INV-DESR | ETI-ACT-ER,ETI-ACT-DESR |  |  |
| [IU-ETI-0010-001 Búsqueda y listado de convocatorias reunión](/confluence/spaces/HERCULES/pages/597853546/IU-ETI-0010-001+B%C3%BAsqueda+y+listado+de+convocatorias+reuni%C3%B3n) | ETI-CNV-C, ETI-CNV-E, ETI-CNV-B, ETI-CNV-ENV |  |  |  |  |  |  |
| [IU-ETI-0050-006 Búsqueda y listado de seguimientos](/confluence/spaces/HERCULES/pages/597853377/IU-ETI-0050-006+B%C3%BAsqueda+y+listado+de+seguimientos) |  |  |  | ETI-EVC-INV-VR, ETI-EVC-INV-EVALR | ETI-EVC-VR, ETI-EVC-EVALR |  |  |
| [IU-ETI-0100-001 Búsqueda y listado de evaluaciones de seguimiento](/confluence/spaces/HERCULES/pages/597853457/IU-ETI-0100-001+B%C3%BAsqueda+y+listado+de+evaluaciones+de+seguimiento) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0040-003 Modificar evaluador](/confluence/spaces/HERCULES/pages/597853813/IU-ETI-0040-003+Modificar+evaluador) | ETI-ACT-E |  |  |  |  |  |  |
| [IU-ETI-0040-002 Alta evaluador](/confluence/spaces/HERCULES/pages/597853802/IU-ETI-0040-002+Alta+evaluador) | ETI-ACT-C |  |  |  |  |  |  |
| [IU-ETI-0040-001 Búsqueda y listado de evaluadores](/confluence/spaces/HERCULES/pages/597853801/IU-ETI-0040-001+B%C3%BAsqueda+y+listado+de+evaluadores) | ETI-EVR-C, ETI-EVR-E, ETI-EVR-B |  |  |  |  |  |  |
| [IU-ETI-0010-003 Modificar convocatoria reunión](/confluence/spaces/HERCULES/pages/597853552/IU-ETI-0010-003+Modificar+convocatoria+reuni%C3%B3n) | ETI-CNV-E |  |  |  |  |  |  |
| [IU-ETI-0050-007 Evaluar memoria seguimiento](/confluence/spaces/HERCULES/pages/597853383/IU-ETI-0050-007+Evaluar+memoria+seguimiento) |  |  |  | ETI-EVC-INV-EVALR | ETI-EVC-EVALR |  |  |
| [IU-ETI-0130 Conflicto de interés](/confluence/spaces/HERCULES/pages/597852417/IU-ETI-0130+Conflicto+de+inter%C3%A9s) | ETI-COI-ER |  |  | ETI-COI-INV-ER | ETI-COI-ER |  |  |
| [IU-ETI-0110-001 Búsqueda y listado de memorias](/confluence/spaces/HERCULES/pages/597852404/IU-ETI-0110-001+B%C3%BAsqueda+y+listado+de+memorias) |  | ETI-MEM-INV-ER, ETI-MEM-INV-BR, ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR | ETI-MEM-INV-ER, ETI-MEM-INV-BR, ETI-MEM-INV-ESCR, ETI-MEM-INV-ERTR |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0120-001 Búsqueda y listado de memorias](/confluence/spaces/HERCULES/pages/597852373/IU-ETI-0120-001+B%C3%BAsqueda+y+listado+de+memorias) | ETI-MEM-V, ETI-MEM-CEST |  |  |  |  |  |  |
| [IU-ETI-0090-002 Consulta petición de evaluación](/confluence/spaces/HERCULES/pages/597852556/IU-ETI-0090-002+Consulta+petici%C3%B3n+de+evaluaci%C3%B3n) | ETI-MEM-V, ETI-MEM-CEST, CSP-SOL-ETI-V |  |  |  |  |  |  |
| [IU-ETI-0080- Configuración](/confluence/spaces/HERCULES/pages/597852515/IU-ETI-0080-+Configuraci%C3%B3n) |  |  |  |  |  |  | ETI-CNF-E |
| [IU-ETI-0100-002 Evaluar memoria seguimiento](/confluence/spaces/HERCULES/pages/597853352/IU-ETI-0100-002+Evaluar+memoria+seguimiento) | ETI-EVC-EVAL |  |  |  |  |  |  |
| [IU-ETI-0070- Formulario Checklist](/confluence/spaces/HERCULES/pages/597852380/IU-ETI-0070-+Formulario+Checklist) |  | ETI-CHK-INV-E | ETI-CHK-INV-E |  |  |  |  |
| [IU-ETI-0030-003 Modificar acta](/confluence/spaces/HERCULES/pages/597853799/IU-ETI-0030-003+Modificar+acta) | ETI-ACT-E, ETI-ACT-DES |  |  | ETI-ACT-INV-ER,ETI-ACT-INV-DESR | ETI-ACT-ER,ETI-ACT-DESR |  |  |
| [IU-ETI-0120-002 Consulta memoria](/confluence/spaces/HERCULES/pages/597852465/IU-ETI-0120-002+Consulta+memoria) | ETI-MEM-V,ETI-MEM-EDOC |  |  |  |  |  |  |
| [IU-ETI-0090-003 Consulta memoria - Adjuntar Documentación](/confluence/spaces/HERCULES/pages/597852478/IU-ETI-0090-003+Consulta+memoria+-+Adjuntar+Documentaci%C3%B3n) | ETI-MEM-EDOC |  |  |  |  |  |  |
| [IU-ETI-0090-004 Consultar Memoria - Edición documentación - Aportar documento](/confluence/spaces/HERCULES/pages/597852484/IU-ETI-0090-004+Consultar+Memoria+-+Edici%C3%B3n+documentaci%C3%B3n+-+Aportar+documento) | ETI-MEM-EDOC |  |  |  |  |  |  |
| [IU-ETI-0060-012 Memorias - Edición documentación - Aportar documento](/confluence/spaces/HERCULES/pages/597852423/IU-ETI-0060-012+Memorias+-+Edici%C3%B3n+documentaci%C3%B3n+-+Aportar+documento) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-011 Memorias - Edición documentación](/confluence/spaces/HERCULES/pages/597852320/IU-ETI-0060-011+Memorias+-+Edici%C3%B3n+documentaci%C3%B3n) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0010-002 Alta convocatoria reunión](/confluence/spaces/HERCULES/pages/597853545/IU-ETI-0010-002+Alta+convocatoria+reuni%C3%B3n) | ETI-CNV-C |  |  |  |  |  |  |
| [IU-ETI-0030-005 Modificar acta - Comentarios - Añadir/modificar](/confluence/spaces/HERCULES/pages/597852518/IU-ETI-0030-005+Modificar+acta+-+Comentarios+-+A%C3%B1adir+modificar) | ETI-ACT-E |  |  | ETI-ACT-INV-ER | ETI-ACT-ER |  |  |
| [IU-ETI-0060-019 Memorias - Edición retrospectiva](/confluence/spaces/HERCULES/pages/597853436/IU-ETI-0060-019+Memorias+-+Edici%C3%B3n+retrospectiva) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0040-004 Conflicto de intereses - Añadir](/confluence/spaces/HERCULES/pages/597852415/IU-ETI-0040-004+Conflicto+de+intereses+-+A%C3%B1adir) | ETI-ACT-C, ETI-ACT-E |  |  |  |  |  |  |
| [IU-ETI-0060-006 Equipo investigador - Alta](/confluence/spaces/HERCULES/pages/597852301/IU-ETI-0060-006+Equipo+investigador+-+Alta) |  | ETI-PEV-INV-C, ETI-PEV-INV-ER | ETI-PEV-INV-C, ETI-PEV-INV-ER |  |  | ETI-PEV-INV-C, ETI-PEV-INV-ER |  |
| [IU-ETI-0060-007 Asignación de tareas - Alta-modificación](/confluence/spaces/HERCULES/pages/597852307/IU-ETI-0060-007+Asignaci%C3%B3n+de+tareas+-+Alta-modificaci%C3%B3n) |  | ETI-PEV-INV-ER | ETI-PEV-INV-ER |  |  | ETI-PEV-INV-ER |  |
| [IU-ETI-0060-020 Memorias - Edición retrospectiva - Aportar documento](/confluence/spaces/HERCULES/pages/597853427/IU-ETI-0060-020+Memorias+-+Edici%C3%B3n+retrospectiva+-+Aportar+documento) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-018 Memorias - Edición seguimiento final - Aportar documento](/confluence/spaces/HERCULES/pages/597853392/IU-ETI-0060-018+Memorias+-+Edici%C3%B3n+seguimiento+final+-+Aportar+documento) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-017 Memorias - Edición seguimiento final](/confluence/spaces/HERCULES/pages/597853401/IU-ETI-0060-017+Memorias+-+Edici%C3%B3n+seguimiento+final) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-016 Memorias - Edición seguimiento anual - Aportar documento](/confluence/spaces/HERCULES/pages/597853313/IU-ETI-0060-016+Memorias+-+Edici%C3%B3n+seguimiento+anual+-+Aportar+documento) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-015 Memorias - Edición seguimiento anual](/confluence/spaces/HERCULES/pages/597853306/IU-ETI-0060-015+Memorias+-+Edici%C3%B3n+seguimiento+anual) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-013 Memorias - Edición informes](/confluence/spaces/HERCULES/pages/597852322/IU-ETI-0060-013+Memorias+-+Edici%C3%B3n+informes) |  | ETI-MEM-INV-ER | ETI-MEM-INV-ER |  |  | ETI-MEM-INV-ER |  |
| [IU-ETI-0060-008 Memorias - Alta datos generales](/confluence/spaces/HERCULES/pages/597852311/IU-ETI-0060-008+Memorias+-+Alta+datos+generales) |  | ETI-MEM-INV-CR | ETI-MEM-INV-CR |  |  |  |  |
| [IU-ETI-0030-004 Editar asistencia](/confluence/spaces/HERCULES/pages/597853800/IU-ETI-0030-004+Editar+asistencia) | ETI-ACT-C, ETI-ACT-E |  |  |  |  |  |  |
| [IU-ETI-0030-002 Alta acta](/confluence/spaces/HERCULES/pages/597853794/IU-ETI-0030-002+Alta+acta) | ETI-ACT-C |  |  |  |  |  |  |
| [IU-ETI-0010-006 Asignación memorias - Modificar](/confluence/spaces/HERCULES/pages/597853607/IU-ETI-0010-006+Asignaci%C3%B3n+memorias+-+Modificar) | ETI-CNV-C, ETI-CNV-E |  |  |  |  |  |  |
| [IU-ETI-0010-005 Asignación memorias - Añadir](/confluence/spaces/HERCULES/pages/597853609/IU-ETI-0010-005+Asignaci%C3%B3n+memorias+-+A%C3%B1adir) | ETI-CNV-C, ETI-CNV-E |  |  |  |  |  |  |