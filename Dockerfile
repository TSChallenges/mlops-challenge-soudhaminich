# This is from Question 
# CANDIDATES ENTER YOUR CODE HERE
FROM python:3.8-slim
WORKDIR /workspaces/mlops-challenge-soudhaminich/
COPY models/churn_mode.pkl .
COPY src/run_model.py .
RUN pip instaall --no-cache-dir -r requirements.txt
CMD ["python" , "run_model.py"]

