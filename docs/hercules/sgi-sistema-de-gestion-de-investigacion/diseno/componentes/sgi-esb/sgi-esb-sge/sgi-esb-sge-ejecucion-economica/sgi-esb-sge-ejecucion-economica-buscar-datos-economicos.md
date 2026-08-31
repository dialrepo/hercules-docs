# SGI - ESB - SGE - Ejecución económica - Buscar datos económicos

|  |  |
| --- | --- |
| Método | GET |
| URL | /ejecucion-economica |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * anualidad * tipoOperacion * reducida * fechaPago * fechaDevengo * fechaContabilizacion   El campo reducida puede tomar los siguientes valores:   * true: sólo se envían las columnas a mostrar en la pantalla principal * false:  se envían todas las columnas (para su exportación)   Si no esta informado el campo reducida se considera false.  El tipoOperacion puede tomar los siguientes valores:   * EPA (Ejecución presupestaria - Estado actual) * EPG (Ejecución presupestaria - Gastos) * EPI (Ejecución presupestaria - Ingresos) * FJF (Facturas y justificantes - Facturas y gastos) * FJV (Facturas y justificantes - Viajes y dietas * FJP (Facturas y justificantes - Personal contratado) * DOG (Detalle de operaciones - Gastos) * DOI (Detalle de operaciones - Ingresos) * DOM (Detalle de operaciones - Modificaciones) |
| Respuesta | Lista[[DatoEconomico](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103905017#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-DatoEconomico)] |
| Descripción | Listado con los datos económicos pedidos según el campo tipoOperacion. Por cada dato económico se devolverán los siguientes campos:   * Identificador del dato económico * Identificador del proyecto SGE * Anualidad * Partida presupuestaria * Fecha de devengo * Clasificación SGE * Código económico * Tipo (si es Gasto o Ingreso) * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /ejecucion-economica/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables,se tenga que hacer sumas sobre ellas, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto)). Ver el apartado "**Columnas Ejecución económica**" para ver los id de la columnas que se deben de mostrar dependiendo del tipo de operación (campo tipoOperacion) y si es reducida o no. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)