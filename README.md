# 🏦 Credit Scoring System with Logistic Regression & Streamlit

A microservice-based credit scoring system that evaluates loan eligibility using a Logistic Regression model. The project consists of a **FastAPI** backend for model inference and a **Streamlit** frontend for user interaction.

## 📋 Project Overview

This application predicts the probability of borrower default based on financial and demographic data.
- **Backend**: A FastAPI server loads a pre-trained Logistic Regression model and exposes a `/score` endpoint.
- **Frontend**: A Streamlit interface allows users to input their details (age, income, education, etc.) and receive an instant decision.
- **Model**: Trained on historical banking data with balanced class weights to handle imbalanced datasets.

## 🛠 Tech Stack

*   **Python 3.12**
*   **FastAPI**: High-performance web framework for building APIs.
*   **Streamlit**: For creating the interactive web UI.
*   **Scikit-Learn**: For the Logistic Regression model and data preprocessing.
*   **Pandas**: For data manipulation.
*   **Joblib**: For model serialization.
*   **Pydantic**: For data validation in the API.

## 📂 Project Structure

```text
Scoring_service/
├── data/
│   └── scoring.csv          # Training dataset
├── other files/             # Additional resources
├── app_front.py             # Streamlit frontend application
├── main.py                  # Model training and evaluation script
├── server.py                # FastAPI backend server
├── model.pkl                # Serialized trained model
├── requirements.txt         # (Optional) List of dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.12+ installed. Install the required libraries:

```bash
pip install fastapi uvicorn streamlit scikit-learn pandas pydantic requests joblib
```

### 1. Train the Model (Optional)

If you want to retrain the model or evaluate metrics, run `main.py`:

```bash
python main.py
```
This will generate/update the `model.pkl` file.

### 2. Run the Backend Server

Start the FastAPI application using Uvicorn:

```bash
uvicorn server:app --reload
```
The API will be available at `http://127.0.0.1:8000`. You can view the automatic docs at `http://127.0.0.1:8000/docs`.

### 3. Run the Frontend Application

In a separate terminal, start the Streamlit app:

```bash
streamlit run app_front.py
```
Open the local URL provided (usually `http://localhost:8501`) in your browser.

## 💻 Usage

1.  Enter your details in the Streamlit form:
    *   **Age**
    *   **Annual Income** (in thousands)
    *   **Higher Education** (Checkbox)
    *   **Stable Job** (Checkbox)
    *   **Car Ownership** (Checkbox)
2.  Click **"Submit Application"**.
3.  The app sends a request to the FastAPI backend.
4.  **Result**:
    *   ✅ **Approved**: If the model predicts low risk.
    *   ℹ️ **Alternative Offer**: If the loan is declined, a debit card offer is shown.

## 📊 Model Metrics

The model was evaluated using Precision and Recall on the test set:
*   **Precision**: ~14%
*   **Recall**: ~67%

*Note: The model uses `class_weight='balanced'` to improve recall for the minority class (defaults).*

## 🔌 API Endpoint

**POST** `/score`

Request Body:
```json
{
  "age": 25,
  "income": 50.0,
  "education": true,
  "work": true,
  "car": false
}
```

Response:
```json
{
  "approved": true
}
```

## 📝 License

This project is licensed under the Apache-2.0 License.
```
