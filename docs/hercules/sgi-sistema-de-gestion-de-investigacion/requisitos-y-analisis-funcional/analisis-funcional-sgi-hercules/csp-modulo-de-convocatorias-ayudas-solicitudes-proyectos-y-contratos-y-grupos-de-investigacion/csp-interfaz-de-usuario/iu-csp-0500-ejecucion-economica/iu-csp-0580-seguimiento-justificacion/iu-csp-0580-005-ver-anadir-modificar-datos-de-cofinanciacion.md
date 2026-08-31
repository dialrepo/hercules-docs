# IU-CSP-0580-005 - Ver-añadir-modificar datos de cofinanciación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0580-005 - Ver-añadir-modificar datos de cofinanciación******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado |  |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-003-Gestor, ACT-CSP-004-Administrador, ACT-CSP-005-Visor |
| Frecuencia | Media |

## Formulario Detalle cofinanciación

Formulario que permitirá añadir/modificar o ver los datos de la cofinanciación de un gasto

|  |  |  |
| --- | --- | --- |
| **Caso 1: Con buscador de entidades**      **Caso 2: Con listado de entidades** | | |
| Nombre | Tipo | Características / Notas |
| Convocatoria cofinanciación | Buscador  Texto  Opcional | Convocatoria que cofinancia el gasto.  Si se accede al formulario par "ver" o "modificar" un dato de cofinanciación:   * Se mostrará el título de la convocatoria (campo "título" de la tabla "convocatoria") para la referencia establecida por el campo "convocatoria ref" de la tabla "cofinanciación gasto justificación"   Para indicar un nuevo valor:   * La convocatoria se seleccionará a través del buscador común de convocatorias (Acción "Buscar convocatoria"). * La convocatoria seleccionada se almacenará en el campo "convocatoria ref" de la tabla "cofinanciación gasto justificación" * Es un campo opcional |
| Proyecto cofinanciación | Buscador  Texto  Opcional | Proyecto que cofinancia el gasto.  Si se accede al formulario par "ver" o "modificar" un dato de cofinanciación:   * Se mostrará el título del proyecto (campo "título" de la tabla "proyecto") para la referencia establecida por el campo "proyecto ref" de la tabla "cofinanciación gasto justificación"   Para indicar un nuevo valor:   * El proyecto se seleccionará a través del buscador común de convocatorias (Acción "Buscar proyecto"). * El proyecto seleccionado se almacenará en el campo "proyecto ref" de la tabla "cofinanciación gasto justificación" * Es un campo opcional |
| Entidad cofinanciación | Buscador o Selector  Texto  Obligatorio | Entidad que cofinancia el gasto.  Para indicar un nuevo valor:   * Si se ha seleccionado un proyecto en el campo previo "proyecto cofinanciación":   + Este campo se mostrará como un selector que listará los nombres de todas las empresas financiadoras del proyecto seleccionado. Las entidades financiadoras del proyecto se recuperarán de la tabla "proyecto entidad financiadora" para el id del proyecto seleccionado. Se mostrará el nombre de la entidad, recuperado a través de servicio de integración [REQ-INT-0015-SGEMP-0030 - Consultar datos generales de empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/int-requisitos-de-integracion/req-int-0015-sgemp-integracion-con-sistema-de-gestion-de-empresas/req-int-0015-sgemp-0030-consultar-datos-generales-de-empresa) a partir del campo "entidad ref" * Si no se ha seleccionado un proyecto:   + La entidad se seleccionará a través del buscador común de empresas (Acción "Buscar entidad") * La entidad seleccionada, de una u otra forma, se almacenará en el campo "entidad ref" de la tabla "cofinanciación gasto justificación" * Es un campo obligatorio |
| Importe cofinanciación | Económico  Obligatorio | Importe cofinanciado por la convocatoria/proyecto y/o entidad indicadas  Es un campo obligatorio  Se corresponde con el campo "importe" de la tabla "cofinanciación gasto justificación" |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Buscar convocatoria | Permite buscar una convocatoria | Muestra el buscador [IU-GEN-0050 - Búsqueda de convocatorias](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0050-busqueda-de-convocatorias)  La referencia de la convocatoria seleccionada se almacenará en el campo "convocatoria ref" de la tabla "cofinanciación gasto justificación" |
| Buscar proyecto | Permite buscar un proyecto | Muestra el buscador [IU-GEN-0030 - Búsqueda de proyectos](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0030-busqueda-de-proyectos)  La referencia del proyecto seleccionado se almacenará en el campo "proyecto ref" de la tabla "cofinanciación gasto justificación" |
| Buscar entidad | Permite buscar una entidad | Muestra el buscador [IU-GEN-0080 - Búsqueda de empresas](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0080-busqueda-de-empresas)  La referencia de la entidad seleccionado se almacenará en el campo "entidad ref" de la tabla "cofinanciación gasto justificación" |

### Botones generales de la pantalla

| Acciones | Descripción | Enlace CU. | Permiso |
| --- | --- | --- | --- |
| Aceptar | Almacena los cambios introducidos | Inserta o actualiza el registro correspondiente sobre la tabla "cofinanciación gasto justificación"  Tras realizar la operación retorna al detalle del gasto [IU-CSP-0580-004 - Ver-modificar gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-004-ver-modificar-gasto-justificado) | CSP-SJUS-E  CSP-SJUS-E\_UO |
| Cancelar | Descarta los cambios introducidos | Cierra la ventana y retorna a [IU-CSP-0580-004 - Ver-modificar gasto justificado](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0500-ejecucion-economica/iu-csp-0580-seguimiento-justificacion/iu-csp-0580-004-ver-modificar-gasto-justificado) sin realizar ningún cambio |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-003-Gestor | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-004-Administrador** | CSP-SJUS-E, CSP-SJUS-E\_UO |
| **ACT-CSP-005-Visor** | CSP-SJUS-V, CSP-SJUS-V\_UO |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-SJUS-E, CSP-SJUS-E\_UO, CSP-SJUS-V, CSP-SJUS-V\_UO |