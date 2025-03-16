import marimo

__generated_with = "0.11.20"
app = marimo.App(width="full", app_title="ETL Argentina Dataset")


@app.cell
def _():
    import pandas as pd
    import requests
    response = requests.get('https://datos.acumar.gob.ar/dataset/2e4de507-5a60-4156-9212-424d00f165c9/resource/2a68b41c-7f17-4333-a64f-0e279890c5c7/download/registro-proveedores-sociales-mipymes-20250228.csv')
    data = response.json
    pd.DataFrame(data)
    return data, pd, requests, response


if __name__ == "__main__":
    app.run()
