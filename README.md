# 📰 News Scraping & Analytics Pipeline

## Overview

This project implements a data-engineering-oriented pipeline to collect news articles from online magazines, transform them into structured datasets, and make them available for product analytics, NLP, and data science workflows.

The system follows a modular architecture inspired by modern data stacks: ingestion → transformation → storage → analytics.

It is designed to be reproducible, extensible, and suitable for analytics teams.

---

## Objectives

- Automatically collect articles from news websites
- Extract structured fields (title, date, author, category, content, URL)
- Handle pagination and infinite scroll
- Clean and normalize text data
- Store datasets in analytics-friendly formats
- Enable downstream product analytics and NLP

## Data Engineering Architecture

The pipeline follows a layered approach similar to modern analytics stacks.

### High-Level Flow

[ News Websites / APIs ]
|
v
Ingestion Layer
|
v
Raw Storage (data/raw)
|
v
Parsing & Extraction
|
v
Transformation & Cleaning
|
v
Processed Storage (data/processed)
|
v
Analytics / NLP / Dashboards


---

### Detailed Architecture

            +----------------------+
            |   News Websites     |
            +----------+-----------+
                       |
                       v
              +------------------+
              |   Ingestion      |
              | (requests / API) |
              +------------------+
                       |
                       v
              +------------------+
              |   Raw Layer      |
              |   data/raw       |
              +------------------+
                       |
                       v
              +------------------+
              | Parsing Layer   |
              | BeautifulSoup  |
              +------------------+
                       |
                       v
              +------------------+
              | Transformation |
              | Cleaning / NLP |
              +------------------+
                       |
                       v
              +------------------+
              | Processed Layer |
              | data/processed |
              +------------------+
                       |
                       v
    +------------------+------------------+
    |                                     |
    v                                     v
