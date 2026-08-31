# IU-CSP-0406-005 - Modificar proyecto - Entidad gestora

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-005 - Modificar proyecto - Entidad gestora******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Modificar proyecto - Entidad gestora

Formulario que permite añadir o modificar la entidad u organismo que actuará como gestor del proyecto/contrato. Solo se permitirá indicar una única entidad gestora. El listado de entidades disponible procederá del módulo Empresas, común a todo el SGI.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario de entidad gestora | | |
| Entidad gestora | Texto  Opcional | Empresa u organismo que financia la convocatoria.  Cuando el proyecto ya tenga una entidad gestora asociada, se mostrará el nombre de la empresa recuperado a través del requisito de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa).  El buscador disponible será el buscador de empresas común a todo el SGI, [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas), resuelto por medio del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa). |
| Buscar | Icono de acción | Acción "Buscar" |
| Eliminar | Icono de acción | Acción "Eliminar" |
| Datos de la entidad. Este bloque solo se mostrará en el caso de que se haya vinculado una entidad gestora al proyecto | | |
| Tipo de identificador | Texto | Tipo de identificador fiscal de la entidad gestora, recuperado a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Número de identificación | Texto | Número de identificador fiscal de la entidad gestora, recuperado a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Nombre | Texto | Nombre de la entidad gestora, recuperado a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Razón social | Texto | Razón social de la entidad gestora, recuperado a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) |
| Dirección postal | Texto | Dirección postal de la entidad gestora, recuperado a través de [REQ-INT-0015-SGEMP-0032 - Consultar datos de contacto de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0032-consultar-datos-de-contacto-de-empresa) |
| Tipo de empresa | Texto | Valores de acuerdo a la clasificación del sistema de gestión de empresas correspondiente. Recuperado a través de [REQ-INT-0015-SGEMP-0033 - Consultar datos de tipo de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0033-consultar-datos-de-tipo-de-empresa) |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Buscar | Muestra la pantalla de búsqueda para seleccionar la entidad gestora | El buscador disponible será el buscador de empresas común a todo el SGI, [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas), resuelto por medio del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa)  En el caso de que el buscador no devolviese la  empresa que se desea añadir como entidad gestora del proyecto se podrá solicitar el registro de la nueva empresa, utilizando para ello el formulario de solicitud de alta [IU-GEN-0081 - Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0081-solicitar-alta-de-empresa) que cumple con el requisito [REQ-INT-0015-SGEMP-0040 - Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0040-solicitar-alta-de-empresa). Este registro solo podrá ser provocado por ACT-CSP-004-Administrador o ACT-CSP-003-Gestor.  En el caso de que el buscador devolviese la empresa que se desea añadir como entidad gestora del proyecto, pero se quisiera realizar alguna modificación en sus datos, se podrá solicitar dicha modificación, utilizando para ello el formulario de solicitud de modificación IU-GEN-0082 - Ver detalle - Solicitar modificación de empresa que cumple con el requisito [REQ-INT-0015-SGEMP-0045 - Solicitar modificación de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0050-solicitar-modificacion-de-empresa)[.](https://confluence.um.es/confluence/pages/viewpage.action?pageId=89621944) Esta modificación solo podrá ser provocado por ACT-CSP-004-Administrador o ACT-CSP-003-Gestor. | No se necesita permiso para mostrar la pantalla de búsqueda de empresas |
| Eliminar | Elimina la relación entre el proyecto y la entidad gestora | Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modifica el Proyecto con la información introducida en el formulario.  Al guardar un proyecto se guardar la información de todos los apartados de definición del proyecto. | Ver documentación de restricciones en [CU-1200-002 - Modificar proyecto - Unidad de gestión](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100764578). | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyectos sin salvar los posibles cambios.  Al cancelar un proyecto se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-001-Investigador | CSP-PRO-INV-VR | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) y en [CU-1200-003 - Ver proyecto - Investigador (rol principal/responsable económico)](https://confluence.um.es/confluence/pages/viewpage.action?pageId=100766521) |
| ACT-CSP-003-Gestor | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-004-Administrador | CSP-PRO-E, CSP-PRO-E\_UO |  |
| ACT-CSP-005-Visor | CSP-PRO-V, CSP-PRO-V\_UO | Ver detalle en documentación asociada en [CU-CSP-1200-004 - Ver proyecto - Visor e Investigador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-004-ver-proyecto-visor-e-investigador) (sería el caso del Visor) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-PRO-V, CSP-PRO-V\_UO, CSP-PRO-E, CSP-PRO-E\_UO, CSP-PRO-INV-VR |