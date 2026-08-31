# Añadir acceso a salas.um.es a una nueva unidad de gestión

1.- Vamos al directorio y buscamos el codigo de la unidad en la ulr de alguna persona que trabaje en la misma, por ejemplo, la UCC (Unidad de Cultura Científica):

<https://www.um.es/atica/directorio/?nivel=a003b027c001&usuario=mamenmar.PAS1&lang=0&vista=unidades&search=>

Que tiene el código [a003b027c001](https://www.um.es/atica/directorio/?nivel=a003b027c001&usuario=mamenmar.PAS1&lang=0&vista=unidades&search=).

2.- En Keyclack, en identity provider, seleccionamos CAS y en Mappers, seleccionamos Gruop-Mapper

![](/attachments/1150320670/1150320671.png)

![](/attachments/1150320670/1150320672.png)

en la sección de código "unidades" se crea una nueva, por ejemplo:

var SERVICIO\_DIVULGACION\_CIENTIFICA = 'a003b027c001';

Creamos los roles correspondientes:

ADMINISTRADOR-CSP-UCC

GESTOR-CSP-UCC

VISOR-CSP-UCC

como por ejemplo para el visor:

var ROL\_VISOR\_CSP\_UCC = 'VISOR-CSP-UCC';

Añadimos:

        if (isUnidad(value, UNIDAD\_CULTURA\_CIENTIFICA)) {  
            grp.add(ROL\_VISOR\_CSP\_UCC);  
            grp.add(ROL\_GESTOR\_CSP\_UCC);              
        }

para que todas las personas de la unidad tengan roles gestor y visor. 

           if (isGroupMember(value, VISOR\_CSP\_UCC)) {

                grp.add(ROL\_VISOR\_CSP\_UCC);  
            }

            if (isGroupMember(value, GESTOR\_CSP\_UCC)) {  
                grp.add(ROL\_VISOR\_CSP\_UCC);  
            }            if (isGroupMember(value, ADMINISTRADOR\_CSP\_UCC)) {  
                grp.add(ROL\_VISOR\_CSP\_UCC);  
            }

y creamos, en grupos.um.es, los grupos correspondientes grupos. En este caso, hemos dejado en grupos.um.es el seleccionar quien pertenecerá al grupo administradores y hemos asignado por defecto el rol gestor y visor a todas la spersonal de la unidad.