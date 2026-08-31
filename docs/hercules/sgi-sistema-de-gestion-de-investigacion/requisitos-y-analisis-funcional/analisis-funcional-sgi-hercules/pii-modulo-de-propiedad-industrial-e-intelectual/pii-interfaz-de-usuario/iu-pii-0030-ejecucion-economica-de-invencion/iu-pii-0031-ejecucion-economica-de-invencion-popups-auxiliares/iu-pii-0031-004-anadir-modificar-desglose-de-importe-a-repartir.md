# IU-PII-0031-004 - Añadir-modificar desglose de importe a repartir

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0031-004 - Añadir-modificar desglose de importe a repartir |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

## Formulario Añadir-modificar desglose de importe a repartir

Pantalla que muestra el formulario para añadir un nuevo desglose de un importe a repartir o modificar los datos de uno ya informado para un ingreso en un reparto en una ventana emergente.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | *Formulario en "modo añadir"* | *Formulario en "modo modificar"* | | | |
| Nombre | Tipo | Características / Notas |
| Importe pendiente de repartir | Numérico decimal  Solo consulta | Importe que está aún pendiente de repartir del ingreso al que se le está añadiendo el desglose. |
| Importe a repartir | Numérico decimal  Obligatorio | Importe del ingreso que se quiere repartir.  Debe ser mayor que 0 y menor o igual que el importe pendiente de repartir. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Añadir | Añade el desglose del ingreso al reparto que se está haciendo y retorna a la pantalla de alta-modificación del reparto. |  |
| Aceptar | Modifica el desglose del gasto dentro del reparto que se está haciendo y retorna a la pantalla de alta-modificación del reparto. |  |
| Cancelar | Vuelve a la pantalla de alta-modificación del reparto sin aplicar ningún cambio. |  |