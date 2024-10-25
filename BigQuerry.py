import requests
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


API_URL = "https://jsonplaceholder.typicode.com/posts"  # 
CSV_FILE_PATH = "data/sales_data.csv"  
PROJECT_ID = "seu_projeto_id"
DATASET_ID = "seu_dataset_id"
TABLE_ID = "dados_transformados"
CREDENTIALS_PATH = "caminho/para/sua/chave.json"


def authenticate_bigquery(credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client


def extract_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f"Erro na API: {response.status_code}")
        return None


def extract_data_from_csv(file_path):
    return pd.read_csv(file_path)

#Função de transformação de dados
def transform_data(api_data, csv_data):
 
    merged_data = pd.merge(api_data, csv_data, left_on='userId', right_on='customer_id', how='inner')
    
  
    merged_data['title'] = merged_data['title'].str.upper() 
    merged_data.dropna(subset=['title', 'body'], inplace=True)  # Remoção de valores nulos
    
    return merged_data


def load_data_to_bigquery(df, client, dataset_id, table_id):
    table_ref = client.dataset(dataset_id).table(table_id)
    

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
 
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Aguarda a conclusão do job
    print(f"Dados carregados com sucesso em {dataset_id}.{table_id}")


def run_pipeline():
    client = authenticate_bigquery(CREDENTIALS_PATH)
    

    api_data = extract_data_from_api(API_URL)
    csv_data = extract_data_from_csv(CSV_FILE_PATH)
    
    if api_data is not None and csv_data is not None:
   
        transformed_data = transform_data(api_data, csv_data)
        
   
        load_data_to_bigquery(transformed_data, client, DATASET_ID, TABLE_ID)
    else:
        print("Erro na extração de dados. Pipeline não executado.")


if __name__ == "__main__":
    run_pipeline()
