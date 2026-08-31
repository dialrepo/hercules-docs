# REQ-INT-0020-SGP-0015 - Listar tipos de documento de identificación personal

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0020-SGP-0015 - Listar tipos de documento de identificación personal** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Recuperación de los tipos de documento de identificación personal utilizados en el sistema de gestión de personas universitario. El listado será utilizado en [IU-GEN-0061- Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0061-solicitar-alta-de-persona). El objetivo de este requisito de integración es alinear la recogida de datos desde el SGI para solicitar el alta de una persona con el sistema de gestión universitario correspondiente donde se materializará el registro.

### Descripción integración

Parámetros de entrada: sin parámetros de entrada.

Parámetros de salida: listado de tipos de documento:

* Identificador del tipo de documento
* Nombre de tipo de documento

El listado devuelto será presentado al usuario, por norma general, en un componente selector (combo).

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Personas y, en concreto, de los Servicios Básicos: [SGI - ESB - SGP - Servicios Básicos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGP - Tipos de documento - Listar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos/sgi-esb-sgp-tipos-de-documento-listar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)