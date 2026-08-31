# IU-ETI-0040-003 Modificar evaluador

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0040-003 Modificar evaluador******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Modificar evaluador

Pantalla compuesta por dos formularios:

* Datos generales
* Conflicto de intereses

### Datos generales

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Evaluador | Botón Buscar  Texto corto  Obligatorio | Nombre y apellidos del evaluador.  Se recupera a través de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona). Se muestra en modo solo consulta. |
| Comité | Desplegable  abreviatura  Obligatorio | Desplegable con los valores:    * CEISH * CEEA * CEIAB   Se muestra en modo solo consulta. Una vez creado no se puede modificar. |
| Fecha alta | fecha  Obligatorio | Calendario para marcar el día de alta. |
| Fecha baja | fecha  Obligatorio | Calendario para marcar el día de baja. Debe de ser mayor que la fecha de alta. |
| Cargo | Desplegable  Texto corto  Obligatorio | Desplegable con los valores:    * Presidente * Vocal * Secretario |
| Resumen | Texto  Opcional | Caja de texto para explicar la actividad que realiza. |

### Conflicto de intereses

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de usuarios con conflicto de interés | | |
| NIF/NIE | Texto corto | NIF/NIE de la persona con el que tiene un conflicto de interés, por lo que no podrá estar en una evaluación de una memoria en la que dicha persona forme parte del equipo. Recuperado por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona). |
| Nombre y apellidos | Texto | Nombre y apellidos de la persona con la que tiene un conflicto de interés, por lo que no podrá estar en una evaluación de una memoria en la que dicha persona forme parte del equipo. Recuperado por medio de [REQ-INT-0020-SGP-0030 - Consultar datos generales de persona](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0020-sgp-integracion-con-sistema-de-gestion-de-personas/req-int-0020-sgp-0030-consultar-datos-generales-de-persona). |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Añadir | Se añade una relación de conflicto de interés con la persona. [IU-ETI-0040-004 Conflicto de intereses - Añadir](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-interfaz-de-usuario/iu-eti-0040-gestion-de-evaluadores/iu-eti-0040-004-conflicto-de-intereses-anadir) | [CU-ETI-0040-003 - Alta usuario conflicto de intereses](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0040-gestion-de-evaluadores/cu-eti-0040-003-alta-usuario-conflicto-de-intereses) | ETI-EVR-E |
| Eliminar | Se elimina la relación con la persona. |  | ETI-EVR-E |

### Botones generales a la pantalla

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Modifica los datos del evaluador con la información introducida en el formulario | [CU-ETI-0040-002 - Alta/Modificar Evaluador](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/eti-modulo-de-etica/eti-casos-de-uso/cu-eti-0040-gestion-de-evaluadores/cu-eti-0040-002-altamodificar-evaluador) | ETI-EVR-E |
| Cancelar | Retorna al listado de Evaluadores sin salvar los posibles cambios. |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-ACT-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-ACT-V, ETI-ACT-E |