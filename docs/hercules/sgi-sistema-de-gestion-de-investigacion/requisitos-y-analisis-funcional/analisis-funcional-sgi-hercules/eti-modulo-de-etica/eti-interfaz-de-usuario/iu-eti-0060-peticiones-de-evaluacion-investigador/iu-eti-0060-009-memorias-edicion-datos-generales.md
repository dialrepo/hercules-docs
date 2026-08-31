# IU-ETI-0060-009 Memorias - Edición datos generales

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0060-009- Memorias - Edición datos generales******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-002-Investigador  ACT-ETI-003-Solicitante  ACT-ETI-006-Responsable memoria |
| Frecuencia | Media |

## Formulario de Memorias - Edición datos generales

Pantalla que muestra el formulario de edición de una memoria la parte de Datos generales.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Comité | Selector  Texto corto | Comité asociado a la memoria. Modo consulta. |
| Tipo | Selector  Texto corto | Tipo de memoria. Modo consulta. |
| Título | Texto  Opcional | Título descriptivo de la memoria |
| Responsable | Texto  Opcional | Desplegable con las distintas personas del equipo.  Nombre y apellidos recuperado por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Se guardan los datos generales de la memoria y se mantiene en la misma pantalla.  Ver precondiciones de modificación en el caso de uso. | [CU-ETI-0060-009 - Memorias - Edición datos generales](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0060-peticiones-de-evaluacion-investigador/cu-eti-0060-009-memorias-edicion-datos-generales) | ETI-MEM-INV-ER |
| Formulario | Se va a la pantalla de Formulario de la memoria [IU-ETI-0060-010 Memorias - Edición formulario](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0060-peticiones-de-evaluacion-investigador/iu-eti-0060-010-memorias-edicion-formulario).  Ver precondiciones de modificación en el caso de uso. Si no cumple las condiciones de modificación se mostrará en modo consulta. | [CU-ETI-0060-010 - Memorias - Edición formulario](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0060-peticiones-de-evaluacion-investigador/cu-eti-0060-010-memorias-edicion-formulario) | ETI-MEM-INV-ER |
| Documentación | Se va a la pantalla Documentación de la memoria [IU-ETI-0060-011 Memorias - Edición documentación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0060-peticiones-de-evaluacion-investigador/iu-eti-0060-011-memorias-edicion-documentacion).  Ver precondiciones de modificación en el caso de uso. Si no cumple las condiciones de modificación se mostrará en modo consulta. | [CU-ETI-0060-011 - Memorias - Edición documentación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0060-peticiones-de-evaluacion-investigador/cu-eti-0060-011-memorias-edicion-documentacion) | ETI-MEM-INV-ER |
| Seguimiento anual | Se va a la pantalla Seguimiento anual [IU-ETI-0060-015 Memorias - Edición seguimiento anual](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0060-peticiones-de-evaluacion-investigador/iu-eti-0060-015-memorias-edicion-seguimiento-anual).  Ver precondiciones de modificación en el caso de uso. | [CU-ETI-0060-13-Memorias - Edición formulario seguimiento anual](https://confluence.um.es/confluence/spaces/GES/pages/221388636/CU-ETI-0060-013+-+Memorias+-+Edici%C3%B3n+formulario+seguimiento+anual) | ETI-MEM-INV-ER |
| Seguimiento final | Se va a la pantalla Seguimiento final [IU-ETI-0060-017 Memorias - Edición seguimiento final](http://IU-ETI-0060-017 Memorias - Edición seguimiento final).  Ver precondiciones de modificación en el caso de uso. | [CU-ETI-0060-014 - Memorias - Edición formulario seguimiento final](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0060-peticiones-de-evaluacion-investigador/cu-eti-0060-014-memorias-edicion-formulario-seguimiento-final) | ETI-MEM-INV-ER |
| Retrospectiva | Se va a la pantalla Retrospectiva [IU-ETI-0060-019 Memorias - Edición retrospectiva](http://IU-ETI-0060-019 Memorias - Edición retrospectiva).  Ver precondiciones de modificación en el caso de uso. | [CU-ETI-0060-015 - Memorias - Edición formulario retrospectiva](https://confluence.um.es/confluence/spaces/GES/pages/221388638/CU-ETI-0060-015+-+Memorias+-+Edici%C3%B3n+formulario+retrospectiva) | ETI-MEM-INV-ER |
| Informes | Se va a la pantalla Informes de la memoria [IU-ETI-0060-013 Memorias - Edición informes](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0060-peticiones-de-evaluacion-investigador/iu-eti-0060-013-memorias-edicion-informes). |  | ETI-MEM-INV-ER |
| Evaluaciones | Se va a la pantalla Evaluaciones de la memoria [IU-ETI-0060-014 Memorias - Edición evaluaciones](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0060-peticiones-de-evaluacion-investigador/iu-eti-0060-014-memorias-edicion-evaluaciones). |  | ETI-MEM-INV-ER |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-002-Investigador | ETI-MEM-INV-ER |
| ACT-ETI-003-Solicitante | ETI-MEM-INV-ER |
| ACT-ETI-006-Responsable memoria | ETI-MEM-INV-ER |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-MEM-INV-ER |