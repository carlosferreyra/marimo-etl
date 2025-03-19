# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.11.20"
app = marimo.App(width="medium", app_title="ETL Demo")


@app.cell
def _():
    from pathlib import Path

    import marimo as mo
    import pandas as pd
    import quak
    import seaborn as sns

    return Path, mo, pd, quak, sns


@app.cell
def _(Path, mo, pd, quak):
    # Load the iris dataset
    iris_df = pd.read_csv(str(Path().cwd() / "public" / "penguins.csv"))

    # Create a quak widget to display the dataset
    widget = mo.ui.anywidget(quak.Widget(iris_df))
    # widget
    return iris_df, widget


@app.cell
def _(widget):
    # Display the SQL state of the widget
    widget.sql
    widget  # # Display the widget
    return widget


if __name__ == "__main__":
    app.run()
