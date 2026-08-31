# PRC - Permisos - Actores

## Catálogo de Permisos

Listado con todos los permisos del módulo PRC y la descripción de sus abreviaturas así como los criterios seguidos en el diseño para el nombrado de dichos permisos.

---

Ver Catálogo de permisos

## Diseño de permisos

Se siguen los criterios generales descritos en Permisos.

Ver detalle de criterios de diseño de permisos

**Error al renderizar el macro 'excerpt-include'**

No link could be created for 'Permisos'.

## Abreviaturas de entidades

| Abreviatura | Nombre |
| --- | --- |
| VAL | Validación de producción científica |
| INF | Informes |
| CON | Convocatorias |
|  |  |

## Catálogo de permisos

| Nombre abreviado | Descripción |
| --- | --- |
| PRC-VAL-V | Visualización.  Acceso al listado y utilización de su filtro.  Habilita el botón de acceso al detalle en modo consulta.  Todos los campos estarán en modo consulta y los botones de acción des-habilitados. |
| PRC-VAL-E | Edición.  Habilita el botón de acceso al detalle en modo edición para validar/rechazar el item de producción científica. |
| PRC-VAL-INV-ER | Edición restringido.  Habilita el botón de acceso al detalle en modo edición para validar/rechazar el item de producción científica. |
| CSP-PRO-PRC-V | Visualización datos proyectos desde Producción científica  Permite acceso a la consulta de los datos: Título, acrónimo, código interno, fecha inicio, fecha fin y fecha fin definitiva de los proyectos. |
| PRC-CON-C | Creación.  Habilita el botón de creación. |
| PRC-CON-E | Edición.  Habilita el botón de acceso al detalle en modo edición. |
| PRC-CON-B | Borrado.  Habilita el botón de borrado (lógico). |
| PRC-CON-R | Recuperación.  Habilita el botón de recuperación de un elemento borrado (lógico).  Habilita el campo de filtrado por estado de borrado.  Habilita la columna que muestra el estado de borrado. |
| PRC-CON-BAR | Baremación.  Habilita el botón de lanzamiento del proceso de baremación. |
| PRC-CON-V | Visualización.  Acceso al listado y utilización de su filtro.  Todos los campos estarán en modo consulta y los botones de acción des-habilitados. |
| PRC-INF-G | Generación del informe  Habilita el botón de Generar informes y la opción del menú de Informes |
| PRC-INF-INV-GR | Generación del informe restringido  Habilita el botón de Generar informes y la opción del menú de Informes de forma restringida |

---

## Permisos de Acciones y/o Accesos por Actor

| Actor | Permisos |
| --- | --- |
| [ACT-PRC-001-Investigador](/confluence/spaces/HERCULES/pages/597852349/ACT-PRC-001-Investigador) | PRC-VAL-INV-ER  CSP-PRO-PRC-V  PRC-INF-INV-GR |
| [ACT-PRC-004-Visor](/confluence/spaces/HERCULES/pages/597852814/ACT-PRC-004-Visor) | PRC-VAL-V  PRC-CON-V  CSP-PRO-PRC-V  PRC-INF-G |
| [ACT-PRC-003-Gestor](/confluence/spaces/HERCULES/pages/597852344/ACT-PRC-003-Gestor) | PRC-VAL-E  PRC-CON-C, PRC-CON-E, PRC-CON-B, PRC-CON-R, PRC-CON-BAR  CSP-PRO-PRC-V  PRC-INF-G |

## Permisos de Acceso a Pantallas (IU)

