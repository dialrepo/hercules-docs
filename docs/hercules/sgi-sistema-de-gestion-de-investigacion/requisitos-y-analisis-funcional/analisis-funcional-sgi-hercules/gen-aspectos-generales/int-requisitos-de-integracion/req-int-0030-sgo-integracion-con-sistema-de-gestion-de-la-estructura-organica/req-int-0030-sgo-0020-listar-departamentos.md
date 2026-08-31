# REQ-INT-0030-SGO-0020 - Listar departamentos

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0030-SGO-0020 - Listar departamentos** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | ESB (Persona), PRC |

### Definición y objetivos

El SGI requiere la disponibilidad del listado de departamentos. Este listado deberá ser obtenido del sistema de gestión universitario correspondiente.

### Descripción integración

Parámetros de entrada: La solicitud no requiere parámetros de entrada.

Parámetros de salida: listado de departamentos. Para cada elemento se devolverá:

* Identificador
* Nombre

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de la estructura Orgánica [SGI - ESB - SGO](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGO - Departamentos - Listar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo/sgi-esb-sgo-departamentos-listar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)