import marimo

__generated_with = "0.11.20"
app = marimo.App(width="full", app_title="ETL Argentina Dataset")


@app.cell
def _():
    # dedicated to marimo env setup
    import marimo as mo
    import pandas as pd
    import requests as rq
    from pathlib import Path
    return Path, mo, pd, rq


@app.cell
def _(mo):
    mo.md(r"""# Bienvenidos a el ETL de Datasets de Argentina""")
    return


@app.cell
def _(Path):
    file_path = Path().cwd()
    print(file_path)
    return (file_path,)


if __name__ == "__main__":
    app.run()
