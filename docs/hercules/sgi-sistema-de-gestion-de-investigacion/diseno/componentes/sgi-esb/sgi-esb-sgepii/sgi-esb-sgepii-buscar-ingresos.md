# SGI - ESB - SGEPII - Buscar ingresos

|  |  |
| --- | --- |
| Método | GET |
| URL | /ingresos-invencion |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId |
| Respuesta | Lista[[DatoEconomico](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii#SGIESBSGEPII-DatoEconomico)] |
| Descripción | Listado de todos los ingresos asociados a una invención. La asociación en el SGI se realizará a través de contratos de CSP (proyectos) y el identificador de proyecto a enviar al SGE ha de ser el del proyecto económico en Justo.  Los ingresos devueltos se corresponderán con las facturas emitidas asociadas a la invención a través del contrato.  Para cada ingreso se devolverán los siguientes datos:   * Identificador del ingreso * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /ingresos-pii/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables, esto es, se puedan manejar como un importe y hacer operaciones numéricas con ella en el SGI, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto). |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)