import pandas as pd

def remove_duplicates(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicate rows
    df_cleaned = df.drop_duplicates()

    # Save cleaned dataset
    df_cleaned.to_csv(output_path, index=False)

    return len(df), len(df_cleaned)

if __name__ == "__main__":
    original, cleaned = remove_duplicates(
        "data/dataset.csv",
        "data/processed_dataset.csv"
    )

    print(f"Original rows: {original}")
    print(f"Rows after duplicate removal: {cleaned}")
