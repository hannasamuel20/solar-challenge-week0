import pandas as pd

def load_country_data(filepath, country_name):
    df = pd.read_csv(filepath)
    df['Country'] = country_name
    return df
