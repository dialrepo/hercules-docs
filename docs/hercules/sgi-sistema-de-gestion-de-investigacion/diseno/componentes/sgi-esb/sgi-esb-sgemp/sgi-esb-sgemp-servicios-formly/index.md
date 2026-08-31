# SGI - ESB - SGEMP - Servicios Formly

##### Métodos únicamente necesarios si se requiere gestionar empresas desde el SGI (Alta, Baja, Modificación y Detalle).

---

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGEMP - Empresas - Consultar campos ver detalle](/confluence/spaces/HERCULES/pages/597853362/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+ver+detalle) | GET | /empresas/formly/view |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de ver detalle de empresa. |
| [SGI - ESB - SGEMP - Empresas - Consultar campos modificación](/confluence/spaces/HERCULES/pages/597853359/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+modificaci%C3%B3n) | GET | /empresas/formly/update |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar modificación empresa, pestaña "Datos generales". Ver IU-GEN-0082 - Ver detalle - Solicitar modificación de empresa. |
| [SGI - ESB - SGEMP - Empresas - Consultar detalle](/confluence/spaces/HERCULES/pages/597853025/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+detalle) | GET | /empresas/formly/{id} |  | JSON | Devuelve los datos a pintar en el formulario de Ver Detalle/Actualizar en el SGI (formly). |
| [SGI - ESB - SGEMP - Empresas - Modificar](/confluence/spaces/HERCULES/pages/597853024/SGI+-+ESB+-+SGEMP+-+Empresas+-+Modificar) | PUT | /empresas | JSON | id  Vendrá relleno si la creación es síncrona y no vendrá si es asíncrona. | Recibe como parámetro la respuesta del usuario del formulario de datos de modificación (formly) con los campos necesarios para actualizar una empresa. |
| [SGI - ESB - SGEMP - Empresas - Dar de alta](/confluence/spaces/HERCULES/pages/597853019/SGI+-+ESB+-+SGEMP+-+Empresas+-+Dar+de+alta) | POST | /empresas | JSON |  | Recibe como parámetro la respuesta del usuario del formulario de datos de alta (formly) con los campos necesarios para crear una empresa. |
| [SGI - ESB - SGEMP - Empresas - Consultar campos alta](/confluence/spaces/HERCULES/pages/597853018/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+alta) | GET | /empresas/formly/create |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar alta empresa, pestaña "Datos generales". Ver [IU-GEN-0081 - Solicitar alta de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0081-solicitar-alta-de-empresa) |