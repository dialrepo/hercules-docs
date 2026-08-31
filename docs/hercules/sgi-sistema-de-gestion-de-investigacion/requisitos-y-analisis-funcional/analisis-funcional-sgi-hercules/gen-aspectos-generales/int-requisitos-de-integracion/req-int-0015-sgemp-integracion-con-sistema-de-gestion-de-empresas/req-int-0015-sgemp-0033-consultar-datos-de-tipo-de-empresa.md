# REQ-INT-0015-SGEMP-0033 - Consultar datos de tipo de empresa

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0015-SGEMP-0033 - Consultar datos de tipo de empresa** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor | CSP, ESB (Empresa) |

### Definición y objetivos

Obtener los datos de una empresa relacionados con su tipología de empresa (en función de su tamaño por ejemplo) a partir de su identificador de referencia en el SGI. El ESB recibirá del SGI la solicitud de información de tipología de una determinada empresa. El ESB a través de la referencia de la empresa derivará la solicitud al sistema universitario correspondiente.

### Descripción técnica integración

Parámetro de entrada: referencia de empresa (identificador de referencia entre SGI y ESB).

Salida: se devolverá un registro de un tipo de empresa de la empresa con la siguiente información:

* Tipo empresa (PYME, Microempresa, ...). Habría de ser uno de los tipos devueltos a través de la llamada al sistema universitario que corresponda usando el requisito de integración REQ-INT-0015-SGEMP-0010 - Listar tipos de empresa.

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión de Empresas: [SGI - ESB - SGEMP](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)