# IU-CSP-0550-004 - Validación de gastos - Detalle gasto

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0550-005 - Validación de gastos - Detalle gasto******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador,ACT-CSP-001-Investigador |
| Frecuencia | Media |

## Formulario Ejecución económica - Validación de gastos - Detalle gasto

Formulario que permite consultar el detalle del gasto, todos sus campos y el listado de documentos relacionados con el gasto (recuperados de la integración con el SGE [REQ-INT-0010-SGE-0103 - Detalle gasto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0103-detalle-gasto)).

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Detalle del gasto obtenido de la integración con el SGE [REQ-INT-0010-SGE-0103 - Detalle gasto](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0103-detalle-gasto) | | |
| Estado actual | Texto corto | Estado actual del gasto pendiente de contabilización  Modo consulta |
| Clasificación SGE | Texto corto | Clasificación del gasto en el SGE.  Modo consulta. |
| Aplicación presupuestaria | Texto corto | Aplicación presupuestaria asociada al gasto  Modo consulta |
| Código económico | Texto corto | Código económico asociado al gasto  Modo consulta |
| Anualidad | Texto corto | Anualidad  Modo consulta |
| Fecha | Fecha | Fecha del gasto  Modo consulta |
| Listado de campos nombre - valor | | |
| Nombre del campo: Valor del campo | Texto | Se muestra el campo nombre que indica el nombre del campo y el campo valor que es el valor del campo |
| Listado de documentos del gasto | | |
| Nombre | Texto | Nombre del documento asociado al gasto |
| Descargar | Acción "descargar" | Se descarga el fichero para su visualización |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Descargar | Descargar el contenido del ficheo | Se obtendrá el contenido del fichero a través del requisito de integración [REQ-INT-0010-SGE-0104 - Descargar Binario documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0104-descargar-binario-documento) |
| Cancelar | Retorna al formulario de gastos pendientes de contabilización |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-003-Gestor | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-004-Administrador** | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-001-Investigador** | CSP-EJEC-INV-ER | Ver documentación en [CU-CSP-1200-008 [CU-CSP-1200-008 - Ver ejecución económica - Investigador (rol responsable económico)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-008-ver-ejecucion-economica-investigador-rol-responsable-economico) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-EJEC-E, CSP-EJEC-E\_UO, CSP-EJEC-INV-ER |