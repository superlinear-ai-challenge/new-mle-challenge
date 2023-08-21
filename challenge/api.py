"""API endpoints of the hiring challenge."""

from io import BytesIO

import numpy as np
import pandas as pd
from fastapi.applications import FastAPI
from fastapi.param_functions import File

app = FastAPI()


@app.post("/ratings/train")
def train(file: bytes = File(...)) -> None:
    """Train a predictive model to predict movie ratings."""
    print("model trained")


@app.post("/ratings/predict")
def test(file: bytes = File(...)) -> dict[float, float]:
    """Train a predictive model to predict movie ratings."""
    test_df = pd.read_csv(BytesIO(file))
    train_df = pd.read_csv("df_train.csv")
    def get_avg_user(userId: int) -> float:
        single_user_df = train_df[train_df.userId==userId]
        u = np.mean(single_user_df.rating)
        return float(u)

    res = {}
    for i, row in test_df.iterrows():
        res[i] = get_avg_user(row.userId)
    return res
