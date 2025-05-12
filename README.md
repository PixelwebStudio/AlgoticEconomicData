# Algotic Economic Data Crawler

This project is a Python-based web scraper that extracts economic calendar data from [algoticlab.com/calendar.html](https://algoticlab.com/calendar.html) using Selenium and BeautifulSoup.

## Features
- Extracts table data with event importance (RED, Orange, Yellow, Holiday)
- Outputs data in three formats: CSV, JSON, Markdown
- Fully automated and ready for AI/LLM data pipelines

## How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Make sure you have Chrome and ChromeDriver installed.
3. Run the script:
    ```
    python selenium_script.py
    ```

## Output Files
- `economic_calendar.csv` : Table data in CSV format
- `economic_calendar.json` : Data in JSON format
- `economic_calendar.md` : Data in Markdown table format

## Notes
- The script works locally and can be adapted for cloud/VPS environments.
- For private repository, set the repo visibility to "Private" on GitHub.

---

## License
This project is for educational and research purposes. 