# SGI - ESB - SGEMP - Servicios Pasarela

##### Métodos donde el SGI solo hace de pasarela entre Universidad y el sistema de terceros llamante (No son necesarios para el funcionamiento del SGI)

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGEMP - Empresas - Consultar empresas modificadas](/confluence/spaces/HERCULES/pages/597853241/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+empresas+modificadas) | GET | /empresas/modificadas-ids | q+s  La query estará formada por:   * fechaModificacion | Lista[String] | Listado de los identificadores de empresas que han sufrido cambios en los datos de identificativos de la empresa o en sus datos de contacto. |