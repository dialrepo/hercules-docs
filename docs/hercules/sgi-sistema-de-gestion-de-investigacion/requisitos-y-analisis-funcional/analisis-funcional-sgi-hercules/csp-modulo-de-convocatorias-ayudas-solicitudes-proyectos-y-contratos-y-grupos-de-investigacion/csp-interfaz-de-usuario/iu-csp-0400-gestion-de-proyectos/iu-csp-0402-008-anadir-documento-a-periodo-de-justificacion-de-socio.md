# IU-CSP-0402-008 - Añadir documento a periodo de justificación de socio

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0402-008 Añadir documento a periodo de justificación de socio******** |
| Ver. objetivo | 0.4.0 |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir documento a periodo de justificación de socio

Formulario que permitirá un documento dentro de un periodo de justificación de un socio de proyecto.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Nombre del documento | Texto corto  Obligatorio | Nombre del documento |
| Documento | Documento  Obligatorio | Documento a adjuntar |
| Tipo de documento | Selector  Texto corto  Opcional | Listado de tipos de documento activos que estén asociados al Modelo de ejecución (ModeloTipoDocumento activos y que no tengan asociada una fase, campo modeloTipoFase = null ) al que se haya vinculado el proyecto en el campo "Modelo ejecución" |
| Visible | Selector  Booleano  Valores: Sí, No  Obligatorio | Tomará los valores Sí/No.  Indica si el documento va a ser visible para los ACT- CSP-001-Investigador que forman parte del equipo del proyecto.  Por defecto que este seleccionado el valor "Sí". |
| Comentarios | Texto largo  Opcional | Comentarios del documento |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Examinar | Muestra pantalla de búsqueda para seleccionar documento a adjuntar |  |  |
| Aceptar | Añade el documento al periodo de justificación del socio colaborador del proyecto | Se muestra el documento en el árbol de la izquierda. | CSP-PRO-E  CSP-PRO-E\_UO |
| Cancelar | Retorna al formulario del periodo de justificación sin salvar los posibles cambios |  |  |