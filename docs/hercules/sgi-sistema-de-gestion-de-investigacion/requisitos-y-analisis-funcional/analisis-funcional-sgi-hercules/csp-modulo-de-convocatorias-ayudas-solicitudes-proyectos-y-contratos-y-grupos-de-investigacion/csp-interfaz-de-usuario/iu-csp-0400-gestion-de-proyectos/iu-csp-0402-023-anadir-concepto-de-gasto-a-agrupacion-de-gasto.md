# IU-CSP-0402-023 - Añadir concepto de gasto a agrupación de gasto

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0402-023 - Añadir concepto de gasto a agrupación de gasto******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario  Añadir concepto de gasto a agrupación de gasto

Formulario que permite añadir un concepto de gasto a la agrupación de gastos durante la modificación de un proyecto/contrato.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario para añadir concepto de gasto a agrupación de gasto del proyecto | | |
| Concepto gasto | Texto corto  Obligatorio | Listado de conceptos de gasto definidos en la pantalla de Elegibilidad (tanto conceptos de gasto permitidos como no permitidos) (tabla "ProyectoConceptoGasto"). No se sacarán conceptos repetidos (en caso de que exista el mismo concepto en rangos distintos o en permitidos y no permitidos) ni se sacarán aquellos conceptos que ya estén asignados en otra agrupación del proyecto. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Formulario para añadir concepto de gasto a agrupación de gasto del proyecto | | | |
| Añadir | Añade el concepto de gasto a la agrupación de gasto del proyecto | Un mismo concepto  de gasto no puede pertenecer a mas de una agrupación de gasto dentro del mismo proyecto. | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al formulario de agrupación de gasto, sin salvar los posibles cambios |  |  |