import pandas as pd
import os

def save_to_excel(data, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)