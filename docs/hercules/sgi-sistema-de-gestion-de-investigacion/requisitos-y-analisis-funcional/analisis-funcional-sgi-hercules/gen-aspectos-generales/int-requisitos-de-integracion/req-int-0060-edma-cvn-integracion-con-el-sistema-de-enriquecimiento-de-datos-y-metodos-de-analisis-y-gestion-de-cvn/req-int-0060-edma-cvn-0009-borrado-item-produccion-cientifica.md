# REQ-INT-0060-EDMA-CVN-0009 - Borrado item producción científica

|  |  |
| --- | --- |
| Cod. REQ | **REQ-INT-0060-EDMA-CVN-0007 - Borrado item producción científica** |
| Ver. Objetivo |  |
| Ver. REQ | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |
| Características |  |
| M. Consumidor |  |

### Definición y objetivos

El SGI deberá disponer de una función que permita al módulo de CVN (parte del sistema EDMA) enviar a eliminar en el módulo de Producción científica un item eliminado en el  módulo de CVN.

### Descripción integración

Parámetros de entrada:

* Identificador del item de producción científica en el módulo CVN

Parámetros de salida:

* No tiene

### Diseño técnico

En el siguiente enlace se muestra el diseño del modelo lógico y el diseño de la API del SGI para la gestión de la producción científica [ESB - SGI - Producción Científica](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/esb-sgi/esb-sgi-produccion-cientifica).

El servicio concreto del API que cubre este requisito es [ESB - SGI - Producción científica - Eliminar](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/esb-sgi/esb-sgi-produccion-cientifica/esb-sgi-produccion-cientifica-eliminar).

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Informes relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)