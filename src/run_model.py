import os
import pickle
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

def load_model():
    
    model_path = '/workspaces/mlops-challenge-soudhaminich/models/churn_model.pkl' 
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def get_customer_input():
    # ENTER YOUR CODE HERE
    credit_score = float(input("Enter credit score: "))
    age = int(input("Enter age: "))
    balance = float(input("Enter balance: "))
    products_number = int(input("Enter product_number: "))
    credit_card = int(input("Enter 0/1 if credit card is there 1 or 0 if no: "))
    active_member = int(input("Enter 0/1 if active member 1 or 0 if no: "))
    estimated_salary = float(input("Enter age: "))
    tenure = int(input("Enter tenure: "))
    return [[credit_score, age, balance, products_number, credit_card, active_member, estimated_salary, tenure]]

def predict_churn(model, customer_data):
    prediction = model.predict(customer_data)
    return prediction[0]

if __name__ == "__main__":
    model = load_model()
    customer_data = get_customer_input()
    result = predict_churn(model, customer_data)
    print("Churn Prediction:", "Will Churn" if result == 1 else "Will Not Churn")
