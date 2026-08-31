# IU-CSP-0204-003 - Modificar convocatoria - Entidades Financiadoras

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0204-002 - Modificar convocatoria - Entidades Financiadoras******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Modificar convocatoria - Entidades Financiadoras

### Formulario con el listado de entidades financiadoras

**La modificación de los datos de una convocatoria se rige por lo establecido en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)**

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| **La modificación de los datos de una convocatoria se rige por lo establecido en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)** | | |
| Listado de entidades financiadoras | | |
| Nombre | Texto | Nombre de la entidad financiadora, obtenido a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa). |
| Número de identificación fiscal | Texto corto | Número de identificación de la entidad convocante, obtenido a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa). |
| Fuente financiación | Texto corto | Fuente de la financiación de la convocatoria.  Se corresponde con el campo "nombre" de la tabla "fuente financiación" recuperado a través del campo "fuente financiación" de la tabla "convocatoria entidad financiadora" |
| Ámbito | Texto corto | Ámbito geográfico de la convocatoria  Se corresponde con el campo "nombre" de la tabla "tipo ámbito geográfico" recuperado a través de campo "tipo ámbito geográfico" de la tabla "fuente financiación" para la fuente financiación de la convocatoria (campo "fuente financiación" de la tabla "convocatoria entidad financiadora") |
| Tipo financiación | Texto corto | Tipo de financiación de la convocatoria  Se corresponde con el campo "nombre" de la tabla "tipo financiación" recuperado a través del campo "tipo financiación" de la tabla "convocatoria entidad financiadora" |
| % financiación | Numérico Porcentaje | Porcentaje de financiación de la convocatoria  Se corresponde con el campo "porcentaje financiación" de la tabla "convocatoria entidad financiadora" |
| Importe financiación | Económico | Importe de financiación de la convocatoria  Se corresponde con el campo "importe financiación" de la tabla "convocatoria entidad financiadora" |
| Modificar | Icono de acción | Acción modificar |
| Eliminar | Icono de acción | Acción eliminar |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Modificar | Muestra la pantalla de modificación de la entidad seleccionada del listado de entidades financiadora | Esta opción sólo estará disponible si es el estado de la convocatoria es:   * "Borrador" * "Registrada" pero no existen solicitudes o proyectos asociados a la convocatoria   Muestra la pantalla de abajo de "Modificar entidad financiadora a la convocatoria".  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Eliminar | Elimina la entidad financiadora | Esta opción sólo estará disponible si es el estado de la convocatoria es:   * "Borrador" * "Registrada" pero no existen solicitudes o proyectos asociados a la convocatoria   Elimina el registro de la tabla de Entidades financiadoras de la convocatoria.  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |
| Añadir entidad financiadora | Muestra la pantalla de Nueva entidad financiadora | Esta opción sólo estará disponible si es el estado de la convocatoria es:   * "Borrador" * "Registrada" pero no existen solicitudes o proyectos asociados a la convocatoria   Muestra la pantalla [IU-CSP-202-004 - Añadir entidad financiadora](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0200-gestion-de-convocatorias/iu-csp-202-004-anadir-entidad-financiadora).  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |

### Formulario para modificar las entidades financiadoras de una convocatoria.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| **La modificación de los datos de una convocatoria se rige por lo establecido en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria)** | | |
| Entidad financiadora | Texto | Empresa u organismo que financia la convocatoria. Se visualizará el nombre de la entidad financiadora seleccionada en el alta de la entidad financiadora, recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa).  **Se muestra en modo consulta. No se permite modificar la entidad** |
| Fuente de financiación | Selector  Texto corto  Opcional | Listado de fuentes de investigación activas  Se listarán los valores (campo "nombre" ) de la tabla "fuente financiación" que tengan el campo "activo" a "true" |
| Tipo financiación | Selector  Texto corto  Opcional | Listado de Tipos de financiación activas  Se listarán los valores (campo "nombre" ) de la tabla "tipo financiación" que tengan el campo "activo" a "true" |
| Porcentaje de financiación | Numérico Porcentaje  Opcional | Porcentaje de financiación  Se corresponde con el campo "porcentaje financiación" de la tabla "convocatoria entidad financiadora" |
| Importe de financiación | Numérico Económico  Opcional | Importe de financiación  Se corresponde con el campo "importe financiación" de la tabla "convocatoria entidad financiadora" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Actualiza el registro en base de datos | Se realizarán las comprobaciones de tipo y de unicidad sobre los campos entidad financiadora, fuente y tipo.  Se guardarán los cambios modificando los datos de la entidad financiadora de la convocatoria en la tabla "convocatoria entidad financiadora"  Ver restricciones en [CU-CSP-1000-001 - Modificar convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1000-gestion-de-convocatorias/cu-csp-1000-001-modificar-convocatoria). | CSP-CON-E  CSP-CON-E\_UO |
| Cancelar | No realiza ninguna operación en base de datos | No se tendrán en cuenta los cambios indicados en el formulario y se volverá al listado de entidades financiadoras de la convocatoria. |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-CON-E, CSP-CON-E\_UO |
| ACT-CSP-003-Gestor | CSP-CON-E, CSP-CON-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-CON-V, CSP-CON-V\_UO, CSP-CON-E, CSP-CON-E\_UO |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.