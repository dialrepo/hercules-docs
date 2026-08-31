# IU-CSP-0560-011 - Añadir viaje/dieta a periodo de justificación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0560-011 - Añadir viaje/dieta a periodo de justificación******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir viaje/dieta a periodo de justificación

Formulario que permite añadir uno o varios gastos de viajes y/o dietas a la justificación de un periodo.

Los gastos de viajes y dietas disponibles serán los que figuren en el apartado "Facturas y justificantes" - "Viajes y dietas" de la sección "Ejecución económica" del proyecto que, a su vez, habrán sido recuperados del SGE por medio de los servicios de integración correspondientes.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Añadir gasto a la justificación del periodo | | | |
| Anualidad | | Selector  Numérico entero genérico  Opcional | Listado de todas anualidades del/de los proyecto/s que tengan vinculado el identificador del SGE para el que se está viendo la ejecución económica |
| Núm. justificante | | Texto corto  Opcional | Número justificante del gasto |
| Fecha viaje | | Fecha  Opcional | Fecha del viaje |
| Fecha gasto | | Fecha  Opcional | Fecha del gasto |
| Filtrar | | Icono de acción | Acción "Filtrar" |
| Listado de facturas y justificantes | | | |
|  | | Check  Booleano | Permite seleccionar los gastos a incluir en el periodo de justificación de forma individual, marcando el check de la columna, o seleccionar todos los gastos, marcando el check de la cabecera de la tabla. |
| Anualidad | | Numérico entero genérico | Año de la anualidad |
| Número justificante gasto | | Texto corto | Número justificante del gasto |
| Proveedor | | Texto corto | Proveedor del gasto |
| Num. factura | | Texto corto | Número factura del gasto |
| Fecha emisión | | Fecha | Fecha de emisión de la factura |
| Estado | | Texto corto | Estado de la factura |
| Importe total | | Económico | Importe total de la factura |
| Importe imputado | | Económico | Importe imputado de la factura |
| Origen | | Texto corto | Origen del viaje |
| Destino | | Texto corto | Destino del viaje |
| Fecha ida | | Fecha | Fecha de ida |
| Fecha vuelta | | Fecha | Fecha de vuelta |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Filtrar | Aplica los filtros introducidos sobre la lista de gastos de viajes y dietas mostrando las que cumplen las condiciones |  |
| Guardar | Añade el/los gasto/s seleccionados a la justificación del periodo |  |
| Cancelar | Retorna al formulario de justificación sin salvar los posibles cambios |  |

### Acciones

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |
| ACT-CSP-004-Administrador | CSP-PROYECTO-CREAR, CSP-PROYECTO-EDITAR |