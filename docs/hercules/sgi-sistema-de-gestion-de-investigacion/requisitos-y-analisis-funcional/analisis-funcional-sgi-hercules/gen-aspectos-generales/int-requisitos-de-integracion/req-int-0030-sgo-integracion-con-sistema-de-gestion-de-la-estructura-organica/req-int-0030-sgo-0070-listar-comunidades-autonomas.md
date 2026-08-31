# REQ-INT-0030-SGO-0070 - Listar comunidades autónomas

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0030-SGO-0070 - Listar comunidades autónomas** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | ESB (Persona) |

### Definición y objetivos

El SGI requiere la disponibilidad del listado de comunidades autónomas de un país para mostrarlas en los módulos del SGI.

### Descripción integración

Parámetros de entrada:

* Identificador del país

Parámetros de salida: listado de comunidades autónomas. Para cada elemento se devolverá:

* Identificador
* Nombre
* Identificador del país

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de la estructura Orgánica [SGI - ESB - SGO](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGO - Comunidades autónomas - Buscar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo/sgi-esb-sgo-comunidades-autonomas-buscar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)