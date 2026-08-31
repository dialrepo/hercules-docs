# SGI - ESB - SGE - Ejecución económica - Consultar detalle de gasto

|  |  |
| --- | --- |
| Método | GET |
| URL | /gastos/{id} |
| Parámetros |  |
| Respuesta | [DatoEconomicoDetalle](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103905017#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-DatoEconomicoDetalle) |
| Descripción | Detalle de un gasto.  Para cada gasto se devolverán los siguientes datos:   * Identificador del gasto * Identificador del proyecto SGE * Partida presupuestaria a la que esta asignado el gasto * Fecha de devengo * Clasificación SGE * Código económico asignado al gasto * Anualidad * Listado de campos con su nombre y valor (Ver el apartado "**Campos Detalle dato económico**" para ver que campos se deben de mostrar dependiendo del tipo de operación (campo tipoOperacion). En el detalle se muestran todos la columnas o campos.) * Listado de documentos (identificador, nombre del documento y nombre del fichero, sin el contenido) |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)