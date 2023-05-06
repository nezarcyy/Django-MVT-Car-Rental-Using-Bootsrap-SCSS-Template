# Rental Car Management System
This is a Rental Car Management System designed to facilitate the management of rental cars, clients, reservations, and employees. It provides a user-friendly interface for administrators to handle various operations related to rental car management.
#

The system is built using the Datta Able template, which offers a modern and responsive design. It utilizes a database to store information about employees, clients, types of cars, car brands, rental cars, and reservations.

Features
User Authentication: The system provides user authentication for administrators to access the management features.
Employee Management: Add, edit, and delete employee details such as name, contact information, and role.
Client Management: Manage client information including name, contact details, and rental history.
Car Type Management: Add and manage car types such as sedan, SUV, or sports car.
Car Brand Management: Manage car brand details like Toyota, BMW, Ford, etc.
Car Management: Add, edit, and delete rental car information including car type, brand, model, registration number, and availability.
Reservation Management: Create and manage reservations by specifying the client, rental car, pickup and return dates, and rental duration.
Technologies Used
Backend Framework: Django
Frontend Template: Datta Able
Database: PostgreSQL
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/rental-car-management-system.git
Navigate to the project directory:

bash
Copy code
cd rental-car-management-system
Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
Install the project dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Create a PostgreSQL database and update the database settings in the settings.py file.

Apply database migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000.

Usage
Create a superuser account:

bash
Copy code
python manage.py createsuperuser
This will allow you to access the admin interface at http://localhost:8000/admin and manage the system data.

Log in to the system using your superuser credentials.

Use the sidebar navigation to access various management features such as employee management, client management, car type management, car brand management, car management, and reservation management.

Screenshots
Insert screenshots of the system's UI here to give a visual representation of the features and layout.

Contributing
Contributions to the Rental Car Management System are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
