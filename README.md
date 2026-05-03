# BookHaven - Django Online Book Store

A responsive and professionally styled online book store built with Django.

## Implemented Pages
- Home Page
- Login Page
- Catalogue Page
- Registration Page

## Tech Stack
- Backend: Django
- Database: MySQL (primary) with SQLite fallback for quick local run
- Frontend: HTML, CSS, Django Templates

## Setup on a New Laptop (Simple Guide)

### 1. Install required software
- Install Python 3.11+ from https://www.python.org/downloads/
- Install Git from https://git-scm.com/downloads

### 2. Get the project code
```bash
git clone <your-repo-url>
cd Syllabus_Assignment9
```

### 3. Create and activate a virtual environment

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set environment variables
- Copy the values from `.env.example` into your terminal environment.
- Quick local run (recommended first time): keep `USE_MYSQL=False` so SQLite is used.
- If you want MySQL, set `USE_MYSQL=True` and configure MySQL credentials.

### 6. Run database migrations
```bash
python manage.py migrate
```

### 7. Create an admin account
```bash
python manage.py createsuperuser
```

### 8. Start the server
```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## URLs
- `/` Home
- `/login/` Login
- `/register/` Registration
- `/catalogue/` Catalogue
- `/admin/` Admin panel

## Add Books
- Login to `/admin/`
- Open `Books`
- Add title, author, genre, price, stock, and description
