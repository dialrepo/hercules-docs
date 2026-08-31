# IU-CSP-0402-014 - Añadir-modificar paquete de trabajo

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0402-014 - Añadir-modificar paquete de trabajo******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir/modificar paquete de trabajo

Formulario que permitirá añadir/modificar un paquete de trabajo a un proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario para añadir/modificar paquete de trabajo | | | |
| Nombre del paquete de trabajo | | Texto corto  Obligatorio | Nombre del paquete de trabajo.  Debe ser único dentro del proyecto. |
| Duración | Fecha de inicio | Fecha  Obligatorio | Fecha de inicio del paquete de trabajo |
| Fecha de fin | Fecha  Obligatorio | Fecha de fin del paquete de trabajo |
| Persona/mes | | Numérico entero genérico  Obligatorio | Indica el esfuerzo (cantidad de tiempo) que se dedica al paquete de trabajo |
| Descripción | | Texto largo  Opcional | Descripción del paquete de trabajo |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Añadir/Aceptar | El botón se muestra como:   * Añadir, cuando se accede al formulario para añadir un nuevo paquete de trabajo al proyecto. * Aceptar, cuando se accede al formulario para modificar los datos de un paquete de trabajo existente. | Todos los campos son obligatorios salvo la descripción.  El campo nombre del paquete de trabajo no se puede repetir dentro del mismo proyecto.  Las fecha de inicio y fin del paquete de trabajo deben de estar dentro del rango de fecha inicio y fin del proyecto. | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al formulario del proyecto, sin salvar los posibles cambios |  |  |