# SGI - ESB - SGEPII - Buscar columnas de ingresos

|  |  |
| --- | --- |
| Método | GET |
| URL | /ingresos-invencion/columnas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId |
| Respuesta | Lista[[Columna](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgepii#SGIESBSGEPII-Columna)] |
| Descripción | Listado con las columnas que va a devolver la llamada /ingresos-invencion.  El identificador de proyecto a enviar al SGE ha de ser el del proyecto económico en Justo.  Por cada columna se indica un id, nombre, si es una columna acumulable (se puede manejar como un importe y hacer operaciones numéricas con ella en el SGI).  Por defecto, devolverá las siguientes columnas:   * Fecha * Referencia * Importe (acumulable = Sí) * Nº interno de contrato * Entidad pagadora |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)