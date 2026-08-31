# IU-CSP-0406-032 - Exportación consulta presupuesto

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-032 - Exportación consulta presupuesto******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Exportación consulta presupuesto

Pantalla que permite la exportación de la consulta de presupuesto de un proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de informe asociado a la consulta de presupuesto de proyecto | | | |
| Formato de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * csv * xlsx   Será obligatorio seleccionar un valor. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Exportar | Genera el informe asociado al listado de acuerdo al formato de exportación seleccionado | Si se selecciona el formato de exportación "csv" se generará el informe  [REP-CSP-0015 - Exportación presupuesto de proyecto - Formato csv](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0015-exportacion-presupuesto-de-proyecto-formato-csv)  Si se selecciona el formato de exportación "xlsx" se generará el informe [REP-CSP-0014 - Exportación presupuesto de proyecto - Formato xlsx](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0014-exportacion-presupuesto-de-proyecto-formato-xlsx) | No se necesita permisos adicionales |
| Cancelar | Retorna a la pantalla de procedencia (búsqueda y listado de proyectos) |  | No se necesita permisos adicionales |