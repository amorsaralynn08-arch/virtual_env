# Price Scraper & Currency Converter

A Python project that scrapes product prices from an e-commerce website, converts the prices into another currency using an exchange rate API.

## Project Overview

This project combines web scraping and API integration to collect product information and perform real-time currency conversion.

The scraper extracts:

- Product Name
- Original Price
- Converted Price

The converted data is then saved to a CSV file for further analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- Currency Exchange API


## Features

- Scrapes prices from an online store
- Extracts and cleans product information
- Converts prices to another currency using live exchange rates
- Displays results in a tabular format





## How It Works

1. Sends a request to the target website.
2. Extracts product names and prices.
3. Retrieves current exchange rates from an API.
4. Converts prices into the target currency.
5. Displays the results in a table.


## Example Output

| Product | Original Price | Converted Price |
|----------|---------------|----------------|
| Book A | £51.77 | KES 9,100 |
| Book B | £35.02 | KES 6,150 |

## Installation

```bash
pip install requests beautifulsoup4 pandas
```

## Run

```bash
python price_scraper.py
```


## Author

Saralynn Amor