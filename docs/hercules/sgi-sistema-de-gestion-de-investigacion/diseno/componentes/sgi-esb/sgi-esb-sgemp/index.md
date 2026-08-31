# SGI - ESB - SGEMP

---

* [Sistema de gestión de empresas](#SGIESBSGEMP-Sistemadegestióndeempresas)
  + [Entidades](#SGIESBSGEMP-Entidades)
  + [Modelo lógico](#SGIESBSGEMP-Modelológico)
  + [API](#SGIESBSGEMP-API)
    - [Definición de los objetos](#SGIESBSGEMP-Definicióndelosobjetos)
      * [Empresa](#SGIESBSGEMP-Empresa)
      * [TipoIdentificador](#SGIESBSGEMP-TipoIdentificador)
      * [DatosContacto](#SGIESBSGEMP-DatosContacto)
    - [Servicios](#SGIESBSGEMP-Servicios)
      * [Métodos imprescindibles para el funcionamiento de los módulos y gestiones que utilicen empresas.](#SGIESBSGEMP-Métodosimprescindiblesparaelfuncionamientodelosmódulosygestionesqueutilicenempresas.)
      * [Métodos únicamente necesarios si se requiere gestionar empresas desde el SGI (Alta, Baja, Modificación y Detalle).](#SGIESBSGEMP-MétodosúnicamentenecesariossiserequieregestionarempresasdesdeelSGI(Alta,Baja,ModificaciónyDetalle).)
      * [Métodos donde el SGI solo hace de pasarela entre Universidad y el sistema de terceros llamante (No son necesarios para el funcionamiento del SGI)](#SGIESBSGEMP-MétodosdondeelSGIsolohacedepasarelaentreUniversidadyelsistemadetercerosllamante(NosonnecesariosparaelfuncionamientodelSGI))

---

## Sistema de gestión de empresas

### Entidades

| Entidad | Descripción |
| --- | --- |
| Empresa | Contiene los datos básicos de una empresa. |
| DatosContacto | Contiene los datos de contacto de la empresa. |
| TipoIdentificador | Listado con los tipos de identificador fiscal (CIF, VAT, ...). |
| EmpresaClasificacion | Listado de relaciones entre empresas y clasificaciones. Las empresas se relacionarán únicamente con las clasificaciones del tipo "Sector Industrial". Ver definición de clasificaciones en [SGI - ESB - SGO](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgo).  IMPORTANTE  La relación entre empresas y clasificaciones de tipo "Sector industrial" se considera algo que puede generalizarse a cualquier empresa y no algo específico de las empresas con las que se relaciona UM, es por ello que se ha modelado a nivel lógico en el diagrama.  Al no haberse identificado por el momento necesidad de gestionar en ningún punto del SGI como producto, sino solamente en los formularios específicos de UM, la clasificación de una empresa no se ha modelado a nivel de objetos de transferencia del API ni tiene servicios específicos para su gestión. |

### Modelo lógico

![](/attachments/597853152/597884381.png)

### API

Características generales que todas las API REST deben de cumplir:

* [Consultas filtradas y paginadas](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/consultas-filtradas-y-paginadas)
* [Formatos de datos API](/hercules/sgi-sistema-de-gestion-de-investigacion/desarrollo-y-configuracion/estandares-de-desarrollo/formatos-de-datos-api)

#### Definición de los objetos

##### Empresa

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | String | Identificador de la empresa. |
| nombre | String | Nombre de la empresa. |
| tipoIdentificador | TipoIdentificador | Tipo de identificador fiscal de la empresa. Se devuelve la entidad TipoIdentificador con todos sus campos. |
| numeroIdentificacion | String | Número de identificación fiscal de la empresa del tipo indicado en "tipoIdentificador". |
| razonSocial | String | Razón social de la empresa. |
| datosEconomicos | Boolean | Indicador de si se trata de una empresa con datos económicos (está dada de alta en GENTE y en JUSTO) o sin datos económicos (está dada de alta solo en GENTE). |
| padreId | String | Identificador de la empresa padre o entidad principal. Estará informado en el caso de empresas que son subentidad de otra. |

**Empresa** Ampliar origen

```
{
    "id": "ent-002",
    "nombre": "Empresa de Prueba",
    "tipoIdentificador": {
          "id":"tp-1",
          "nombre":"CIF"
     },
    "numeroIdentificacion": "H11111111",
    "razonSocial": "Empresa que es mayoritariamente de prueba del SGI",
	"datosEconomicos": false,
    "padreId": "ent-001"
}
```

##### TipoIdentificador

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| id | String | Identificador de la entidad TipoIdentificador. |
| nombre | String | Nombre (Posibles valores: CIF, VAT, ...). |

**TipoIdentificador** Ampliar origen

```
{ 
    "id":"tp-1",
    "nombre": "CIF"   
}
```

##### DatosContacto

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| direccion | String | Dirección de contacto de la empresa. |

**DatosContacto** Ampliar origen

```
{
	"direccion": "C/ Uría, número 4, puerta A, 33002, Oviedo, Asturias, España"
}
```

#### Servicios

Para componer la URL llamada completa, se debe anteponer a lo indicado en la columna URL lo siguiente: **{HOST}/api/sgemp**, donde **{HOST}** de deberá sustituir el dominio correspondiente al entorno al que se está accediendo y dicho acceso será por http o https según el caso.

##### Métodos imprescindibles para el funcionamiento de los módulos y gestiones que utilicen empresas.

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGEMP - Empresas - Consultar detalle (Datos generales)](/confluence/spaces/HERCULES/pages/597853021/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+detalle+Datos+generales) | GET | /empresas/{id} |  | [Empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp#SGIESBSGEMP-Empresa) | Detalle de los datos generales de una empresa. |
| [SGI - ESB - SGEMP - Empresas - Buscar](/confluence/spaces/HERCULES/pages/597853020/SGI+-+ESB+-+SGEMP+-+Empresas+-+Buscar) | GET | /empresas | q+s (query + sort)  La query estará formada por:   * id * nombre * razonSocial * numeroIdentificacion | Lista[[Empresa](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp#SGIESBSGEMP-Empresa)] | Listado de Empresa.  *Ejemplo*:  nombre=like=(Tree);(razonSocial=like=SL) |
| [SGI - ESB - SGEMP - Empresas - Consultar datos contacto](/confluence/spaces/HERCULES/pages/597853022/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+datos+contacto) | GET | /datos-contacto/empresa/{id} |  | [DatosContacto](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp#SGIESBSGEMP-DatosContacto) | Contiene los datos de contacto de una empresa. |
| [SGI - ESB - SGEMP - Empresas - Listar tipos de identificador](/confluence/spaces/HERCULES/pages/597853016/SGI+-+ESB+-+SGEMP+-+Empresas+-+Listar+tipos+de+identificador) | GET | /tipos-identificador |  | Lista[[TipoIdentificador](/hercules/sgi-sistema-de-gestion-de-investigacion/diseno/componentes/sgi-esb/sgi-esb-sgemp#SGIESBSGEMP-TipoIdentificador)] | Listado de tipos de identificador fiscal para las empresas ordenados alfabéticamente de forma ascendente. |

##### Métodos únicamente necesarios si se requiere gestionar empresas desde el SGI (Alta, Baja, Modificación y Detalle).

---

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGEMP - Empresas - Consultar campos ver detalle](/confluence/spaces/HERCULES/pages/597853362/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+ver+detalle) | GET | /empresas/formly/view |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de ver detalle de empresa. |
| [SGI - ESB - SGEMP - Empresas - Consultar campos modificación](/confluence/spaces/HERCULES/pages/597853359/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+modificaci%C3%B3n) | GET | /empresas/formly/update |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar modificación empresa, pestaña "Datos generales". Ver [IU-GEN-0082 - Ver detalle - Solicitar modificación de empresa](null/pages/createpage.action?spaceKey=HERCULES&title=IU-GEN-0082+-+Ver+detalle+-+Solicitar+modificaci%C3%B3n+de+empresa&linkCreation=true&fromPageId=597853359). |
| [SGI - ESB - SGEMP - Empresas - Consultar detalle](/confluence/spaces/HERCULES/pages/597853025/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+detalle) | GET | /empresas/formly/{id} |  | JSON | Devuelve los datos a pintar en el formulario de Ver Detalle/Actualizar en el SGI (formly). |
| [SGI - ESB - SGEMP - Empresas - Modificar](/confluence/spaces/HERCULES/pages/597853024/SGI+-+ESB+-+SGEMP+-+Empresas+-+Modificar) | PUT | /empresas | JSON | id  Vendrá relleno si la creación es síncrona y no vendrá si es asíncrona. | Recibe como parámetro la respuesta del usuario del formulario de datos de modificación (formly) con los campos necesarios para actualizar una empresa. |
| [SGI - ESB - SGEMP - Empresas - Dar de alta](/confluence/spaces/HERCULES/pages/597853019/SGI+-+ESB+-+SGEMP+-+Empresas+-+Dar+de+alta) | POST | /empresas | JSON |  | Recibe como parámetro la respuesta del usuario del formulario de datos de alta (formly) con los campos necesarios para crear una empresa. |
| [SGI - ESB - SGEMP - Empresas - Consultar campos alta](/confluence/spaces/HERCULES/pages/597853018/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+campos+alta) | GET | /empresas/formly/create |  | Formly | Devuelve el formulario (formly) a pintar para la pantalla de solicitar alta empresa, pestaña "Datos generales". Ver [IU-GEN-0081 - Solicitar alta de empresa.](/hercules/sgi-sistema-de-gestion-de-investigacion/requisitos-y-analisis-funcional/analisis-funcional-sgi-hercules/gen-aspectos-generales/sha-buscadores-y-listados-comunes/iu-gen-0081-solicitar-alta-de-empresa) |

##### Métodos donde el SGI solo hace de pasarela entre Universidad y el sistema de terceros llamante (No son necesarios para el funcionamiento del SGI)

| Servicio | Método | URL | Parámetros | Respuesta | Descripción |
| --- | --- | --- | --- | --- | --- |
| [SGI - ESB - SGEMP - Empresas - Consultar empresas modificadas](/confluence/spaces/HERCULES/pages/597853241/SGI+-+ESB+-+SGEMP+-+Empresas+-+Consultar+empresas+modificadas) | GET | /empresas/modificadas-ids | q+s  La query estará formada por:   * fechaModificacion | Lista[String] | Listado de los identificadores de empresas que han sufrido cambios en los datos de identificativos de la empresa o en sus datos de contacto. |