# SIN IMPLEMENTAR - CU-PII-0010-002 - Solicitudes de protección - Avisos

|  |  |
| --- | --- |
| Cod. CU | ********CU-PII-0010-002 - Solicitudes de protección-Avisos******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

### Descripción

Cuando el usuario genera la primera solicitud o una segunda PCT de protección asociada a una invención, el sistema ha de generar los avisos en el sistema para que los usuarios Gestor de la OTRI reciban recordatorios antes de se cumplan algunas fechas ([\_\_NO USAR CU-COM-0020 - Generar comunicado automático - Original con enlaces de AFs fuera de PMV](/confluence/pages/createpage.action?spaceKey=HERCULES&title=__NO+USAR+CU-COM-0020+-+Generar+comunicado+autom%C3%A1tico+-+Original+con+enlaces+de+AFs+fuera+de+PMV&linkCreation=true&fromPageId=597853200)). La forma de generar estos avisos es:

* De manera genérica para una primera solicitud:
  + avisos a los usuarios dentro de los X meses desde la fecha de prioridad hasta la fecha de fin de prioridad. Los avisos han de ser:
    - A los X/2, a los 2X/3 y a los X-1 meses, avisando de lo que queda a hasta los X meses y que no se ha añadido una segunda solicitud de protección. Si hay más de una solicitud ya no se avisa.
    - Al mes X, avisando de que se ha terminado el periodo de prioridad.
* La solicitud es de tipo PCT y no es la primera solicitud:
  + avisos a los usuarios dentro de los 18 meses siguientes a los X de prioridad. Los avisos han de ser:
    - A los 9, a los 14 y a los 17 meses.
    - Al mes 18, avisando de que se ha terminado de extensión.

### Actores

#### Actor principal

ACT-PII-001-Gestor

### Precondiciones

Usuario logado en el sistema con el rol adecuado dentro del módulo PII.

Haber accedido a la opción de Invenciones y dentro de una invención haber accedido a Solicitudes de protección y haber generado o modificado alguna.

### Garantías de éxito (postcondiciones)

Los usuarios va recibiendo los avisos generados por el sistema a medida que se cumplen las fechas.

### Escenario principal (flujo básico)

1. Se presenta la Solicitudes de protección.
2. El gestor genera o modifica una primera solicitud o una segunda siendo esta de tipo PCT.

### Extensiones (flujos alternativos)

N/A

### Requisitos especiales

N/A

### Lista de tecnología y variaciones de datos

N/A

### Acciones

|  |  |
| --- | --- |
| ACT-PII-001-Gestor | PII-INVENCION-EDITAR |

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Interfaces relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)