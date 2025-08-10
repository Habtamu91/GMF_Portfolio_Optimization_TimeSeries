# src/config.py
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")

def get_data_path(ticker):
    return os.path.join(PROCESSED_DATA_DIR, f"{ticker}_cleaned.csv")

def get_output_path(*subpaths):
    return os.path.join(OUTPUT_DIR, *subpaths)