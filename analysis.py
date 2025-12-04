# marimo
# @app
# Interactive Data Analysis Notebook
# Author: Janani (23f1002293@ds.study.iitm.ac.in)

import marimo as mo
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# Cell 1: Create dataset and expose variables
# This cell generates synthetic data and shares variables
# ---------------------------------------------------------
@app.cell
def cell1():
    np.random.seed(42)
    x = np.linspace(0, 10, 200)
    y = 3 * x + np.random.normal(0, 3, size=len(x))  # Linear with noise

    df = pd.DataFrame({"x": x, "y": y})
    return x, y, df

# ---------------------------------------------------------
# Cell 2: Create an interactive slider
# This cell provides widget → used by downstream cells
# ---------------------------------------------------------
@app.cell
def cell2(mo):
    slope_slider = mo.ui.slider(1, 10, step=1, value=3, label="Select slope")
    slope_slider
    return slope_slider

# ---------------------------------------------------------
# Cell 3: Dynamic computation based on slider
# Comment: This depends on slope_slider from Cell 2
# ---------------------------------------------------------
@app.cell
def cell3(slope_slider, x):
    predicted = slope_slider.value * x
    predicted
    return predicted

# ---------------------------------------------------------
# Cell 4: Dynamic markdown output
# Comment: This cell auto-updates using slope_slider + data
# ---------------------------------------------------------
@app.cell
def cell4(mo, slope_slider):
    mo.md(f"""
    # 📊 Analysis Summary  
    **Selected slope:** `{slope_slider.value}`  
    The linear model currently predicts values using:  

    $$
    \hat{{y}} = {slope_slider.value} \cdot x
    $$
    """)
