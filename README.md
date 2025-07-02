# CampusPlay — Book. Play. Repeat.

A full-stack campus sports facility booking app for students and faculty, built with Django (backend) and React Native (Expo, frontend).

---

## 🚀 Features
- Student & Faculty roles
- College email/mobile-based login (email/password or OTP)
- Sports facility & slot booking (per-court, per-sport)
- Admin (faculty) dashboard: add/remove students, set limits, view logs
- Student dashboard: view/book/cancel slots
- OTP and email/password authentication
- Push notification device token support
- Booking rules (per day, per sport, weekend/weekday)

---

## 🗂️ Project Structure
```
backend/        # Django backend (APIs, DB)
frontend/       # Expo React Native app
frontend.env    # Frontend environment config
backend/.env    # Backend environment config
```

---

## ⚙️ Backend Setup (Django)
1. **Install Python 3.10+ and pip**
2. **Install dependencies:**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Configure environment:**
   - Copy `backend/.env` and set your `SECRET_KEY` and `DATABASE_URL` (default is SQLite for dev)
4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create first faculty user:**
   - Use the API: `POST /api/register/faculty/` with name, email, mobile, password, device_token
   - Or add via Django shell:
     ```bash
     python manage.py shell
     >>> from booking.models import Faculty
     >>> Faculty.objects.create(name='Admin', email='admin@college.edu', mobile='9999999999', password='YourPassword')
     ```
6. **Run the server:**
   ```bash
   python manage.py runserver
   ```
   - Default: http://127.0.0.1:8000/

---

## 📱 Frontend Setup (Expo React Native)
1. **Install Node.js (18+) and npm**
2. **Install Expo CLI:**
   ```bash
   npm install -g expo-cli
   ```
3. **Configure environment:**
   - Edit `frontend.env` and set your backend API URL (default: `http://10.0.2.2:8000/api` for Android emulator)
4. **Install dependencies:**
   ```bash
   cd frontend/CampusPlay
   npm install
   ```
5. **Run the app:**
   ```bash
   npx expo start
   ```
   - Scan QR code with Expo Go app or run on emulator/simulator

---

## 🌐 API Endpoints (Key)
- `POST /api/register/faculty/` — Add faculty (first user)
- `POST /api/register/student/` — Faculty adds students
- `POST /api/login/` — Login (email/password or mobile/OTP)
- `POST /api/send-otp/` — Send OTP to mobile
- `POST /api/verify-otp/` — Verify OTP
- ... (see backend code for full list)

---

## 🛠️ Deployment Notes
- **Backend:**
  - Use PostgreSQL for production (set `DATABASE_URL`)
  - Set `DEBUG=False` and configure allowed hosts
  - Use Gunicorn + Nginx or similar for deployment
- **Frontend:**
  - Build with `expo build` or `eas build` for app store deployment
  - Set production API URL in `frontend.env`

---

## 👤 First User (Faculty/Admin) Creation
- The first user must be a faculty (admin) and can be created via the API or Django shell (see above).
- Faculty can then add students via the dashboard or API.

---

## 📋 .env Example Files
- `backend/.env`:
  ```
  SECRET_KEY=your-django-secret-key
  DATABASE_URL=sqlite:///db.sqlite3
  ```
- `frontend.env`:
  ```
  API_URL=http://10.0.2.2:8000/api
  ```

---

## 🧩 Customization
- Add more sports/facilities in the Django admin or via API
- Adjust booking rules in the backend logic
- Expand mobile UI for booking, notifications, and reporting

---

## 🤝 Contributing
PRs and suggestions welcome! 