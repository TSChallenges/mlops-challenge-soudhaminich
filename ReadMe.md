[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LXHBeF4t)
# MLOps Playground Challenge: Customer Churn Prediction (40 Points)

## Objective

In this challenge, you will deploy a pre-trained machine learning model to predict customer churn using the Bank Customer Churn Dataset. The provided model (`churn_model.pkl`) will be integrated into a pipeline for model loading, input collection, and prediction. You’ll also automate the process using Docker and GitHub Actions for CI/CD. GitHub Codespaces will help you set up, run, and test the project in a consistent environment.

### Note the Repository Structure 

Organize your project with the following structure (Note that the directory has sub directories and files in it ):

```
- models/              # Directory for storing the pre-trained model
  - churn_model.pkl    # Pre-trained model pickle file
- src/                 # Directory for deployment scripts
  - run_model.py       # Script for interacting with the model
- Dockerfile           # Docker configuration file
- .github/workflows/   # CI/CD configuration files
  - deploy.yml         # GitHub Actions workflow file
- requirements.txt     # Python dependencies

```

## Task Breakdown

### Task 1: Load the Pre-Trained Model (10 Points)

- Write a Python script (`load_model.py` in the `src/` directory) to load the pre-trained model using `pickle`.
- Ensure the model is loaded correctly from the `models/` directory, where the `churn_model.pkl` file is stored.

---

### Task 2: Interactive Prediction (10 Points)

- Implement a Python script (`run_model.py`) to prompt the user for customer data (e.g., credit score, age, balance, number of products, etc.).
- Use the pre-trained model to predict whether the customer will churn based on the input values.

---

### Task 3: Dockerize the Application (10 Points)

- Create a `Dockerfile` that:
  1. Uses **Python 3.8 or later** as the base image.
  2. Copies the necessary files (model, scripts, etc.) into the container.
  3. Installs the required dependencies from `requirements.txt`.
  4. Runs the `run_model.py` script within the container.

---

### Task 4: Set Up CI/CD Pipeline with GitHub Actions (10 Points)

- Configure a GitHub Actions workflow that:
  1. Installs the dependencies.
  2. Builds the Docker image.
  3. Runs the container to execute the `run_model.py` script.
- The workflow should be triggered whenever changes are pushed to the `main` branch.

---

### Using GitHub Codespaces

To develop and test the project, use **GitHub Codespaces** as your development environment:

1. **Fork the repository** and click the green **Code** button in your forked repository.
2. Select **Codespaces** and choose "Create codespace on main" to open your development environment.
3. Once your Codespace is ready, navigate to the `src/` folder and start working on the `load_model.py` and `run_model.py` scripts.
4. Follow the project structure to implement each task and test your code directly within the Codespace.

---

## Submission Instructions

- Submit the following files:
  - Python scripts (`load_model.py`, `run_model.py` in the `src/` directory),
  - Dockerfile (in the main directory),
  - CI/CD workflow (`deploy.yml` in `.github/workflows/`),
  - Pre-trained model (`churn_model.pkl` in `models/`).
- Ensure your repository is properly organized and tested. You can use **GitHub Codespaces** to test your code before submission.

---

## Evaluation Criteria

- **Model Loading (10 Points):** Ensure the pre-trained model is loaded correctly from the `models/` directory.
- **Interactive Prediction (10 Points):** The script should prompt for inputs and return a valid prediction on customer churn.
- **Dockerization (10 Points):** Verify that the Docker image builds successfully and runs the model.
- **CI/CD Pipeline (10 Points):** GitHub Actions workflow should automate the build and run process.


