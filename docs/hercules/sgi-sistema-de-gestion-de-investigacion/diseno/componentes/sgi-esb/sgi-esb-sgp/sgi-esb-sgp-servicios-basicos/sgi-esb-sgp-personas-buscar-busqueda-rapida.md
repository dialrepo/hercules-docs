# SGI - ESB - SGP - Personas - Buscar (Búsqueda rápida)

|  |  |
| --- | --- |
| Método | GET |
| URL | /personasFast |
| Parámetros | * busqueda (cadena a buscar en nombre / apellidos / email / nombre + apellidos). * colectivoId (uno o varios colectivos sobre los que realizar la búsqueda). |
| Respuesta | Lista[[Persona](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp#SGIESBSGP-Persona)] |
| Descripción | Listado de Persona.  *Ejemplo*:  [mailto:busqueda=skarmeta@[um.es](http://um.es)&colectivoId=]busqueda=skarmeta@[um.es](http://um.es)&colectivoId=(1,2,3,4)  busqueda=jorge carrillo&colectivoId=(2)  **NOTA**:  La búsqueda no es sensible a mayúsculas ni minúsculas. Los parámetros no deben ir entrecomillados.  Si no se indica el parámetro colectivoId, se buscará en todos los colectivos.  Se devuelven como máximo 11 registros, al devolver más de 10 registros el buscador indicará que existen más registros y se puede refinar la búsqueda. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)