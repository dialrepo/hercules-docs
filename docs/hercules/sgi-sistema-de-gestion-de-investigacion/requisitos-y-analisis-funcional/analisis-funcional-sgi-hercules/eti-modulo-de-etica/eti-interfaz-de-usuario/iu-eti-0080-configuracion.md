# IU-ETI-0080- Configuración

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0080-001 Configuración******** |
| Ver. objetivo |  |
| Ver. CU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-007-Administrador |
| Frecuencia | Baja |

## Formulario Configuración

Pantalla que muestra el formulario de configuración para administrar ciertos datos de los que depende el resto de la aplicación.

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Listado de datos parametrizables | | |
| Código | código | No se podrá modificar. Es el código usado dentro de la aplicación para referirse al dato. |
| Descripción | descripción | Descripción del parámetros de configuración. |
| Valor | Numérico decimal genérico | Valor que toma |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Editar | Se muestra una pantalla con la descripción y el valor por si se quisiera modificar. |  | ETI-CNF-E |
| Cancelar | No se guardan los datos |  |  |
| Guardar | Guarda las modificaciones realizadas. |  | ETI-CNF-E |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-007-Administrador | ETI-CNF-E |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-CNF-E |