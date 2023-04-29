---
layout: default
title: Week 9 - How to Remember Things
nav_order: 9
permalink: /weekly-content/week-9
---

# Week 9 - How to Remember Things
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Basic SQL Data Manipulation Language (DML) Statements

**Creating Tables**

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
    PRIMARY KEY (column1)
);
```

**Inserting Data**

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**Updating Data**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Deleting Data**

```sql
DELETE FROM table_name
WHERE condition;
```

**Retrieving Data**

```sql
SELECT [DISTINCT | ALL] [* | column_list | expression_list]
FROM table_list
[WHERE condition]
[GROUP BY column_list]
[ORDER BY column_list [ASC | DESC]];
```
### `SELECT` - `FROM`

The `SELECT` statement is used to select data from a database. The data returned is stored in a result table, called the result-set.

```sql
SELECT column1, column2, ...
FROM table_name;
```

To select all columns in a table, use the `*` character:

```sql
SELECT *
FROM table_name;
```

### `WHERE`

The `WHERE` clause is used to filter records. The `WHERE` clause is used to extract only those records that fulfill a specified condition.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

For example, to select all records where the `age` is greater than or equal to 18 from the `customers` table:

| id | name | age | state |
| --- | --- | --- | --- |
| 1 | John | 18 | QLD |
| 2 | Peter | 25 | NSW |
| 3 | Amy | 16 | VIC |
| 4 | Hannah | 21 | QLD |
| 5 | Michael | 22 | VIC |
| 6 | Sandy | 15 | VIC |
| 7 | Betty | 19 | NSW |
| 8 | Richard | 17 | QLD |
| 9 | Susan | 30 | QLD |
| 10 | Vicky | 60 | VIC |

```sql
SELECT *
FROM customers
WHERE age >= 18;
```

Result:

| id | name | age | state |
| --- | --- | --- | --- |
| 1 | John | 18 | QLD |
| 2 | Peter | 25 | NSW |
| 4 | Hannah | 21 | QLD |
| 5 | Michael | 22 | VIC |
| 7 | Betty | 19 | NSW |
| 9 | Susan | 30 | QLD |
| 10 | Vicky | 60 | VIC |

### `GROUP BY`

The `GROUP BY` statement is often used with aggregate functions (`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`) to group the result-set by one or more columns.

```sql
SELECT column_list, aggregate_function(column3)
FROM table_name
GROUP BY column_list;
```

For example, to count the number of customers in each state:

```sql
SELECT state, COUNT(*) AS num_customers
FROM customers
GROUP BY state;
```

Result:

| state | num_customers |
| --- | --- |
| NSW | 2 |
| QLD | 4 |
| VIC | 4 |

### `ORDER BY`

The `ORDER BY` keyword is used to sort the result-set in ascending or descending order.

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

For example, to select all customers from the `customers` table, sorted by the `age` column:

```sql
SELECT *
FROM customers
ORDER BY age ASC;
```

Result:

| id | name | age | state |
| --- | --- | --- | --- |
| 6 | Sandy | 15 | VIC |
| 3 | Amy | 16 | VIC |
| 8 | Richard | 17 | QLD |
| 1 | John | 18 | QLD |
| 7 | Betty | 19 | NSW |
| 4 | Hannah | 21 | QLD |
| 5 | Michael | 22 | VIC |
| 2 | Peter | 25 | NSW |
| 9 | Susan | 30 | QLD |
| 10 | Vicky | 60 | VIC |

## Python SQL Module - `sqlite3`

The `sqlite3` module provides a SQL interface to the SQLite database that is built into Python. It is a built-in module, so you don't need to install it.

The following example shows how to generate the `customers` table above using the `sqlite3` module:

```python
from sqlite3 import *

# Create a connection to the database
connection = connect(database = 'customers.db')

# Get a local view of the database
cursor = connection.cursor()

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
    command = f'INSERT INTO customers VALUES ({row[0]}, {row[1]}, {row[2]}, {row[3]})'
    cursor.execute(command) 

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()
```

The following example shows how to retrieve data where the `age` is greater than or equal to 18 from the `customers` table:

```python
from sqlite3 import *

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

# Output:
# John is 18 years old and lives in QLD
# Peter is 25 years old and lives in NSW
# Hannah is 21 years old and lives in QLD
# Michael is 22 years old and lives in VIC
# Betty is 19 years old and lives in NSW
# Susan is 30 years old and lives in QLD
# Vicky is 60 years old and lives in VIC
```

The following example shows how to count the number of customers in each state:

```python
from sqlite3 import *

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

# Output:
# NSW has 2 customers
# QLD has 4 customers
# VIC has 4 customers
```