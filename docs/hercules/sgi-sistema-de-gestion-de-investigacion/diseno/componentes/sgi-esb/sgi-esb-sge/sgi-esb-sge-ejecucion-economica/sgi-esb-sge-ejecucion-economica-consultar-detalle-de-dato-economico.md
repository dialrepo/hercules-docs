# SGI - ESB - SGE - Ejecución económica - Consultar detalle de dato económico

|  |  |
| --- | --- |
| Método | GET |
| URL | /ejecucion-economica/{id} |
| Parámetros | tipoOperacion  El tipoOperacion puede tomar los siguientes valores (cuando estamos en la llamada de detalle de dato económico):   * FJF (Facturas y justificantes - Facturas y gastos) * FJV (Facturas y justificantes - Viajes y dietas * FJP (Facturas y justificantes - Personal contratado) |
| Respuesta | [DatoEconomicoDetalle](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103905017#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-DatoEconomicoDetalle) |
| Descripción | Detalle del dato económico con todas sus columnas.   * Identificador del dato económico * Identificador del proyecto SGE * Anualidad * Partida presupuestaria * Fecha de devengo * Clasificación SGE * Código económico * Listado de campos con su nombre y valor (Ver el apartado "**Campos Detalle dato económico**" para ver que campos se deben de mostrar dependiendo del tipo de operación (campo tipoOperacion). En el detalle se muestran todos la columnas o campos.) * Listado de documentos (identificador, nombre del documento y nombre del fichero, sin el contenido)   El listado de campos a mostrar dependerá de que dato económico sea, si es una factura o gasto, un viaje o dieta o un personal contratado. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)