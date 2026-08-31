# IU-CSP-0501-006 - Exportación de requerimientos

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0501-006 - Exportación de requerimientos******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Exportación de requerimientos

Pantalla que muestra el formulario de exportación de los requerimientos del seguimiento de justificación de un listado de proyectos económicos.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de la exportación de los gastos justificados de un proyecto económico | | | |
| Seleccione el tipo de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * xlsx * csv   Será obligatorio seleccionar un valor. |

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Exportar | Genera el informe de exportación correspondiente. | Se generará el report correspondiente en función de la opción de exportación seleccionada:   * xslx: [REP-CSP-0092 - Exportación de requerimientos de justificación - Formato xlsx](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0092-exportacion-de-requerimientos-de-justificacion-formato-xlsx) * csv: [REP-CSP-0093 - Exportación de requerimientos de justificación - Formato csv](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0093-exportacion-de-requerimientos-de-justificacion-formato-csv) | CSP-SJUS-E  CSP-SJUS-E\_UO  CSP-SJUS-V  CSP-SJUS-V\_UO |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-003-Gestor | CSP-SJUS-E, CSP-SJUS-E\_UO |  |
| **ACT-CSP-004-Administrador** | CSP-SJUS-E, CSP-SJUS-E\_UO |  |
| **ACT-CSP-005-Visor** | CSP-SJUS-V, CSP-SJUS-V\_UO |  |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SJUS-E, CSP-SJUS-E\_UO, CSP-SJUS-V, CSP-SJUS-V\_UO |