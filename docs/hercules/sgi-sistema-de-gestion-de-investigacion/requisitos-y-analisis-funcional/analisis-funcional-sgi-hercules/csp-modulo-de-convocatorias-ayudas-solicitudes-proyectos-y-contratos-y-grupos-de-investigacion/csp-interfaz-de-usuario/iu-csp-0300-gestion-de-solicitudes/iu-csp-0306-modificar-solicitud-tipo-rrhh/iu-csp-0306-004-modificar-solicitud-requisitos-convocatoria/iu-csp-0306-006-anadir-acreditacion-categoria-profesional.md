# IU-CSP-0306-006 - Añadir acreditación categoría profesional

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0306-006 - Añadir acreditación categoría profesional******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-002-InvestigadorExterno, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir acreditación categoría profesional

Formulario para adjuntar el documento acreditativo de una categoría profesional exigida por la convocatoria

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Nivel académico | Texto  Consulta | Nombre de la categoría profesional. El valor a mostrar se obtendrá a través del requisito de integración [REQ-INT-0020-SGP-0017 - Consultar detalle de categoría profesional](https://confluence.um.es/confluence/pages/viewpage.action?pageId=108608461) a partir de la referencia almacenada en el campo "categoría profesional ref." de la tabla "requisito IP categoría"  de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") para la cual se va a adjuntar el documento. |
| Obtención posterior a | Fecha  Consulta | Fecha más antigua en la que puede haber sido obtenida la categoría para poder optar a la convocatoria  Se corresponde con el campo "fecha mínima categoría profesional" de la tabla "requisito IP" de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") |
| Obtención anterior a | Fecha  Consulta | Fecha tope en la que puede haber sido obtenida la categoría para poder optar a la convocatoria  Se corresponde con el campo "fecha máxima categoría profesional" de la tabla "requisito IP" de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") |
| Adjunte el documento acreditativo | Examinar fichero  Obligatorio | Documento a adjuntar |

| Acciones | Descripción | Descripción C.U. | Permisos |
| --- | --- | --- | --- |
| Aceptar | Añade la acreditación al requisito de la convocatoria |  | CSP-SOL-INV-ER  CSP-SOL-E  CSP-SOL-E\_UO |
| Cancelar | Retorna al formulario de la solicitud, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-001-Investigador | CSP-SOL-INV-ER |
| **ACT-CSP-003-Gestor** | CSP-SOL-E, CSP-SOL-E\_UO |
| **ACT-CSP-004-Administrador** | CSP-SOL-E, CSP-SOL-E\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SOL-INV-ER, CSP-SOL-V\_UO, CSP-SOL-E, CSP-SOL-E\_UO |