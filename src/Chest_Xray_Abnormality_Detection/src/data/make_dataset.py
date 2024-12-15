import pandas as pd

# Đọc file CSV
csv_path = '../../data/processed/annotations/train_2000.csv'
file_names = pd.read_csv(csv_path)['name'].tolist()
file_names_2000 = file_names[:2000]
