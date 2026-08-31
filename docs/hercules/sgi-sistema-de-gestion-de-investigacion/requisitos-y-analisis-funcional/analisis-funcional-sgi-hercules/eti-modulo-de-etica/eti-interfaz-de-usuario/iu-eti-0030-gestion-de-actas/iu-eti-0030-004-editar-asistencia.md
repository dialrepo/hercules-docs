# IU-ETI-0030-004 Editar asistencia

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0030-004 Editar asistencia******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Editar asistencia

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Asistente | Texto corto | Nombre y apellidos del evaluador asistente o no a la reunión de convocatoria, recuperado por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) |
| Asistencia | Selector  Booleano  Valores: Si/No | Si ha podido o no asistir |
| Motivo | Texto  Opcional | En caso de no poder asistir será obligatorio introducir el motivo. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Modifica los datos de asistencia del evaluador | [CU-ETI-0030-005 - Asistentes - Modificar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0030-gestion-de-actas/cu-eti-0030-005-asistentes-modificar) | ETI-ACT-C  ETI-ACT-E |
| Cancelar | Retorna al listado de Asistentes del acta sin salvar los posibles cambios. |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-ACT-C, ETI-ACT-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-ACT-C, ETI-ACT-E |