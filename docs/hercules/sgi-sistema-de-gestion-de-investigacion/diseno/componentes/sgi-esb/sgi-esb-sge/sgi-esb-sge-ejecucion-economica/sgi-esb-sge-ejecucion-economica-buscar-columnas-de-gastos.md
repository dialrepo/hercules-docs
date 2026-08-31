# SGI - ESB - SGE - Ejecución económica - Buscar columnas de gastos

|  |  |
| --- | --- |
| Método | GET |
| URL | /gastos/columnas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * fecha * id * estado * reducida   Si no esta informado el campo reducida se considera false.  El campo estado puede tomar dos valores:   * Pendiente * Validado   El campo reducida puede tomar los siguientes valores:   * true: sólo se envían las columnas a mostrar en la pantalla principal * false:  se envían todas las columnas (para su exportación) |
| Respuesta | Lista[[Columna](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103905017#SGIESBSGEEjecuci%C3%B3necon%C3%B3mica-Columna)] |
| Descripción | Listado con las columnas que va a devolver la llamada /gastos  Por cada columna se indica un id, nombre, si es una columna acumulable (se va a hacer una suma de ella en el SGI)  Ver el apartado "**Columnas Validación de gastos**" para ver que columnas se deben de mostrar dependiendo de si es reducida o no. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)