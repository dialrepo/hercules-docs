# IU-CSP-0080-001 - Crear tipo de financiación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0080-001 Crear tipo de financiación******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador |
| Frecuencia | Baja |

## Formulario Crear tipo de financiación

Formulario de creación de un tipo de financiación

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Creación de un tipo de financiación | | |
| Nombre | Texto corto  Obligatorio | Es el nombre identificativo del tipo de financiación, con el que se listará en todos los desplegables de creación de convocatorias/proyectos.  Debe de validarse su unicidad en la tabla de tipos de financiación entre aquello elementos activos (campo "activo" a "true"). |
| Descripción | Texto  Opcional | Descripción del tipo de financiación. Puede dejarse vacío. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Se crea un nuevo registro en la tabla "tipo financiación". | El registro se creará con el campo Activo=true.  Se debe verificar la unicidad del campo Nombre en la tabla "Tipo financiación" sobre aquellos elementos con campo "activo" a "true"  [CU-CSP-0080-002 - Crear tipo de financiación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0080-gestion-de-tipos-de-financiacion/cu-csp-0080-002-crear-tipo-de-financiacion) | CSP-TFNA-C |
| Cancelar | No se realiza ninguna operación | Se retorna a la pantalla de [IU-CSP-0080-002 - Buscar y listar tipos de financiación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0080-gestion-de-tipos-de-financiacion/iu-csp-0080-002-buscar-y-listar-tipos-de-financiacion) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| **ACT-CSP-004-Administrador** | CSP-TFNA-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| **Permisos** | CSP-TFNA-C |