# REQ-INT-0030-SGO-0090 - Dar de alta palabra clave

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0030-SGO-0090 - Dar de alta palabra clave** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | CSP, PII |

### Definición y objetivos

El ESB proporcionará el interface de integración para que desde el SGI se puedan dar de alta palabras clave desde cualquier otro módulo. Al estar encapsulada dentro del Bus de integración, esta funcionalidad podría ser adaptada por implantación de forma que se comunicase con un sistema externo, que pueden ser los propios sistemas de la Universidad, como puede ser un tesauro propio u otros diccionarios de palabras clave.

### Descripción integración

Parámetros de entrada:

* Lista de palabras clave.

Parámetros de salida: sin parámetros de salida.

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de la estructura Orgánica [SGI - ESB - SGO](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGO - Palabras clave - Crear](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo/sgi-esb-sgo-palabras-clave-crear).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)