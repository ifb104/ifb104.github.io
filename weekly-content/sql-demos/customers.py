from sqlite3 import *

def create_and_populate():
    # Create a connection to the database
    connection = connect(database = 'customers.db')

    # Get a local view of the database
    cursor = connection.cursor()

    # Drop the customers table if it exists
    cursor.execute('DROP TABLE IF EXISTS customers')

    # Create the customers table
    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            state TEXT
        );
    ''')

    # Define the data as a list of tuples
    data = [
        (1, 'John', 18, 'QLD'),
        (2, 'Peter', 25, 'NSW'),
        (3, 'Amy', 16, 'VIC'),
        (4, 'Hannah', 21, 'QLD'),
        (5, 'Michael', 22, 'VIC'),
        (6, 'Sandy', 15, 'VIC'),
        (7, 'Betty', 19, 'NSW'),
        (8, 'Richard', 17, 'QLD'),
        (9, 'Susan', 30, 'QLD'),
        (10, 'Vicky', 60, 'VIC')
    ]

    # Insert the data into the table
    for row in data:
        command = f'INSERT INTO customers VALUES ({row[0]}, "{row[1]}", {row[2]}, "{row[3]}")'
        cursor.execute(command) 

    # Commit the changes
    connection.commit()

    # Close the connection
    cursor.close()
    connection.close()

def age_over_18():
    # Create a connection to the database
    connection = connect(database = 'customers.db')

    # Get a local view of the database
    cursor = connection.cursor()

    # Select all customers where the age is greater than or equal to 18
    cursor.execute('''
        SELECT *
        FROM customers
        WHERE age >= 18;
    ''')

    # Print the result
    for id, name, age, state in cursor.fetchall():
        print(name + ' is ' + str(age) + ' years old and lives in ' + state)

    # Close the connection
    cursor.close()
    connection.close()

def customers_by_state():
    # Create a connection to the database
    connection = connect(database = 'customers.db')

    # Get a local view of the database
    cursor = connection.cursor()

    # Count the number of customers in each state
    cursor.execute('''
        SELECT state, COUNT(*) AS num_customers
        FROM customers
        GROUP BY state;
    ''')

    # Print the result
    for state, num_customers in cursor.fetchall():
        print(state + ' has ' + str(num_customers) + ' customers')

    # Close the connection
    cursor.close()
    connection.close()

create_and_populate()
age_over_18()
customers_by_state()