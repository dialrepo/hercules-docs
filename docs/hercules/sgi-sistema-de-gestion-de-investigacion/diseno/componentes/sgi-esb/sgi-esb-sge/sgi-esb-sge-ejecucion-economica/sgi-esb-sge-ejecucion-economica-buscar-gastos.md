# SGI - ESB - SGE - Ejecución económica - Buscar gastos

|  |  |
| --- | --- |
| Método | GET |
| URL | /gastos |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * fecha * id * estado * reducida   El campo estado puede tomar dos valores:   * Pendiente * Validado   El campo reducida puede tomar los siguientes valores:   * true: sólo se envían las columnas a mostrar en la pantalla principal * false:  se envían todas las columnas (para su exportación)   Si no esta informado el campo reducida se considera false. |
| Respuesta | Lista[[DatoEconomico](https://confluence.um.es/confluence/pages/viewpage.action?pageId=141920117#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-DatoEconomico)] |
| Descripción | Listado de gastos pendientes de pasar por la "Validación de gastos" si en el campo del filtrado estado = 'Pendiente' o listado de gastos que ya han sido validados (han pasado por la "Validación de gastos") si en el campo del filtrado estado = 'Validado'  Para cada gasto se devolverán los siguientes datos:   * Identificador del gasto * Identificador del proyecto SGE * Partida presupuestaria a la que esta asignado el gasto * Fecha de devengo * Clasificación SGE * Código económico asignado al gasto * Anualidad * Tipo: Gasto * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /gastos/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables,se tenga que hacer sumas sobre ellas, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto)). Ver el apartado "**Columnas Validación de gastos**" para ver los id de la columnas que se deben de mostrar dependiendo de si es reducida o no |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)