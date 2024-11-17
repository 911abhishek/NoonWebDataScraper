
# Noon Web Data Scraper

## Description
**Noon Web Data Scraper** is a Python-based web scraping project designed to extract product information, ratings, pricing details, and other attributes from the **Noon** e-commerce platform. It utilizes the powerful `Scrapy` framework for efficient and scalable data extraction.

## Features
- **Comprehensive Product Details**: Extracts product names, SKU codes, links, and brands.
- **Ratings and Reviews**: Captures average ratings and the number of reviews.
- **Pricing Information**: Scrapes current prices and old prices (if available).
- **Sponsored Identification**: Detects if a product is marked as sponsored.
- **Express Delivery Check**: Flags products eligible for Noon Express delivery.
- **Pagination Support**: Automatically navigates and scrapes multiple pages.
- **Timestamped Data**: Records the exact date and time of extraction.

## Technologies Used
- **Python**: Core programming language for scripting.
- **Scrapy**: Web scraping framework for fast and efficient data retrieval.
- **Regex**: For parsing and cleaning extracted text data.
- **CSV**: Structured format for storing extracted data.

## Installation and Setup

### Prerequisites
Ensure the following are installed:
- Python 3.7+
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/911abhishek/NoonWebDataScraper.git
   cd NoonWebDataScraper
   ```

2. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Scrapy spider:
   ```bash
   scrapy crawl itemDetails -o Extractions.csv
   ```

## Output
The scraped data will be stored in a CSV file named `Extractions.csv`. Below are the fields included in the output:
- **Date & Time**: The timestamp of when the data was scraped.
- **SKU**: Unique product identifier.
- **Name**: Product title.
- **Brand**: Brand name of the product.
- **Average Rating**: The average rating of the product.
- **Rating Count**: Total number of ratings.
- **Sponsored**: Whether the product is sponsored (Yes/No).
- **Price**: Current price of the product.
- **Sales Price**: Previous (old) price of the product, if available.
- **Express**: Indicates if the product is eligible for Noon Express delivery.
- **Rank**: Rank of the product on the page.
- **Link**: URL of the product page.

## Project Structure
```
.
├── README.md              # Documentation
├── requirements.txt       # Project dependencies
├── NoonWebDataScraper/    # Scrapy project folder
│   ├── spiders/           # Contains spider logic for scraping
│   └── settings.py        # Scrapy project settings
└── Extractions.csv        # Output file (after scraping)
```

## License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project under the terms of the license.  

## Author
**Abhishek Kumar**  
- GitHub: [911abhishek](https://github.com/911abhishek)
- Email: codeitabhishek911@gmail.com
