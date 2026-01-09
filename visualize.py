import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("data/imdb_cleaned.csv")

# Count number of movies per genre (top 10)
genre_counts = df['Genre'].value_counts().head(10)

# Plot bar chart
plt.figure(figsize=(10,6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Movie Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as image
plt.savefig("data/top_genres.png")
plt.show()

print("✅ Visualization saved as data/top_genres.png")
