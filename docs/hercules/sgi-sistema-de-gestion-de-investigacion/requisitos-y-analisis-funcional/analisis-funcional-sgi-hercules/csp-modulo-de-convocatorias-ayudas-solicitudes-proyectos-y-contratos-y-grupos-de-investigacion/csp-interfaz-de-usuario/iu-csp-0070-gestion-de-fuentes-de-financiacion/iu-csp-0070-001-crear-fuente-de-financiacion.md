# IU-CSP-0070-001 - Crear fuente de financiación

|  |  |
| --- | --- |
| Cod. IU | ********IU-CSP-0070-001 Crear fuente de financiación******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-CSP-004-Administrador, ACT-CSP-003-Gestor |
| Frecuencia | Media |

## Formulario Crear fuente de financiación

Formulario de creación de una fuente de financiación

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Creación de fuente de financiación | | |
| Nombre | Texto corto  Obligatorio | Nombre identificativo de la fuente de financiación. Debe comprobarse la unicidad por el campo "nombre" entre los elementos activos (campo "activo"= true) |
| Descripción | Texto  Opcional | Descripción de la fuente de financiación. De introducción libre y no obligatoria. |
| Ámbito geográfico | Selector  Obligatorio | Los valores listados serán los incluidos en la tabla "Tipo ámbito geográfico" que tengan el campo "activo = true". Esta tabla no dispone de configuración habilitada en el SGI. Es una tabla precargada en periodo de implantación que inicialmente tomará los valores   * Propio * Local * Autonómico * Nacional * Europeo * Internacional |
| Origen | Selector  Obligatorio | Los valores listados serán los incluidos en la tabla "Tipo origen fuente financiación" que tengan el campo "activo = true". Esta tabla no dispone de configuración habilitada en el SGI. Es una tabla precargada en periodo de implantación que inicialmente tomará los valores:   * Público * Privado |
| Fondo estructural | Selector  Booleano  Valores: sí, no  Obligatorio | Tomará valor true o false, en función del check o selector con el que se muestre en pantalla el dato booleano (sí/no). |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Guardar | Inserta un nuevo registro con los datos recogidos en el formulario | Se debe de comprobar que se haya indicado un valor para:   * Nombre * Ámbito geográfico * Origen * Fondo estructural   Se debe de verificar la unicidad del campo Nombre entre los registros con campo "activo" a true.  Se creará el nuevo registro en la tabla "Fuente financiación" con el campo "activo=true".  [CU-CSP-0070-002 - Crear fuente de financiación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-casos-de-uso/cu-csp-0070-gestion-de-fuentes-de-financiacion/cu-csp-0070-002-crear-fuente-de-financiacion) | CSP-FNT-C |
| Cancelar | No se realiza ninguna operación | Se retorna al formulario de listado de fuentes de financiación [IU-CSP-0070-002 - Buscar y listar fuentes de financiación](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/csp-modulo-de-convocatorias-ayudas-solicitudes-proyectos-y-contratos-y-grupos-de-investigacion/csp-interfaz-de-usuario/iu-csp-0070-gestion-de-fuentes-de-financiacion/iu-csp-0070-002-buscar-y-listar-fuentes-de-financiacion) |  |

### Permisos de acceso a la pantalla

#### Por actor

|  |  |
| --- | --- |
| ACT-CSP-004-Administrador | CSP-FNT-C |
| ACT-CSP-003-Gestor | CSP-FNT-C |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | CSP-FNT-C |