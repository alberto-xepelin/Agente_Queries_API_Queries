from google.cloud import bigquery

def create_client():

    try:
        client = bigquery.Client(project="xepelin-lab-data-iaml")
        return client, 200
    
    except Exception as e:
        return f"❌ Error al crear cliente: {e}", 500


def ejecutar_query(query, client):

    try:
        query_job = client.query(query)
        df = query_job.to_dataframe()
        return df, 200
    
    except Exception as e:
        return f"❌ Error al ejecutar query: {e}", 500
    