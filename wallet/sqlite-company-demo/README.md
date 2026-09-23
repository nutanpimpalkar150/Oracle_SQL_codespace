# SQLite Company Demo

This project demonstrates how to create and interact with an SQLite database using Python. The database is named `company.db` and contains two tables: `department` and `employee`. 

## Project Structure

```
sqlite-company-demo
├── sqlite_company_demo.py  # Main Python program
├── company.db              # SQLite database file
└── README.md               # Project documentation
```

## Description

- **sqlite_company_demo.py**: This file contains the main logic for creating the SQLite database, defining the tables, inserting dummy records, and fetching/displaying the records. The code is beginner-friendly and includes comments to explain each step.

- **company.db**: This is the SQLite database file that will be created when you run the Python program. It will contain the `department` and `employee` tables populated with sample data.

## How to Run the Program

1. Ensure you have Python installed on your machine.
2. Install the SQLite library if it's not already available (it comes pre-installed with Python).
3. Clone this repository or download the files to your local machine.
4. Open a terminal and navigate to the project directory.
5. Run the Python program using the following command:

   ```
   python sqlite_company_demo.py
   ```

6. The program will create the `company.db` database, insert records into the tables, and display the records in the console.

## Requirements

- Python 3.x
- SQLite (included with Python)

## License

This project is open-source and available for anyone to use and modify.