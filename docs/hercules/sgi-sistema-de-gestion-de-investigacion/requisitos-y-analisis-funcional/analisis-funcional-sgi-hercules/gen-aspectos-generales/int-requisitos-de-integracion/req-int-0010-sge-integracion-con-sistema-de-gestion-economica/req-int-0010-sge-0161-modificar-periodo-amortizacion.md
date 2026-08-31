# REQ-INT-0010-SGE-0161 - Modificar periodo amortización

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0010-SGE-0161 - Modificar periodo amortización** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

Modificar los datos de  un periodo de amortización en el SGE de acuerdo a la edición realizada en el SGI del mismo.

### Descripción técnica integración

Parámetros de entrada:

* Identificador interno del SGI para el periodo de amortización
* Identificación del proyecto SGE
* Referencia de la entidad financiadora
* Identificador del tipo financiación
* Nombre tipo financiación
* Identificador de la fuente de financiación
* Nombre de la fuente de financiación
* Anualidad
* Fecha límite del periodo de amortización
* Importe del periodo de amortización

Parámetros de salida:

* Sin parámetros de salida.

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del Sistema de Gestión Económica y, en concreto, de la Amortización de fondos: [SGI - ESB - SGE - Amortización fondos](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sge/sgi-esb-sge-amortizacion-fondos).

El servicio concreto del API que cubre este requisito es [SGI - ESB - SGE - Amortización fondos - Modificar período amortización](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sge/sgi-esb-sge-amortizacion-fondos/sgi-esb-sge-amortizacion-fondos-periodo-amortizacion-modificar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)