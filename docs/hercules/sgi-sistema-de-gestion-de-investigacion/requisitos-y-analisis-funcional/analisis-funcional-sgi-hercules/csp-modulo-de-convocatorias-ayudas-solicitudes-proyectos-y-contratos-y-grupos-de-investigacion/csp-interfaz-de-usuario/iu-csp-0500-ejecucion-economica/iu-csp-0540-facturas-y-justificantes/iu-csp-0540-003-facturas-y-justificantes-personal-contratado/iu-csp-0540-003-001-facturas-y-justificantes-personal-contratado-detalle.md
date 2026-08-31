# IU-CSP-0540-003-001 - Facturas y justificantes - Personal contratado - Detalle

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0540-003-001 - Facturas y justificantes - Personal contratado - Detalle******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Ejecución económica - Personal contratado - Facturas y gastos - Detalle

Formulario que muestra el detalle de un justificantes de gasto asociado a una nómina. Se obtiene del SGE a través de [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado)

El detalle de campos a recoger de cada justificante/factura será común a todos ellos y deberá ser configurado en tiempo de implantación, pues esta información debe ser recuperada desde el SGE por medio de los mecanismos de integración disponibles.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Anualidad | Numérico entero genérico | Año de la anualidad. Recuperado a través de  [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado) |
| Clasificación SGE | Texto corto | Clasificación del gasto según SGE. Recuperado a través de [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado) |
| Aplicación presupuestaria | Texto corto | Aplicación presupuestaria asociado al gasto, recuperada a través de [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado) |
| Código económico | Texto corto | Código económico asociado al gasto, recuperado a través de [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado) |
| Fecha devengo | Fecha | Fecha de devengo del gasto, recuperado a través de [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado) |
| Campo X | Texto corto | Columnas configuradas en la implantación de acuerdo a lo devuelto por la integración con el sistema de gestión económico, [REQ-INT-0010-SGE-0142 - Detalle personal contratado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0142-detalle-personal-contratado)  Ejemplos de ellas serían:   * Nº documento identificación (del contratado) * Nombre y apellidos (del contratado) * Concepto (seguridad social o retribuciones) * Fecha contabilización * Fecha pago * Importe * Fecha inicio del contrato * Fecha fin del contrato * Categoría laboral * Jornada semanal o diaria |
| Listado de documentos devueltos por el sistema de gestión económico | | |
| Nombre | Texto | Nombre del documento |
| Descargar fichero | Icono de "descargar" | Acción de descargar el fichero |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Descargar fichero | Se hace una llamada al SGE para obtener el contenido del fichero (el binario) | Se recupera el contenido del fichero en binario para que el usuario lo pueda abrir o guardar el documento.  Se obtiene del SGE a través de [REQ-INT-0010-SGE-0104 - Descargar Binario documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0104-descargar-binario-documento) | CSP-EJEC-E  CSP-EJEC-E\_UO  CSP-EJEC-V  CSP-EJEC-V\_UO  CSP-EJEC-INV-VR |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |  |
| --- | --- | --- |
| ACT-CSP-003-Gestor | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-004-Administrador** | CSP-EJEC-E, CSP-EJEC-E\_UO |  |
| **ACT-CSP-005-Visor** | CSP-EJEC-V, CSP-EJEC-V\_UO |  |
| **ACT-CSP-001-Investigador** | CSP-EJEC-INV-VR | Ver documentación en [CU-CSP-1200-007 - Ver ejecución económica - Investigador (rol principal)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-007-ver-ejecucion-economica-investigador-rol-principal) y  [CU-CSP-1200-008 - Ver ejecución económica - Investigador (rol responsable económico)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-008-ver-ejecucion-economica-investigador-rol-responsable-economico) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-EJEC-E, CSP-EJEC-E\_UO, CSP-EJEC-V, CSP-EJEC-V\_UO, CSP-EJEC-INV-VR |