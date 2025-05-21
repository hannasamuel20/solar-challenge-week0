import os
from scripts import load_data
import pandas as pd

def load_all_data():
    df_benin = load_data.load_country_data("data/benin_clean.csv", "Benin")
    df_sierraleone = load_data.load_country_data("data/sierraleone_clean.csv", "Sierra Leone")
    df_togo = load_data.load_country_data("data/togo_clean.csv", "Togo")

    df_benin = df_benin[df_benin['z_outlier'] == False ]
    df_sierraleone = df_sierraleone[df_sierraleone['z_outlier'] == False ]
    df_togo = df_togo[df_togo['z_outlier'] == False ]
    
    return df_benin,df_sierraleone,df_togo

def compute_summary(df_benin, df_sierraleone, df_togo):
    countries = ['Benin', 'Sierra Leone', 'Togo']
    dataframes = [df_benin, df_sierraleone, df_togo]
    attributes = ['GHI', 'DNI', 'DHI']

    # Create an empty list to store results
    summary_data = []

    # Loop through each country and attribute to calculate stats
    for country, df in zip(countries, dataframes):
        for attr in attributes:
            mean_val = df[attr].mean()
            median_val = df[attr].median()
            std_val = df[attr].std()
            
            summary_data.append({
                'Country': country,
                'Attribute': attr,
                'Mean': round(mean_val, 2),
                'Median': round(median_val, 2),
                'Std Dev': round(std_val, 2)
            })

    # Convert to a summary DataFrame
    summary_df = pd.DataFrame(summary_data)

    # Pivot for a cleaner comparison table 
    pivot_summary = summary_df.pivot(index='Attribute', columns='Country', values=['Mean', 'Median', 'Std Dev'])

    # Display the pivot table
    return pivot_summary

