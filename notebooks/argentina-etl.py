import marimo

__generated_with = "0.11.20"
app = marimo.App(width="full", app_title="ETL Argentina Dataset")


@app.cell
def _():
    # dedicated to marimo env setup
    from pathlib import Path

    import marimo as mo
    import pandas as pd
    import requests as rq
    return Path, mo, pd, rq


@app.cell
def _(mo):
    mo.md(r"""# Bienvenidos a el ETL de Datasets de Argentina""")
    return


@app.cell
def _(mo):

    options = {
        "op1": "Cargar un dataset",
        "op2": "Limpiar un dataset",
        "op3": "Transformar un dataset",
    }

    mo.accordion(options)
    return (options,)


if __name__ == "__main__":
    app.run()
