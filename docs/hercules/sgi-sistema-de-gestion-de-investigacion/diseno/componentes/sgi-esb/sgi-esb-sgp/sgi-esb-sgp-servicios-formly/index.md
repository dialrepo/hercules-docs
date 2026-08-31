# SGI - ESB - SGP - Servicios Formly

##### Métodos únicamente necesarios si se requiere gestionar personas desde el SGI (Alta, Baja, Modificación y Detalle).

---

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGP - Personas - Consultar detalle](/confluence/spaces/HERCULES/pages/597853037/SGI+-+ESB+-+SGP+-+Personas+-+Consultar+detalle) | GET | /personas/formly/{id} |  | JSON | Devuelve los datos a pintar en el formulario de Ver Detalle/Actualizar en el SGI (formly). |
| [SGI - ESB - SGP - Personas - Consultar campos ver detalle](/confluence/spaces/HERCULES/pages/597853040/SGI+-+ESB+-+SGP+-+Personas+-+Consultar+campos+ver+detalle) | GET | /personas/formly/view |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de ver detalle de persona. |
| [SGI - ESB - SGP - Personas - Modificar](/confluence/spaces/HERCULES/pages/597853042/SGI+-+ESB+-+SGP+-+Personas+-+Modificar) | PUT | /personas | JSON |  | Recibe como parámetro la respuesta del usuario del formulario de datos de modificación (formly) con los campos necesarios para actualizar una persona. |
| [SGI - ESB - SGP - Personas - Consultar campos modificación](/confluence/spaces/HERCULES/pages/597853039/SGI+-+ESB+-+SGP+-+Personas+-+Consultar+campos+modificaci%C3%B3n) | GET | /personas/formly/update |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar modificar persona. |
| [SGI - ESB - SGP - Personas - Dar de alta](/confluence/spaces/HERCULES/pages/597853041/SGI+-+ESB+-+SGP+-+Personas+-+Dar+de+alta) | POST | /personas | JSON | id  Vendrá relleno si la creación es síncrona y no vendrá si es asíncrona. | Recibe como parámetro la respuesta del usuario del formulario de datos de alta (formly) con los campos necesarios para crear una persona. |
| [SGI - ESB - SGP - Personas - Consultar campos alta](/confluence/spaces/HERCULES/pages/597853038/SGI+-+ESB+-+SGP+-+Personas+-+Consultar+campos+alta) | GET | /personas/formly/create |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar alta persona. Ver  [IU-GEN-0061- Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0061-solicitar-alta-de-persona). |