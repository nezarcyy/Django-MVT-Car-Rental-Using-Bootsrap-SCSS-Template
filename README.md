# Rental Car Management System
This is a Rental Car Management System designed to facilitate the management of rental cars, clients, reservations, and employees. It provides a user-friendly interface for administrators to handle various operations related to rental car management.

The system is built using the Datta Able template, which offers a modern and responsive design. It utilizes a database to store information about employees, clients, types of cars, car brands, rental cars, and reservations.

# Features
User Authentication: The system provides user authentication for administrators, employees and clients to access the management features.
Employee Management: Add, edit, and delete employee details such as name, contact information..
Client Management: Manage client information including name, contact details.
Car Management: Add, edit, and delete rental car information including car type, brand, model, registration number, and availability.
Reservation Management: Create and manage reservations by specifying the client, rental car, pickup and return dates, and rental duration.
# Technologies Used
Backend Framework: Django
Frontend Template: Datta Able
Database: Sqlite3
Installation
Clone the repository:

git clone (https://github.com/nezarcyy/car-rental-management-system)
Navigate to the project directory:

cd rental-car-management-system
Create and activate a virtual environment:

python -m venv env

source env/bin/activate  # For Linux/Mac

env\Scripts\activate  # For Windows

Install the project dependencies:

pip install -r requirements.txt
Set up the database:

Create a Sqlite3 database and update the database settings in the settings.py file.

Apply database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Access the application in your web browser at http://localhost:8000.

# Usage
Create a superuser account:

python manage.py createsuperuser
This will allow you to access the admin interface at http://localhost:8000/admin and manage the system data.

Log in to the system using your superuser credentials.

Use the sidebar navigation to access various management features such as employee management, client management, car management, and reservation management.

# Class Diagram

