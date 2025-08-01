from flask import Flask, request, jsonify
from io import StringIO
from functions import create_client, ejecutar_query
from tabulate import tabulate

app = Flask(__name__)

print("✔ Flask app is loading...")

@app.route("/", methods=["POST"])
def pipeline():
    #query = request.args.get("query", "-")

    # Cambio de input
    data = request.get_json()
    query = data.get("query", "-")

    # 1. Setear el cliente
    client, signal_1 = create_client()

    if signal_1 != 200:
        return client, signal_1
    
    # 2. Ejecutar la query

    df, signal_2 = ejecutar_query(query, client)

    if signal_2 != 200:
        return df, signal_2
    
    df_str = tabulate(df.head(), headers='keys', tablefmt='grid')

    output = "✅ La ejecución de query fue exitosa.\n\n" \
         "```text\n" \
         f"{df_str}\n" \
         "```"

    return output, 200