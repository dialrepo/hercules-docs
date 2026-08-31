# IU-CSP-0205-003 - Ver convocatoria - Entidades financiadoras

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0205-003 - Ver convocatoria - Entidades financiadoras******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT- CSP-001-Investigador, ACT-CSP-005-Visor  Usuario externo |
| Frecuencia | Media |

## Formulario Ver convocatoria - Entidades financiadoras

Formulario para ver las entidades financiadoras de una convocatoria.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de entidades financiadoras | | |
| Nombre | Texto | Nombre de la entidad financiadora, obtenido a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa). |
| CIF | Texto corto | CIF de la entidad financiadora, obtenido a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa). |
| Fuente financiación | Texto corto | Fuente de la financiación que aplica sobre la entidad para la convocatoria |
| Ámbito | Texto corto | Ámbito geográfico de la  fuente de financiación |
| Tipo financiación | Texto corto | Tipo de financiación con la que la entidad participa en esta convocatoria |
| % financiación | Numérico Porcentaje | Porcentaje de financiación de la  entidad para esta convocatoria |
| Importe financiación | Numérico Económico | Importe de financiación de la entidad para esta convocatoria |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Paginación | Componente estándar de paginación sobre la tabla de lista de |  |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Cancelar | Retorna al listado de Convocatorias. |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-001-Investigador | CSP-CON-INV-V |
| ACT-CSP-005-Visor | CSP-CON-V |
| Usuario externo | Sin permisos |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-INV-V, CSP-CON-V |