# IU-PII-0040-0020-001 - Crear tipo de protección - Datos generales

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0040-0020-001 - Crear tipo de protección - Datos generales |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-002-Administrador |
| Frecuencia | Baja |

## Formulario Crear tipo de protección - Datos generales

Formulario para crear un nuevo tipo de protección. Apartado de Datos generales.

Para dar de alta un tipo de protección, únicamente se podrá informar este apartado.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| *Datos generales* | | |
| Tipo de propiedad | Selector  Obligatorio | Tipo de propiedad a asociar al tipo de protección.  Se podrá seleccionar de un listado que tendrá únicamente dos valores:   * Propiedad industrial * Propiedad intelectual |
| Nombre | Texto corto  Obligatorio | Es el nombre identificativo del tipo, con el que se listará en todos los desplegables.  Debe de validarse su unicidad respecto al resto de tipos del mismo nivel (padres activos). |
| Descripción | Texto  Obligatorio | Campo de texto de introducción libre para descripción ampliada. |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar tipo de protección | Se creará el nuevo tipo de protección con los datos informados y se volverá a la pantalla de listado de tipos de protección dentro del menú de Configuración.  Validaciones de obligatoriedad:   * Tipo de propiedad * Nombre * Descripción   Otras validaciones:   * El nombre ha de ser único respecto al resto de tipos del mismo nivel (padres). |  | PII-TPR-C |
| Cancelar | Vuelve a la pantalla listado de tipos de protección dentro del menú de Configuración sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-PII-002-Administrador | PII-TPR-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | PII-TPR-C |