# IU-ETI-0040-004 Conflicto de intereses - Añadir

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0040-004- Conflicto de intereses - Añadir******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Conflicto de intereses - Añadir

Pantalla que muestra el formulario para crear un nuevo conflicto de intereses de un evaluador, es decir, seleccionar un usuario con el que tiene conflicto de intereses por lo cual no podría evaluar una memoria en la que dicho usuario estuviera formando parte del equipo.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Usuario | Botón Buscar  Texto corto  Obligatorio | A través del botón Buscar se dará acceso al buscador común [IU-GEN-0060 - Búsqueda de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas).  El listado de investigadores disponible se obtendrá del requisito de integración [REQ-INT-0020-SGP-0020 - Buscar persona en un listado de colectivos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0020-buscar-persona-en-un-listado-de-colectivos)  Una vez buscado se mostrará el nombre y apellidos de la persona. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Buscar | A través del botón Buscar se dará acceso al buscador común [IU-GEN-0060 - Búsqueda de personas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas). El listado de investigadores disponible se obtendrá del requisito de integración [REQ-INT-0020-SGP-0020 - Buscar persona en un listado de colectivos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0020-buscar-persona-en-un-listado-de-colectivos).  Se le deberá pasar a este buscador el tipo de colectivo que haya sido identificado en periodo de implantación como personal de investigación que puede formar parte del equipo de trabajo de una solicitud de evaluación de ética ("Equipo trabajo ética").  En caso de no existir la persona, se podrá solicitar por parte del usuario gestor el alta de la misma a través del formulario de alta [IU-GEN-0061- Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0061-solicitar-alta-de-persona) que hará uso del requisito de integración [REQ-INT-0020-SGP-0050 - Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0050-solicitar-alta-de-persona).  En el caso de que el buscador devolviese la persona, pero se quisiera realizar alguna modificación en sus datos, se podrá solicitar dicha modificación, utilizando para ello el formulario de solicitud de modificación IU-GEN-0062 - Ver detalle - Solicitar modificación de persona, que cumple con el requisito de integración [REQ-INT-0020-SGP-0060 - Solicitar modificación de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0060-solicitar-modificacion-de-persona) y a la que se accede desde el propio formulario de búsqueda [IU-GEN-0100-0060 - Búsqueda de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas). Solamente podrá realizar esta solicitud de modificación el usuario gestor. |  | No se necesita permiso para abrir la pantalla de búsqueda de personas |
| Añadir | Añade un nuevo usuario al listado de conflictos de intereses |  | ETI-EVR-C  ETI-EVR-E |
| Cancelar | Se vuelve al listado de conflictos de intereses sin añadir el nuevo usuario |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-ACT-C, ETI-ACT-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-ACT-C, ETI-ACT-E |