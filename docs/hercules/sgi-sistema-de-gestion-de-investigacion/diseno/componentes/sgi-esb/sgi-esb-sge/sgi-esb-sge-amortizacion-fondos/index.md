# SGI - ESB - SGE - Amortización fondos

---

* [Ejecución económica](#SGIESBSGEAmortizaciónfondos-Ejecucióneconómica)
  + [Entidades](#SGIESBSGEAmortizaciónfondos-Entidades)
  + [API](#SGIESBSGEAmortizaciónfondos-API)
    - [Definición de los objetos](#SGIESBSGEAmortizaciónfondos-Definicióndelosobjetos)
      * [PeriodoAmortizacion](#SGIESBSGEAmortizaciónfondos-PeriodoAmortizacion)
      * [TipoFinanciacion](#SGIESBSGEAmortizaciónfondos-TipoFinanciacion)
      * [FuenteFinanciacion](#SGIESBSGEAmortizaciónfondos-FuenteFinanciacion)
    - [Servicios](#SGIESBSGEAmortizaciónfondos-Servicios)

## Ejecución económica

### Entidades

| Entidad | Descripción |
| --- | --- |
| PeriodoAmortizacion | Entidad que representa un periodo de amortización de un proyecto. |
| FuenteFinanciacion | Entidad que representa una fuente de financiación. Las fuentes de financiación son configuradas en el SGI. |
| TipoFinanciacion | Entidad que representa un tipo de financiación. Los tipos de financiación son configurados en el SGI. |

### API

Características generales que todas las API REST deben de cumplir:

* [Consultas filtradas y paginadas](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/consultas-filtradas-y-paginadas)
* [Formatos de datos API](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/formatos-de-datos-api)

#### Definición de los objetos

##### PeriodoAmortizacion

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador interno del SGI del periodo de amortización. Debe de ser único. |
| proyectoId | String | Identificación del proyecto SGE |
| anualidad | String | Anualidad |
| empresaRef | String | Referencia de la entidad financiadora. Es el identificador único de la empresa en el sistema de gestión de empresas de la Universidad |
| tipoFinanciacion | TipoFinanciacion | Entidad Tipo de financiación. |
| fuenteFinanciacion | FuenteFinanciacion | Entidad Fuente de financiación. |
| fecha | String | Fecha límite del periodo de amortización |
| importe | Número | Importe del periodo de amortización |

**PeriodoAmortizacion**

```
{
"id": "1234566",
"proyectoId": "25888"
"anualidad": "2021",
"empresaRef": "2855466 ,
"tipoFinanciacion": {
        "id": "1",
        "nombre": "Subvención"
        },
"fuenteFinanciacion":  {
        "id": "2",
        "nombre": "Plan propio 2020-2025"
        }, 
"fecha": "01/02/2021",
"importe": 15000 
}
```

##### TipoFinanciacion

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador interno del SGI del tipo de financiación. |
| nombre | String | Nombre del tipo de financiación |

##### FuenteFinanciacion

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador interno del SGI de la fuente de financiación. |
| nombre | String | Nombre de la fuente de financiación |

#### Servicios

Para componer la URL llamada completa, se debe anteponer a lo indicado en la columna URL lo siguiente: **{HOST}/api/sge**, donde **{HOST}** de deberá sustituir el dominio correspondiente al entorno al que se está accediendo y dicho acceso será por http o https según el caso.

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGE - Amortización fondos - Período amortización - Eliminar](/confluence/spaces/HERCULES/pages/597853060/SGI+-+ESB+-+SGE+-+Amortizaci%C3%B3n+fondos+-+Per%C3%ADodo+amortizaci%C3%B3n+-+Eliminar) | DELETE | /periodos-amortizacion/{id} |  |  | Elimina un periodo de amortización. Se pasa por url el identificador del periodo de amortización. |
| [SGI - ESB - SGE - Amortización fondos - Período amortización - Modificar](/confluence/spaces/HERCULES/pages/597853059/SGI+-+ESB+-+SGE+-+Amortizaci%C3%B3n+fondos+-+Per%C3%ADodo+amortizaci%C3%B3n+-+Modificar) | PUT | /periodos-amortizacion/{id} | [PeriodoAmortizacion](https://confluence.um.es/confluence/pages/viewpage.action?pageId=120032553#SGIESBSGEAmortizaci%C3%B3nfondos-PeriodoAmortizacion) |  | Modifica un periodo de amortización. Se pasa por url el identificador del periodo de amortización. |
| [SGI - ESB - SGE - Amortización fondos - Período amortización - Crear](/confluence/spaces/HERCULES/pages/597853058/SGI+-+ESB+-+SGE+-+Amortizaci%C3%B3n+fondos+-+Per%C3%ADodo+amortizaci%C3%B3n+-+Crear) | POST | /periodos-amortizacion | [PeriodoAmortizacion](https://confluence.um.es/confluence/pages/viewpage.action?pageId=120032553#SGIESBSGEAmortizaci%C3%B3nfondos-PeriodoAmortizacion) |  | Crea un periodo de amortización |