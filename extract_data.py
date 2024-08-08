import pandas as pd

data = pd.read_csv('ka-data.csv', encoding='ISO-8859-1')
grouped = data.groupby('Country')

for country, group in grouped:
    filename = f"{country.replace(' ', '_')}.csv"
    group.to_csv(filename, index=False)