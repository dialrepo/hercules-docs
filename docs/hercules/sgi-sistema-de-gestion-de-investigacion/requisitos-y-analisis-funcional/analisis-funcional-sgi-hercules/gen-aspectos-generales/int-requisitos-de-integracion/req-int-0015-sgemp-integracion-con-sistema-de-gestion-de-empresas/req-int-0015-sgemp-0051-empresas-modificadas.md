# REQ-INT-0015-SGEMP-0051 - Empresas modificadas

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0015-SGEMP-0051 - Empresas modificadas** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

El ESB deberá de disponer de una función que permita consultar las empresas que han sufrido cambios en los datos identificativos de la empresa o en sus datos de contacto a partir de la fecha de modificación pasada por parámetro.

### Descripción integración

Parámetros de entrada:

* Fecha modificación: Es la fecha que se debe considerar para filtrar las empresas a remitir

Parámetros de salida:

* Listado de Identificadores de empresas

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Empresas y, en concreto, de los Servicios Pasarela: [SGI - ESB - SGEMP - Servicios Pasarela](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp/sgi-esb-sgemp-servicios-pasarela).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGEMP - Empresas - Consultar empresas modificadas](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp/sgi-esb-sgemp-servicios-pasarela/sgi-esb-sgemp-empresas-consultar-empresas-modificadas).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)