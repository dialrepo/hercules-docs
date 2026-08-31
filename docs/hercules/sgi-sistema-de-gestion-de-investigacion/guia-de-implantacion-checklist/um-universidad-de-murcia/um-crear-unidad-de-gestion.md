# UM - Crear unidad de gestión

Sirva como guía en la creación de nuevas unidades de gestión.

Pasos a seguir:

1) En primer lugar hay que añadir, en la bbdd, tanto en el esquema USR  los valores correspondientes: USR\_SGI.UNIDAD (secuencia UNIDAD\_SEQ)

La sentencia SQL es:

INSERT INTO USR\_SGI.UNIDAD VALUES (UNIDAD\_SEQ.NEXTVAL, NULL, NULL, NULL, NULL, 'UCC', 1, 'Unidad de Cultura Cientifica', 'UCC');

donde UCC es un ejemplo del acrónimo de la Unidad  y "Unidad de Cultura Cientifica" la descripción del nombre de la unidad.

Una vez hecho el insert, guardar el número que se ha obtenido para esa unidad con: UNIDAD\_SEQ.NEXTVAL porque será necesario luego, en el Keycloack para generar los roles.

2) en salas, en CSP, Configuración, asociar al modelo de ejecución que se quiera usar, la unidad de gestión que se acaba de crear.

![](/attachments/857473189/1150320652.png)

Si el modelo de ejecución no existe, habrá que crearlo y eso hay que trasladarlo al equipo de gestión económica para que estos nuevos modelos se mapeen a justo.

3) En la url

salas.um.es/auth/ (salas.um.es en el caso de Murcia) en:

![](/attachments/857473189/1150320657.png)

Crear nuevo grupo en Keycloak: ADMINISTRADOR-CSP-XXX/GESTOR-CSP-XXX/VISOR-CSP-XXX

![](/attachments/857473189/857473193.png)

3) Crear los roles con el valor de X obtenido en el paso 1 en la secuencia generada en el insert.

En el keycloack, en la opción de menu Roles:

![](/attachments/857473189/1150320661.png)

añadimos todos los roles correspondientes que son:.

CSP-ME-E\_X  
CSP-ME-R\_X       
CSP-SJUS-V\_X  
CSP-SOL-B\_X   
CSP-CON-B\_X   
CSP-PRO-V\_X   
CSP-EJEC-V\_X   
CSP-ME-B\_X   
CSP-ME-C\_X   
CSP-CON-V\_X  
CSP-EJEC-E\_X       
CSP-PRO-R\_X       
CSP-SJUS-E\_X   
CSP-CON-C\_X   
CSP-PRO-B\_X  
CSP-CON-R\_X   
CSP-CON-E\_X   
CSP-ME-V\_X      
CSP-PRO-C\_X  
CSP-PRO-E\_X  
CSP-SOL-C\_X  
CSP-SOL-E\_X  
CSP-SOL-R\_X  
CSP-SOL-V\_X

Sustituyendo la X por el número obtenido en la secuencia.

Estos roles deben crearse nuevos para cada unidad. Tener en cuenta que el número final se corresponde al identificador de la tabla USR\_SGI.UNIDAD (el 4 por ejemplo es ARI)

4) Modificar el group-mapper, asignando el grupo creado (ADMINISTRADOR-CSP-XXX/GESTOR-CSP-XXX/VISOR-CSP-XXX) a los usuarios para los que el CAS devuelva el código de unidad correspondiente.

Esto se hace de forma automática a traves del fichero de roles que se exporta aqui:

![](/attachments/857473189/1150320664.png)

Se modifica a mano el mismo copiando los realm\_roles de algún grupo similar y pegándolos en los grupos administrador, gestor y visor de la nueva unidad que hemos creado.

Por ejemplo, para VISOR-CSP- , hemos copiado los realm\_roles de VISOR-CSP-OTRI

 "id": "ee921734-ec9b-42bf-a9db-d2dd7f7cd9e3",  
      "name": "VISOR-CSP-UCC",  
      "path": "/VISOR-CSP-UCC",  
      "attributes": {},  
      "realmRoles": [  
        "ETI-CHKLST-MOD-V",  
        "CSP-SJUS-V\_21",  
        "CSP-PRO-V\_21",  
        "PII-INV-MOD-V",  
        "REL-V",  
        "CSP-SOL-V\_21",  
        "CSP-AUT-V",  
        "CSP-EJEC-V\_21",  
        "CSP-CON-V\_21",  
        "ESB-EMP-V",  
        "CSP-CVPR-V"  
      ],  
      "clientRoles": {},  
      "subGroups": []

y los pegamos en el mismo fichero, en la parte de realmRoles de VISOR-CSP-UCC.

A continuación, grabamos el fichero y lo importamos en el keycloak en la sección importación con los siguientes valores en las distintas opciones:

![](/attachments/857473189/1150320666.png)

PAra comprobar que lo ha hecho bien, nos vamos a:

![](/attachments/857473189/1150320668.png)

Donde podemos ver que ya tiene roles asignados ese nuevo grupo.

5) Comprobar que aparece la nueva unidad en las búsquedas:

![](/attachments/857473189/857473197.png)