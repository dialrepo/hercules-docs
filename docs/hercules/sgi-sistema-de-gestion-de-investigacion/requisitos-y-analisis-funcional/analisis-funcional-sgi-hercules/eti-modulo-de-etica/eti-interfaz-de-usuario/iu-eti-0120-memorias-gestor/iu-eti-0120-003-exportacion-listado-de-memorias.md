# IU-ETI-0120-003 - Exportación listado de memorias

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0120-003 - Exportación listado de memorias******** |
| Ver. objetivo |  |
| Ver. IU |  |
| Estado | LIBERADO |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor, ACT-ETI-002-Investigador, ACT-ETI-003-Solicitante, ACT-ETI-006-Responsable memoria |
| Frecuencia | Media |

## Formulario Exportación listado de memorias

Pantalla de configuración de la exportación del listado detallado de memorias.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de informe asociado al listado de memorias devueltas por el buscador correspondiente. | | | |
| Formato de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * csv * xlsx   Será obligatorio seleccionar un valor. |
| Evaluaciones | | Check | Por defecto estará seleccionado. Podrá dejarse desmarcado.  Si está marcado, el informe de salida contendrá los campos asociados a este bloque. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Exportar | Genera el informe asociado al listado de acuerdo al formato de exportación seleccionado | Si se selecciona el formato de exportación "csv" se generará el informe [REP-ETI-0142 - Listado general de memorias - Formato csv](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/eti-informes-predifinidos/rep-eti-0142-listado-general-de-memorias-formato-csv) pasando como parámetros los bloques de datos seleccionados (aquellos que tengan el check correspondiente marcado).  Si se selecciona el formato de exportación "xlsx" se generará el informe [REP-ETI-0143 - Listado general de memorias - Formato xlsx](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0150-sgrep-integracion-con-sistema-de-generacion-de-reportes/eti-informes-predifinidos/rep-eti-0143-listado-general-de-memorias-formato-xlsx) pasando como parámetros los bloques de datos seleccionados (aquellos que tengan el check correspondiente marcado). | No se necesita permisos adicionales |
| Cancelar | Retorna a la pantalla de procedencia (búsqueda y listado de memorias) |  | No se necesita permisos adicionales |