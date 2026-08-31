# IU-CSP-0050-006 Añadir tipo de enlace al modelo de ejecución

|  |  |
| --- | --- |
| Cod. IU | **IU-CSP-0050-006 Añadir tipo de enlace al modelo de ejecución** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador |
| Frecuencia | Baja |

## Formulario Añadir tipo de enlace al modelo de ejecución

Formulario para añadir un tipo de enlace a un modelo de ejecución. Podrá accederse a este formulario desde la creación o modificación de un modelo de ejecución.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Añadir tipo de enlace al modelo de ejecución | | |
| Tipo de enlace | Selector  Texto corto  Obligatorio | El desplegable cargará el listado de los tipos de enlace que estén activos (campo Activo = true) y que aún no hayan sido asociados al modelo:   * Figuren en la tabla "TipoEnlace" con el campo "activo" a "true" * No existan en la tabla "ModeloTipoEnlace" para el modelo en creación/edición o que existan pero con el campo "activo" a "false" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea un nuevo registro en base de datos | Almacena la relación entre el tipo de enlace seleccionado y el modelo de ejecución que está siendo creado/modificado en la tabla "Modelo Tipo Enlace".  El registro se creará con el campo "activo" a "true".  En caso de que ya existiese la relación con el campo "activo" a "false" se volverá a activar, para ello se pondrá el campo "activo" a "true". | CSP-ME-E  CSP-ME-E\_UO  CSP-ME-C  CSP-ME-C\_UO |
| Cancelar | No realiza ninguna operación en base de datos | Vuelve a la pestaña de Tipos de enlace del modelo de ejecución |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-ME-C, CSP-ME-C\_UO, CSP-ME-E, CSP-ME-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-ME-C, CSP-ME-C\_UO, CSP-ME-E, CSP-ME-E\_UO |