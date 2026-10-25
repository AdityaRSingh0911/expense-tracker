# Feature Specification: User Registration

**Goal:** Implement a secure and user-friendly registration system that allows new users to create an account to track their expenses.

## 1. Functional Requirements
- **User Input:**
    - Username (Unique, required)
    - Email (Valid format, Unique, required)
    - Password (Required, minimum length/complexity)
    - Confirm Password (Must match password)
- **Validation:**
    - Check if the username or email already exists in the database.
    - Validate email format.
    - Ensure passwords match.
- **Security:**
    - Passwords must be hashed (e.g., using `Werkzeug` or `bcrypt`) before being stored in the database. Never store passwords in plain text.
- **User Experience:**
    - Display clear error messages for validation failures (e.g., "Email already registered").
    - Redirect to the login page upon successful registration with a success message.

## 2. Technical Design
- **Database Schema (`users` table):**
    - `id`: Integer, Primary Key, Autoincrement
    - `username`: String, Unique, Not Null
    - `email`: String, Unique, Not Null
    - `password_hash`: String, Not Null
    - `created_at`: Timestamp, Default current time
- **Routes:**
    - `GET /register`: Renders the registration form.
    - `POST /register`: Processes the form data, validates it, hashes the password, and saves the user to the database.
- **Frontend:**
    - A registration page in `templates/register.html` with a clean form and client-side validation.

## 3. Implementation Plan
1. **Database Update:** Modify `database/db.py` to ensure the `users` table is correctly initialized with the required fields.
2. **Backend Logic:** Implement the `/register` route in `app.py` including validation and password hashing.
3. **Frontend Development:** Create/Update `templates/register.html` to provide the registration interface.
4. **Testing:** 
    - Test successful registration.
    - Test registration with existing email/username.
    - Test registration with mismatched passwords.
