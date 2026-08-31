# IU-CSP-0302-020 - Exportación presupuesto

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0302-020 - Exportación presupuesto******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Exportación presupuesto

Pantalla que permite la exportación del presupuesto completo de una solicitud de tipo proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de informe asociado al presupuesto completo de una solicitud | | | |
| Título | | Texto  Opcional | Título a incluir en el informe generado.  Por defecto tomará el valor "Exportación de presupuesto de proyecto". |
| Formato de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * csv * xlsx * rtf * pdf   Será obligatorio seleccionar un valor. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Exportar | Genera el informe asociado al listado de acuerdo al formato de exportación seleccionado | Si se selecciona el formato de exportación "csv" se generará el informe [REP-CSP-0026 - Exportación presupuesto de solicitud - Formato csv](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0026-exportacion-presupuesto-de-solicitud-formato-csv)  Si se selecciona el formato de exportación "xlsx" se generará el informe [REP-CSP-0025 - Exportación presupuesto de solicitud - Formato xlsx](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/csp-informes-predefinidos/rep-csp-0025-exportacion-presupuesto-de-solicitud-formato-xlsx) | No se necesita permisos adicionales |
| Cancelar | Retorna a la pantalla de procedencia (desglose de presupuesto de solicitud) |  | No se necesita permisos adicionales |