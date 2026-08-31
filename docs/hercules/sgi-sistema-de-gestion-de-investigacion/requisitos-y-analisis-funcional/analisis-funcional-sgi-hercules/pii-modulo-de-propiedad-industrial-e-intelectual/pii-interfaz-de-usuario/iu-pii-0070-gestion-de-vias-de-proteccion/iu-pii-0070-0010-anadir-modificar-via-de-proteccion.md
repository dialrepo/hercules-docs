# IU-PII-0070-0010 - Añadir-modificar vía de protección

|  |  |
| --- | --- |
| Cod. IU | IU-PII-0070-0010 - Añadir-modificar vía de protección |
| Ver. objetivo |  |
| Ver. IU | 1.0.0 |
| Estado | LIBERADO\_ |
| Fec. Aprobación |  |
| Épica, historia |  |
| Actores | ACT-PII-002-Administrador |
| Frecuencia | Baja |

## Formulario Añadir-modificar vía de protección

Formulario para crear un nueva vía de protección o modificar los datos de una vía de protección ya existente.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | *Formulario en "modo alta"* | *Formulario en "modo modificación" - Ejemplo PCT* | | | |
| Nombre | Tipo | Características / Notas |
| Nombre | Texto corto  Obligatorio  Modificable | Es el nombre identificativo del tipo, con el que se listará en todos los desplegables. Debe de validarse su unicidad en la tabla de tipos (entre los activos) |
| Descripción | Texto  Obligatorio  Modificable | Campo de texto de introducción libre para descripción ampliada. |
| Tipo de propiedad | Selector  Obligatorio  Modificable | Tipo de propiedad a asociar a la vía de protección.  Tendrá dos valores posibles:   * Propiedad industrial * Propiedad intelectual |
| Meses prioridad / plazo ent. fases nac./reg. | Numérico entero  Obligatorio  Modificable | Meses de prioridad a aplicar cuando la solicitud es la primera de una invención o de plazo para la entrada a las fases nacionales / regionales en el caso concreto de solicitudes que sean extensión internacional (p.ej. vía PCT).  Este campo solo aparecerá en el caso de seleccionarse como Tipo propiedad "Propiedad industrial" y, en este caso, será obligatorio. |
| País específico | Check  Opcional  Modificable | Marca si al ser seleccionada esta vía en el desplegable de vías de una solicitud de protección ha de mostrarse el desplegable de países para elegir uno concreto. |
| Extensión internacional | Check  Opcional  Modificable | Marca si al ser seleccionada esta vía en el desplegable de vías de una solicitud de protección ha de adaptarse el texto para los campos de "Fecha prioridad" y "Fecha fin prioridad" a los adecuados para este tipo de vías, que será respectivamente, "Fecha solicitud" y "F. fin pres. f. nac./reg.". |
| Varios países | Check  Opcional  Modificable | Marca si al ser seleccionada esta vía en el desplegable de vías de una solicitud de protección ha de mostrarse el listado de países en los que se ha validado la invención a través de la solicitud de protección. |

| Acciones | Descripción | Enlace CU. |
| --- | --- | --- |
| Añadir | Añade la vía de protección y vuelve a la pantalla listado de vías de protección. |  |
| Aceptar | Guarda los cambios realizados sobre la vía de protección y vuelve a la pantalla listado de vías de protección. |  |
| Cancelar | Vuelve a la pantalla listado de vías de protección sin salvar los posibles cambios. |  |