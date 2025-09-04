
🚀**Exoplanet Prediction API**

A FastAPI-based machine learning API that predicts whether a celestial body is an Exoplanet or Not Exoplanet based on input CSV data. 

**Here the API Key-**
https://exoplanet-api-cxu0.onrender.com

📂 **Project Structure**

├── main.py             # FastAPI application

├── requirements.txt    # Project dependencies

├── Procfile            # Deployment instructions (Render/Heroku)

├── rf_pipeline.pkl     # Trained ML model

⚡ **Features**

REST API built with FastAPI
Supports CSV upload for predictions
Deployed on Render
Returns results in JSON format

🛠 **Installation & Setup**

1️⃣ Clone the repo
git clone https://github.com/MdTariq01/Exoplanet_Api.git
cd Exoplanet_Api

2️⃣ Create virtual environment-

    python -m venv venv

    source venv/bin/activate   # Linux / Mac

    venv\Scripts\activate      # Windows


3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the API locally
uvicorn main:app --reload


Now visit 👉 http://127.0.0.1:8000/docs for Swagger UI.

🌍 **Deployment**

This project is configured for deployment on Render (works on Heroku too).

Example Procfile:
web: uvicorn main:app --host 0.0.0.0 --port $PORT

📡 **API Endpoints**

Health Check
GET /

Response:

{"message": "✅ Exoplanet Detection API is running!"}

Predict from CSV
POST /predict_json/

Body (form-data):

file: CSV file containing input features

Response:

{
  "predictions": ["Exoplanet", "Not Exoplanet"]
}

🧑‍💻 **Tech Stack**

FastAPI (API framework)

Uvicorn (server)

Render (deployment)
