# IU-ETI-0060-008 Memorias - Alta datos generales

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0060-008- Memorias - Alta datos generales******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-002-Investigador  ACT-ETI-003-Solicitante |
| Frecuencia | Media |

## Formulario de Alta datos generales

Pantalla que muestra el formulario de alta de una memoria con los datos generales para poder crear una nueva memoria.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Comité | Selector  Texto corto  Obligatorio | Desplegable con los valores:    * CEISH * CEEA * CEIAB |
| Tipo | Selector  Texto corto  Obligatorio | Desplegable con los valores dependiendo del tipo de comité:  * Si comité CEISH:   + Nueva   + Modificación   + Ratificación * Si comité CEEA:   + Nueva   + Modificación * Si comité CEIAB:   + Nueva   + Modificación |
| Memoria original | Selector  Opcional | Desplegable con las referencias de las memorias del comité elegido y que están en un estado mayor o igual a "Fin de evaluación" si se ha elegido en Tipo la opción de "Modificación" |
| Título | Texto  Opcional | Título descriptivo de la memoria. Únicamente se muestra cuando la memoria es de tipo CEEA (M20) |
| Responsable | Selector  Texto  Opcional | Desplegable con las distintas personas del equipo.  Nombre y apellidos, recuperado por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea la memoria en el sistema en estado "En elaboración".  Se muestra la pantalla de edición. | [CU-ETI-0060-008 - Memorias - Alta datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0060-peticiones-de-evaluacion-investigador/cu-eti-0060-008-memorias-alta-datos-generales) | ETI-MEM-INV-CR |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-002-Investigador | ETI-MEM-INV-CR |
| ACT-ETI-003-Solicitante | ETI-MEM-INV-CR |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-MEM-INV-CR |