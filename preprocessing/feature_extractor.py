import os
import pandas as pd
import numpy as np

DROP_COLUMNS = [
    'Flow ID',
    'Src IP',
    'Src Port',
    'Dst IP',
    'Dst Port',
    'Timestamp'
]


RAW_DATA_PATH = 'data/raw/'
OUTPUT_PATH = 'data/flows/clean_flows.csv'

def load_and_merge_csvs(path):
    dataframes = []

    for file in os.listdir(path):
        if file.endswith(".csv"):
            file_path = os.path.join(path, file)
            print(f"Loading {file}")
            df = pd.read_csv(file_path)
            dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df

def clean_column_names(df):
    df.columns = df.columns.str.strip()
    return df

def inspect_data(df):
    print("Dataset shape:", df.shape)
    print("\nColumns:\n", list(df.columns))
    print("\nLabel distribution:\n", df['Label'].value_counts())

def drop_unnecessary_columns(df):
    df = df.drop(columns=[col for col in DROP_COLUMNS if col in df.columns])
    return df

def clean_missing_values(df):
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    return df

def convert_labels(df):
    df['Label'] = df['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)
    return df

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Clean dataset saved to {output_path}")

if __name__ == "__main__":
    df = load_and_merge_csvs(RAW_DATA_PATH)
    df = clean_column_names(df)
    inspect_data(df)

    df = drop_unnecessary_columns(df)
    df = clean_missing_values(df)
    df = convert_labels(df)

    save_clean_data(df, OUTPUT_PATH)
