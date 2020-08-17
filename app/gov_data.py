from google.cloud.datacatalog import DataCatalogClient, enums, types


def results_from_catalog(filtro):
    ## Service account authentication
    serviceAccount = 'data-catalog.json'
    datacatalog_client = DataCatalogClient.from_service_account_json(serviceAccount)

    scope = types.SearchCatalogRequest.Scope()
    scope.include_project_ids.append('dataflow-271218')

    #query = "column:MEMBROS"
    #query = "projectid:dataflow-271218 and TRELLO and type=table"
    query = str(filtro)
    results = datacatalog_client.search_catalog(scope=scope, query=query)

    ## A vector that will have all the query response from data catalog
    content_vet = []

    for result in results:
        result_resource = result.linked_resource.split('/')[3::]
        result_resource_json = {
            'projeto': result_resource[1],
            'dataset': result_resource[3],
            'tabela': result_resource[5]
        }
        content_vet.append(result_resource_json)

    return content_vet

## Search for all the project that hava a column searched in data calog
"""
for search in range(len(content_vet)):
    print("Dataset: {dataset}".format(dataset = content_vet[search]['dataset']))
    print("Tabela: {tabela}".format(tabela = content_vet[search]['tabela']))
"""
