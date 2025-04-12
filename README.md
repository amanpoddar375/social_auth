# Django Social Authentication Project

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![Allauth](https://img.shields.io/badge/allauth-0.62-lightgrey)

A complete Django project with Google and Facebook authentication using django-allauth.

## Features

✅ Google OAuth2 authentication  
✅ Facebook OAuth2 authentication  
✅ Automatic social app configuration  
✅ REST API endpoints for user information  
✅ Token-based authentication  
✅ Admin interface for user management  

## Complete Setup Guide

### 1. Prerequisites
- Python 3.8+
- Google OAuth2 credentials
- Facebook App credentials

### 2. Project Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/social_auth.git
cd social_auth

# Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```
### 3. Environment Configuration

#### Create .env file
```
DJANGO_SECRET_KEY=your-django-secret-key-here
GOOGLE_CLIENT_ID=your-google-client-id-here
GOOGLE_CLIENT_SECRET=your-google-client-secret-here
FACEBOOK_APP_ID=your-facebook-app-id-here
FACEBOOK_APP_SECRET=your-facebook-app-secret-here
```
### 4. Database Setup and Run Server
```
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

### 5. Configure Site Domain in Django Admin
After creating the superuser, configure the default site for social login:

- Open your browser and go to the Django admin panel:
    http://localhost:8000/admin/sites/site/ 
- Click on the existing site (usually ID = 1) and update it as follows:

        Domain name: localhost:8000

        Display name: localhost

### 5. Access the login page
Now that everything is set up, navigate to the login page in your browser:

http://localhost:8000/accounts/login/

![alt text](image.png)

On clicking Continue with Google
![alt text](image-1.png)
![alt text](image-2.png)

On Clickeing Continue with Facebook
![alt text](image-3.png)
![alt text](image-4.png)