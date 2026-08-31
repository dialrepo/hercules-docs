# IU-CSP-0406-025-004 - Modificar proyecto - Configuración económica - Presupuesto - Anualidad - Resumen

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0406-025-004 - Modificar proyecto - Configuración económica - Presupuesto - Anualidad - Resumen******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Modificar proyecto - Configuración económica - Presupuesto - Anualidad - Resumen

Formulario que muestra en forma de tabla el resumen de la anualidad, ingresos y gastos, calculados a partir de la información introducida en los apartados "Gastos" e "Ingresos" de la anualidad.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Tipo | Texto corto | Tipo dentro del presupuesto.  Tomará los valores Gastos o Ingresos. |
| Partida/aplicación presupuestaria | Texto corto | Partida/aplicación presupuestaria |
| Importe presupuesto | Económico | Sumatorio del importe presupuesto por partida presupuestaria:   * Si el tipo es "Gastos": Sumatorio del "importe presupuesto" del apartado "Gastos" de la anualidad para esa partida presupuestaria. * Si el tipo es "Ingresos": Se pone un "-", no existe ese dato en ingresos. |
| Importe concedido | Económico | Sumatorio del importe concedido por partida presupuestaria:   * Si el tipo es "Gastos": Sumatorio del "importe concedido" del apartado "Gastos" de la anualidad para esa partida presupuestaria. * Si el tipo es "Ingresos": Sumatorio del "importe concedido" del apartado "Ingresos" de la anualidad para esa partida presupuestaria. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
|  |  |  |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Crea la anualidad del proyecto con la información introducida en el formulario.  Al guardar una anualidad se guarda la información de todos los apartados de definición de la anualidad. |  | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al listado de Proyecto sin salvar los posibles cambios.  Al cancelar una anualidad se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |