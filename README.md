# Secure File Sharing System

This is a secure file-sharing system built with Flask, providing different functionalities for two types of users:

- **Ops User**: Can upload files of specific types (.pptx, .docx, .xlsx).
- **Client User**: Can sign up, verify their email, log in, list uploaded files, and download them securely.

---

## Features

### 1. Ops User Actions
- **Login**: Authenticate as an Ops User.
- **Upload File**: Upload files of type `.pptx`, `.docx`, or `.xlsx`. Files are stored in a secure directory.

### 2. Client User Actions
- **Sign Up**: Registers a new client user. Returns an encrypted URL.
- **Email Verification**: Verifies the client user's email address.
- **Login**: Authenticate as a Client User.
- **List Files**: Retrieves a list of all uploaded files.
- **Download File**: Downloads a file via a secure encrypted URL. Only accessible to authenticated client users.

### Security Features
- **Encrypted File URLs**: URLs for downloading files are encrypted and tied to client users.
- **Access Control**: Unauthorized users cannot access secure URLs.
- **File Validation**: Only specific file types are allowed for upload.

---

## Prerequisites

1. **Python**: Install Python 3.8 or higher.
2. **Dependencies**: Install required Python packages using pip.
3. **Email Account**: Enable and generate an app-specific password for sending emails.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/secure-file-sharing.git
cd secure-file-sharing
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_specific_password
UPLOAD_FOLDER=uploads/
```

### 5. Initialize the Database
```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Start the Server
```bash
flask run
```
Access the application at `http://127.0.0.1:5000/`.

---

## API Endpoints

### Authentication Endpoints
- **Ops User Login**: `POST /auth/ops-login`
- **Client User Signup**: `POST /auth/signup`
- **Client User Email Verify**: `GET /auth/verify-email/<token>`
- **Client User Login**: `POST /auth/login`

### File Management Endpoints
- **Upload File (Ops User)**: `POST /files/upload`
- **List Files (Client User)**: `GET /files/list`
- **Download File (Client User)**: `GET /files/download/<file_id>`

---

## Postman Collection
A Postman dump is provided for testing the APIs. Import the JSON file into Postman to get pre-configured API requests.

---

## File Uploads
Uploaded files are stored in the `uploads/` directory. Ensure this directory exists and has the correct permissions:
```bash
mkdir uploads
chmod 755 uploads
```

---

## Dependencies
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Mail
- Python Dotenv

Install them using:
```bash
pip install flask flask-sqlalchemy flask-migrate flask-jwt-extended flask-mail python-dotenv
```

---

## Security Considerations
- Use a strong `SECRET_KEY` and `JWT_SECRET_KEY`.
- Use an app-specific password for your email account.
- Validate all inputs to prevent security vulnerabilities such as SQL injection or file upload exploits.
- HTTPS is recommended for secure communication.

---

## License
This project is licensed under the MIT License.
