# How to Run and Deploy CampusPlay

This guide covers how to set up, run, and deploy the CampusPlay project (Django backend + Expo React Native frontend).

---

## 1. Prerequisites
- Python 3.10+
- Node.js 18+ and npm
- (Recommended) PostgreSQL for production
- Expo Go app (for mobile testing)

---

## 2. Backend (Django) Setup

### a. Install dependencies
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### b. Configure environment
- Copy `backend/.env` and set:
  - `SECRET_KEY` (any random string)
  - `DATABASE_URL` (default: `sqlite:///db.sqlite3` for dev)

### c. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### d. Create the first faculty (admin) user
- **Via API:**
  - Send a POST request to `/api/register/faculty/` with JSON:
    ```json
    {
      "name": "Admin",
      "email": "admin@college.edu",
      "mobile": "9999999999",
      "password": "YourPassword",
      "device_token": "optional-device-token"
    }
    ```
- **Or via Django shell:**
  ```bash
  python manage.py shell
  >>> from booking.models import Faculty
  >>> Faculty.objects.create(name='Admin', email='admin@college.edu', mobile='9999999999', password='YourPassword')
  ```

### e. Run the backend server
```bash
python manage.py runserver
```
- Default: http://127.0.0.1:8000/

---

## 3. Frontend (Expo React Native) Setup

### a. Install dependencies
```bash
cd frontend/CampusPlay
npm install
```

### b. Configure environment
- Edit `frontend.env` and set:
  - `API_URL` (e.g., `http://10.0.2.2:8000/api` for Android emulator, or your backend IP)

### c. Run the Expo app
```bash
npx expo start
```
- Scan the QR code with Expo Go or run on an emulator/simulator.

---

## 4. Booking Flow
- **Faculty** logs in and can add students via the API or (future) dashboard.
- **Students** log in with email/password or mobile/OTP (default password: `Student@123` if set by faculty).
- **Booking, slot management, and admin features** are available as per your backend API and frontend screens.

---

## 5. Deployment

### Backend (Django)
- Use PostgreSQL in production. Set `DATABASE_URL` accordingly.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` in `settings.py`.
- Use Gunicorn + Nginx or similar for production deployment.
- Set up environment variables securely (do not commit secrets).

### Frontend (Expo)
- Set `API_URL` in `frontend.env` to your production backend URL.
- Build the app for production:
  - `expo build` or `eas build` (see Expo docs)
- Publish to app stores as needed.

---

## 6. Notes
- **Default student password:** `Student@123` (can be changed by student after first login, if you implement password change)
- **Device tokens** can be set for push notifications (future feature)
- **All environment files** (`.env`, `frontend.env`) should NOT be committed to public repos.

---

## 7. Troubleshooting
- If you get CORS errors, configure Django CORS headers.
- For mobile device testing, ensure your backend is accessible from your device (use LAN IP, not localhost).
- For any issues, check logs in both backend and frontend.

---

## 8. Useful Commands
- **Backend:**
  - `python manage.py createsuperuser` (for Django admin)
  - `python manage.py runserver 0.0.0.0:8000` (to allow LAN access)
- **Frontend:**
  - `npx expo start --tunnel` (for easier device testing)

---

## 9. Contributing
- PRs and suggestions are welcome! 