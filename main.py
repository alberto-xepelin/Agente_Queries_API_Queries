from flask import Flask, request
from io import StringIO
from functions import create_client, ejecutar_query

app = Flask(__name__)

print("✔ Flask app is loading...")

@app.route("/", methods=["GET"])
def pipeline():
    query = request.args.get("query", "-")

    # 1. Setear el cliente
    client, signal_1 = create_client()

    if signal_1 != 200:
        return client, signal_1
    
    # 2. Ejecutar la query

    df, signal_2 = ejecutar_query(query, client)

    if signal_2 != 200:
        return df, signal_2
    
    df_str = df.head().to_string()

    output = f"""
    ✅ La ejecución de query fue exitosa.

    El output del dataframe es:

    {df_str}
    """

    return output, 200