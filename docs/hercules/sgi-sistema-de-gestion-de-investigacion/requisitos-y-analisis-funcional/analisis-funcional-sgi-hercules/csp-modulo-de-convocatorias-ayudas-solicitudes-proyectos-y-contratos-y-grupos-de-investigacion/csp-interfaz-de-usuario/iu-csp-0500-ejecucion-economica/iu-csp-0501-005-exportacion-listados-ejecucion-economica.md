# IU-CSP-0501-005 - Exportación listados ejecución económica

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0501-005 - Exportación listados ejecución económica******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor, ACT-CSP-001-Investigador |
| Frecuencia | Media |

## Formulario Exportación listados ejecución económica

Pantalla que muestra el formulario de exportación de los listados del apartado de Ejecución económica:

* Ejecución presupuestaria - Estado actual
* Ejecución presupuestaria - Gastos
* Ejecución presupuestaria - Ingresos
* Detalle operaciones - Gastos
* Detalle operaciones - Ingresos
* Detalle operaciones - Modificaciones
* Facturas y justificantes - Facturas y gastos
* Facturas y justificantes - Viajes y dietas
* Facturas y justificantes - Personal contratado
* Facturas emitidas

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Formulario de parámetros para generación de informe asociado a un listado de Ejecución económica | | | |
| Título | | Texto  Opcional | Título a incluir en el informe generado.  Por defecto tomará el valor del nombre del apartado que se está exportando. |
| Seleccione el tipo de exportación | | Selector  Texto corto  Obligatorio | Selector con los valores:   * xlsx * csv   Será obligatorio seleccionar un valor. |

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Exportar | Genera el informe de exportación correspondiente. | Invoca al requisito de integración con el SGE para obtener los datos a incluir en el informe. El requisito de integración a invocar se indica en el requisito de cada report. | CSP-EJEC-V  CSP-EJEC-V\_UO  CSP-EJEC-E  CSP-EJEC-E\_UO  CSP-EJEC-INV-VR |

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