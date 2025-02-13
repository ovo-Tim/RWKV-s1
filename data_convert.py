import pandas as pd
import ujson as json

# Load the Parquet file
parquet_file_path = './train-00000-of-00001.parquet'  # Replace with your Parquet file path
df = pd.read_parquet(parquet_file_path)

# Create a list to hold each converted JSON line entry
jsonl_entries = []

# Iterate over each row in the DataFrame and create the desired JSON format
for index, row in df.iterrows():
    entry = {
        "text": f"User: {row['question'].replace('\n\n', '\n')}\n\nAssistant: <think>{row['gemini_thinking_trajectory'].replace('\n\n', '\n')}</think> {row['gemini_attempt'].replace('\n\n', '\n')}"
    }
    jsonl_entries.append(entry)

# Write the results to a JSON Lines (.jsonl) file
output_jsonl_file_path = 'jsonl_dataset.jsonl'  # Replace with your desired output .jsonl file path
with open(output_jsonl_file_path, 'w') as jsonl_file:
    for entry in jsonl_entries:
        jsonl_file.write(json.dumps(entry) + '\n')

print(f"Conversion complete, file saved to: {output_jsonl_file_path}")