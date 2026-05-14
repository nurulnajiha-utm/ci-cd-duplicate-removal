import pandas as pd
import os
import sys

sys.path.append(os.path.abspath("src"))

from remove_duplicates import remove_duplicates

def test_duplicate_removal():
    test_data = pd.DataFrame({
        "Name": ["Ali", "Ali", "Sara"],
        "Age": [20, 20, 22]
    })

    os.makedirs("data", exist_ok=True)

    test_input = "data/test_dataset.csv"
    test_output = "data/test_output.csv"

    test_data.to_csv(test_input, index=False)

    original, cleaned = remove_duplicates(test_input, test_output)

    cleaned_df = pd.read_csv(test_output)

    assert original == 3
    assert cleaned == 2
    assert len(cleaned_df) == 2
