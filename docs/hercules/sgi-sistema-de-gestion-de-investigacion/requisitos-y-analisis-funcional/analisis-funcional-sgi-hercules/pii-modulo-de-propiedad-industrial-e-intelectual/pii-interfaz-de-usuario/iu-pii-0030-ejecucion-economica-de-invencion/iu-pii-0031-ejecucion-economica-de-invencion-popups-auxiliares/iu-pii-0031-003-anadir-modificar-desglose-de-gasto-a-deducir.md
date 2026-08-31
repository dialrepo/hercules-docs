# IU-PII-0031-003 - Añadir-modificar desglose de gasto a deducir

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0031-003 - Añadir-modificar desglose de gasto a deducir |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

## Formulario Añadir-modificar desglose de gasto a deducir

Pantalla que muestra el formulario para añadir un nuevo desglose de un gasto a deducir o modificar los datos de uno ya informado para un gasto en un reparto en una ventana emergente.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | *Formulario en "modo añadir"* | *Formulario en "modo modificar"* | | | |
| Nombre | Tipo | Características / Notas |
| Importe pendiente de compensar | Numérico decimal  Solo consulta | Importe que está aún pendiente de deducir del gasto al que se le está añadiendo el desglose. |
| Importe a compensar | Numérico decimal  Obligatorio | Importe del gasto que se quiere compensar.  Debe ser mayor que 0 y menor o igual que el importe pendiente de compensar. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Añadir | Añade el desglose del gasto al reparto que se está haciendo y retorna a la pantalla de alta del reparto. |  |
| Aceptar | Modifica el desglose del gasto dentro del reparto que se está haciendo y retorna a la pantalla de alta del reparto. |  |
| Cancelar | Vuelve a la pantalla de alta de reparto sin aplicar ningún cambio. |  |