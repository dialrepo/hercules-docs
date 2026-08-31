# REQ-INT-0013-SGEPII-0010 - Buscar  detalle de operaciones - Gastos

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0013-SGE-0010 - Buscar detalle de operaciones - Gastos** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Consultar el listado de operaciones de gasto asociadas a las invenciones.

El detalle de campos a recoger de cada operación de gasto asociada a una invención será común a todos ellos y deberá ser configurado en tiempo de implantación, pues esta información debe ser recuperada desde el SGEPII por medio de los mecanismos de integración disponibles.

### Descripción técnica integración

Parámetros de entrada:

* Identificador de la invención en el SGI
* Tipo de operación:
  + Gastos (todos los gastos que se quiere que se visualicen asociados a una invención en el SGI)
  + Gastos a deducir (del total de gastos asociados a la invención, serían aquellos gastos que se han de tener en cuenta para los repartos)

Parámetros de salida:

* Listado de operaciones de gastos, donde para cada una se muestra la siguiente información:
  + Listado de columnas a mostrar de cada gasto. Las columnas serán devueltas por el SGEPII y estarán formadas por dos campos:
    - Id: Indica la columna que es (previamente se llamará a otro método de la API que devuelve el listado de columnas con los valores, id, nombre, acumulable)
    - Valor: Valor a mostrar en dicha columna

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión Económica para la Protección Industrial e Intelectual: [SGI - ESB - SGEPII](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii).

Los servicios del API que cubren este requisito son:

* [SGI - ESB - SGEPII - Buscar columnas gastos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii/sgi-esb-sgepii-buscar-columnas-gastos)
  + Se llamará en primer lugar para obtener las columnas de gastos que se han de presentar por pantalla.
* [SGI - ESB - SGEPII - Buscar gastos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii/sgi-esb-sgepii-buscar-gastos)
  + Se llamará a continuación para obtener los valores correspondientes a cada una de las columnas devueltas por el servicio anterior.

A continuación se detallan los dos casos de cómo sería el flujo de llamadas para la búsqueda de gastos por tipo de operación :

* Buscar **todos los Gastos** que están asociados a una invención :  
  + al servicio de **/gastos** [SGI - ESB - SGEPII - Buscar gastos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii/sgi-esb-sgepii-buscar-gastos) se le debe pasar por parámetro:
    - tipoOperacion = GAS (Ejecución económica - Gastos)
* Buscar **los Gastos "deducibles" de los ingresos** generados por las invenciones, esto es, de entre todos los gastos que están asociados a una invención, los que pueden intervenir en los repartos:  
  + al servicio de **/gastos** [SGI - ESB - SGEPII - Buscar gastos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii/sgi-esb-sgepii-buscar-gastos) se le debe pasar por parámetro:
    - tipoOperacion = REP (Ejecución económica - Repartos - Gastos a deducir)

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)