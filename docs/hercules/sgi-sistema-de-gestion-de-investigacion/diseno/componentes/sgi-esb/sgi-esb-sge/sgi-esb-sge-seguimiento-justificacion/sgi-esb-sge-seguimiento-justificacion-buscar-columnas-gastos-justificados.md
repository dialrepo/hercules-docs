# SGI - ESB - SGE - Seguimiento justificación - Buscar columnas gastos justificados

| Método | GET |
| --- | --- |
| URL | /seguimiento-justificacion/columnas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * justificacionId * numRegistroProveedor * importeJustificado * fechaDevengo * fechaPago * id (se pasará un listado de id de gastos que se quieren buscar) |
| Respuesta | Lista[[Columna](https://confluence.um.es/confluence/pages/viewpage.action?pageId=140641365#SGIESBSGESeguimientojustificaci%C3%B3n-Columna)] |
| Descripción | Listado con las columnas que va a devolver la llamada /seguimiento-justificacion  Por cada columna se indica un id, nombre, si es una columna acumulable (se va a hacer una suma de ella en el SGI)  Ver el apartado "**Columnas Seguimiento Justificación**" para ver que columnas se deben de mostrar. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)