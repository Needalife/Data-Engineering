from google.cloud import bigquery

def fetch_from_bigquery(table_name):
    client = bigquery.Client()
    query = f"""
    SELECT * 
    FROM `{table_name}`
    LIMIT 10
    """
    query_job = client.query(query)  # API request

    results = query_job.result()
    rows = [dict(row) for row in results] 
    return rows

def main():
    table_name = 'project-finance-400806.mental_health_finaldata_1.mental_health'
    data = fetch_from_bigquery(table_name)
    print(data)

if __name__ == "__main__":
    main()