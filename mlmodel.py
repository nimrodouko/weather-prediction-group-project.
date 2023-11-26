import joblib

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def load_model():
    model =  joblib.load(BASE_DIR,'savedmodels')
    return model

def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction
