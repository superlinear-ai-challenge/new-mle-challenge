"""API endpoints of the hiring challenge."""

from io import BytesIO

import pandas as pd
from fastapi.applications import FastAPI
from fastapi.param_functions import File

app = FastAPI()


@app.post("/ratings/train")
def train(file: bytes = File(...)) -> None:
    """Train a predictive model to predict movie ratings."""
    df = pd.read_csv(BytesIO(file))
    print(df)
    
    # TODO:
    #  - Create a model
    #  - Train the model on the received data
    #  - Save the model
    raise NotImplementedError


# TODO:
#  - Create a '/genres/predict' endpoint (POST)
#  - Load in the previously trained model
#  - Make predictions on the received data 
#  - Return your predictions as a dictionary of the following format:
#       {
#           0:<rating of first test example>,
#           1:<rating of second test example>,
#           ...
#       }
