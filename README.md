# Multi-Line ETA Predictor

A web application that uses historical Transloc bus data to predict delays and compute an estimated time of arrival (ETA) for any stop on the Gold, Orange, or Green line. The application consists of a Python Flask backend and a React frontend.

## Features

- Simulated historical data for three lines (Gold, Orange, Green) under different weather and load conditions  
- Encodes categorical features (line, stop name, weather, load) with `LabelEncoder`  
- Trains a separate `LinearRegression` model per line  
- Modern React UI for easy interaction
- Real-time ETA predictions via REST API
- Outputs an ETA in `h:mm AM/PM` format  

## Requirements

### Backend
- Python 3.7+  
- Flask and Flask-CORS
- See `requirements.txt` for full list of Python dependencies  

### Frontend
- Node.js 14+ and npm
- React 17+

## Installation

1. Clone or download this repository  
```bash
git clone https://github.com/<your-username>/Bus-Estimator.git
cd Bus-Estimator
```

2. (Optional) Create and activate a virtual environment for the backend:  
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

4. Install frontend dependencies:
```bash
cd eta-ui
npm install
```

## Running the Application

1. Start the backend server (from the root directory):
```bash
python3 server.py
```
The server will run on http://localhost:8080

2. In a new terminal, start the frontend development server:
```bash
cd eta-ui
npm start
```
The React app will run on http://localhost:3000

3. Open your browser and navigate to http://localhost:3000 to use the application

## Usage

1. Select your bus line (Gold, Orange, or Green)
2. Choose your stop from the dropdown
3. Enter the scheduled arrival time (e.g., "3:25 PM")
4. Select current weather conditions
5. Choose the current bus load
6. Click "Predict ETA" to get your estimated arrival time
