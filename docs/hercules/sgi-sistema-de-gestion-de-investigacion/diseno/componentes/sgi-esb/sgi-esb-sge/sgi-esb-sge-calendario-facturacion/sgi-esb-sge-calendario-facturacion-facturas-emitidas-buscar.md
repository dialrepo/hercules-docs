# SGI - ESB - SGE - Calendario facturación - Facturas emitidas - Buscar

|  |  |
| --- | --- |
| Método | GET |
| URL | /facturas-emitidas |
| Parámetros | q+s (query + sort)  La query estará formada por:   * proyectoId * reducida * fechaFactura   El campo reducida puede tomar los siguientes valores:   * true: sólo se envían las columnas a mostrar en la pantalla principal * false:  se envían todas las columnas (para su exportación)   Si no esta informado el campo reducida se considera false. |
| Respuesta | Lista[[FacturaEmitida](https://confluence.um.es/confluence/pages/viewpage.action?pageId=113050871#SGIESBSGECalendariofacturaci%C3%B3n-FacturaEmitida)] |
| Descripción | Listado con las facturas emitidas del SGE. Por cada factura emitida se devolverán los siguientes campos:   * Identificador de la factura emitida * Identificador del proyecto SGE * Anualidad * Número de factura * Mapa de columnas de clave - valor (donde la clave será los id definidos en la llamada /facturas-emitidas/columnas y el valor será el valor de la columna. El valor será un String salvo en aquellas columnas que sean acumulables,se tenga que hacer sumas sobre ellas, donde será de tipo Numérico (sin separador de miles y como separador decimal el punto)). Ver el apartado "**Columnas Factura Emitida**" para ver los id de la columnas que se deben de mostrar. |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)