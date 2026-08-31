# REQ-INT-0020-SGP-0016 - Listar categorías profesionales

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0020-SGP-0016 - Listar categorías profesionales** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Recuperación de las categorías profesionales utilizadas en la universidad para clasificar a una persona. La categoría profesional junto a los datos de subcategoria profesional, departamento, área de conocimiento y  empresa sirven para ubicar a la persona en la universidad. El listado será utilizado en [IU-GEN-0061- Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0061-solicitar-alta-de-persona). El objetivo de este requisito de integración es alinear la recogida de datos desde el SGI para solicitar el alta de una persona con el sistema de gestión universitario correspondiente donde se materializará el registro.

### Descripción integración

Parámetros de entrada: sin parámetros de entrada.

Párametros de salida: listado de tipos de categorías profesionales:

* Identificador de la categoría
* Nombre de la categoría

El listado devuelto será presentado al usuario, por norma general, en un componente selector (combo).

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Personas y, en concreto, de los Servicios Básicos: [SGI - ESB - SGP - Servicios Básicos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGP - Categorías profesionales - Listar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp/sgi-esb-sgp-servicios-basicos/sgi-esb-sgp-categorias-profesionales-listar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)