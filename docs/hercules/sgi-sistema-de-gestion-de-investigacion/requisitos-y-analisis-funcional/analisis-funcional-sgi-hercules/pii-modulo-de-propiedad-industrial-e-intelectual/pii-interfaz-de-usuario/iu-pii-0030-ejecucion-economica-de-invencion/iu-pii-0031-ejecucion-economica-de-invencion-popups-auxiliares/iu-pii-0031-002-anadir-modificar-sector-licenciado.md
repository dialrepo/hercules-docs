# IU-PII-0031-002 - Añadir-modificar sector licenciado

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0031-002 - Añadir-modificar sector licenciado |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

## Formulario Añadir-modificar sector licenciado

Pantalla que muestra el formulario para añadir un nuevo sector licenciado o modificar los datos de uno asociado a un contrato relacionado con la invención en una ventana emergente.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | *Formulario en "modo añadir"* | *Formulario en "modo modificar"* | | | |
| Nombre | Tipo | Características / Notas |
| País | Selector  Texto corto  Obligatorio  Modificable | País del sector que se licencia para la invención.  Se cargará un listado de países recuperado a través del requisito de integración [REQ-INT-0030-SGO-0060 - Listar países](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103891354) de los que seleccionar uno a asociar con el sector. |
| Exclusividad | Selector  Texto corto  Obligatorio  Modificable | Indicador de si la licencia en el país y sector es en exclusividad o no.  Tendrá dos valores posibles Sí / No. |
| Fecha inicio licencia | Fecha (sin hora)  Obligatorio  Modificable | Fecha de inicio de vigencia de la licencia en el país y sector. |
| Fecha fin licencia | Fecha (sin hora)  Obligatorio  Modificable | Fecha de inicio de vigencia de la licencia en el país y sector. |
| Sector | Selector  Texto  Obligatorio  Modificable | Listado de sectores en los que la invención se puede licenciar de los que elegir uno a asociar para el país indicado.  Listado configurable en [IU-PII-0050 - Gestión de sectores de aplicación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/pii-modulo-de-propiedad-industrial-e-intelectual/pii-interfaz-de-usuario/iu-pii-0050-gestion-de-sectores-de-aplicacion). |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Añadir | Añade el sector licenciado a la lista de sectores licenciados asociados a la invención a través del contrato y retorna a la pantalla de listado de contratos y sectores licenciados. |  |
| Aceptar | Modifica el sector licenciado asociado a la invención a través del contrato y retorna a la pantalla de listado de contratos y sectores licenciados. |  |
| Cancelar | Vuelve a la pantalla que contiene el listado de contratos y sectores licenciados sin añadir el sector licenciado. |  |