import sqlite3

# Create a database connection
conn = sqlite3.connect('cognitive_biases.db')
cursor = conn.cursor()

# Create a table for biases
cursor.execute('''
    CREATE TABLE IF NOT EXISTS biases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Predefined biases
biases = [
    "Cognitive Bias", 
    "Halo Effect", 
    "Hindsight Bias", 
    "Anchoring Bias", 
    "Self-Serving Bias", 
    "Illusion of Control", 
    "Confirmation Bias"
]

# Insert biases into the table
for bias in biases:
    cursor.execute('INSERT INTO biases (name) VALUES (?)', (bias,))

# Commit and close
conn.commit()
conn.close()

print("Database and biases created successfully!")
