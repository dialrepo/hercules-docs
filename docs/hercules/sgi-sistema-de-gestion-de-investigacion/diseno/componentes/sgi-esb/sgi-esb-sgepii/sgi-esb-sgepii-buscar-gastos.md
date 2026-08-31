# SGI - ESB - SGEPII - Buscar gastos

|  |  |
| --- | --- |
| Método | GET |
| URL | /gastos-invencion |
| Parámetros | q+s (query + sort)  La query estará formada por:   * invencionId * tipoOperacion   El tipo de operación puede tomar los siguientes valores:   * GAS (Ejecución económica - Gastos) * REP (Ejecución económica - Repartos - Gastos a deducir) |
| Respuesta | Lista[[DatoEconomico](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii#SGIESBSGEPII-DatoEconomico)] |
| Descripción | Listado de todos los gastos asociados a una invención.  Para cada gasto se devolverán los siguientes datos:   * Identificador del gasto * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /gastos-invencion/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables, esto es, se puedan manejar como un importe y hacer operaciones numéricas con ella en el SGI, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto).   Si el tipo de operación se informa con el valor GAS, se han de devolver todos los gastos asociados a la invención.  Si por el contrario el tipo de operación es REP, se han de devolver del conjunto de gastos asociados a la invención únicamente aquellos que se deban tener en cuenta para el reparto de regalías. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)