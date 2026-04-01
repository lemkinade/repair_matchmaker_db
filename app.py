import psycopg2

def setup_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="circular_economy_db",
        user="myuser",
        password="mypassword",
        host="localhost"
    )
    cursor = conn.cursor()

    print("Connected to database. Setting up tables...")

    # Drop tables if they exist to avoid conflicts when re-running the script
    cursor.execute('''
        DROP TABLE IF EXISTS Reviews, Appointments, ServiceRequests, RepairerSkills, Repairers, Categories, Users CASCADE;
    ''')

    # Create Tables based on your project specification
    cursor.execute('''
        CREATE TABLE Users (
            UserID SERIAL PRIMARY KEY,
            FullName VARCHAR(100) NOT NULL,
            Email VARCHAR(100) NOT NULL UNIQUE,
            City VARCHAR(50) NOT NULL,
            ZipCode VARCHAR(10) NOT NULL,
            DateJoined TIMESTAMP NOT NULL
        );

        CREATE TABLE Categories (
            CategoryID SERIAL PRIMARY KEY,
            CategoryName VARCHAR(50) NOT NULL UNIQUE,
            AvgLandfillSaved_KG DOUBLE PRECISION NOT NULL
        );

        CREATE TABLE Repairers (
            RepairerID SERIAL PRIMARY KEY,
            BusinessName VARCHAR(100) NOT NULL,
            ContactEmail VARCHAR(100) NOT NULL UNIQUE,
            City VARCHAR(50) NOT NULL,
            Bio TEXT NOT NULL
        );

        CREATE TABLE RepairerSkills (
            SkillID SERIAL PRIMARY KEY,
            RepairerID INTEGER NOT NULL REFERENCES Repairers(RepairerID),
            CategoryID INTEGER NOT NULL REFERENCES Categories(CategoryID),
            HourlyRate NUMERIC(10,2) NOT NULL
        );

        CREATE TABLE ServiceRequests (
            RequestID SERIAL PRIMARY KEY,
            UserID INTEGER NOT NULL REFERENCES Users(UserID),
            CategoryID INTEGER NOT NULL REFERENCES Categories(CategoryID),
            ItemDescription TEXT NOT NULL,
            RequestStatus VARCHAR(50) NOT NULL,
            RequestDate TIMESTAMP NOT NULL,
            WarrantyEnd TIMESTAMP
        );

        CREATE TABLE Appointments (
            ApptID SERIAL PRIMARY KEY,
            RequestID INTEGER NOT NULL REFERENCES ServiceRequests(RequestID),
            RepairerID INTEGER NOT NULL REFERENCES Repairers(RepairerID),
            ApptDate TIMESTAMP NOT NULL,
            ApptStatus VARCHAR(50) NOT NULL
        );

        CREATE TABLE Reviews (
            ReviewID SERIAL PRIMARY KEY,
            ApptID INTEGER NOT NULL REFERENCES Appointments(ApptID),
            Rating SMALLINT NOT NULL,
            Comment TEXT,
            ReviewDate TIMESTAMP NOT NULL
        );
    ''')

    # Insert sample data to test with
    cursor.execute('''
        INSERT INTO Users (FullName, Email, City, ZipCode, DateJoined) 
        VALUES ('Alice Johnson', 'alice.j@email.com', 'Springfield', '62704', '2023-01-15'),
               ('Bob Smith', 'bob.smith@email.com', 'Shelbyville', '62565', '2023-02-10');
               
        INSERT INTO Categories (CategoryName, AvgLandfillSaved_KG) 
        VALUES ('Electronics', 0.5),
               ('Furniture', 15.0);
               
        INSERT INTO Repairers (BusinessName, ContactEmail, City, Bio) 
        VALUES ('Tech Fix Pro', 'contact@techfix.com', 'Springfield', 'Specializing in laptops and phones.'),
               ('Woodwork Wizards', 'info@woodwizards.com', 'Shelbyville', 'Restoring antique furniture.');
    ''')

    # Query to verify data was inserted
    cursor.execute("SELECT * FROM Users;")
    users = cursor.fetchall()
    
    print("\n--- Registered Users in Database ---")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, City: {user[3]}")

    # Commit the changes and close connections
    conn.commit()
    cursor.close()
    conn.close()
    print("\nDatabase setup completed successfully!")

if __name__ == "__main__":
    setup_database()