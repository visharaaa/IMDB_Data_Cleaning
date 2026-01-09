import pandas as pd

# Load messy dataset
df = pd.read_csv("data/messy_IMDb_dataset.csv", encoding="ISO-8859-1", sep=";")

# 1) Rename messy column names
df.rename(columns={
    'IMBD title ID': 'IMDb_Title_ID',
    'Original titlÊ': 'Original_Title',
    'Release year': 'Release_Year',
    'Genrë¨': 'Genre',
    ' Votes ': 'Votes'
}, inplace=True)

# 2) Remove completely empty column if it exists
if 'Unnamed: 8' in df.columns:
    df.drop(columns=['Unnamed: 8'], inplace=True)

# 3) Convert numeric columns
df['Release_Year'] = pd.to_numeric(df['Release_Year'], errors='coerce')
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

# 4) Handle missing values (future-proof version)
df.loc[:, 'Genre'] = df['Genre'].fillna('Unknown')
df.loc[:, 'Original_Title'] = df['Original_Title'].fillna("No Title")

# 5) Remove duplicates
df.drop_duplicates(inplace=True)

# 6) Save cleaned data
df.to_csv("data/imdb_cleaned.csv", index=False)
print("✅ Cleaned data saved as data/imdb_cleaned.csv")
