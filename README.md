# 🎬 Netflix Titles Analyser

A menu-driven Python + SQL application for exploring the Netflix titles dataset. It lets you search and filter titles by genre, country, rating, release year, or keyword, manage records (add/delete), and generate visual insights with Matplotlib.

Originally built as a Class XII Computer Science project (CBSE) demonstrating database management integrated with Python.

## Features

- 🔍 **Search** titles by genre, country, rating, release year, or title keyword
- 🧩 **Advanced search** combining multiple filters at once
- ➕ **Add** new records to the database
- ➖ **Delete** records by show ID
- 📊 **Visualisations**: top 10 countries, rating distribution, movies vs. TV shows, titles per year
- 🗂️ Neatly formatted table output via `tabulate`

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core application logic |
| SQLite | Lightweight relational database |
| pandas | Loading and cleaning the CSV dataset |
| matplotlib | Data visualisations |
| tabulate | Formatted console tables |

## Project Structure

```
netflix-titles-analyser/
├── data/
│   └── netflix_titles.csv     # Source dataset (Kaggle)
├── load_data.py                # Loads CSV into SQLite (creates netflix.db)
├── netflix_analyser.py         # Main menu-driven application
├── netflix.db                  # Generated SQLite database (not tracked in git)
└── README.md
```

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install pandas matplotlib tabulate
   ```
2. Load the dataset into SQLite:
   ```bash
   python load_data.py
   ```
3. Run the analyser:
   ```bash
   python netflix_analyser.py
   ```

## Usage

The app presents a menu:

```
Netflix Titles Analyser
1. Search by Genre
2. Search by Country
3. Search by Rating
4. Search by Release Year
5. Search by Title Keyword
6. Add Record
7. Delete Record
8. Advanced Search
9. Show Visualisations
10. Exit
```

Enter a number to select an option, then follow the prompts.

## Dataset

The dataset used is the [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) dataset from Kaggle, containing fields such as `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, and `description`.

## Sample Visualisations

The `Show Visualisations` option generates:
- Bar chart of the top 10 countries by title count
- Bar chart of rating distribution
- Pie chart of Movies vs. TV Shows
- Line chart of number of titles released per year

## Future Improvements

- Add a GUI (e.g. Tkinter or Streamlit) instead of a console menu
- Export search results to CSV/Excel
- Add pagination for large result sets
- Input validation for `Add Record`

## Author

**Ishaan Lamkhade**
Class XII-D, GEMS New Millennium School, Al Khail
Computer Science Project, 2025–26

## License

This project is for educational purposes.
