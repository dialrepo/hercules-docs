# SGI - ESB - SGE - Ejecución económica - Buscar columnas de datos económicos

|  |  |
| --- | --- |
| Método | GET |
| URL | /ejecucion-economica/columnas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * anualidad * tipoOperacion * reducida * fechaPago * fechaDevengo * fechaContabilizacion   El campo reducida puede tomar los siguientes valores:   * true: sólo se envían las columnas a mostrar en la pantalla principal * false:  se envían todas las columnas (para su exportación)   Si no esta informado el campo reducida se considera false.  El tipoOperacion puede tomar los siguientes valores:   * EPA (Ejecución presupestaria - Estado actual) * EPG (Ejecución presupestaria - Gastos) * EPI (Ejecución presupestaria - Ingresos) * FJF (Facturas y justificantes - Facturas y gastos) * FJV (Facturas y justificantes - Viajes y dietas * FJP (Facturas y justificantes - Personal contratado) * DOG (Detalle de operaciones - Gastos) * DOI (Detalle de operaciones - Ingresos) * DOM (Detalle de operaciones - Modificaciones) |
| Respuesta | Lista[[Columna](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103905017#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-Columna)] |
| Descripción | Listado con las columnas que va a devolver la llamada /ejecucion-economica  Por cada columna se indica un id, nombre, si es una columna acumulable (se va a hacer una suma de ella en el SGI)  Ver el apartado "**Columnas Ejecución económica**" para ver que columnas se deben de mostrar dependiendo del tipo de operación (campo tipoOperacion) y si es reducida o no |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)