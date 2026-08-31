# IU-CSP-0540-001-001 - Facturas y justificantes - Facturas y gastos - Detalle

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0540-001-001 - Facturas y justificantes - Facturas y gastos - Detalle******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Ejecución económica - Facturas y justificantes - Facturas y gastos - Detalle

Formulario que muestra el detalle de un justificantes de gasto. Se obtiene del SGE a través de [REQ-INT-0010-SGE-0140 - Detalle justificante-factura](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0140-detalle-justificante-factura)

El detalle de campos a recoger de cada justificante/factura será común a todos ellos y deberá ser configurado en tiempo de implantación, pues esta información debe ser recuperada desde el SGE por medio de los mecanismos de integración disponibles.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Anualidad | Numérico entero genérico | Año de la anualidad |
| Clasificación SGE | Texto corto | Campo recogido a través del requisito de integración [REQ-INT-0010-SGE-0140 - Detalle justificante-factura](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0140-detalle-justificante-factura) |
| Aplicación presupuestaria | Texto corto | Aplicación presupuestaria asociado al gasto |
| Código económico | Texto corto | Código económico asociado al gasto |
| Fecha devengo | Fecha | Fecha de devengo del gasto |
| Campo X | Texto corto | Columnas configuradas en la implantación de acuerdo a lo devuelto por la integración con el sistema de gestión económico [REQ-INT-0010-SGE-0140 - Detalle justificante-factura](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0140-detalle-justificante-factura)  Ejemplos de ellas serían:   * Número de registro * Tipo de operación (si es factura, OK, justificante,…) * Proveedor * Nº de registro del proveedor * Concepto de la Fac/Gasto * Importe Base Imponible * Importe IVA * Fecha contabilización * Fecha de pago * Nº de documento de gasto * Nº de señalamiento |
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
| **ACT-CSP-001-Investigador** | CSP-EJEC-INV-VR | Ver documentación en [CU-CSP-1200-007 - Ver ejecución económica - Investigador (rol principal)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-007-ver-ejecucion-economica-investigador-rol-principal) y [CU-CSP-1200-008 - Ver ejecución económica - Investigador (rol responsable económico)](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1200-gestion-de-proyectos/cu-csp-1200-008-ver-ejecucion-economica-investigador-rol-responsable-economico) |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-EJEC-E, CSP-EJEC-E\_UO, CSP-EJEC-V, CSP-EJEC-V\_UO, CSP-EJEC-INV-VR |