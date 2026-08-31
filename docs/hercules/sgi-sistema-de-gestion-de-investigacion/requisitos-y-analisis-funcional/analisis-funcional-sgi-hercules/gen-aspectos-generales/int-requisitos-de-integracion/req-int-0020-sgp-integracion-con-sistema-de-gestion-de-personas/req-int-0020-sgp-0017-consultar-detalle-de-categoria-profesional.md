# REQ-INT-0020-SGP-0017 - Consultar detalle de categoría profesional

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0020-SGP-0017 - Consultar detalle de categoría profesional** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | CSP |

### Definición y objetivos

Recuperación del detalle de una categoría profesional en la universidad. Será necesario por ejemplo para mostrar esta información en pantallas en modo solo lectura donde se presenta como texto simple (label).

### Descripción integración

Parámetros de entrada:

* Identificador de la categoría profesional

Párametros de salida: detalle de la categoría profesional con el identificador pasado como parámetro con los siguientes datos:

* Identificador de la categoría profesional
* Nombre de la categoría profesional

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Personas y, en concreto, de los Servicios Básicos: [SGI - ESB - SGP - Servicios Básicos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGP - Personas - Consultar detalle de categoría profesional](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos/sgi-esb-sgp-personas-consultar-detalle-de-categoria-profesional).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)