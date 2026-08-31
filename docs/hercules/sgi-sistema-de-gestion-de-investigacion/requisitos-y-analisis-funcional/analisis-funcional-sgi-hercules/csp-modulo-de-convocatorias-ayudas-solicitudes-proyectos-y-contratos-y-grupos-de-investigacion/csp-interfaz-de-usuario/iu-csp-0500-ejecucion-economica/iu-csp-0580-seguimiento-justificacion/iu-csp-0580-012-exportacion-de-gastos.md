# IU-CSP-0580-012 - Exportación de gastos

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0580-012 - Exportación de gastos******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Exportación de gastos

Pantalla que muestra el formulario de exportación de los gastos del seguimiento de justificación de un proyecto económico.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de la exportación de los gastos justificados de un proyecto económico | | | |
| Seleccione el tipo de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * xlsx * csv   Será obligatorio seleccionar un valor. |

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Exportar | Genera el informe de exportación correspondiente. | Invoca al requisito de integración con el SGE para obtener los datos a incluir en el informe. El requisito de integración a invocar se indica en el requisito de cada report. | CSP-SJUS-E  CSP-SJUS-E\_UO  CSP-SJUS-V  CSP-SJUS-V\_UO |

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