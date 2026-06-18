# Quote Scraper

A simple Python web scraping project that extracts quotes and their authors from the Quotes to Scrape website and stores the data in a CSV file.

## Project Overview

This project demonstrates the fundamentals of web scraping using Python. It sends a request to a webpage, parses the HTML content, extracts useful information, and saves the results into a structured CSV file.

The scraper collects:

- Quote text
- Author name

The extracted data is stored in a CSV file for further analysis or processing.

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- CSV Module

---

## Project Structure

```
quote_scraper.py
books.csv
README.md
```

---

## How It Works

1. Sends an HTTP request to the website.
2. Retrieves the HTML content.
3. Uses BeautifulSoup to parse the page.
4. Finds all quote containers.
5. Extracts:
   - Quote text
   - Author name
6. Saves the data into a CSV file.

---

## Sample Output

| Description | Author |
|------------|---------|
| “The world as we have created it...” | Albert Einstein |
| “It is our choices, Harry...” | J.K. Rowling |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amorsaralynn08-arch/virtual_env
```

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## Usage

Run the scraper:

```bash
python quote_scraper.py
```

After execution, a CSV file named `books.csv` will be generated containing the scraped data.

---

## Learning Objectives

This project helped demonstrate:

- Making HTTP requests in Python
- Parsing HTML using BeautifulSoup
- Extracting specific webpage elements
- Storing scraped data in CSV format
- Basic web scraping workflow

---

## Future Improvements

- Scrape multiple pages automatically
- Export data to Excel
- Store data in a database
- Add error handling and logging
- Create a simple GUI for users

---

## Author

Saralynn Amor

Student Project – Python Web Scraping Practice