# IU-CSP-0060-005 - Modificar programa de investigación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0060-005 Modificar programa de investigación******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Modificar programa de investigación

Formulario de modificación de un programa de investigación.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Modificación de elemento de primer nivel del árbol de programas de un plan | | |
| Nombre | Texto  Obligatorio | Nombre identificativo del programa. Será obligatorio y se comprobará su unicidad dentro del plan. Se podrá modificar el nombre del programa siempre y cuando no se repitan dos programas activos con el mismo nombre dentro del plan al que pertenece (siendo plan el nodo raíz del árbol de programas, es decir, aquel cuyo campo "padre" tome el valor "null"). |
| Descripción | Texto  Opcional | Se podrá modificar libremente este campo, pudiendo dejarse vacío. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Aceptar | Actualiza el registro cuyos datos están siendo modificados.  Actualiza los datos del registro en la tabla programa. | Se comprobará la unicidad del campo "nombre" sobre los elementos activos del árbol de programas de un mismo del plan. No pueden existir dos elementos activos con el mismo nombre dentro de mismo árbol de programas, pero sí podrán existir dos elementos activos con el mismo nombre en diferentes árboles de programa. Un árbol de programas será aquel que comparte nodo raíz (plan), siendo el nodo raíz aquel cuyo campo "padre" tome el valor "null".  [CU-CSP-0050-005 - Modificar programa al plan de investigación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0050-gestion-de-planes-de-investigacion/cu-csp-0050-005-modificar-programa-al-plan-de-investigacion) | CSP-PRG-E |
| Cancelar | No realiza ninguna operación en base de datos. | Se mantiene en la pantalla de edición del árbol de programas |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-PRG-E |
| ACT-CSP-003-Gestor | CSP-PRG-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRG-V, CSP-PRG-E |