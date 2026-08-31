# IU-CSP-0306-001 - Modificar solicitud - Solicitante - Investigador

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0306-001 - Modificar solicitud - Solicitante - Investigador******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | IN PROGRESS |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-001-Investigador |
| Frecuencia | Media |

## Formulario Modificar solicitud - Solicitante - Investigador

Formulario de modificación de solicitud de RRHH, apartado Solicitante, cuando la solicitud es cumplimentada por el propio  ACT-CSP-001-Investigador o cuando es el "tutor/a" de la "solicitud RRHH"

Si se trata del ACT-CSP-001-Investigador que ha cumplimentado la solicitud (el creador de la solicitud es la misma persona que el "solicitante ref" de la tabla "solicitud") podrá modificar la solicitud mientras ésta se encuentre en estado "**Borrador**" y "**Rechazada**". Si se trata del ACT-CSP-001-Investigador que es el "tutor ref" de la tabla "solicitud RRHH" verá todos los campos en modo consulta.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Este apartado "Solicitante" y, en general, todo del bloque "Datos solicitudes RRHH" solamente se hará visible cuando el campo "formulario solicitud" de la tabla "solicitud" toma valor "RRHH" | | |
| Nombre | Texto  Consulta | Campo "nombre" recuperado a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Apellidos | Texto  Consulta | Campo "apellidos" recuperado a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Tipo de documento | Texto  Consulta | Campo "nombre" de la entidad "tipo documento" recuperado a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Número documento | Texto  Consulta | Campo "número documento" recuperado a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Sexo | Texto  Consulta | Campo "nombre" de la "sexo" recuperado a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Fecha de nacimiento | Texto  Consulta | Campo "fecha nacimiento" recuperado a través de [REQ-INT-0020-SGP-0031 - Consultar datos personales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0031-consultar-datos-personales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| País de nacimiento | Texto  Consulta | Campo "nombre" de la entidad "país nacimiento" recuperado a través de [REQ-INT-0020-SGP-0031 - Consultar datos personales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0031-consultar-datos-personales-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Teléfonos | | |
| Teléfono | Texto  Consulta | Campo "telefonos" recuperado a través de [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud".  Cada elemento de la lista de "telefonos" se dibuja en una fila de la tabla. |
| E-mails | | |
| E-mail | Texto  Consulta | Campo "emails" recuperado a través de [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud".  Cada elemento de la lista de "emails" se dibuja en una fila de la tabla. |
| Dirección de contacto | | |
| Dirección | Texto  Consulta | Campo "dirección contacto" recuperado a través de  [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| País | Texto  Consulta | Campo "nombre" de la entidad "país contacto" recuperado a través de  [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Comunidad autónoma | Texto  Consulta | Campo "nombre" de la entidad "comunidad autónoma contacto" recuperado a través de [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Provincia | Texto  Consulta | Campo "nombre" de la entidad "provincia contacto" recuperado a través de  [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud". |
| Localidad | Texto  Consulta | Campo "ciudad contacto" recuperado a través de  [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud"." |
| Código postal | Texto  Consulta | Campo "código postal contacto" recuperado a través de  [REQ-INT-0020-SGP-0032 - Consultar datos de contacto de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0032-consultar-datos-de-contacto-de-persona) para la referenciada indicada en el campo "solicitanteRef" de la tabla "solicitud"." |
|  | | |
| Universidad de origen | Texto  Opcional | Campo para que el investigador pueda introducir el nombre de la Universidad de origen del trabajo.  Campo "universidad" de la tabla "solicitud rrhhh" |
| Área ANEP | Buscador  Texto  Opcional | Muestra la pantalla común [IU-GEN-0120 - Selección de clasificaciones](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103904412) filtrando por el "Tipo de clasificación" igual a "Áreas ANEP" de tal manera que únicamente se podrá seleccionar un nodo hijo del tipo de clasificación "Áreas ANEP" estando inicializado el combo de "Clasificación" con dicho valor y no dejando modificar el valor del combo. El combo estará deshabilitado.  Sólo se permite seleccionar un nodo del árbol de área ANEP.  La referencia de la área ANEP recuperada se almacenará en el campo "área ANEP ref" de la tabla "solicitud rrhh". |
| Mensaje informativo | Texto largo | Este mensaje solo se mostrará si la solicitud se encuentra en estado borrador (campo "estado" de la tabla "solicitud").  Se mostrará con los estilos de aviso informativo el siguiente mensaje "Para que la solicitud pueda ser validad por su tutor/a debe cambiar el estado de la misma a "Solicitada"". |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Buscar (área ANEP) | Abre la pantalla del buscador de la clasificación de "Áreas ANEP" | Muestra la pantalla común [IU-GEN-0120 - Selección de clasificaciones](https://confluence.um.es/confluence/pages/viewpage.action?pageId=103904412) filtrando por el "Tipo de clasificación" igual a "Áreas ANEP" de tal manera que únicamente se podrá seleccionar un nodo hijo del tipo de clasificación "Áreas ANEP" estando inicializado el combo de "Clasificación" con dicho valor y no dejando modificar el valor del combo. El combo estará deshabilitado.  Sólo se permite seleccionar un nodo del árbol de área ANEP. | No se necesita permiso adicional para realizar esta búsqueda |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modificar la solicitud con la información introducida en el formulario.  Al guardar una solicitud se guardar la información de todos los apartados de definición de la solicitud. | Ver precondiciones en [CU-CSP-1100-001 Modificar solicitud - Guardar](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-1100-gestion-de-solicitudes/cu-csp-1100-001-modificar-solicitud-guardar). | CSP-SOL-INV-ER |
| Cancelar | Retorna al listado de Solicitud sin salvar los posibles cambios.  Al cancelar una solicitud se cancela la información de todas las pestañas de la pantalla, sin salvar los posibles cambios. |  |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-001-Investigador | CSP-SOL-INV-ER |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SOL-INV-ER |