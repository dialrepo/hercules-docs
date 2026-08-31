# SGI - ESB - SGO - Áreas de conocimiento - Buscar

|  |  |
| --- | --- |
| Método | GET |
| URL | /areas-conocimiento |
| Parámetros | q+s (query + sort)  La query estará formada por:   * padreId |
| Respuesta | Lista[[AreaConocimiento](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-AreaConocimiento)] |
| Descripción | Listado de áreas de conocimiento.  Nota: en el caso de no recibirse un padreId en la query, se devolverán todas las áreas de conocimiento y en caso de indicarse en la query que se quieren solo las que tengan un padreId con valor "null" se devolverán únicamente las de primer nivel o nivel raíz.  *Ejemplo de query para obtener solo áreas de conocimiento raíz (su padre es null)*:  padreId=na= |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)