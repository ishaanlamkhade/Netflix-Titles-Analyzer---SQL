import sqlite3
import pandas as pd

# Load the CSV
df = pd.read_csv("netflix_titles.csv")

# Connect to SQLite (creates netflix.db)
conn = sqlite3.connect("netflix.db")
cursor = conn.cursor()

# Drop old table if it exists
cursor.execute("DROP TABLE IF EXISTS netflix")

# Create new table
cursor.execute("""
CREATE TABLE netflix (
    show_id TEXT PRIMARY KEY,
    type TEXT,
    title TEXT,
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added TEXT,
    release_year INTEGER,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
)
""")

# Insert records
df.to_sql("netflix", conn, if_exists="append", index=False)

# Commit & close
conn.commit()
conn.close()

print("✅ Data loaded successfully!")
