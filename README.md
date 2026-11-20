# FoodBridge – Food Donation & Rescue Platform

A full-stack Django project for listing surplus food so community members can claim and collect it.

## Features
- Create food donation listings with category, quantity, pickup location, contact and best-before date
- Search and filter donations
- Claim available donations and mark them collected
- Dashboard statistics
- Django backend and SQLite database
- HTML, CSS and JavaScript frontend

## Run in VS Code
1. Extract this ZIP and open `foodbridge_django` in VS Code.
2. In the terminal run:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
   On macOS/Linux activate with `source venv/bin/activate`.
3. Open http://127.0.0.1:8000/

Educational demo only; no real notifications or food-safety verification.

## User accounts
- Visit `/register/` to create an account.
- Visit `/login/` to sign in.
- Use the Logout link in the homepage navigation to end your session.
- Only logged-in users can publish, claim, mark collected, or delete donation listings.

After updating the project, activate your virtual environment and run:

```bash
python -m pip install -r requirements.txt
python manage.py makemigrations donations
python manage.py migrate
python manage.py runserver
```
