# IU-ETI-0010-006 Asignación memorias - Modificar

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0010-006-  Asignación memorias - Modificar******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Asignación memorias - Modificar

Pantalla que muestra el formulario de modificar asignación de memoria

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Memoria | Desplegable  Texto corto  Obligatorio | Desplegable con las memorias en estado "En secretaria" que pertenecen al comité indicado en la convocatoria y que no han superado la fecha límite indicada en la convocatoria. Se muestra una concatenación del número de referencia de la memoria y el título descriptivo de la misma. |
| Evaluador1 | Desplegable  Texto corto  Obligatorio | Desplegable con los evaluadores activos del comité indicado en la convocatoria y que no entre en conflicto de intereses con ningún miembro del equipo investigador de la memoria seleccionada.  Nombre y apellidos recuperados por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) |
| Evaluador2 | Desplegable  Texto corto  Obligatorio | Desplegable con los evaluadores activos del comité indicado en la convocatoria y que no entre en conflicto de intereses con ningún miembro del equipo investigador de la memoria seleccionada.  Nombre y apellidos recuperados por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Se modifica los valores de la asignación de memoria, y los datos se ven reflejados en el listado de memorias asignadas a la reunión de evaluación | [CU-ETI-0010-007 - Asignación de memorias - Modificar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0010-gestion-convocatorias-reunion/cu-eti-0010-007-asignacion-de-memorias-modificar) | ETI-CNV-C  ETI-CNV-E |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-CNV-C, ETI-CNV-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-CNV-C, ETI-CNV-E |