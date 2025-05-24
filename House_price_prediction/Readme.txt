HOUSE PRICE PREDICTION - MINI PROJECT
--------------------------------------

This is a simple machine learning mini project built using:
- Python (Flask for backend)
- Scikit-learn (for model)
- HTML, CSS, JavaScript (for frontend)
- VS Code + virtual environment

--------------------------------------
PROJECT STRUCTURE
--------------------------------------

House_price_prediction/
├── backend/
│   ├── app.py          --> Flask backend
│   ├── model.pkl       --> Trained ML model (Linear Regression)
├── frontend/
│   └── index.html      --> Frontend UI (HTML + JS)
└── README.txt          --> This file

--------------------------------------
HOW TO RUN THIS PROJECT
--------------------------------------

1. Open the project folder in VS Code

2. Create a virtual environment (if not already):

   On Windows:
   > python -m venv venv
   > .\venv\Scripts\activate

   On Linux/macOS:
   $ python3 -m venv venv
   $ source venv/bin/activate

3. Install required packages:

   > pip install flask flask-cors numpy scikit-learn

4. Make sure your trained model file `model.pkl` is inside the `backend/` folder.

5. Start the Flask backend:

   > cd backend
   > python app.py

   This will start the server on:
   http://127.0.0.1:5000

6. Open the frontend:

   - Option A: Use VS Code Live Server to open `frontend/index.html`
   - Option B: Double-click `index.html` to open it in your browser

7. Enter area, bedrooms, bathrooms → Click "Predict Price" → See the result.

--------------------------------------
NOTES
--------------------------------------

- If you get a "model.pkl not found" error, make sure it's in the backend folder.
- You can train a simple model using sklearn and save it using pickle.
- You must keep the backend running in one terminal while using the frontend.

--------------------------------------
CREDITS
--------------------------------------

Project by: Akshay K
Language: Python 3.x, HTML/CSS/JS
IDE: Visual Studio Code

