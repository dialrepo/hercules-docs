# REP-CSP-0070 - Exportación Detalle operaciones - Modificaciones - Formato xlsx

|  |  |
| --- | --- |
| Cod. REP | ********REP-CSP-0070 - Exportación Detalle operaciones - Modificaciones - Formato xlsx******** |
| Ver. Objetivo |  |
| Ver. REP | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |

### Diseño Informe

Se debe de generar un informe en formato xlsx.

Los datos a mostrar deberán obtenerse a partir de integración con el SGE, incluyendo todas las columnas devueltas por el servicio de integración [REQ-INT-0010-SGE-0139 - Buscar detalle de operaciones - Modificaciones](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0139-buscar-detalle-de-operaciones-modificaciones). Los parámetros de entrada al servicio se corresponderán con los recogidos en el formulario desde el que se invoca a este informe.  Cada fila del informe será un registro devuelto por el servicio y cada columna un campo de cada registro.

### Permisos

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-EJEC-E, CSP-EJEC-E\_UO |
| ACT-CSP-004-Administrador | CSP-EJEC-E, CSP-EJEC-E\_UO |
| ACT-CSP-005-Visor | CSP-EJEC-V, CSP-EJEC-V\_UO |

### Interfaces de usuario relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)