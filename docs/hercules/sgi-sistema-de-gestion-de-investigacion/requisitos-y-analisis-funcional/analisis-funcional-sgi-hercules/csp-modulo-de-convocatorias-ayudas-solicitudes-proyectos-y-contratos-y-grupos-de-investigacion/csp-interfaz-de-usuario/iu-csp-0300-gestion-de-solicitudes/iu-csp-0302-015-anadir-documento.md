# IU-CSP-0302-015 - Añadir documento

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0302-015 - Añadir documento******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT- CSP-001-Investigador, ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Añadir documento

Formulario que permite añadir un documento a la solicitud.

Los documentos se añaden desde la pestaña de "Documentos" de la solicitud [IU-CSP-0304-009 - Modificar Solicitud - Documentos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0300-gestion-de-solicitudes/iu-csp-0304-modificar-solicitud/iu-csp-0304-009-modificar-solicitud-documentos)

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Nombre del documento | Texto corto  Obligatorio | Nombre del documento |
| Tipo de documento | Selector  Texto  Opcional | Nombre del tipo de documento. Procedente de la tabla "Tipo de documento" a través del identificador del tipo de documento. Los tipos disponibles serán los tipos de documento asociados a la fase de presentación de solicitudes configurada en la pantalla de "Configuración Solicitud de la Convocatoria". En caso de estar creando una solicitud no vinculada a una convocatoria del SGI o que no se haya definido dicha fase se mostrará el combo vacío.  Aunque la solicitud esté vinculad a una convocatoria del SGI, no será obligatorio que un documento subido tenga obligatoriamente uno de los tipos de documentos del listado (podrá seleccionarse el valor vacío sobre él). En este caso el documento será uno de los que se visualice en el árbol bajo la rama genérica "sin tipo documento" |
| Documento | Documento  Obligatorio | Documento a adjuntar |
| Comentarios | Texto largo  Opcional | Indicaciones u observaciones sobre el documento subido almacenado de la tabla "Solicitud Documento" |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Acción "Subir documento" | Muestra pantalla de búsqueda para seleccionar documento a adjuntar, sobrescribiendo el fichero previo |  |
| Aceptar | Añade el documento a la solicitud, se visualiza en el árbol |  |
| Cancelar | Retorna al formulario de la solicitud, sin salvar los posibles cambios |  |