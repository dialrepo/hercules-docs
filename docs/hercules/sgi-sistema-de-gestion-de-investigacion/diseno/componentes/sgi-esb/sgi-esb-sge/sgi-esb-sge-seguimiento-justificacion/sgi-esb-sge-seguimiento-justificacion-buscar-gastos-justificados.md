# SGI - ESB - SGE - Seguimiento justificación - Buscar gastos justificados

| Método | GET |
| --- | --- |
| URL | /seguimiento-justificacion |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * justificacionId * numRegistroProveedor * importeJustificado * fechaDevengo * fechaPago * id (se pasará un listado de id de gastos que se quieren buscar) |
| Respuesta | Lista[[GastoJustificado](https://confluence.um.es/confluence/pages/viewpage.action?pageId=140641365#SGIESBSGESeguimientojustificaci%C3%B3n-GastoJustificado)] |
| Descripción | Listado con los gastos. Por cada gasto se devolverán los siguientes campos:   * Identificador del gasto * Identificador del proyecto SGE * Identificador justificación (del SGE) * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /seguimiento-justificacion/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables,se tenga que hacer sumas sobre ellas, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto)).   Los gastos devueltos estarán ordenados por identificador del periodo de justificación y por fecha devengo.  Ver el apartado "**Columnas Seguimiento Justificación**" para ver los id de la columnas que se deben de mostrar. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)