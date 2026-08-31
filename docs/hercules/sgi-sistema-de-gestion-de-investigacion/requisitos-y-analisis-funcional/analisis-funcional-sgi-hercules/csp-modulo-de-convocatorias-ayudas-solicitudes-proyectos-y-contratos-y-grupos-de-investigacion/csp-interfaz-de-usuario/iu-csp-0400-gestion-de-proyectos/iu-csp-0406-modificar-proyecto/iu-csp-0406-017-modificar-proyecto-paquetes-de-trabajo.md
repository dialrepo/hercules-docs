# IU-CSP-0406-017 - Modificar proyecto - Paquetes de trabajo

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-017 - Modificar proyecto - Paquetes de trabajo******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Modificar proyecto - Paquetes de trabajo

Formulario que permite definir los paquetes de trabajo. Si bien los paquetes de trabajo son propios de la gestión de proyectos europeos, el SGI no establece ninguna restricción para activarlos sobre cualquier tipo de proyecto/contrato. Esta activación se realiza desde la "Ficha general" del proyecto, a través del campo "Paquetes de trabajo". Si en este campo se recoge  un valor afirmativo, el apartado "Paquetes de trabajo" estará disponible.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de paquetes de trabajo de un proyecto | | |
| Nombre | Texto corto | Nombre del paquete de trabajo.  Debe ser único dentro del proyecto. |
| Fecha de inicio | Fecha | Fecha de inicio del paquete de trabajo |
| Fecha de fin | Fecha | Fecha de fin del paquete de trabajo |
| Persona/mes | Numérico entero genérico | Indica el esfuerzo (cantidad de tiempo) que se dedica al paquete de trabajo |
| Descripción | Texto largo | Descripción del paquete de trabajo |
| Modificar | Icono de acción | Acción "Modificar" |
| Eliminar | Icono de acción | Acción "Eliminar" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Muestra la pantalla de modificación del paquete de trabajo seleccionado del listado de paquetes del proyecto | Se resuelve con la pantalla [IU-CSP-0402-014 - Añadir-modificar paquete de trabajo](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0402-014-anadir-modificar-paquete-de-trabajo)  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Eliminar | Elimina el paquete de trabajo del proyecto | Lo elimina del listado, al pulsar el botón de Guardar se realizará un borrado físico del registro en la tabla "proyecto paquete trabajo".  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |
| Añadir paquete de trabajo | Muestra la pantalla de Añadir paquete de trabajo al proyecto | Muestra la pantalla [IU-CSP-0402-014 - Añadir-modificar paquete de trabajo](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0400-gestion-de-proyectos/iu-csp-0402-014-anadir-modificar-paquete-de-trabajo)  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modifica el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todos los apartados de definición del proyecto. | En caso de eliminación de un registro se realizará un borrado físico del registro en la tabla "proyecto paquete trabajo"  Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) y en [CU-1200-003 - Ver proyecto - Investigador (rol principal/responsable económico)](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100766521) |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) (sería el caso del Visor) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.