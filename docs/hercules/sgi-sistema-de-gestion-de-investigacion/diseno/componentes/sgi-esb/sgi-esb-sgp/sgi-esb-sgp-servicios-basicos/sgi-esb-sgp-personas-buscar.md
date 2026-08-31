# SGI - ESB - SGP - Personas - Buscar

|  |  |
| --- | --- |
| Método | GET |
| URL | /personas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * id * tipoColectivo * colectivoId * nombre * apellidos * email * nombreApellidos |
| Respuesta | Lista[[Persona](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgp#SGIESBSGP-Persona)] |
| Descripción | Listado de Persona.  *Ejemplo*:  colectivoId=in=(refPAS,refPDI);(nombre=like=jim,apellidos=like=jim,email=like=jim,nombreApellidos=like=jim)  colectivoId=in=(refPAS,refPDI);(nombre=like=nombre.apellido@[um.es](http://um.es),apellidos=like=nombre.apellido@[um.es](http://um.es),email=like=nombre.apellido@[um.es](http://um.es),nombreApellidos=like=nombre.apellido@[um.es](http://um.es))  Nota: tipoColetivo y colectivoId son mutuamente excluyentes. En el caso se recibir un tipoColectivo se traducirá a los colectivos que lo formen. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)