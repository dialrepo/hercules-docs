# REP-CSP-0026 - Exportación presupuesto de solicitud - Formato csv

|  |  |
| --- | --- |
| Cod. REP | **REP-CSP-0026 - Exportación presupuesto de solicitud - Formato csv** |
| Ver. Objetivo |  |
| Ver. REP | 1.0.0 |
| Estado | PENDIENTE |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |

### Diseño Informe

Se debe de generar un informe en formato CSV. A continuación se indica el mapeo de los nombres de columnas del fichero csv de salida con la tabla y campo del SGI desde el que deben ser recuperadas. 

| Columna informe | Campo SGI |
| --- | --- |
| Anualidad | Se corresponde con el campo "anualidad" de la tabla  "solicitud proyecto presupuesto". |
| Concepto de gasto | Campo "nombre" de la tabla "concepto gasto" correspondiente  al campo "concepto gasto" de la tabla  "solicitud proyecto presupuesto". |
| Importe presupuestado | Campo "importe presupuestado" de la tabla  "solicitud proyecto presupuesto". |
| Importe solicitado | Campo "importe solicitado" de la tabla  "solicitud proyecto presupuesto". |

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

|  |  |
| --- | --- |
| ACT-CPS-003-Gestor | CSP-SOL-E\_UO |
| ACT-CSP-004-Administrador | CSP-SOL-E\_UO |
| ACT-CSP-005-Visor | CSP-SOL-V\_UO |