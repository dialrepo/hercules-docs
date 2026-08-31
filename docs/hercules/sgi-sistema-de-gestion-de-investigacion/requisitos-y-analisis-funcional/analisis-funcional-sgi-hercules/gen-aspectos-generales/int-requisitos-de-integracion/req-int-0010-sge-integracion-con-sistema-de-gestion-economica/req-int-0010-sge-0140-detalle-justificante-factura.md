# REQ-INT-0010-SGE-0140 - Detalle justificante-factura

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0010-SGE-0140 - Detalle justificante-factura** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Detalle de todos los campos de un justificante/factura, proporcionado por el SGE. Los campos devueltos serán una listado de campos formado por nombre - valor, donde nombre será el nombre del campo a mostrar y el valor, el propio valor del campo.

### Descripción técnica integración

Parámetros de entrada:

* Identificador gasto
* Tipo operación

Parámetros de salida:

* Identificador del dato económico
* Identificador del proyecto SGE
* Anualidad
* Partida presupuestaria
* Fecha devengo
* Clasificación SGE
* Código económico
* Listado de campos con su nombre y valor
* Listado de documentos (identificador, nombre del documento y nombre del fichero, sin el contenido)

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión Económica y, en concreto, de la Ejecución económica de proyectos: [SGI - ESB - SGE - Ejecución económica](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sge/sgi-esb-sge-ejecucion-economica).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGE - Ejecución económica - Consultar detalle de dato económico](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sge/sgi-esb-sge-ejecucion-economica/sgi-esb-sge-ejecucion-economica-consultar-detalle-de-dato-economico) pasando el identificador del justificante/factura y como parámetro:

* tipoOperacion == "FJF"

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)