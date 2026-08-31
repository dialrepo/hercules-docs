# IU-EER-0010-0010-001 - Crear empresa de explotación de resultados - Datos Generales

|  |  |
| --- | --- |
| Cod. IU | IU-EER-0010-0010-001 - Crear empresa de explotación de resultados - Datos Generales |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-EER-001-Gestor |
| Frecuencia | Media |

## Formulario Crear empresa de explotación de resultados - Datos generales

Pantalla que muestra el formulario de alta de una empresa de explotación de resultados. Apartado de datos generales de una nueva empresa.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Formulario de datos generales de una empresa de explotación de resultados. | | |
| Fecha solicitud | Fecha  Obligatorio | Fecha de la solicitud de creación de la empresa de explotación de resultados. |
| Tipo empresa | Selector  Texto corto  Obligatorio | Tipo de la empresa de explotación de resultados.  Listado con las opciones:   * EBT (Empresa de base tecnológica) * EINCNT (Empresa intensiva en conocimiento no tecnológico) |
| Estado | Selector  Texto corto  Obligatorio | Listado con las opciones:   * En tramitación * No aprobada * Activa * Sin actividad * Disuelta |
| Solicitante | Texto  Opcional | Solicitante que consta en la solicitud de creación de la empresa de explotación de resultados.  Campo de búsqueda de personas en los sistemas de la Universidad. |
| Nombre / Razón social | Texto  Obligatorio | Nombre / Razón social de la empresa de explotación de resultados.  Se podrá informar únicamente si el campo Entidad no tiene valor, en otro caso, no se podrá informar. |
| Entidad | Texto  Opcional | Campo de búsqueda de entidades/empresas en los sistemas de la universidad. |
| Objeto social | Texto largo  Obligatorio | Objeto social de la empresa de explotación de resultados. |
| Conocimiento / Tecnología | Texto largo  Obligatorio | Descripción del conocimiento o tecnología de la empresa de explotación de resultados.  En el campo se mostrará una u otra etiqueta en función del tipo de empresa seleccionado en el campo "Tipo":   * Si se selecciona el tipo EBT o aún no se ha seleccionado ningún tipo, se mostrará la etiqueta "Tecnología". * Si se selecciona el tipo EINCNT, se mostrará la etiqueta "Conocimiento". |
| Nº de protocolo | Texto  Opcional | Número de la notaría asociado a la constitución o a la incorporación de la Universidad a la empresa de explotación de resultados. |
| Notario | Texto  Opcional | Datos del notario que intervino en la constitución o a la incorporación de la Universidad a la empresa de explotación de resultados. |
| Fecha constitución | Fecha  Opcional | Fecha de constitución de la empresa de explotación de resultados. |
| Fecha aprobación CG | Fecha  Opcional | Fecha de aprobación en Consejo de Gobierno de la constitución o incorporación de la Universidad a la empresa de explotación de resultados. |
| Fecha incorporación | Fecha  Opcional | Fecha de incorporación de la Universidad a la empresa de explotación de resultados. |
| Fecha desvinculación | Fecha  Opcional | Fecha de desvinculación de la Universidad de la empresa de explotación de resultados. |
| Fecha cese | Fecha  Opcional | Fecha de cese de la empresa de explotación de resultados. |
| Observaciones | Texto largo  Opcional | Observaciones que se quieran aportar a la empresa de explotación de resultados. |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Buscar (solicitante) | A través del botón Buscar se dará acceso al buscador común [IU-GEN-0060 - Búsqueda de personas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas) que hará uso del requisito de integración [REQ-INT-0020-SGP-0020 - Buscar persona en un listado de colectivos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0020-buscar-persona-en-un-listado-de-colectivos). Se le deberán pasar a este buscador el listado de colectivos asociados al tipo de colectivo "Miembro Equipo de Empresa de Explotación de Resultados".  En el caso de que el buscador no devolviese a la persona que se desea añadir como solicitante de la creación/incorporación de la Universidad de la empresa de explotación de resultados, se podrá realizar la solicitud de registro a través del requisito de integración [REQ-INT-0020-SGP-0050 - Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0050-solicitar-alta-de-persona)  desencadenado desde la pantalla de solicitar alta de persona [IU-GEN-0061- Solicitar alta de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0061-solicitar-alta-de-persona) a la que se accede desde el propio formulario de búsqueda [IU-GEN-0060 - Búsqueda de personas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas).  En el caso de que el buscador devolviese a la persona que se desea añadir como solicitante de la creación/incorporación de la Universidad de la empresa de explotación de resultados, pero se quisiera realizar alguna modificación en sus datos, se podrá solicitar dicha modificación, utilizando para ello el formulario de solicitud de modificación [IU-GEN-0062 - Ver detalle - Solicitar modificación de persona](/confluence/pages/createpage.action?spaceKey=HERCULES&title=IU-GEN-0062+-+Ver+detalle+-+Solicitar+modificaci%C3%B3n+de+persona&linkCreation=true&fromPageId=597852931), que cumple con el requisito de integración [REQ-INT-0020-SGP-0060 - Solicitar modificación de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0060-solicitar-modificacion-de-persona) y a la que se accede desde el propio formulario de búsqueda [IU-GEN-0060 - Búsqueda de personas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0060-busqueda-de-personas).  En el caso de encontrarse la persona y de seleccionarse en el formulario de búsqueda, se visualizarán los datos del solicitante seleccionado en el campo Solicitante de la empresa de explotación de resultados. |  | No se necesita permiso para mostrar la pantalla de búsqueda de personas. |
| Buscar (entidad) | A través del botón Buscar se dará acceso al buscador de empresas/entidades común a todo el SGI [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas).  El listado de entidades disponibles se obtendrá del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa), que realizará la búsqueda de entidades en los sistemas de la Universidad. |  | No se necesita permiso para mostrar la pantalla de búsqueda de empresas. |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar empresa de explotación de resultados | Crea la empresa de explotación de resultados.  Al guardar la Empresa, se guardará la información de todos los formularios de la pantalla de creación de empresa de explotación de resultados.  Validaciones de obligatoriedad en este formulario específico:   * Fecha solicitud * Tipo empresa * Estado * Nombre / Razón social (solo si no se ha seleccionado una entidad en el campo "Entidad") * Objeto social * Conocimiento / Tecnología   Además, se validará que el campo "Estado" no se pueda informar con el valor "Activa" si no se ha informado el campo "Entidad". |  | EER-EER-C |
| Cancelar | Retorna al listado de empresas de explotación de resultados sin salvar los posibles cambios.  Al cancelar la creación de la empresa de explotación de resultados, se cancela el guardado de la información de todo los formularios de la pantalla. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-EER-001-Gestor | EER-EER-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | EER-EER-C |

Se aplican las mismas restricciones para todos los elementos del árbol de navegación bajo este path.