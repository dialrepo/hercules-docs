# IU-CSP-0406-032 - Modificar proyecto - Clasificaciones

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-032 - Modificar proyecto - Clasificaciones******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Modificar proyecto - Clasificaciones

Formulario para añadir de forma genérica la clasificación del proyecto bajo cualquiera de los listados de clasificación configurados en la implantación de SGI. Ejemplos de estos listados de clasificación son: clasificación UNESCO, clasificación NABS, clasificación CNAE.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de clasificaciones del proyecto, extraídas de la tabla "proyecto clasificación". Un proyecto podrá estar asociado a más de una clasificación. | | |
| Clasificación | Texto | Nombre de la clasificación (padre).   Será el nombre de la raíz del árbol de la que cuelga el elemento final, esto es, el nivel seleccionado, al que pertenece el elemento de clasificación al que se vincula el proyecto en la tabla "proyecto clasificación".  El nombre a mostrar se obtendrá a partir del requisito de integración [REQ-INT-0030-SGO-0031 - Consultar clasificación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0030-sgo-integracion-con-sistema-de-gestion-de-la-estructura-organica/req-int-0030-sgo-0031-consultar-clasificacion).  Nota: en el caso del escenario en el que se acaban de seleccionar una o varias clasificaciones en el popup, puede que para estas clasificaciones esta información ya esté disponible en la respuesta devuelta tras la selección y no sea necesario realizar nuevas llamadas para presentarla en pantalla. |
| Niveles | Texto | Concatenación de los nombres de los elementos de clasificación que ocupan niveles superiores al elemento con el que se vincula el proyecto (el referenciado en la tabla "proyecto clasificación") .  La cadena de texto a mostrar se compondrá a la hora de hacer la presentación por pantalla, obteniendo para ello la información necesaria a través de sucesivas peticiones del detalle de cada clasificación a partir de [REQ-INT-0030-SGO-0031 - Consultar clasificación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0030-sgo-integracion-con-sistema-de-gestion-de-la-estructura-organica/req-int-0030-sgo-0031-consultar-clasificacion). La concatenación de nombres habría de hacerse utilizando algún tipo de separador (ej: "-") y sería de los nombres de los niveles jerárquicamente superiores al de la clasificación seleccionada, ordenados desde la raíz hasta el inmediatamente superior a esa clasificación, esto es, sin incluir el nombre de la clasificación seleccionada.  Si la cadena de texto a mostrar es muy larga se cortará con "...". Se acompañará de un componente tipo "tooltip" que mostrará la cadena completa al pasar sobre el texto.  Nota: en el caso del escenario en el que se acaban de seleccionar una o varias clasificaciones en el popup, puede que para estas clasificaciones esta información ya esté disponible en la respuesta devuelta tras la selección y no sea necesario realizar nuevas llamadas para presentarla en pantalla. |
| Nivel seleccionado | Texto | Nombre del elemento de clasificación seleccionado. Es el nombre del elemento de clasificación con el que se relaciona directamente el proyecto en la tabla "proyecto clasificación".  El nombre a mostrar se obtendrá a partir del requisito de integración [REQ-INT-0030-SGO-0031 - Consultar clasificación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0030-sgo-integracion-con-sistema-de-gestion-de-la-estructura-organica/req-int-0030-sgo-0031-consultar-clasificacion).  Nota: en el caso del escenario en el que se acaban de seleccionar una o varias clasificaciones en el popup, puede que para estas clasificaciones esta información ya esté disponible en la respuesta devuelta tras la selección y no sea necesario realizar nuevas llamadas para presentarla en pantalla. |
| Eliminar | Icono de acción | Acción "Eliminar" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Eliminar | Elimina el código de clasificación para el proyecto | Elimina el registro del listado.  Ver documentación de restricciones en [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion) | CSP-PRO-E  CSP-PRO-E\_UO |
| Añadir clasificación | Muestra la pantalla "Selección de clasificaciones" | Muestra la pantalla común [IU-GEN-0120 - Selección de clasificaciones](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0120-seleccion-de-clasificaciones). Podrán seleccionarse más de una clasificación, tanto dentro de un mismo árbol (clasificación) como de árboles (clasificaciones) diferentes. No existirá ninguna restricción por "Tipo de clasificación", es decir, estarán disponibles todas las clasificaciones disponibles en a tabla "clasificación" (tabla del módulo ESB)  Ver documentación de restricciones en [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion) | No se necesita permiso para mostrar la pantalla de selección de clasificaciones. |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todas las pestañas de la pantalla. | Por cada código de clasificación añadido al listado se creará un registro en la tabla "Proyecto clasificación".  Ver documentación de restricciones en  [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion) | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) y en [CU-CSP-1200-003 - Ver proyecto - Investigador (rol principal/responsable económico)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-003-ver-proyecto-investigador-rol-principalresponsable-economico) |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) (sería el caso del Visor) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.