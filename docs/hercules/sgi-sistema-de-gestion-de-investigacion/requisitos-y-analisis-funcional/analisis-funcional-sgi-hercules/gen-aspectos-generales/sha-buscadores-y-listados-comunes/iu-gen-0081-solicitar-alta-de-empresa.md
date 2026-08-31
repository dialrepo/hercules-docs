# IU-GEN-0081 - Solicitar alta de empresa

|  |  |
| --- | --- |
| Cod. IU | ********IU-GEN**-0081 - Solicitar alta de empresa********** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-PII-001-Gestor, ACT-EER-001-Gestor |
| Frecuencia | Baja |

## Formulario Solicitar alta de empresa

Pantalla que muestra el formulario específico y hecho a medida con los datos necesarios o de interés para llevar a cabo la solicitud de alta de una empresa en los sistemas de cada universidad en la que se implante el producto SGI.

Se abrirá en una ventana emergente o popup desde el popup común a todo el SGI de búsqueda de empresas [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas).

A partir de los datos introducidos se invocará al servicio de integración del ESB [REQ-INT-0015-SGEMP-0040 - Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0040-solicitar-alta-de-empresa) que resolverá la solicitud de alta de persona hacia el sistema o sistemas universitarios que correspondan.

Los formularios de solicitud de alta de empresas específicos de cada implantación/universidad tienen en común los permisos y relaciones con interfaces y casos de uso que se incluyen en esta página y, en cuanto a su presentación por pantalla, tendrán un diseño y funcionalidad específica descrita en los apartados correspondientes a la implantación.

Para el caso de la implantación en UM, este formulario se describe en: [IU-GEN-0081-UM - Formulario Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/guia-de-implantacion-checklist/um-universidad-de-murcia/um-formularios-especificos/um-formularios-de-gestion-de-empresas-sgemp/iu-gen-0081-um-formulario-solicitar-alta-de-empresa).

### Interfaces de usuario  y casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | ESB-EMP-C |
| ACT-CSP-004-Administrador | ESB-EMP-C |
| ACT-PII-001-Gestor | ESB-EMP-C |
| ACT-EER-001-Gestor | ESB-EMP-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ESB-EMP-C |