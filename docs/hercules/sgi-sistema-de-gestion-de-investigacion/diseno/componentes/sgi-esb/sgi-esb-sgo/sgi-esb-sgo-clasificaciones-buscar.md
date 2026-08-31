# SGI - ESB - SGO - Clasificaciones - Buscar

|  |  |
| --- | --- |
| Método | GET |
| URL | /clasificaciones |
| Parámetros | q+s (query + sort)  La query estará formada por:   * tipoClasificacion * padreId |
| Respuesta | Lista[[Clasificacion](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Clasificacion)] |
| Descripción | Listado de clasificaciones.  Nota: en el caso de no recibirse un padreId en la query, se devolverán todas las clasificaciones y en caso de indicarse en la query que se quieren solo las que tengan un padreId con valor "null" se devolverán únicamente las de primer nivel o nivel raíz. Sobre estas clasificaciones se aplicará además el filtro indicado en tipoClasificacion (en caso de venir informado).  *Ejemplo de query para obtener sólo las clasificaciones raíz (su padre es null) del tipo de clasificación "Sectores Industriales"*:  tipoClasificacion==(SECTORES\_INDUSTRIALES);padreId=na= |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)