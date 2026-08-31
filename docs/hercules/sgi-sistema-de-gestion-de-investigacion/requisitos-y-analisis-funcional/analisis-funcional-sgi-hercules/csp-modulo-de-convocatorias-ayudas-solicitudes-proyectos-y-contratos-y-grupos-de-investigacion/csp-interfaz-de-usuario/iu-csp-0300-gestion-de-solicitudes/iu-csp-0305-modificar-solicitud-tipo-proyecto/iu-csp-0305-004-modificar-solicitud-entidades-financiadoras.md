# IU-CSP-0305-004 - Modificar solicitud - Entidades financiadoras

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0305-004 - Modificar solicitud - Entidades financiadoras******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario de Modificar solicitud - Entidades financiadoras

Formulario que permitirá indicar en la solicitud de proyecto las entidades financiadoras de la solicitud. Se mostrarán en modo consulta las entidades provenientes de la convocatoria y se dejarán crear nuevas entidades financiadoras ajenas a la convocatoria. Las entidades financiadoras ajenas se guardan en la tabla "SolicitudProyectoEntidadFinanciadoraAjena"

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| El apartado "Entidades financiadoras" y, en general, todo del bloque "Datos proyecto" solamente estará visible si el campo "formulario solicitud" de la tabla "solicitud" toma valor "proyecto". | | |
| Listado de entidades financiadoras: Entidades financiadoras registradas en la convocatoria para la que realiza la solicitud. Se obtiene de la tabla "solicitud proyecto entidad", serán aquellos registros que tengan informado el campo "convocatoriaEntidadFinanciadora" | | |
| Nombre | Texto | Nombre de la entidad financiadora, empresa u organismo que financia la convocatoria. El dato será recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| CIF | Texto corto | Número de identificación fiscal de la entidad financiadora, empresa u organismo que financia la convocatoria.  El dato será recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Fuente financiación | Texto corto | Fuente de la financiación de la convocatoria  Se mostrará el campo "nombre" de la tabla "fuente financiación" para el registro referenciado por el campo "fuente financiación" del campo "convocatoriaEntidadFinanciadora" de la tabla "SolicitudProyectoEntidad" |
| Ámbito | Texto corto | Ámbito geográfico de la convocatoria  Se mostrará el campo "nombre" de la tabla "tipo ámbito geográfico" de la fuente de financiación recuperada a partir del campo  "tipo financiación" del campo "convocatoriaEntidadFinanciadora" de la tabla "SolicitudProyectoEntidad" |
| Tipo financiación | Texto corto | Tipo de financiación de la convocatoria  Se mostrará el campo "nombre" de la tabla "tipo financiación" para el registro referenciado por el campo "tipo financiación" del campo "convocatoriaEntidadFinanciadora" de la tabla "SolicitudProyectoEntidad" |
| % financiación | Numérico porcentaje | Porcentaje de financiación de la convocatoria  Campo "porcentaje financiación" del campo "convocatoriaEntidadFinanciadora" de la tabla "SolicitudProyectoEntidad" |
| Importe financiación | Económico | Importe de financiación  Campo "importe financiación" del campo "convocatoriaEntidadFinanciadora" de la tabla "SolicitudProyectoEntidad" |
| Listado de entidades ajenas a la convocatoria: entidades financiadoras ajenas a la convocatoria,es decir, entidades financiadoras registradas en la tabla "solicitud proyecto entidad financiadora ajena" | | |
| Nombre | Texto | Nombre de la entidad financiadora, empresa u organismo que financiará el proyecto de manera ajena a la convocatoria.  El dato será recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| CIF | Texto corto | Número de identificación fiscal de la entidad financiadora, empresa u organismo financiará el proyecto de manera ajena a la convocatoria.  El dato será recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Fuente financiación | Texto corto | Fuente de la financiación  Se mostrará el campo "nombre" de la tabla "fuente financiación" para el registro referenciado por el campo "fuente financiación" de la tabla "solicitud proyecto entidad financiadora ajena" |
| Ámbito | Texto corto | Ámbito geográfico  Se mostrará el campo "nombre" de la tabla "tipo ámbito geográfico" de la fuente de financiación recuperada a partir del campo  "fuente financiación" de la tabla "solicitud proyecto entidad financiadora ajena" |
| Tipo financiación | Texto corto | Tipo de financiación  Se mostrará el campo "nombre" de la tabla "tipo financiación" para el registro referenciado por el campo "tipo financiación" de la tabla "solicitud proyecto entidad financiadora ajena" |
| % financiación | Numérico porcentaje | Porcentaje de financiación  Campo "porcentaje financiación" de la tabla "solicitud proyecto entidad financiadora ajena" |
| Importe financiación | Económico | Importe de financiación  Campo "importe financiación" de la tabla "solicitud proyecto entidad financiadora ajena" |
| Modificar | Icono de acción | Acción "Modificar Entidad financiadora ajena" |
| Eliminar | Icono de acción | Acción "Eliminar Entidad financiadora ajena".  Si la entidad financiadora ajena tiene desglose de presupuesto asociado (tabla "SolicitudProyectoPresupuesto") no saldrá la opción de eliminar. En estos casos en vez de sacar el icono de eliminar mostrar el icono de información con el siguiente texto "No se puede eliminar la entidad porque tiene desglose de presupuesto" |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Eliminar | Elimina la entidad financiadora ajena | Elimina el registro de la tabla de Entidades financiadoras ajenas de la solicitud.  Si la entidad financiadora ajena tiene desglose de presupuesto asociado (tabla "SolicitudProyectoPresupuesto") no saldrá la opción de eliminar hasta que se borren todos los registros del presupuesto. En estos casos en vez de sacar el icono de eliminar mostrar el icono de información con el siguiente texto "No se puede eliminar la entidad porque tiene desglose de presupuesto"  Ver precondiciones en  [CU-CSP-1100 -001 Modificar solicitud - Guardar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1100-gestion-de-solicitudes/cu-csp-1100-001-modificar-solicitud-guardar). | CSP-SOL-E  CSP-SOL-E\_UO |
| Paginación | Componente estándar de paginación sobre la tabla de lista de resultados. |  |  |
| Modificar entidad financiadora | Muestra la pantalla de Modificar entidad financiadora ajena | Muestra la pantalla [IU-CSP-0302-009 - Añadir entidad financiadora ajena a la convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0300-gestion-de-solicitudes/iu-csp-0305-modificar-solicitud-tipo-proyecto/iu-csp-0302-009-anadir-modificar-entidad-financiadora-ajena-a-la-convocatoria).  Ver precondiciones en  [CU-CSP-1100 -001 Modificar solicitud - Guardar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1100-gestion-de-solicitudes/cu-csp-1100-001-modificar-solicitud-guardar). | CSP-SOL-E  CSP-SOL-E\_UO |
| Añadir entidad financiadora | Muestra la pantalla de Nueva entidad financiadora ajena | Muestra la pantalla [IU-CSP-0302-009 - Añadir entidad financiadora ajena a la convocatoria](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0300-gestion-de-solicitudes/iu-csp-0305-modificar-solicitud-tipo-proyecto/iu-csp-0302-009-anadir-modificar-entidad-financiadora-ajena-a-la-convocatoria).  Ver precondiciones en  [CU-CSP-1100 -001 Modificar solicitud - Guardar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1100-gestion-de-solicitudes/cu-csp-1100-001-modificar-solicitud-guardar). | CSP-SOL-E  CSP-SOL-E\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea la Solicitud con la información introducida en el formulario.  Al guardar una solicitud se guardar la información de todas las pestañas de la pantalla. | Ver precondiciones en [CU-CSP-1100-001 Modificar solicitud - Guardar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1100-gestion-de-solicitudes/cu-csp-1100-001-modificar-solicitud-guardar). | CSP-SOL-E  CSP-SOL-E\_UO |
| Cancelar | Retorna al listado de Solicitudes sin salvar los posibles cambios.  Al cancelar una solicitud se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-SOL-E, CSP-SOL-E\_UO |
| ACT-CSP-003-Gestor | CSP-SOL-E, CSP-SOL-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SOL-V, CSP-SOL-V\_UO, CSP-SOL-E, CSP-SOL-E\_UO |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.