| Título | Permisos |
| --- | --- |
| [IU-PRC-0202-003 - Crear-Modificar-Consultar convocatoria de baremación - Baremos y puntuaciones](/confluence/spaces/HERCULES/pages/597852315/IU-PRC-0202-003+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Baremos+y+puntuaciones) | PRC-CON-V, PRC-CON-C, PRC-CON-E |
| [IU-PRC-0201-012 Búsqueda y listado de actividades de I+D+i - Investigador](/confluence/spaces/HERCULES/pages/597852248/IU-PRC-0201-012+B%C3%BAsqueda+y+listado+de+actividades+de+I+D+i+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-010 Búsqueda y listado de dirección de tesis - Investigador](/confluence/spaces/HERCULES/pages/597852246/IU-PRC-0201-010+B%C3%BAsqueda+y+listado+de+direcci%C3%B3n+de+tesis+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-008 Búsqueda y listado de comités editoriales - Investigador](/confluence/spaces/HERCULES/pages/597852261/IU-PRC-0201-008+B%C3%BAsqueda+y+listado+de+comit%C3%A9s+editoriales+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-006 Búsqueda y listado de obras artísticas - Investigador](/confluence/spaces/HERCULES/pages/597852283/IU-PRC-0201-006+B%C3%BAsqueda+y+listado+de+obras+art%C3%ADsticas+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-004 Búsqueda y listado de congresos - Investigador](/confluence/spaces/HERCULES/pages/597852281/IU-PRC-0201-004+B%C3%BAsqueda+y+listado+de+congresos+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-001 Búsqueda y listado de publicaciones - Investigador](/confluence/spaces/HERCULES/pages/597852345/IU-PRC-0201-001+B%C3%BAsqueda+y+listado+de+publicaciones+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0202-001 Búsqueda y listado de convocatorias](/confluence/spaces/HERCULES/pages/597852525/IU-PRC-0202-001+B%C3%BAsqueda+y+listado+de+convocatorias) | PRC-VAL-V, PRC-CON-C, PRC-CON-E, PRC-CON-B, PRC-CON-R, PRC-CON-BAR |
| [IU-PRC-0201-009 - Ver comité editorial - Investigador](/confluence/spaces/HERCULES/pages/597852245/IU-PRC-0201-009+-+Ver+comit%C3%A9+editorial+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0200-009 - Ver comité editorial - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852332/IU-PRC-0200-009+-+Ver+comit%C3%A9+editorial+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-012 Búsqueda y listado de actividades de I+D+i - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852331/IU-PRC-0200-012+B%C3%BAsqueda+y+listado+de+actividades+de+I+D+i+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-010 Búsqueda y listado de dirección de tesis - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852333/IU-PRC-0200-010+B%C3%BAsqueda+y+listado+de+direcci%C3%B3n+de+tesis+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-008 Búsqueda y listado de comités editoriales - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852337/IU-PRC-0200-008+B%C3%BAsqueda+y+listado+de+comit%C3%A9s+editoriales+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-006 Búsqueda y listado de obras artísticas - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852299/IU-PRC-0200-006+B%C3%BAsqueda+y+listado+de+obras+art%C3%ADsticas+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-001 Búsqueda y listado de publicaciones - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852600/IU-PRC-0200-001+B%C3%BAsqueda+y+listado+de+publicaciones+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-004 Búsqueda y listado de congresos - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852308/IU-PRC-0200-004+B%C3%BAsqueda+y+listado+de+congresos+-+Unidades+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0201-005 - Ver congreso - Investigador](/confluence/spaces/HERCULES/pages/597852282/IU-PRC-0201-005+-+Ver+congreso+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-002 - Ver publicación - Investigador](/confluence/spaces/HERCULES/pages/597852319/IU-PRC-0201-002+-+Ver+publicaci%C3%B3n+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0200-005 - Ver congreso - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852298/IU-PRC-0200-005+-+Ver+congreso+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-002 - Ver publicación - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852362/IU-PRC-0200-002+-+Ver+publicaci%C3%B3n+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0201-013 - Ver organización de actividad de I+D+i - Investigador](/confluence/spaces/HERCULES/pages/597852249/IU-PRC-0201-013+-+Ver+organizaci%C3%B3n+de+actividad+de+I+D+i+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-011 - Ver dirección de tesis - Investigador](/confluence/spaces/HERCULES/pages/597852247/IU-PRC-0201-011+-+Ver+direcci%C3%B3n+de+tesis+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0201-007 - Ver obra artística - Investigador](/confluence/spaces/HERCULES/pages/597852284/IU-PRC-0201-007+-+Ver+obra+art%C3%ADstica+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0200-013 - Ver organización de actividad de I+D+i - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852292/IU-PRC-0200-013+-+Ver+organizaci%C3%B3n+de+actividad+de+I+D+i+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-011 - Ver dirección de tesis - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852325/IU-PRC-0200-011+-+Ver+direcci%C3%B3n+de+tesis+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0200-007 - Ver obra artística - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852336/IU-PRC-0200-007+-+Ver+obra+art%C3%ADstica+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-V, PRC-VAL-E |
| [IU-PRC-0203-001 Infomes - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852371/IU-PRC-0203-001+Infomes+-+Unidad+de+gesti%C3%B3n) | PRC-INF-G |
| [IU-PRC-0203-003 Infomes Investigador](/confluence/spaces/HERCULES/pages/597852560/IU-PRC-0203-003+Infomes+Investigador) | PRC-INF-INV-GR |
| [IU-PRC-0201-003 - Rechazar item de producción científica - Investigador](/confluence/spaces/HERCULES/pages/597852310/IU-PRC-0201-003+-+Rechazar+item+de+producci%C3%B3n+cient%C3%ADfica+-+Investigador) | PRC-VAL-INV-ER |
| [IU-PRC-0202-004 - Crear-Modificar-Consultar convocatoria de baremación - Moduladores y rangos](/confluence/spaces/HERCULES/pages/597852458/IU-PRC-0202-004+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Moduladores+y+rangos) | PRC-CON-V, PRC-CON-C, PRC-CON-E |
| [IU-PRC-0202-007 - Añadir-Modificar rango licencia](/confluence/spaces/HERCULES/pages/597852436/IU-PRC-0202-007+-+A%C3%B1adir-Modificar+rango+licencia) | PRC-CON-C, PRC-CON-E |
| [IU-PRC-0202-005 - Añadir-Modificar rango costes indirectos](/confluence/spaces/HERCULES/pages/597852440/IU-PRC-0202-005+-+A%C3%B1adir-Modificar+rango+costes+indirectos) | PRC-CON-C, PRC-CON-E |
| [IU-PRC-0202-006 - Añadir-Modificar rango cuantía contratos](/confluence/spaces/HERCULES/pages/597852439/IU-PRC-0202-006+-+A%C3%B1adir-Modificar+rango+cuant%C3%ADa+contratos) | PRC-CON-C, PRC-CON-E |
| [IU-PRC-0202-002 - Crear-Modificar-Consultar convocatoria de baremación - Datos generales](/confluence/spaces/HERCULES/pages/597852338/IU-PRC-0202-002+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Datos+generales) | PRC-CON-V, PRC-CON-C, PRC-CON-E |
| [IU-PRC-0200-003 - Rechazar item de producción científica - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852316/IU-PRC-0200-003+-+Rechazar+item+de+producci%C3%B3n+cient%C3%ADfica+-+Unidad+de+gesti%C3%B3n) | PRC-VAL-E |

## Agrupación Pantallas (IU) - Actores - Permisos de acciones

| Título | ACT-PRC-001-Investigador | ACT-PRC-003-Gestor | ACT-PRC-004-Visor |
| --- | --- | --- | --- |
| [IU-PRC-0202-003 - Crear-Modificar-Consultar convocatoria de baremación - Baremos y puntuaciones](/confluence/spaces/HERCULES/pages/597852315/IU-PRC-0202-003+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Baremos+y+puntuaciones) |  | PRC-CON-C, PRC-CON-E | PRC-CON-V |
| [IU-PRC-0201-012 Búsqueda y listado de actividades de I+D+i - Investigador](/confluence/spaces/HERCULES/pages/597852248/IU-PRC-0201-012+B%C3%BAsqueda+y+listado+de+actividades+de+I+D+i+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0201-010 Búsqueda y listado de dirección de tesis - Investigador](/confluence/spaces/HERCULES/pages/597852246/IU-PRC-0201-010+B%C3%BAsqueda+y+listado+de+direcci%C3%B3n+de+tesis+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0201-008 Búsqueda y listado de comités editoriales - Investigador](/confluence/spaces/HERCULES/pages/597852261/IU-PRC-0201-008+B%C3%BAsqueda+y+listado+de+comit%C3%A9s+editoriales+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0201-006 Búsqueda y listado de obras artísticas - Investigador](/confluence/spaces/HERCULES/pages/597852283/IU-PRC-0201-006+B%C3%BAsqueda+y+listado+de+obras+art%C3%ADsticas+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0201-004 Búsqueda y listado de congresos - Investigador](/confluence/spaces/HERCULES/pages/597852281/IU-PRC-0201-004+B%C3%BAsqueda+y+listado+de+congresos+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0201-001 Búsqueda y listado de publicaciones - Investigador](/confluence/spaces/HERCULES/pages/597852345/IU-PRC-0201-001+B%C3%BAsqueda+y+listado+de+publicaciones+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0202-001 Búsqueda y listado de convocatorias](/confluence/spaces/HERCULES/pages/597852525/IU-PRC-0202-001+B%C3%BAsqueda+y+listado+de+convocatorias) |  | PRC-CON-C, PRC-CON-E, PRC-CON-B, PRC-CON-R, PRC-CON-BAR | PRC-CON-V |
| [IU-PRC-0201-009 - Ver comité editorial - Investigador](/confluence/spaces/HERCULES/pages/597852245/IU-PRC-0201-009+-+Ver+comit%C3%A9+editorial+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0200-009 - Ver comité editorial - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852332/IU-PRC-0200-009+-+Ver+comit%C3%A9+editorial+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0200-012 Búsqueda y listado de actividades de I+D+i - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852331/IU-PRC-0200-012+B%C3%BAsqueda+y+listado+de+actividades+de+I+D+i+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0200-010 Búsqueda y listado de dirección de tesis - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852333/IU-PRC-0200-010+B%C3%BAsqueda+y+listado+de+direcci%C3%B3n+de+tesis+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0200-008 Búsqueda y listado de comités editoriales - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852337/IU-PRC-0200-008+B%C3%BAsqueda+y+listado+de+comit%C3%A9s+editoriales+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0200-006 Búsqueda y listado de obras artísticas - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852299/IU-PRC-0200-006+B%C3%BAsqueda+y+listado+de+obras+art%C3%ADsticas+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0200-001 Búsqueda y listado de publicaciones - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852600/IU-PRC-0200-001+B%C3%BAsqueda+y+listado+de+publicaciones+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0200-004 Búsqueda y listado de congresos - Unidades de gestión](/confluence/spaces/HERCULES/pages/597852308/IU-PRC-0200-004+B%C3%BAsqueda+y+listado+de+congresos+-+Unidades+de+gesti%C3%B3n) |  | PRC-VAL-E | PRC-VAL-V |
| [IU-PRC-0201-005 - Ver congreso - Investigador](/confluence/spaces/HERCULES/pages/597852282/IU-PRC-0201-005+-+Ver+congreso+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0201-002 - Ver publicación - Investigador](/confluence/spaces/HERCULES/pages/597852319/IU-PRC-0201-002+-+Ver+publicaci%C3%B3n+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0200-005 - Ver congreso - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852298/IU-PRC-0200-005+-+Ver+congreso+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0200-002 - Ver publicación - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852362/IU-PRC-0200-002+-+Ver+publicaci%C3%B3n+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0201-013 - Ver organización de actividad de I+D+i - Investigador](/confluence/spaces/HERCULES/pages/597852249/IU-PRC-0201-013+-+Ver+organizaci%C3%B3n+de+actividad+de+I+D+i+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0201-011 - Ver dirección de tesis - Investigador](/confluence/spaces/HERCULES/pages/597852247/IU-PRC-0201-011+-+Ver+direcci%C3%B3n+de+tesis+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0201-007 - Ver obra artística - Investigador](/confluence/spaces/HERCULES/pages/597852284/IU-PRC-0201-007+-+Ver+obra+art%C3%ADstica+-+Investigador) | PRC-VAL-INV-ER, CSP-PRO-PRC-V |  |  |
| [IU-PRC-0200-013 - Ver organización de actividad de I+D+i - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852292/IU-PRC-0200-013+-+Ver+organizaci%C3%B3n+de+actividad+de+I+D+i+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0200-011 - Ver dirección de tesis - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852325/IU-PRC-0200-011+-+Ver+direcci%C3%B3n+de+tesis+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0200-007 - Ver obra artística - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852336/IU-PRC-0200-007+-+Ver+obra+art%C3%ADstica+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E, CSP-PRO-PRC-V | PRC-VAL-V, CSP-PRO-PRC-V |
| [IU-PRC-0203-001 Infomes - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852371/IU-PRC-0203-001+Infomes+-+Unidad+de+gesti%C3%B3n) |  | PRC-INF-G | PRC-INF-G |
| [IU-PRC-0203-003 Infomes Investigador](/confluence/spaces/HERCULES/pages/597852560/IU-PRC-0203-003+Infomes+Investigador) | PRC-INF-INV-GR |  |  |
| [IU-PRC-0201-003 - Rechazar item de producción científica - Investigador](/confluence/spaces/HERCULES/pages/597852310/IU-PRC-0201-003+-+Rechazar+item+de+producci%C3%B3n+cient%C3%ADfica+-+Investigador) | PRC-VAL-INV-ER |  |  |
| [IU-PRC-0202-004 - Crear-Modificar-Consultar convocatoria de baremación - Moduladores y rangos](/confluence/spaces/HERCULES/pages/597852458/IU-PRC-0202-004+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Moduladores+y+rangos) |  | PRC-CON-C, PRC-CON-E | PRC-CON-V |
| [IU-PRC-0202-007 - Añadir-Modificar rango licencia](/confluence/spaces/HERCULES/pages/597852436/IU-PRC-0202-007+-+A%C3%B1adir-Modificar+rango+licencia) |  | PRC-CON-C, PRC-CON-E |  |
| [IU-PRC-0202-005 - Añadir-Modificar rango costes indirectos](/confluence/spaces/HERCULES/pages/597852440/IU-PRC-0202-005+-+A%C3%B1adir-Modificar+rango+costes+indirectos) |  | PRC-CON-C, PRC-CON-E |  |
| [IU-PRC-0202-006 - Añadir-Modificar rango cuantía contratos](/confluence/spaces/HERCULES/pages/597852439/IU-PRC-0202-006+-+A%C3%B1adir-Modificar+rango+cuant%C3%ADa+contratos) |  | PRC-CON-C, PRC-CON-E |  |
| [IU-PRC-0202-002 - Crear-Modificar-Consultar convocatoria de baremación - Datos generales](/confluence/spaces/HERCULES/pages/597852338/IU-PRC-0202-002+-+Crear-Modificar-Consultar+convocatoria+de+baremaci%C3%B3n+-+Datos+generales) |  | PRC-CON-C, PRC-CON-E | PRC-CON-V |
| [IU-PRC-0200-003 - Rechazar item de producción científica - Unidad de gestión](/confluence/spaces/HERCULES/pages/597852316/IU-PRC-0200-003+-+Rechazar+item+de+producci%C3%B3n+cient%C3%ADfica+-+Unidad+de+gesti%C3%B3n) |  | PRC-VAL-E |  |