# ETL Pipeline para BigQuery

Este repositório contém um pipeline de ETL (Extração, Transformação e Carga) que extrai dados de uma API e de um arquivo CSV, transforma esses dados e os carrega no Google BigQuery.

## Descrição

O pipeline realiza as seguintes etapas:
1. **Extração de Dados**:
   - Extrai dados de uma API pública.
   - Extrai dados de um arquivo CSV local.

2. **Transformação de Dados**:
   - Realiza operações de transformação, como mesclagem de dados e padronização de formatos.

3. **Carregamento de Dados**:
   - Carrega os dados transformados em uma tabela no Google BigQuery.

## Tecnologias Utilizadas

- Python
- Pandas
- Google Cloud BigQuery
- Requests

## Pré-requisitos

Antes de executar o código, você precisa ter:
- Python 3.x instalado.
- A biblioteca `google-cloud-bigquery` instalada. Você pode instalar usando o seguinte comando:

    ```bash
    pip install google-cloud-bigquery pandas requests
    ```

- Um projeto no Google Cloud com o BigQuery habilitado.
- As credenciais do Google Cloud salvas em um arquivo JSON. Você deve definir o caminho para este arquivo no código.

## Configuração

Antes de executar o código, atualize as seguintes variáveis no script:

- `API_URL`: A URL da API de onde os dados serão extraídos.
- `CSV_FILE_PATH`: O caminho para o arquivo CSV local.
- `PROJECT_ID`: O ID do seu projeto no Google Cloud.
- `DATASET_ID`: O ID do seu dataset no BigQuery.
- `TABLE_ID`: O nome da tabela onde os dados serão carregados.
- `CREDENTIALS_PATH`: O caminho para o seu arquivo de credenciais JSON.

## Execução

Para executar o pipeline, execute o seguinte comando:

```bash
python seu_script.py
