import sqlite3
conn = sqlite3.connect('chocolate_shop.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
''')

products = [
    (1, "Milk Chocolate", "Rich and creamy milk chocolate", 2.99, 100),
    (2, "Dark Chocolate", "Intense and bitter dark chocolate", 3.49, 50),
    (3, "White Chocolate", "Sweet and smooth white chocolate", 2.79, 75),
    (4, "Hazelnut Chocolate", "Milk chocolate with crunchy hazelnuts", 3.99, 30),
    (5, "Mint Chocolate", "Dark chocolate with a refreshing mint flavor", 3.29, 60)
]
cursor.executemany('INSERT INTO Products VALUES (?,?,?,?,?)', products)

customers = [
    (1, "Alice Smith", "alice@example.com"),
    (2, "Bob Johnson", "bob@example.com"),
    (3, "Carol Williams", "carol@example.com"),
    (4, "David Brown", "david@example.com"),
    (5, "Eve Davis", "eve@example.com")
]
cursor.executemany('INSERT INTO Customers VALUES (?,?,?)', customers)

orders = [
    (1, 1, 3, 2, "2023-10-01"),
    (2, 2, 1, 1, "2023-10-05"),
    (3, 3, 4, 5, "2023-10-10"),
    (4, 4, 2, 3, "2023-10-15"),
    (5, 5, 5, 4, "2023-10-20")
]
cursor.executemany('INSERT INTO Orders VALUES (?,?,?,?,?)', orders)
conn.commit()
conn.close()