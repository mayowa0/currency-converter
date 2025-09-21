# Currency Converter Web App

A simple Flask-based web application that allows users to:
- Sign up and log in (basic file-based storage).
- Convert between currencies using the [ExchangeRate-API](https://www.exchangerate-api.com/).
- Select from multiple currencies (USD, NGN, EUR, GBP, JPY, CAD, AUD, ZAR, KES, GHS).

---

## Features
- User authentication (Sign up / Log in).
- Real-time currency conversion via API.
- Clean, beginner-friendly code with clear comments.
- Built with Flask, HTML, and CSS.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd currency-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your **API Key**:
   - Create a `.env` file in the project root.
   - Add:
     ```
     API_KEY=your_api_key_here
     ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

---

## File Overview
- `app.py`: Main Flask app with routes.
- `templates/`: HTML files (signup, login, convert pages).
- `users.txt`: Auto-generated user storage file (ignored in git).
- `requirements.txt`: Python dependencies.

---

## Notes
- Replace the demo API key with your own from ExchangeRate-API.
- For production, switch to a database (e.g., SQLite, PostgreSQL) instead of `users.txt`.
- Keep `.env` and `users.txt` out of your repo for security.
