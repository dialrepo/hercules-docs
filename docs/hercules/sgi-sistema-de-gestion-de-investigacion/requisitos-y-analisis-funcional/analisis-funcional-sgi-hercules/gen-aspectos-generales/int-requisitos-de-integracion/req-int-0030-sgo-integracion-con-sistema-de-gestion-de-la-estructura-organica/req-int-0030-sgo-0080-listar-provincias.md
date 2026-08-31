# REQ-INT-0030-SGO-0080 - Listar provincias

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0030-SGO-0080 - Listar provincias** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | ESB (Persona) |

### Definición y objetivos

El SGI requiere la disponibilidad del listado de provincias de una comunidad autónoma para mostrarlas en los módulos del SGI.

### Descripción integración

Parámetros de entrada:

* Identificador de la comunidad autónoma

Parámetros de salida: listado de comunidades autónomas. Para cada elemento se devolverá:

* Identificador
* Nombre
* Identificador de la comunidad autónoma

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de la estructura Orgánica [SGI - ESB - SGO](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGO - Provincias - Buscar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo/sgi-esb-sgo-provincias-buscar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)