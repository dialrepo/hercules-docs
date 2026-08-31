# IU-PII-0021-002 - Añadir-modificar país validado

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0021-002 - Añadir-modificar país validado |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

## Formulario Añadir-modificar país validado

Pantalla que muestra el formulario para añadir un nuevo país validado o modificar los datos de un país validado asociado a una solicitud de invención en una ventana emergente.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario Nuevo documento general | | |
| Fecha validación | Fecha (sin hora)  Obligatorio | Fecha de validación de la invención, a través de la solicitud, en el país indicado. |
| País | Selector  Texto corto  Obligatorio | País en el que se ha validado la invención.  Se cargará una lista con de países para seleccionar uno a la lista de países validados de la solicitud de protección.  Esta lista de países será recuperada a través del requisito de integración [REQ-INT-0030-SGO-0060 - Listar países](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103891354). |
| Código de invención | Texto corto  Obligatorio | Código asignado a la invención. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Añadir | Añade el país validado a la solicitud de protección y vuelve a la pantalla que contiene el listado de países validados. |  |
| Aceptar | Modifica los datos del país validado seleccionado y vuelve a la pantalla que contiene el listado de países validados. |  |
| Cancelar | Vuelve a la pantalla que contiene el listado de países validados sin añadir el nuevo país validado. |  |