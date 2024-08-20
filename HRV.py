import pandas as pd
import requests
import json

def call_api(content, text_type="news", language="hrv"):
    url = "http://sentiment.efficode-systems.hr/sentiment/"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "text_type": text_type,
        "language": language,
        "content": content
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def load_and_process_excel(input_excel, output_excel):
    df = pd.read_excel(input_excel)

    # Add character count columns
    df['HEADLINE_CHAR_COUNT'] = df['HEADLINE'].apply(len)
    df['TEXT_CHAR_COUNT'] = df['TEXT'].apply(len)

    # Add word count columns
    df['HEADLINE_WORD_COUNT'] = df['HEADLINE'].apply(lambda x: len(str(x).split()))
    df['TEXT_WORD_COUNT'] = df['TEXT'].apply(lambda x: len(str(x).split()))
    
    # Initialize lists to store API results
    results = []

    for text_type in ['news', 'social']:
        for index, record in df.iterrows():
            # Call API for HEADLINE
            headline_response = call_api(record['HEADLINE'], text_type)
            headline_response = {f'HEADLINE_{k}_{text_type}': v for k, v in headline_response.items()}
            # Call API for TEXT
            text_response = call_api(record['TEXT'], text_type)
            text_response = {f'TEXT_{k}_{text_type}': v for k, v in text_response.items()}
            
            # Combine the responses with the original record
            combined_result = {**record, **headline_response, **text_response, 'TEXT_TYPE': text_type, 'LANGUAGE': 'hrv'}
            results.append(combined_result)

    # Convert list of results to DataFrame
    result_df = pd.DataFrame(results)

    # Save the combined DataFrame to a new Excel file
    result_df.to_excel(output_excel, index=False)

# Example usage
input_excel = 'C:\\temp\\paperradni\\COVID u Naslovu - HR.xlsx'  # Update with the path to your local Excel file
output_excel = 'C:\\temp\\paperradni\\COVID u Naslovu - HR - result_12_12.xlsx'  # Update with the path to save the output Excel file
load_and_process_excel(input_excel, output_excel)
