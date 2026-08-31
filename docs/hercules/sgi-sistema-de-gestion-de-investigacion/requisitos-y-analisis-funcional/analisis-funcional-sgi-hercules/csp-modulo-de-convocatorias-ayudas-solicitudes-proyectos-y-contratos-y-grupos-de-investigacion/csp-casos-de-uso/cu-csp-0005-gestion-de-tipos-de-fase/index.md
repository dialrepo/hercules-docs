# CU-CSP-0005 - Gestión de tipos de fase

|  |  |
| --- | --- |
| Cod. CU | **CU-CSP-0005 - Gestión de tipos de fase** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador |
| Frecuencia | Baja |

### Descripción

Agrupación de casos de uso que permitirá realizar la gestión de los tipos de fase. Los tipos de fase serán necesarios para realizar la configuración de los modelos de ejecución en base a los que se crearán las convocatorias y proyectos. De acuerdo al modelo de ejecución por el que se rija una convocatoria o proyecto, tendrá disponible unos tipos de fase u otros.

### Actores

#### Actor principal

ACT-CSP-004-Administrador

#### Personal involucrado e intereses

ACT- CSP-003-Gestor que requiere que los tipos de fase estén configurados y vinculados a los modelos de ejecución para poder realizar la gestión de convocatorias y proyectos

### Precondiciones

El usuario ACT-CSP-004-Administrador se autentica a través del usuario de dominio corporativo.

A través del servicio de integración con el directorio activo y de la información del usuario almacenada en el propio SGI, se obtiene su rol y  la unidades de gestión sobre las que tiene disponible el rol. El usuario está autorizado sobre la funcionalidad asociada a esta operación.

### Garantías de éxito (postcondiciones)

La gestión de los tipos de fase se realiza correctamente y están disponibles para poder realizar la cofiguración de los modelos de ejecución y con ello la gestión de convocatorias y proyectos.

### Listado de casos de uso

* [CU-CSP-0005-001 - Buscar y listar tipos de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0005-gestion-de-tipos-de-fase/cu-csp-0005-001-buscar-y-listar-tipos-de-fase)
* [CU-CSP-0005-002 - Crear tipo de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0005-gestion-de-tipos-de-fase/cu-csp-0005-002-crear-tipo-de-fase)
* [CU-CSP-0005-003 - Modificar tipo de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0005-gestion-de-tipos-de-fase/cu-csp-0005-003-modificar-tipo-de-fase)
* [CU-CSP-0005-004 - Eliminar tipo de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0005-gestion-de-tipos-de-fase/cu-csp-0005-004-eliminar-tipo-de-fase)