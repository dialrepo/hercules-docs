# REQ-INT-0020-SGP-0010 - Listar colectivos SGI

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0020-SGP-0010 - Listar colectivos SGI** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Recuperar colectivos de personal de la Universidad que pueden ejercer como miembros de los equipos de proyecto o trabajo de los proyectos/contratos del SGI ([IU-CSP-0100 - Gestión de roles de equipo de proyecto](/confluence/pages/createpage.action?spaceKey=HERCULES&title=_noimplementado_sinactualizar_IU-CSP-0100+-+Gesti%C3%B3n+de+roles+de+equipo+de+proyecto&linkCreation=true&fromPageId=597853185)).

Los roles de los equipos de proyecto serán configurables para cada implantación del SGI. Para cada uno de los roles se debe de especificar a qué colectivos del personal universitario va a estar vinculado. Ver  [CSP - Solicitudes - Gestión de roles de equipo de proyecto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-solicitudes#CSPSolicitudes-Solicitudes-rol_equipoGesti%C3%B3ndeTiposderoldeproyecto).

El ESB-SGP proporcionará al SGI el listado de colectivos. La obtención de este listado de colectivos podrá:

* Provenir de los servicios de integración proporcionados por algún sistema corporativo universitario.
* Estar simplemente recogida como un listado en el ESB que se defina en el periodo de implantación del SGI.

### Descripción integración

Parámetros de entrada: sin parámetros de entrada.

Parámetros de salida: listado de colectivos vigentes:

* Identificador del colectivo
* Nombre de colectivo

El listado devuelto será presentado al usuario, por norma general, en un componente selector (combo).

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Personas y, en concreto, de los Servicios Básicos: [SGI - ESB - SGP - Servicios Básicos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGP - Colectivos - Listar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos/sgi-esb-sgp-colectivos-listar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)