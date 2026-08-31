# CU-PII-0010-005 - Asociar empresa

|  |  |
| --- | --- |
| Cod. CU | ********CU-PII-0010-005 - Asociar empresa******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

### Descripción

El usuario necesita asociar una entidad con capacidad de facturación a la entidad principal de la que se trate. Podrá ser una empresa o un profesional con capacidad de facturación.

Se presenta un diálogo para la búsqueda de esta entidad/empresa en los sistemas de la Universidad.

### Actores

#### Actor principal

ACT-PII-001-Gestor

### Precondiciones

Usuario logueado en el sistema con el rol adecuado dentro del módulo PII.

Haber accedido a la gestión de la entidad que necesita ser asociada a la entidad/empresa.

### Garantías de éxito (postcondiciones)

El usuario asocia una entidad/empresa a la entidad donde necesita.

### Escenario principal (flujo básico) - ACT-PII-001-Gestor

1. Se presenta la pantalla donde se pide asociar a la entidad/empresa.
2. El usuario pulsa el botón del formulario para la asociación.
3. Busca la entidad/empresa ([IU-GEN-0080 - Búsqueda de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas) - [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa)) y la selecciona.
4. Pulsa el botón de asociar.

### Extensiones (flujos alternativos)

N/A

### Requisitos especiales

N/A

### Lista de tecnología y variaciones de datos

N/A

### Acciones

|  |  |
| --- | --- |
| ACT-PII-001-Gestor | PII-INVENCION-ASOCIAREMPRESA |

### Casos de uso relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)

### Interfaces relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)