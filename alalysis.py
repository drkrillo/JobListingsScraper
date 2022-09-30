import pandas as pd

# Read generated file
df = pd.read_csv('job_listings_updated.csv')
# Check columns data
for i in range(10):
    print(f'Listing {i}')
    for column in df.columns.tolist():
        print(column, '', df.loc[i,column])
        print('')