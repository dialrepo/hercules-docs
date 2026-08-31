# IU-GEN-0061- Solicitar alta de persona

|  |  |
| --- | --- |
| Cod. IU | ********IU-GEN**-0061 - Solicitar alta de persona********** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | PENDIENTE |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-ETI-001-Gestor, ACT-PII-001-Gestor, ACT-PRC-003-Gestor, ACT-EER-001-Gestor |
| Frecuencia | Baja |

## Formulario de solicitud de alta de persona

Pantalla que muestra el formulario específico y hecho a medida con los datos necesarios o de interés para llevar a cabo la solicitud de alta de una persona en los sistemas de cada universidad en la que se implante el producto SGI.

Se abrirá en una ventana emergente o popup desde el popup común a todo el SGI de búsqueda de personas [IU-GEN-0060 - Búsqueda de personas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas).

A partir de los datos introducidos se invocará al servicio de integración del ESB [REQ-INT-0020-SGP-0050 - Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0050-solicitar-alta-de-persona) que resolverá la solicitud de alta de persona hacia el sistema o sistemas universitarios que correspondan.

Los formularios de solicitud de alta de personas específicos de cada implantación/universidad tienen en común los permisos y relaciones con interfaces y casos de uso que se incluyen en esta página y, en cuanto a su presentación por pantalla, tendrán un diseño y funcionalidad específica descrita en los apartados correspondientes a la implantación.

Para el caso de la implantación en UM, este formulario se describe en: [IU-GEN-0061-UM - Formulario Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/guia-de-implantacion-checklist/um-universidad-de-murcia/um-formularios-especificos/um-formularios-de-gestion-de-personas-sgper/iu-gen-0061-um-formulario-solicitar-alta-de-persona).

### Interfaces y casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | ESB-PER-C |
| ACT-CSP-004-Administrador | ESB-PER-C |
| ACT-ETI-001-Gestor | ESB-PER-C |
| ACT-PII-001-Gestor | ESB-PER-C |
| ACT-PRC-003-Gestor | ESB-PER-C |
| ACT-EER-001-Gestor | ESB-PER-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ESB-PER-C |