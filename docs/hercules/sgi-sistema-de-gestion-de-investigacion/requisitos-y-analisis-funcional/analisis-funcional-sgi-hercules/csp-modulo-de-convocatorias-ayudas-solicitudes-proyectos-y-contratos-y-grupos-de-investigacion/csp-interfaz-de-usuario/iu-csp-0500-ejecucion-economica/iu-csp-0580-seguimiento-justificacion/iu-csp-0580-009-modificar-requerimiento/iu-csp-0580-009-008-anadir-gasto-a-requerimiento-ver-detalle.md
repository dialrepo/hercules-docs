# IU-CSP-0580-009-008 - Añadir gasto a requerimiento - Ver detalle

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0580-009-008 - Añadir gasto a requerimiento - Ver detalle******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Añadir gasto a requerimiento - Ver detalle

Formulario que permite ver el detalle de un gasto desde la pantalla de añadir gasto  requerimiento

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Detalle del gasto, obtenido a través de requisito de integración [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado) pasando como parámetro el "gasto ref" e "ID justificación" para el registro del listado de gastos desde el que se accede al detalle | | |
| Proyecto SGI | Texto | Identificador interno del proyecto SGI al que pertenece el ID de justificación en el que ha sido incluido del gasto.  El valor de este campo será obtenido a partir del valor "identificador justificación" devuelto en [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado) para el gasto desde el que se accede al detalle. Este valor de "identificador justificación" se buscará en la tabal "proyecto periodo justificación" para alguno de los proyectos SGI con los que se relaciona el proyecto SGE desde el que se accede a la ejecución económica ( esta relación se encuentra en la tabla "proyecto proyecto SGE"). |
| ID justificación | Texto | Campo "identificador justificación" devuelto por [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado) para el gasto desde el que se accede al detalle. |
| Campo X | Tipo de acuerdo al campo recuperado de la función de integración | Listado de campos variables devueltos por [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado)  Se mostrará un campo en cada fila de la pantalla, en el formato "nombre campo":" valor del campo |
| Listado de documentos del gasto. Documentos del gasto recuperados a través de [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado). Se listarán todos los documentos mostrando el nombre recuperado y posibilitando la descarga del mismo | | |
| Nombre | Texto | Campo "nombre documento" recuperado de [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado) |
| Descargar | Icono de acción | Acción "descargar" |

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Descargar documento | Permite la descarga del documento | Se descarga el documento recuperado de [REQ-INT-0010-SGE-0166 - Detalle gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0010-sge-integracion-con-sistema-de-gestion-economica/req-int-0010-sge-0166-detalle-gasto-justificado) | CSP-SJUS-V  CSP-SJUS-V\_UO |
| Cancelar | Cierra la ventana de detalle del gasto | Se cierra la ventana de detalle del gasto, retornando a  [IU-CSP-0580-009-007 - Añadir gasto a requerimiento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-009-modificar-requerimiento/iu-csp-0580-009-007-anadir-gasto-a-requerimiento) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-004-Administrador** | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-005-Visor** | CSP-SJUS-V, CSP-SJUS-V\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SJUS-E, CSP-SJUS-E\_UO, CSP-SJUS-V, CSP-SJUS-V\_UO |