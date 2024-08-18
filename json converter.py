import pandas as pd
import json
import re


# Function to clean illegal characters from strings
def clean_illegal_characters(value):
    if isinstance(value, str):
        # Replace illegal characters with a space
        return re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', value)
    return value


# Function to convert JSON file to Excel file
def json_file_to_excel(json_file_path, excel_file_path):
    # Read the JSON data from the file with explicit UTF-8 encoding
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Clean the data
    cleaned_data = []
    for item in data:
        cleaned_item = {k: clean_illegal_characters(v) for k, v in item.items()}
        cleaned_data.append(cleaned_item)

    # Create a DataFrame from the cleaned JSON data
    df = pd.json_normalize(cleaned_data)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)
    print(f"Data successfully written to {excel_file_path}")


# Example usage
# Specify the input JSON file path
json_file_path = r'C:\Users\soumy\PycharmProjects\DeepSort\bengali_hardcode_mix_qa_252k.json'

# Specify the output Excel file path
excel_file_path = 'output.xlsx'

# Call the function to convert JSON file to Excel file
json_file_to_excel(json_file_path, excel_file_path)
