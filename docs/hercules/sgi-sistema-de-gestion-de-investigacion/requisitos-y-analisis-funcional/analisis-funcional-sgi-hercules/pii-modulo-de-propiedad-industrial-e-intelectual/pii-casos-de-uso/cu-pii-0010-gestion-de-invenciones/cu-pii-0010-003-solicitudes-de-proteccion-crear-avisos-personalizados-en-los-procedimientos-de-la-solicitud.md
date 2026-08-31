# CU-PII-0010-003 - Solicitudes de protección - Crear avisos personalizados en los procedimientos de la solicitud

|  |  |
| --- | --- |
| Cod. CU | ********CU-PII-0010-003 - Solicitudes de protección - Crear avisos personalizados en los procedimientos de la solicitud******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

### Descripción

Cuando el usuario va gestionando una solicitud de protección y se generan procedimientos el usuario va dejando constancia en la misma. Este procedimiento que el usuario registra, normalmente, requerirá de unas acciones a tomar que si no son de manera inmediata o no son para el usuario que está haciendo el registro requieren de un aviso en una fecha y a unos usuarios determinados (\_\_NO USAR CU-COM-0020 - Generar comunicado automático - Original con enlaces de AFs fuera de PMV - IU-COM-0020-001 - Generación de comunicados).

### Actores

#### Actor principal

ACT-PII-001-Gestor

### Precondiciones

Usuario logado en el sistema con el rol adecuado dentro del módulo PII.

Haber accedido a la opción de Invenciones y dentro de una invención haber accedido a Solicitudes de protección y haber generado un procedimiento asociado a la misma.

### Garantías de éxito (postcondiciones)

Los usuarios va recibiendo los avisos generados a medida que se cumplen las fechas.

### Escenario principal (flujo básico)

1. Se presenta la Solicitudes de protección.
2. El gestor crea un procedimiento asociado a la misma y marca el check de Generar aviso.
3. Se presenta un formulario de SGI para la generación del aviso.
4. El usuario rellena los datos necesarios.
5. El usuario guarda el aviso.

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