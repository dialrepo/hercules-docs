# IU-CSP-0402-011 - Añadir documento a periodo de seguimiento científico

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0402-011 - Añadir documento a periodo de seguimiento científico******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir documento a periodo de seguimiento científico

Formulario que permitirá añadir un documento a un periodo de seguimiento científico del proyecto.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario para añadir documento a periodo de seguimiento científico | | |
| Nombre del documento | Texto corto  Obligatorio | Nombre del documento |
| Documento | Documento  Obligatorio | Documento a adjuntar |
| Tipo de documento | Selector  Texto corto  Opcional | Listado de tipos de documento activos que estén asociados al Modelo de ejecución (tabla "modelo tipo documento" activos y que no tengan asociada una fase, campo "modelo tipo fase" = null ) al que se haya vinculado el proyecto en el campo "Modelo ejecución" |
| Visible | Selector  Booleano  Valores: Sí, No  Obligatorio | Tomará los valores Sí/No.  Indica si el documento va a ser visible para los ACT- CSP-001-Investigador que forman parte del equipo del proyecto.  Por defecto que este seleccionado el valor "Sí". |
| Comentarios | Texto largo  Opcional | Comentarios del documento |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Examinar | Muestra pantalla de búsqueda para seleccionar documento a adjuntar |  |  |
| Aceptar | Añade el documento al periodo de seguimiento científico del proyecto | Se muestra el documento en el árbol de la izquierda. | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al formulario del periodo de seguimiento sin salvar los posibles cambios |  |  |