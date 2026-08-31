# IU-CSP-0040-003 Modificar tipo de documento

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0040-003 Modificar tipo de documento******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador |
| Frecuencia | Baja |

## Formulario Modificar tipo de documento

Formulario de modificación de un tipo de documento.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Modificación de tipo de documento | | |
| Nombre | Texto corto  Obligatorio | Campo "nombre" de la tabla "tipo documento".  No se podrá dejar vacío.  Se comprobará la unicidad del campo "nombre" sobre los registros activos (campo "activo" a "true") |
| Descripción | Texto  Opcional | Se podrá modificar libremente el valor, pasando a dejarlo vacío aunque ya estuviese relleno. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Actualiza el registro en base de datos | Se comprobará la unicidad del campo "nombre" sobre los registros activos (campo "activo" a "true")  Se guardarán los cambios modificando los datos del tipo de documento en base de datos.  [CU-CSP-0006-003 - Modificar tipo de documento](/confluence/pages/createpage.action?spaceKey=HERCULES&title=CU-CSP-0006-003+-+Modificar+tipo+de+documento&linkCreation=true&fromPageId=597852571) | CSP-TDOC-E |
| Cancelar | No realiza ninguna operación en base de datos | No se tendrán en cuenta los cambios indicados en el formulario y se volverá a [IU-CSP-0040-002 Buscar y listar tipos de documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0040-gestion-de-tipos-de-documento/iu-csp-0040-002-buscar-y-listar-tipos-de-documento) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-TDOC-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-TDOC-V, CSP-TDOC-E |