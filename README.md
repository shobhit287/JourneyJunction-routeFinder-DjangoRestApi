# AuthenticationApp

AuthenticationApp is a Django-based application designed to manage user authentication securely and efficiently. This guide will help you set up the application locally for development.

## Features
- User Registration
- User Login/Logout
- Password Reset and Change
- API Documentation with Swagger

## Prerequisites

Ensure that you have the following installed:
- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager
- **Virtualenv**: For creating isolated Python environments

---

## Installation Guide

Follow these steps to set up the project locally.

### Step 1: Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/shobhit287/authentication-App-DjangoRestApi-emailService
```
### Step 2: Install Virtal Environemnt and Activate
```bash
pip install virtualenv
python -m venv env
cd env/Scripts
.\activate.ps1 #for Windows
```
### Step 3: Install Virtal Environemnt and Activate
```bash
cd authentication-App-DjangoRestApi-emailService
python -r req.txt
```
### Step 4: Install Virtal Environemnt and Activate
add .env file
```bash
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASSWORD=root
DATABASE_NAME= "demo"
JWT_KEY = <key>
SECRET_KEY= <your secret key>
EMAIL_HOST_USER= <email host>
EMAIL_HOST_PASSWORD= <email host password>
```



### Step 5: Run Server
```bash
python manage.py runserver
```
Note: No need to run migrations i already define it in manage.py when server starts it automatically creates table in database
