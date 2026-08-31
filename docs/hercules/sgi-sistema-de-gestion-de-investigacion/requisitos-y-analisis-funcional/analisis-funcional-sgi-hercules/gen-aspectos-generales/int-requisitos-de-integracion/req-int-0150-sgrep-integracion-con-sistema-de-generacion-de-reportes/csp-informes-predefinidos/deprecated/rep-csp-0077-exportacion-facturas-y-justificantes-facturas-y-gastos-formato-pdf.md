# REP-CSP-0077 - Exportación Facturas y justificantes - Facturas y gastos - Formato pdf

|  |  |
| --- | --- |
| Cod. REP | ********REP-CSP-0077 - Exportación Facturas y justificantes - Facturas y gastos - Formato pdf******** |
| Ver. Objetivo |  |
| Ver. REP | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Frecuencia |  |

### Diseño Informe

Se debe de generar un informe en formato PDF que reciba como parámetro de entrada el título del informe. 

Se incluirá el parámetro de entrada "título" como título del informe.

Los datos a incluir en el informe serán obtenidos del servicio de integración [REQ-INT-0010-SGE-0134 - Buscar justificantes y facturas - Facturas y gastos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0134-buscar-justificantes-y-facturas-facturas-y-gastos). Para cada registro devuelto se incluirán en el informe todos los campos devueltos por el servicio. El formato para mostrar estos campos será en líneas de dos columnas, donde la primera columna será una etiqueta y la segunda el valor recuperado del servicio de integración.

Entre cada registro se mostrará una línea con un formato de fondo que represente separación.

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