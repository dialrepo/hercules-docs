# IU-CSP-0306-005 - Añadir acreditación nivel académico

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0306-005 - Añadir acreditación nivel académico******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador, ACT-CSP-002-InvestigadorExterno, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir acreditación nivel académico

Formulario para adjuntar el documento acreditativo de un nivel académico exigido por la convocatoria

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Nivel académico | Texto  Consulta | Nombre del nivel académico. El valor a mostrar se obtendrá a través del requisito de integración  [REQ-INT-0020-SGP-0019 - Consultar detalle de nivel académico](https://confluence.um.es/confluence/pages/viewpage.action?pageId=108608466) a partir de la referencia almacenada en el campo "nivel académico ref." de la tabla "requisito IP nivel académico" de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") para el cual se va a adjuntar el documento. |
| Obtención posterior a | Fecha  Consulta | Fecha mínima de obtención del nivel académico que exige la convocatoria.  Se corresponde con el campo "fecha mínima nivel académico" de la tabla "requisito IP" de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") |
| Obtención anterior a | Fecha  Consulta | Fecha tope de obtención del nivel académico que exige la convocatoria.  Se corresponde con el campo "fecha máxima nivel académico" de la tabla "requisito IP" de la convocatoria asociada a la solicitud (campo "convocatoria" de la tabla "solicitud") |
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