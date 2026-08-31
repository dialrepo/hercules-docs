# REQ-INT-0020-SGP-0031 - Consultar datos personales de persona

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0020-SGP-0031 - Consultar datos personales de persona** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Obtener el los datos personales de una persona. Dichos datos se mostrarán por ejemplo en el apartado de identificación del CVN del investigador.

### Descripción integración

Parámetros de entrada:

* Referencia de persona (código de identificación de la persona para intercambio de información entre ESB y SGI)

Salida: se devolverá un registro de datos personales de una persona con la siguiente información:

* Fecha de nacimiento
* País de nacimiento
* C. Autón./Reg. de nacimiento
* Ciudad de nacimiento

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Personas y, en concreto, de los Servicios Básicos: [SGI - ESB - SGP - Servicios Básicos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGP - Personas - Consultar datos personales](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos/sgi-esb-sgp-personas-consultar-datos-personales).

### Interfaces relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)