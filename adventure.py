'''
Week 11 coding assignment: The Lost Temple of Data

Submitted by Braden Mills
'''
from datetime import datetime
import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """ Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows. """
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df

def load_location_notes(tsv_filepath):
    """ Reads location data from a Tab-Separated Value (TSV) file. """
    df = pd.read_csv(tsv_filepath, sep='\t')
    return df

def extract_journal_dates(journal_txt):
    """ Extracts all dates in MM/DD/YYYY format from the journal text. """
    date_pattern = r"\d{2}/\d{2}/\d{4}"
    dates = re.findall(date_pattern, journal_txt)
    valid_dates = []
    for date_str in dates:
        try:
            datetime.strptime(date_str, "%m/%d/%Y")
            valid_dates.append(date_str)
        except ValueError:
            continue
    return valid_dates

def extract_secret_codes(journal_text):
    """  Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text. """
    code_pattern = r"AZMAR-\d{3}"
    codes = re.findall(code_pattern, journal_text)
    return codes

 # --- Optional: Main execution block for your own testing ---
if __name__ == '__main__':
    # Define file paths (adjust if your files are located elsewhere)
    EXCEL_FILE = 'artifacts.xlsx'
    TSV_FILE = 'locations.tsv'
    JOURNAL_FILE = 'journal.txt'

    print(f"--- Loading Artifact Data from {EXCEL_FILE} ---")
    try:
        artifacts_df = load_artifact_data(EXCEL_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(artifacts_df.head())
        print("\nDataFrame Info:")
        artifacts_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {EXCEL_FILE}")

    print(f"\n--- Loading Location Notes from {TSV_FILE} ---")
    try:
        locations_df = load_location_notes(TSV_FILE)
        print("Successfully loaded DataFrame. First 5 rows:")
        print(locations_df.head())
        print("\nDataFrame Info:")
        locations_df.info()
    except FileNotFoundError:
        print(f"Error: File not found at {TSV_FILE}")

    print(f"\n--- Processing Journal from {JOURNAL_FILE} ---")
    try:
        with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
            journal_content = f.read()

        print("\nExtracting Dates...")
        journal_dates = extract_journal_dates(journal_content)
        print(f"Found dates: {journal_dates}")

        print("\nExtracting Secret Codes...")
        journal_codes = extract_secret_codes(journal_content)
        print(f"Found codes: {journal_codes}")

    except FileNotFoundError:
        print(f"Error: File not found at {JOURNAL_FILE}")
