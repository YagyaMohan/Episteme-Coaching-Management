# Epistêmê Coaching Management System

This is a desktop-based coaching management system developed using Python's Tkinter library and MySQL. It allows student registration, fee structure viewing, and result retrieval from a MySQL database, with proper validation and GUI interactions.

## Features

- Student registration with full validation (names, Aadhaar, age, mobile number, etc.)
- Guardian details linked to students
- Result display from MySQL database
- Fee structure display
- Prevents duplicate Aadhaar entries
- GUI interface using Tkinter with embedded coaching logo

## Technologies Used

- Python 3.x
- Tkinter (GUI)
- MySQL (Database)
- PIL (for displaying image)
- mysql-connector-python (to connect Python with MySQL)

## How to Run

1. Ensure MySQL is installed and running on your system.
2. Create a database named `coaching_project` in MySQL.
3. Use the `schema.sql` file (included) to create the required tables.
4. Install the Python dependencies listed in `requirements.txt`.
5. Run the application using:

```bash
python main.py
