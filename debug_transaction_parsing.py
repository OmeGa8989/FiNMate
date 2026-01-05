import sys
import os
import pandas as pd
from datetime import datetime
from decimal import Decimal

# Add the project path to sys.path
project_path = r"c:\Users\Sneha Bansal\Downloads\BNP-Hackathon\backend\finmate"
sys.path.append(project_path)

# Sample data that matches the user's input
sample_data = {
    'Date': ['01-Jan-25', '01-Jan-25', '02-Jan-25'],
    'Description': ['OPENING BALANCE', 'SALARY CRED', 'MakeMyTrip'],
    'Withdrawal': [0, 0, 734],
    'Deposit': [0, 75000, 0],
    'Balance': [10000, 85000, 84266]
}

df = pd.DataFrame(sample_data)
print("Original Sample Data:")
print(df)
print(f"Total rows: {len(df)}")
print()

# Test date parsing
DATE_FORMATS = [
    '%Y-%m-%d',
    '%m/%d/%Y',
    '%d/%m/%Y',
    '%m-%d-%Y',
    '%d-%m-%Y',
    '%Y/%m/%d',
    '%d.%m.%Y',
    '%m.%d.%Y',
    '%d-%b-%y',    # 01-Jan-25
    '%d-%b-%Y',    # 01-Jan-2025
    '%d/%b/%Y',    # 01/Jan/2025
    '%d %b %Y',    # 01 Jan 2025
    '%d %b %y',    # 01 Jan 25
    '%b %d, %Y',   # Jan 01, 2025
    '%B %d, %Y',   # January 01, 2025
]

def parse_date(date_str):
    for date_format in DATE_FORMATS:
        try:
            return datetime.strptime(date_str.strip(), date_format)
        except ValueError:
            continue
    return None

print("Date Parsing Test:")
for date_str in df['Date']:
    parsed = parse_date(str(date_str))
    print(f"'{date_str}' -> {parsed}")
print()

# Test amount calculation (like the backend does)
amount_series = pd.Series([0.0] * len(df))

# Process withdrawal column (negative amounts)
withdrawal_values = df['Withdrawal'].fillna(0)
withdrawal_numeric = pd.to_numeric(withdrawal_values, errors='coerce').fillna(0)
amount_series -= withdrawal_numeric.abs()

# Process deposit column (positive amounts)  
deposit_values = df['Deposit'].fillna(0)
deposit_numeric = pd.to_numeric(deposit_values, errors='coerce').fillna(0)
amount_series += deposit_numeric.abs()

df['calculated_amount'] = amount_series

print("Amount Calculation Test:")
print(df[['Description', 'Withdrawal', 'Deposit', 'calculated_amount']])
print()

# Test final transaction filtering
print("Final Transaction Analysis:")
for idx, row in df.iterrows():
    date_val = row['Date']
    desc_val = row['Description'] 
    amount_val = row['calculated_amount']
    
    parsed_date = parse_date(str(date_val))
    
    print(f"Row {idx + 1}: {desc_val}")
    print(f"  Date: '{date_val}' -> {parsed_date}")
    print(f"  Amount: {amount_val}")
    print(f"  Should include: {parsed_date is not None and amount_val != 0}")
    print(f"  Transaction type: {'income' if amount_val > 0 else 'expense' if amount_val < 0 else 'zero'}")
    print()

# Show expected results
print("Expected Results:")
print("- Total transactions: 2 (exclude OPENING BALANCE with ₹0)")
print("- SALARY CRED: +₹75000 (income)")  
print("- MakeMyTrip: -₹734 (expense)")
print("- Total income: ₹75000")
print("- Total expenses: ₹734")
print("- Net savings: ₹74266")