# Algotic Economic Data Crawler

## Version History

- **v2.0.0**: Added Supabase integration for bulk data upload. Now the script can send all extracted data directly to a Supabase database table in addition to saving output files.
- **v1.0.0**: Local file output only. The script extracts data and saves it as CSV, JSON, and Markdown files (no database integration).

This project is a Python-based web scraper that extracts economic calendar data from [algoticlab.com/calendar.html] using Selenium and BeautifulSoup.

## Features
- Extracts table data with event importance (RED, Orange, Yellow, Holiday)
- Outputs data in three formats: CSV, JSON, Markdown
- Fully automated and ready for data/AI pipelines

## How to Run (Local Version)
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Make sure Chrome and ChromeDriver are installed.
3. Run the script:
    ```
    python algoticEconomicData.py
    ```

## Output Files
- `economic_calendar.csv` : Table data in CSV format
- `economic_calendar.json` : Data in JSON format
- `economic_calendar.md` : Data in Markdown table format

## Notes
- The script runs locally and can be adapted for server/cloud environments.
- To make the repository private, set the visibility to "Private" on GitHub.
- The local version produces all output formats.

---

## License
This project is for educational and research purposes. 