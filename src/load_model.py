import pickle
import os

def load_model():
    model_path = os.path.join('/workspaces/mlops-challenge-soudhaminich/models', 'churn_model.pkl')
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

if __name__ == "__main__":
    model = load_model()
    print("Model loaded successfully.")
