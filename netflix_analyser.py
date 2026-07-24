import sqlite3
from tabulate import tabulate
import matplotlib.pyplot as plt

def advanced_search(genre=None, country=None, rating=None, year=None, keyword=None):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()

    query = "SELECT title, release_year, rating, country, listed_in FROM netflix WHERE 1=1"
    params = []

    if genre:
        query += " AND listed_in LIKE ?"
        params.append('%' + genre + '%')
    if country:
        query += " AND country LIKE ?"
        params.append('%' + country + '%')
    if rating:
        query += " AND rating = ?"
        params.append(rating)
    if year:
        query += " AND release_year = ?"
        params.append(year)
    if keyword:
        query += " AND title LIKE ?"
        params.append('%' + keyword + '%')

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()
    conn.close()
    return results

def show_visualisations():
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()

    cursor.execute("SELECT country, COUNT(*) FROM netflix WHERE country NOT NULL GROUP BY country ORDER BY COUNT(*) DESC LIMIT 10")
    data = cursor.fetchall()
    if data:
        countries, counts = zip(*data)
        plt.figure(figsize=(8,5))
        plt.bar(countries, counts)
        plt.title("Top 10 Countries with Most Titles")
        plt.xticks(rotation=45)
        plt.show()

    cursor.execute("SELECT rating, COUNT(*) FROM netflix GROUP BY rating ORDER BY COUNT(*) DESC LIMIT 10")
    data = cursor.fetchall()
    if data:
        ratings, counts = zip(*data)
        plt.figure(figsize=(8,5))
        plt.bar(ratings, counts, color="orange")
        plt.title("Distribution of Ratings")
        plt.xticks(rotation=45)
        plt.show()

    cursor.execute("SELECT type, COUNT(*) FROM netflix GROUP BY type")
    data = cursor.fetchall()
    if data:
        labels, counts = zip(*data)
        plt.figure(figsize=(5,5))
        plt.pie(counts, labels=labels, autopct='%1.1f%%')
        plt.title("Movies vs TV Shows")
        plt.show()

    cursor.execute("SELECT release_year, COUNT(*) FROM netflix GROUP BY release_year ORDER BY release_year")
    data = cursor.fetchall()
    if data:
        years, counts = zip(*data)
        plt.figure(figsize=(10,5))
        plt.plot(years, counts, marker='o')
        plt.title("Number of Titles by Year")
        plt.xlabel("Year")
        plt.ylabel("Count")
        plt.show()

    conn.close()

def search_by_genre(genre):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, release_year, rating FROM netflix WHERE listed_in LIKE ?", ('%' + genre + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def search_by_country(country):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, release_year, rating FROM netflix WHERE country LIKE ?", ('%' + country + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def search_by_rating(rating):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, release_year FROM netflix WHERE rating = ?", (rating,))
    results = cursor.fetchall()
    conn.close()
    return results

def search_by_year(year):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, rating FROM netflix WHERE release_year = ?", (year,))
    results = cursor.fetchall()
    conn.close()
    return results

def search_by_title(keyword):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, release_year, rating FROM netflix WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    conn.close()
    return results


def add_record(record):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO netflix (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, record)
    conn.commit()
    conn.close()
    print("Record added successfully!")

def delete_record(show_id):
    conn = sqlite3.connect("netflix.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM netflix WHERE show_id = ?", (show_id,))
    conn.commit()
    conn.close()
    print("Record deleted successfully!")


while True:
    print("\nNetflix Titles Analyser")
    print("1. Search by Genre")
    print("2. Search by Country")
    print("3. Search by Rating")
    print("4. Search by Release Year")
    print("5. Search by Title Keyword")
    print("6. Add Record")
    print("7. Delete Record")
    print("8. Advanced Search")
    print("9. Show Visualisations")
    print("10. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        genre = input("Enter genre: ")
        results = search_by_genre(genre)
        print(tabulate(results[:10], headers=["Title", "Year", "Rating"], tablefmt="grid"))

    elif choice == "2":
        country = input("Enter country: ")
        results = search_by_country(country)
        print(tabulate(results[:10], headers=["Title", "Year", "Rating"], tablefmt="grid"))

    elif choice == "3":
        rating = input("Enter rating (e.g., PG, TV-MA): ")
        results = search_by_rating(rating)
        print(tabulate(results[:10], headers=["Title", "Year", "Rating"], tablefmt="grid"))

    elif choice == "4":
        year = int(input("Enter release year: "))
        results = search_by_year(year)
        print(tabulate(results[:10], headers=["Title", "Year", "Rating"], tablefmt="grid"))

    elif choice == "5":
        keyword = input("Enter part of title: ")
        results = search_by_title(keyword)
        print(tabulate(results[:10], headers=["Title", "Year", "Rating"], tablefmt="grid"))

    elif choice == "6":
        print("Enter new record details:")
        record = (
            input("show_id: "),
            input("type: "),
            input("title: "),
            input("director: "),
            input("cast: "),
            input("country: "),
            input("date_added: "),
            int(input("release_year: ")),
            input("rating: "),
            input("duration: "),
            input("listed_in: "),
            input("description: ")
        )
        add_record(record)

    elif choice == "7":
        show_id = input("Enter show_id to delete: ")
        delete_record(show_id)

    elif choice == "8":
        print("\nEnter filters (leave blank to skip):")
        genre = input("Genre: ").strip()
        country = input("Country: ").strip()
        rating = input("Rating (e.g., PG, TV-MA): ").strip()
        year = input("Release Year: ").strip()
        keyword = input("Keyword in Title: ").strip()

        year = int(year) if year else None

        results = advanced_search(
            genre if genre else None,
            country if country else None,
            rating if rating else None,
            year,
            keyword if keyword else None
        )

        if results:
            print(tabulate(results[:15], headers=["Title", "Year", "Rating", "Country", "Genre"], tablefmt="grid"))
        else:
            print("No results found.")


    elif choice == "9":
        show_visualisations()
    
    elif choice == "10":
        print("Exiting Netflix Analyser. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
