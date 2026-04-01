# Circular Economy Repair Database

This project is a relational database application designed to support a local circular economy initiative. It connects individuals who have broken household items with skilled local repairers, aiming to reduce landfill waste and promote sustainability.

## Technologies Used
* **Database:** PostgreSQL
* **Language:** Python 3
* **Adapter:** psycopg2
* **Environment:** Windows Subsystem for Linux (WSL / Ubuntu)

## Project Structure
* `app.py`: The main database setup script. It establishes the connection, drops existing tables to ensure a clean state, creates the 7 required tables (Users, Categories, Repairers, RepairerSkills, ServiceRequests, Appointments, Reviews), and populates them with sample test data.
* `queries.py`: The query execution script. It runs specific SQL queries (like calculating the total KG of landfill saved and finding 5-star reviews) to demonstrate the database's analytical capabilities.
* `.gitignore`: Ensures local Python virtual environment files are not uploaded to the repository.

## Setup and Installation

### Prerequisites
Ensure you have PostgreSQL, Python 3, and `pip` installed on your Linux/WSL environment.

### 1. Configure the Database
Start the PostgreSQL service and create the required database and user:
```bash
sudo service postgresql start
sudo -u postgres psql