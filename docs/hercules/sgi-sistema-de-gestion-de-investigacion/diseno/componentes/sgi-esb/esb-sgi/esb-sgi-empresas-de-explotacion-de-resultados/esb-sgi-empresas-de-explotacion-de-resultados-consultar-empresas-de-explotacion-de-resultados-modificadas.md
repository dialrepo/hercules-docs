# ESB - SGI - Empresas de explotación de resultados - Consultar Empresas de explotación de resultados modificadas

|  |  |
| --- | --- |
| Método | GET |
| URL | /empresas/modificados-ids |
| Parámetros | q+s  La query estará formada por:   * fechaModificacion: fecha a partir de la cual se quieren ver los cambios |
| Respuesta | Lista[String] |
| Descripción | Listado de Identificadores de Empresas de explotación de resultados que han sido modificadas en los datos generales (tabla Empresa), en el equipo emprendedor (tabla EmpresaEquipoEmprendedor), en la composición de la sociedad (tabla EmpresaComposicionSociedad), en el equipo de administración de la sociedad (tabla EmpresaAdministracionSociedad) o en los documentos (tabla EmpresaDocumento).  Ejemplo:   * fechaModificacion=ge="2021-08-18T22:00:00Z" |

### Requisitos relacionados

![](plugins/servlet/confluence/placeholder/unknown-macro)