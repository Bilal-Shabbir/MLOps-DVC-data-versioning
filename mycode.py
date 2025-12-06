import pandas as pd
import os

data =  {
    'Name': ["Alice", "Bob", "Charlie"], 
    'Age': [25, 30, 35], 
    'City': ["New York", "Los Angeles", 'Torino']
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.txt')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
