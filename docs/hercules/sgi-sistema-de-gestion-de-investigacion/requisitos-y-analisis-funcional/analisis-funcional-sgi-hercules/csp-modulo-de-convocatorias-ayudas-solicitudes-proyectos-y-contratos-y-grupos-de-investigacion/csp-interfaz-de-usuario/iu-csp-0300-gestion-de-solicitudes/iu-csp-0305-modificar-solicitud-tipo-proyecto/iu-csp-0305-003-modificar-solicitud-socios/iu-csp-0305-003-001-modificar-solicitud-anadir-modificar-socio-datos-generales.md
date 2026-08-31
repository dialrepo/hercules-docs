# IU-CSP-0305-003-001 - Modificar solicitud - Añadir-modificar socio - Datos generales

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0303-003-001 - Modificar solicitud - Añadir-Modificar socio - Datos generales******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador |
| Frecuencia | Media |

## Formulario Modificar solicitud - Añadir-modificar socio - Datos generales

Formulario que permite añadir un socio o modificar los datos generales del mismo durante el proceso de modificación de una solicitud de proyecto.

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
| Nombre | | Tipo | Características / Notas |
| Socio (nombre, identificador fiscal) | | Referencia  Texto  Obligatorio | Nombre o identificador fiscal de la Empresa que participará como socio colaborador en el proyecto propuesto en la solicitud.  Cuando la solicitud ya tenga un socio asociado, el nombre del socio seleccionado será recuperado a través de [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) a partir del campo "empresa ref" de la tabla "solicitud proyecto socio".  La búsqueda se resolverá a través del buscador común de empresas [IU-GEN-0100-0080 - Búsqueda de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas) que precisará del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa). |
| Rol del socio en el proyecto | | Selector  Texto corto  Obligatorio | Rol con el que participará el socio colaborador. Se deberá indicar obligatoriamente un rol para cada uno de los socios colaboradores. Los roles disponibles serán los configurados en la tabla "Rol socio".  El identificador del valor seleccionado se almacenará en el campo "rol socio" de la tabla "solicitud proyecto socio". |
| Número de investigadores del equipo del socio | | Numérico entero genérico  Opcional | Número de investigadores que forman parte del equipo del socio.  Se corresponde con el campo "num. investigadores" de la tabla "solicitud proyecto socio". |
| Importe presupuestado | | Económico  Opcional | Importe presupuestado por el socio para el desarrollo de su parte del proyecto.  Se corresponde con el campo "importe presupuestado" de la tabla "solicitud proyecto socio". |
| Importe solicitado | | Económico  Opcional | Importe solicitado por el socio para el desarrollo de su parte del proyecto dentro de los términos de la convocatoria.  Se corresponde con el campo "importe solicitado" de la tabla "solicitud proyecto socio". |
| Periodo previsto de participación | Mes inicial | Numérico entero genérico  Opcional | Mes de inicio de la colaboración del socio en el proyecto.  Se corresponde con el campo "mes inicio" de la tabla "solicitud proyecto socio". |
| Mes final | Numérico entero genérico  Opcional | Mes de fin de la colaboración del socio en el proyecto.  Se corresponde con el campo "mes fin" de la tabla "solicitud proyecto socio". |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Buscar | Muestra la pantalla de búsqueda para seleccionar un miembro. | La búsqueda se resolverá a través del buscador común de empresas [IU-GEN-0100-0080 - Búsqueda de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas) que requerirá del requisito de integración [REQ-INT-0015-SGEMP-0020 - Buscar empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0020-buscar-empresa)  En el caso de que el buscador no devolviese la  empresa que se desea añadir como socio del proyecto se podrá solicitar el registro de la nueva empresa, utilizando para ello el formulario de solicitud de alta [IU-GEN-0081 - Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0081-solicitar-alta-de-empresa) que cumple con el requisito [REQ-INT-0015-SGEMP-0040 - Solicitar alta de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0040-solicitar-alta-de-empresa). Este registro solo podrá ser provocado por ACT-CSP-004-Administrador o ACT-CSP-003-Gestor.  En el caso de que el buscador devolviese la empresa que se desea añadir como socio del proyecto, pero se quisiera realizar alguna modificación en sus datos, se podrá solicitar dicha modificación, utilizando para ello el formulario de solicitud de modificación IU-GEN-0082 - Ver detalle - Solicitar modificación de empresa que cumple con el requisito [REQ-INT-0015-SGEMP-0045 - Solicitar modificación de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0050-solicitar-modificacion-de-empresa)[.](https://confluence.um.es/confluence/pages/viewpage.action?pageId=89621944) Esta modificación solo podrá ser provocado por ACT-CSP-004-Administrador o ACT-CSP-003-Gestor. |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Guardar | Crea el socio con la información introducida en el formulario. | Al guardar un socio se guardar la información de todos los apartados de definición del socio.  Los datos recogidos en este formulario afectan todos a la tabla "solicitud proyecto socio" |
| Cancelar | Retorna al listado de Socios sin salvar los posibles cambios.  Al cancelar un socio se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |