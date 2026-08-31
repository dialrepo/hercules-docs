# IU-ETI-0090-004 Consultar Memoria - Edición documentación - Aportar documento

|  |  |
| --- | --- |
| Cod. IU | ********IU-ETI-0090-004- Consultar Memoria - Edición documentación - Aportar documento******** |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-ETI-001-Gestor |
| Frecuencia | Media |

## Formulario de Consultar Memoria - Edición documentación - Aportar documento

Pantalla que muestra el formulario para aportar un documento de la lista de documentos de una memoria cuando se trata de un gestor

|  |  |  |
| --- | --- | --- |
|  | | |
| Nombre | Tipo | Características / Notas |
| Nombre | Texto  Obligatorio | Nombre del documento que se le quiera dar |
| Fichero | Selector  Texto  Obligatorio | Documento a adjuntar |

| Acciones | Descripción | Enlace CU. | Permisos |
| --- | --- | --- | --- |
| Examinar | Se abre una pantalla para poder adjuntar el documento desde el equipo |  |  |
| Guardar | Se añade el documento a la lista de documentos aportados de la memoria | El documento es añadido a la lista de documentos de la memoria.  Los documentos aportados por el gestor se les pone de tipo "Documentación adicional" | ETI-MEM-EDOC |
| Cancelar | Se va a la pantalla de Documentación sin aplicar cambios |  |  |

### Acciones

#### Por actor

|  |  |
| --- | --- |
| ACT-ETI-001-Gestor | ETI-MEM-EDOC |

#### Todos los permisos de acceso

|  |  |
| --- | --- |
| Permisos | ETI-MEM-EDOC |