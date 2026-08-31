# IU-CSP-0030-001 Crear tipo de fase

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0030-001 Crear tipo de fase******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador |
| Frecuencia | Baja |

## Formulario Crear tipo de fase

Formulario de creación de un tipo de fase. Los tipos de fase formarán parte de los modelos de ejecución en los que se basarán convocatorias y proyectos.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Creación de tipo de fase | | | |
| Nombre | | Texto corto  Obligatorio | Es el nombre identificativo del tipo de fase con el que se listará en todos los desplegables.  Debe de validarse su unicidad en la tabla de tipos de fase entre aquellos elementos activos (campo "activo"="true") |
| Descripción | | Texto  Opcional | No requiere ser introducido de manera obligatorio. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea un nuevo registro en base de datos. | Se deberá verificar la unicidad a partir del campo "Nombre" entre los registros de la tabla "tipo fase" que tengan el campo "activo" a "true".  El registro se almacenará con el campo "activo" a true.  [CU-CSP-0005-002 - Crear tipo de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0005-gestion-de-tipos-de-fase/cu-csp-0005-002-crear-tipo-de-fase) | CSP-TFASE-C |
| Cancelar | No realiza ninguna operación en base de datos | No se realiza ninguna inserción en base de datos.  Se vuelve a mostrar la pantalla de listado de tipos de enlace [IU-CSP-0030-002 Buscar y listar tipos de fase](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0030-gestion-de-tipos-de-fases/iu-csp-0030-002-buscar-y-listar-tipos-de-fase) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-TFASE-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-TFASE-C |