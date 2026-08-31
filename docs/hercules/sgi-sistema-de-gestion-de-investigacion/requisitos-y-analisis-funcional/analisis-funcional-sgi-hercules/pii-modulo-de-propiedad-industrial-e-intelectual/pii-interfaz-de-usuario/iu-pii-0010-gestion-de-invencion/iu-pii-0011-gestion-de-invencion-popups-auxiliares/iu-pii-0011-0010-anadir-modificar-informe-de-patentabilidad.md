# IU-PII-0011-0010 - Añadir-modificar informe de patentabilidad

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0011-0010 - Añadir-modificar informe de patentabilidad |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-001-Gestor |
| Frecuencia | Media |

## Formulario Añadir-modificar informe de patentabilidad

Pantalla que muestra el formulario para añadir un nuevo de informe de patentabilidad a la invención o modificar los datos de un informe ya asociado a ella.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Fecha informe | Fecha (Sin hora)  Obligatorio  Modificable | Fecha a dar al informe de patentabilidad asociado a la invención. |
| Nombre | Texto  Obligatorio  Modificable | Nombre a dar al informe de patentabilidad asociado a la invención. |
| Fichero | Texto  Obligatorio  Solo consulta | Documento de informe de patentabilidad que se asociará a la invención.  Se abrirá el explorador de archivos para poder seleccionar un archivo a asociar como documento de la invención. |
| Resultado | Selector  Obligatorio  Modificable | Lista de opciones con los siguientes valores:   * Favorable * Parcialmente favorable * Desfavorable |
| Entidad creadora | Texto  Obligatorio  Modificable | Entidad creadora del informe de patentabilidad.  Se mostrará la pantalla de búsqueda de Empresas común a todo el SGI y que se obtienen de los sistemas de la Universidad para seleccionar una a asociar con el informe de patentabilidad. |
| Contacto entidad creadora | Texto  Obligatorio  Modificable | Contacto de la entidad creadora del informe de patentabilidad. |
| Contacto examinador | Texto  Obligatorio  Modificable | Contacto del examinador del informe de patentabilidad. |
| Comentarios | Texto Largo  Opcional  Modificable | Comentarios acerca del informe de patentabilidad. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Examinar | Se abre una pantalla para poder adjuntar el documento desde el equipo, haciendo uso para ello del requisito de integración [REQ-INT-0100-SGDOC-0010 - Añadir-modificar documento](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0100-sgdoc-integracion-con-sistema-gestion-documental/req-int-0100-sgdoc-0010-anadir-modificar-documento). |  |
| Buscar (Entidad creadora) | A través del botón Buscar se dará acceso al buscador común [IU-GEN-0080 - Búsqueda de empresa](https://confluence.um.es/confluence/spaces/GES/pages/221381545/IU-GEN-0080+-+B%C3%BAsqueda+de+empresa).   El listado de entidades disponibles se obtendrá del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa) a través del cuál se obtienen las empresas de los sistemas de la Universidad para seleccionar una a asociar con el informe de patentabilidad. |  |
| Añadir | Añade el informe de patentabilidad a la invención. |  |
| Cancelar | Retorna a la pantalla listado de informes de patentabilidad sin salvar los posibles cambios. |  |