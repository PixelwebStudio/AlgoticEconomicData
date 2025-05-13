from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from bs4 import BeautifulSoup

# Driver settings
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://algoticlab.com/calendar.html")

time.sleep(7)  # Wait for the page to fully load like a real user

try:
    # Find the iframe
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)
    time.sleep(3)  # Wait for the iframe content to load
    try:
        table = driver.find_element(By.ID, "ecEventsTable")
        print("Table found!\n")
        # Extract data with BeautifulSoup
        soup = BeautifulSoup(table.get_attribute('outerHTML'), 'html.parser')
        rows = soup.find_all('tr')
        data = []
        current_date = None
        for row in rows:
            # Check if this row is a date row
            day_td = row.find('td', class_='theDay')
            if day_td:
                current_date = day_td.text.strip()
                continue  # Skip the date row itself
            cols = row.find_all('td')
            if not cols:
                continue
            # Extract importance value
            imp_value = ''
            for idx, col in enumerate(cols):
                if 'sentiment' in col.get('class', []):
                    # If Holiday
                    span = col.find('span', class_='bold')
                    if span and span.text.strip() == 'Holiday':
                        imp_value = 'Holiday'
                    else:
                        icons = col.find_all('i', class_='newSiteIconsSprite')
                        full = sum('grayFullBullishIcon' in i.get('class', []) for i in icons)
                        empty = sum('grayEmptyBullishIcon' in i.get('class', []) for i in icons)
                        if full == 3:
                            imp_value = 'RED'
                        elif full == 2 and empty == 1:
                            imp_value = 'Orange'
                        elif full == 1 and empty == 2:
                            imp_value = 'Yellow'
                    # Replace importance value in the corresponding column
                    cols[idx] = imp_value
            cols = [col.text.strip() if hasattr(col, 'text') else col for col in cols]
            # Insert date as the first column
            row_dict = {'date': current_date}
            # Map columns to headers (skip if headers not yet extracted)
            if not data:
                # Extract headers for mapping
                header_row = soup.find('thead').find('tr')
                headers = [th.text.strip() for th in header_row.find_all('th')]
            for h, v in zip(headers, cols):
                row_dict[h] = v
            data.append(row_dict)
        # Ensure 'date' is the first column in output
        output_headers = ['date'] + [h for h in headers if h != 'date']
        df = pd.DataFrame(data, columns=output_headers)
        # Custom filter: remove rows where all main fields (except date) are empty or NaN
        main_fields = [h for h in output_headers if h != 'date']
        df = df[~df[main_fields].apply(lambda row: all((str(x).strip() == '' or pd.isna(x)) for x in row), axis=1)]
        df = df.fillna("")  # Replace NaN with empty string for clean output
        df.to_csv('economic_calendar.csv', index=False, encoding='utf-8-sig')
        print("Data saved to economic_calendar.csv.")
        df.to_json('economic_calendar.json', orient='records', force_ascii=False, indent=2)
        print("Data saved to economic_calendar.json.")
        with open('economic_calendar.md', 'w', encoding='utf-8') as f:
            f.write(df.to_markdown(index=False))
        print("Data saved to economic_calendar.md.")
        
        # --- Optional: Upload to Supabase ---
        # try:
        #     from supabase_uploader import upload_economic_calendar_bulk
        #     # Prepare data as list of dicts matching Supabase table columns
        #     records = df.rename(columns={
        #         'Time': 'time',
        #         'Cur.': 'cur',
        #         'Imp.': 'imp',
        #         'Event': 'event',
        #         'Actual': 'actual',
        #         'Forecast': 'forecast',
        #         'Previous': 'previous'
        #     }).to_dict(orient="records")
        #     upload_economic_calendar_bulk(records)
        # except ImportError:
        #     print("Supabase uploader module not found. Skipping upload.")
        # except Exception as e:
        #     print("Error uploading to Supabase:", e)
    except Exception as e:
        print("Table with ID ecEventsTable not found or error:", e)
    driver.switch_to.default_content()
except Exception as e:
    print("Error finding or switching to iframe:", e)

driver.quit() 