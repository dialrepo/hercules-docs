# IU-CSP-0406-023 - Modificar proyecto - Configuración económica - Partidas presupuestarias

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-023 - Modificar proyecto - Configuración económica - Partidas presupuestarias******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Configuración económica - Partidas presupuestarias

Formulario que permite introducir las partidas o aplicaciones presupuestarias que se utilizarán para configurar el presupuesto del proyecto (y posteriormente para visualizar los datos económicos del proyecto en el apartado de Ejecución presupuestaria).

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de partidas presupuestarias del proyecto: recuperados de la tabla "proyecto partida" (filas sin icono o con el icono naranja) y "convocatoria partida" (filas con el icono rojo) | | |
|  | Icono de ayuda con tooltip | Se dibujará el icono de ayuda de color naranja en las siguientes situaciones:   1. Datos de la partida del proyecto no coinciden con los datos de la partida de la convocatoria ( los campos del registro de la tabla "proyecto partida" no son iguales al registro de la tabla de la convocatoria "convocatoria partida"): El texto en esta situación del tootip será "Existen diferencias en los datos de la partida presupuestaria respecto a la convocatoria, pulse el botón Editar si desea revisarlos." 2. La partida se ha creado en el proyecto directamente (el identificador del registro de la convocatoria es null en la tabla "proyecto partida"): El texto en esta situación del tootip será "Esta partida presupuestaria no está incluida en la configuración de la convocatoria."   Se dibujará el icono de ayuda de color rojo en la siguiente situación:   3 .La partida no existe en el proyecto (registro no existe en la tabla "proyecto partida")  pero sí en la convocatoria (registro en la tabla "convocatoria partida"), bien porque se ha eliminado en el proyecto o porque se ha creado nueva en la convocatoria una vez creado el proyecto: El texto en esta situación del tootip será "Esta partida presupuestaria está incluida en la convocatoria pero no en el proyecto. Pulse el botón Editar si desea añadirla al proyecto" |
| Código | Texto | Código alfanumérico que identifica la partida o aplicación presupuestaria.  Se corresponde con el campo "código" de la tabla "proyecto partida". |
| Tipo | Texto corto | Tipo de la partida presupuestaria según sea su naturaleza de gastos o ingresos.  Se mostrará el valor recuperado del enumerado "Tipo partida" a partir del campo "tipo partida" de la tabla "proyecto partida". |
| Descripción | Texto largo | Descripción de la partida.  Se corresponde con el campo "descripción" de la tabla "proyecto partida". |
| Modificar | Icono de acción | Acción "Modificar".  Solamente será posible modificar las partidas a las que no se haya vinculado ningún dato presupuestario del proyecto. |
| Eliminar | Icono de acción | Acción "Eliminar".  Solamente será posible eliminar las partidas a las que no se haya vinculado ningún dato presupuestario del proyecto. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Muestra la pantalla de modificación para la partida seleccionada del listado de partidas del proyecto | Solo será posible modificar partidas que no estén asociadas  a datos presupuestarios del proyecto. Para ello deberá cumplirse:   * + Si la partida es de tipo "gasto" se comprobará que ésta no exista en la tabla "anualidad gasto" (campo "partida presupuestaria") del proyecto.   + Si la partida es de tipo "ingreso" se comprobará que ésta no exista en la tabla "anualidad ingreso" (campo "partida presupuestaria") del proyecto.   Si se cumple lo anterior se permitirá la modificación, mostrando la pantalla descrita en [IU-CSP-0402-029 - Añadir-modificar partida presupuestaria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0402-029-anadir-modificar-partida-presupuestaria) a la que se accede en modo edición.  En caso contrario, la acción modificar no estará disponible.  Ver documentación de restricciones en [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion). | CSP-PRO-E  CSP-PRO-E\_UO |
| Eliminar | Elimina la partida seleccionada | Solo será posible eliminar partidas que sean del proyecto (las de la convocatoria, las de icono de ayuda de color rojo) y que no estén asociadas  a datos presupuestarios del proyecto. Para ello deberá cumplirse:   * + Si la partida es de tipo "gasto" se comprobará que ésta no exista en la tabla "anualidad gasto" (campo "partida presupuestaria") del proyecto.   + Si la partida es de tipo "ingreso" se comprobará que ésta no exista en la tabla "anualidad ingreso" (campo "partida presupuestaria") del proyecto.   Si se cumple lo anterior se permitirá la eliminación. Se realizará un borrado físico sobre la tabla "proyecto partida" para la partida seleccionada. Se podrá eliminar una partida del proyecto aunque ésta proceda de una partida de la convocatoria (campo "convocatoria partida id" informado). La partida origen de la convocatoria no deberá ser eliminada.  En caso contrario, la acción modificar no estará disponible  Ver documentación de restricciones en [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion). | CSP-PRO-E  CSP-PRO-E\_UO |
| Añadir partida presupuestaria | Muestra la pantalla para añadir una nuevo partida/aplicación presupuestaria al proyecto | Muestra la pantalla [IU-CSP-0402-029 - Añadir-modificar partida presupuestaria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0402-029-anadir-modificar-partida-presupuestaria) a la que se accede en modo inserción de nuevo registro.  Ver documentación de restricciones en [CU-CSP-1200-002 - Modificar proyecto - Unidad de gestión](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-002-modificar-proyecto-unidad-de-gestion). | CSP-PRO-E  CSP-PRO-E\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todos los apartados de definición del proyecto. | Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR | Ver detalle en documentación asociada en [CU-1200-003 - Ver proyecto - Investigador (rol principal/responsable económico)](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100766521). |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) (sería el caso del Visor) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.