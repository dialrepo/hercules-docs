# SGI - ESB - SGO

---

* [Sistema de Gestión de la estructura Orgánica](#SGIESBSGO-SistemadeGestióndelaestructuraOrgánica)
  + [Entidades](#SGIESBSGO-Entidades)
  + [Enumerados](#SGIESBSGO-Enumerados)
  + [Modelo lógico](#SGIESBSGO-Modelológico)
  + [API](#SGIESBSGO-API)
    - [Definición de los objetos](#SGIESBSGO-Definicióndelosobjetos)
      * [AreaConocimiento](#SGIESBSGO-AreaConocimiento)
      * [Departamento](#SGIESBSGO-Departamento)
      * [Pais](#SGIESBSGO-Pais)
      * [ComunidadAutonoma](#SGIESBSGO-ComunidadAutonoma)
      * [Provincia](#SGIESBSGO-Provincia)
      * [Clasificacion](#SGIESBSGO-Clasificacion)
      * [Centro](#SGIESBSGO-Centro)
    - [Servicios](#SGIESBSGO-Servicios)

---

## Sistema de Gestión de la estructura Orgánica

### Entidades

| Entidad | Descripción |
| --- | --- |
| AreaConocimiento | Listado con las áreas de conocimiento de la Universidad. Se entiende que las áreas de conocimiento de primer nivel son las ramas de conocimiento. |
| Departamento | Listado con los departamentos que tiene la Universidad. |
| Pais | Listado con los países que utiliza el SGI.  Se necesita un mapeo con los valores de la Fecyt para poder mostrarlo en el módulo CVN.  Se necesita un mapeo con los valores del sistema externo de la Universidad. Se hará en fase de implantación, se tendrá una tabla de traducción de los códigos del SGI y los códigos del sistema externo en caso de no ser los mismos. |
| ComunidadAutonoma | Listado con las comunidades autónomas que utiliza el SGI.  Se necesita un mapeo con los valores de la Fecyt para poder mostrarlo en el módulo CVN.  Se necesita un mapeo con los valores del sistema externo de la Universidad. Se hará en fase de implantación, se tendrá una tabla de traducción de los códigos del SGI y los códigos del sistema externo en caso de no ser los mismos. |
| Provincia | Listado con las provincias que utiliza el SGI.  Se necesita un mapeo con los valores de la Fecyt para poder mostrarlo en el módulo CVN.  Se necesita un mapeo con los valores del sistema externo de la Universidad. Se hará en fase de implantación, se tendrá una tabla de traducción de los códigos del SGI y los códigos del sistema externo en caso de no ser los mismos. |
| Clasificacion | Clasificaciones definidas en el SGI para su uso en los distintos módulos.  Ejemplos de clasificaciones:   * **CNAE**: clasificación tomada de los códigos CNAE (Clasificación Nacional de Actividades Económicas). Referencias:    + <https://www.cnae.com.es/lista-actividades.php>   + <https://www.ine.es/daco/daco42/clasificaciones/cnae09/estructura_cnae2009.xls> * **NABS**: nomenclatura para el análisis y programas y presupuestos científicos (NABS) de Eurostat para identificación de objetivos socio-económicos. Referencia:   + <https://www.ciencia.gob.es/stfls/MICINN/Ayudas/PN_2008_2011/LIA_Infraestructuras_CCyTec/FICHERO/FEDER_2010/Nueva_clasificacion_NABS-2007.pdf> * **UNESCO**: Nomenclatura Internacional de la UNESCO para los campos de Ciencia y Tecnología. Referencia:    + <https://www.ciencia.gob.es/portal/site/MICINN/menuitem.8ce192e94ba842bea3bc811001432ea0/?vgnextoid=363ac9487fb02210VgnVCM1000001d04140aRCRD> * **ANEP:** clasificación de las áreas temáticas de la agencia estatal de investigación:   + <https://www.universidades.gob.es/stfls/universidades/Ensenanzas/becas_ayudas_premios/pdi/Documentos/Descriptores_Areas_Tematicas_AEI.pdf> |
| PalabraClave | Diccionario de palabras clave común a todo el SGI. |
| Centro | Listado con los centros de la Universidad. |

### Enumerados

Para la definición de los enumerados en el código seguir lo indicado en: [Enumerados](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/estandares-internos/enumerados)

| Enumerado | Descripción |
| --- | --- |
| TipoClasificacion | Existirá una agrupación de clasificaciones, el tipo de clasificación, que permitirá, en caso de ser necesario, restringir las clasificaciones a utilizar en las gestiones que lo necesiten.  Esta agrupación será un enumerado interno "TipoClasificacion" que a priori solamente tendrá los valores, "Sectores industriales" y "Áreas ANEP". El tipo de clasificación "Sectores industriales" tendrá asociada la clasificación relacionada "CNAE" y el tipo de clasificación "Áreas ANEP" tendrá asociada la clasificación "ANEP" |

### Modelo lógico

![](/attachments/597853249/597862490.jpg)

### API

Características generales que todas las API REST deben de cumplir:

* [Consultas filtradas y paginadas](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/consultas-filtradas-y-paginadas)
* [Formatos de datos API](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/formatos-de-datos-api)

#### Definición de los objetos

##### AreaConocimiento

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador del área de conocimiento. |
| nombre | String | Nombre del área de conocimiento. |
| padreId | String | Identificador de la entidad padre del área de conocimiento. |

**AreaConocimiento** Ampliar origen

```
  {
        "id": "11",
        "nombre": "Medicina Preventiva y Salud Pública",
        "padreId": "1"
	    
    }
```

##### Departamento

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | String | Identificador del departamento. |
| nombre | String | Nombre del departamento. |

**Departamento** Ampliar origen

```
  {
        "id":"dpt-1",
         "nombre":"Departamento Ciencias de la tecnología"
	    
    }
```

##### Pais

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador del país. |
| nombre | String | Nombre del país. |

**Pais** Ampliar origen

```
  {
        "id": "33",
		"nombre": "Francia"
  }
```

##### ComunidadAutonoma

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador de la comunidad autónoma/región. |
| nombre | String | Nombre de la comunidad autónoma/región. |
| paisId | String | Identificador del país. |

**ComunidadAutonoma** Ampliar origen

```
  {
        "id": "1",
        "nombre": "Región central",
        "paisId":"33"
	    
    }
```

##### Provincia

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador de la provincia. |
| nombre | String | Nombre de la provincia. |
| comunidadAutonomaId | String | Identificador de la comunidad autónoma. |

**Provincia** Ampliar origen

```
   {
        "id": "1",
		"nombre": "Provincia central",
        "comunidadAutonomaId":"15"
	    
    }
```

##### Clasificacion

|  |  |  |
| --- | --- | --- |
| **Nombre** | **Tipo** | **Descripción** |
| id | String | Identificador de la clasificación. |
| codigo | String | Código de la clasificación. |
| nombre | String | Nombre de la clasificación. |
| padreId | String | Identificador de la entidad padre de la clasificación. |

**Clasificación padre** Ampliar origen

```
   {
        "id": "1",
		"codigo": "0",
        "nombre":"UNESCO",
        "padreId": null
    }
```

**Clasificación hija de primer nivel** Ampliar origen

```
   {
        "id": "2",
		"codigo":"01"
        "nombre":"Lógica deductiva", 
        "padreId": "1"
    }
```

##### Centro

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | String | Identificador de la entidad Centro. |
| nombre | String | Nombre del centro. |

**Centro** Ampliar origen

```
{
	"id":"cen-1",
    "nombre":"Centro 1 de la Universidad de Murcia"
}
```

#### Servicios

Para componer la URL llamada completa, se debe anteponer a lo indicado en la columna URL lo siguiente: **{HOST}/api/sgo**, donde **{HOST}** de deberá sustituir el dominio correspondiente al entorno al que se está accediendo y dicho acceso será por http o https según el caso.

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGO - Centros - Consultar detalle](/confluence/spaces/HERCULES/pages/597852992/SGI+-+ESB+-+SGO+-+Centros+-+Consultar+detalle) | GET | /centros/{id} |  | [Centro](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Centro) | Detalle del centro cuyo identificador se indica por parámetro. |
| [SGI - ESB - SGO - Centros - Listar](/confluence/spaces/HERCULES/pages/597852991/SGI+-+ESB+-+SGO+-+Centros+-+Listar) | GET | /centros |  | Lista[[Centro](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Centro)] | Listado de centros. |
| [SGI - ESB - SGO - Palabras clave - Buscar](/confluence/spaces/HERCULES/pages/597852984/SGI+-+ESB+-+SGO+-+Palabras+clave+-+Buscar) | GET | /palabras-clave | q+s (query + sort)  La query estará formada por:   * palabra | Lista[String] | Busca/Lista palabras clave. |
| [SGI - ESB - SGO - Palabras clave - Crear](/confluence/spaces/HERCULES/pages/597852983/SGI+-+ESB+-+SGO+-+Palabras+clave+-+Crear) | POST | /palabras-clave | Lista[String] |  | Crea palabras clave si no existen previamente. |
| [SGI - ESB - SGO - Áreas de conocimiento - Buscar](/confluence/spaces/HERCULES/pages/597852997/SGI+-+ESB+-+SGO+-+%C3%81reas+de+conocimiento+-+Buscar) | GET | /areas-conocimiento | q+s (query + sort)  La query estará formada por:   * padreId | Lista[[AreaConocimiento](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-AreaConocimiento)] | Listado de áreas de conocimiento.  Nota: en el caso de no recibirse un padreId en la query, se devolverán todas las áreas de conocimiento y en caso de indicarse en la query que se quieren solo las que tengan un padreId con valor "null" se devolverán únicamente las de primer nivel o nivel raíz.  *Ejemplo de query para obtener solo áreas de conocimiento raíz (su padre es null)*:  padreId=na= |
| [SGI - ESB - SGO - Áreas de conocimiento - Consultar detalle](/confluence/spaces/HERCULES/pages/597852993/SGI+-+ESB+-+SGO+-+%C3%81reas+de+conocimiento+-+Consultar+detalle) | GET | /areas-conocimiento/{id} |  | [AreaConocimiento](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-AreaConocimiento) | Detalle del área de conocimiento cuyo identificador se indica por parámetro. |
| [SGI - ESB - SGO - Departamentos - Listar](/confluence/spaces/HERCULES/pages/597852994/SGI+-+ESB+-+SGO+-+Departamentos+-+Listar) | GET | /departamentos |  | Lista[[Departamento](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Departamento)] | Listado de departamentos. |
| [SGI - ESB - SGO - Países - Listar](/confluence/spaces/HERCULES/pages/597852995/SGI+-+ESB+-+SGO+-+Pa%C3%ADses+-+Listar) | GET | /paises |  | Lista[[Pais](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Pais)] | Listado de países del SGI. |
| [SGI - ESB - SGO - Países - Consultar detalle](/confluence/spaces/HERCULES/pages/597852996/SGI+-+ESB+-+SGO+-+Pa%C3%ADses+-+Consultar+detalle) | GET | /paises/{id} |  | [Pais](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Pais) | Detalle del país cuyo identificador se indica por parámetro. |
| [SGI - ESB - SGO - Comunidades autónomas - Buscar](/confluence/spaces/HERCULES/pages/597852985/SGI+-+ESB+-+SGO+-+Comunidades+aut%C3%B3nomas+-+Buscar) | GET | /comunidades-autonomas | q+s (query + sort)  La query estará formada por:   * paisId | Lista[[ComunidadAutonoma](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-ComunidadAutonoma)] | Listado de comunidades autónomas.  Nota: en el caso de recibirse un país como parámetro se devolverán todas las comunidades autónomas de ese país. |
| [SGI - ESB - SGO - Comunidades autónomas - Consultar detalle](/confluence/spaces/HERCULES/pages/597852986/SGI+-+ESB+-+SGO+-+Comunidades+aut%C3%B3nomas+-+Consultar+detalle) | GET | /comunidades-autonomas/{id} |  | [ComunidadAutonoma](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-ComunidadAutonoma) | Detalle de la comunidad autónoma cuyo identificador se indica por parámetro. |
| [SGI - ESB - SGO - Provincias - Buscar](/confluence/spaces/HERCULES/pages/597852987/SGI+-+ESB+-+SGO+-+Provincias+-+Buscar) | GET | /provincias | q+s (query + sort)  La query estará formada por:   * comunidadAutonomaId | Lista[[Provincia](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Provincia)] | Listado de provincias.  Nota: en el caso de recibirse una comunidad autónoma como parámetro se devolverán todas las provincias de esa comunidad autónoma. |
| [SGI - ESB - SGO - Provincias - Consultar detalle](/confluence/spaces/HERCULES/pages/597852988/SGI+-+ESB+-+SGO+-+Provincias+-+Consultar+detalle) | GET | /provincias/{id} | q+s (query + sort)  La query estará formada por:   * comunidadAutonomaId | [Provincia](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Provincia) | Detalle de la provincia cuyo identificador se indica por parámetro. |
| [SGI - ESB - SGO - Clasificaciones - Buscar](/confluence/spaces/HERCULES/pages/597852989/SGI+-+ESB+-+SGO+-+Clasificaciones+-+Buscar) | GET | /clasificaciones | q+s (query + sort)  La query estará formada por:   * tipoClasificacion * padreId | Lista[[Clasificacion](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Clasificacion)] | Listado de clasificaciones.  Nota: en el caso de no recibirse un padreId en la query, se devolverán todas las clasificaciones y en caso de indicarse en la query que se quieren solo las que tengan un padreId con valor "null" se devolverán únicamente las de primer nivel o nivel raíz. Sobre estas clasificaciones se aplicará además el filtro indicado en tipoClasificacion (en caso de venir informado).  *Ejemplo de query para obtener sólo las clasificaciones raíz (su padre es null) del tipo de clasificación "Sectores Industriales"*:  tipoClasificacion==(SECTORES\_INDUSTRIALES);padreId=na= |
| [SGI - ESB - SGO - Clasificaciones - Consultar detalle](/confluence/spaces/HERCULES/pages/597852990/SGI+-+ESB+-+SGO+-+Clasificaciones+-+Consultar+detalle) | GET | /clasificaciones/{id} |  | [Clasificacion](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo#SGIESBSGO-Clasificacion) | Detalle de la clasificación cuyo identificador se indica por parámetro. |