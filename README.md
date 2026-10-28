# api_extraction
## API Data Extraction and Transformation


A Python-based data engineering project that extracts customer data from a REST API, processes nested JSON structures, transforms the data into a tabular format, and exports a cleaned dataset to CSV.

## Overview

Data engineering begins with collecting raw data and transforming it into a format that can be stored, analyzed, and used downstream.

This project demonstrates a basic ETL workflow:

- **Extract:** Retrieve customer records from a REST API.
- **Transform:** Inspect nested JSON, select relevant fields, flatten nested structures, and standardize data types.
- **Load:** Export the transformed dataset to a CSV file for further analysis.

The project focuses on building practical skills in API integration, data transformation, error handling, and data pipeline development.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | HTTP requests and API communication |
| Pandas | Data transformation and tabular data processing |
| JSON | Handling API responses |
| CSV | Exporting structured data |
| Git & GitHub | Version control and project hosting |

## Features

- Fetch customer data from an external API.
- Handle common HTTP errors, connection failures, timeouts, and invalid JSON responses.
- Inspect nested JSON structures and their data types.
- Extract essential customer information.
- Use list and dictionary comprehensions to construct data structures.
- Flatten nested dictionaries and lists into tabular columns.
- Standardize column names and convert selected fields to appropriate data types.
- Export the transformed dataset to CSV.
- Display a summary of the extracted and processed data.

## Project Structure

```text
api_extraction/
├── extract_customers.py
├── customers_clean.csv
└── README.md
```

The script creates an `output/` directory when it runs successfully and saves the generated CSV there.

## Getting Started

### Prerequisites

- Python 3.9 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/elijahlabsx/api_extraction.git
cd api_extraction
```

### 2. Install dependencies

```bash
pip install requests pandas
```

### 3. Run the pipeline

```bash
python extract_customers.py
```

### 4. Review the output

After a successful run, the script generates:

```text
output/
└── customers_clean.csv
```

The CSV contains structured customer information, including personal contact fields, address details, geographical coordinates, and company information.

## Data Transformation

The pipeline converts nested JSON records into a flat, analysis-ready dataset.

Examples of fields produced include:

- `customer_id`
- `name`
- `email`
- `address_city`
- `address_geo_lat`
- `address_geo_lng`
- `company_name`
- `company_catchphrase`

The transformation process also standardizes selected column names and converts numeric fields to suitable data types.

## Error Handling

The script includes handling for common API request and response failures, including:

- Connection errors
- Request timeouts
- HTTP errors
- Invalid JSON responses
- Other request-related exceptions

This helps make the extraction process more reliable and easier to troubleshoot.

## Learning Outcomes

Through this project, I practised:

- Working with REST APIs and HTTP requests
- Processing nested JSON data
- Writing reusable Python functions
- Applying list and dictionary comprehensions
- Flattening semi-structured data
- Using Pandas for data cleaning and transformation
- Exporting structured datasets
- Managing source code with Git and GitHub

## Future Improvements

Potential improvements include:

- Adding automated unit tests
- Moving API endpoints and configuration into environment variables
- Adding structured logging
- Introducing data validation checks
- Automating pipeline execution
- Loading processed data into a relational database



[View the project on GitHub](https://github.com/elijahlabsx/api_extraction)
