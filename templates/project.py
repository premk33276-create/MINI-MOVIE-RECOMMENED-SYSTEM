import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("movies.csv")
genre=input('Enter your Favourite Genre : ')
recommended_movies = df[df['genres'].str.contains(genre, case=False, na=False)]
recommended_movies.sort_values('vote_average',inplace=True,ascending=False,ignore_index=True)
recommended_movies.columns=recommended_movies.columns.str.capitalize()
print(f"\nTop 10 {genre.title()} Movies Recommended:\n")
recommended_movies=recommended_movies[['Title','Vote_average','Runtime','Homepage']]
for i, (_, movie) in enumerate(recommended_movies.head(10).iterrows(), 1):
    homepage = movie['Homepage']
    if str(homepage)=='nan':
        homepage = "No homepage available Search on Google!"
    print(
        f"{i}. {movie['Title']} "
        f"(⭐ {movie['Vote_average']}/10, "
        f"{movie['Runtime']} min)  "
        f"Homepage : {homepage}")
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
colors = plt.cm.rainbow(np.linspace(0, 1, 10))
top10 = recommended_movies.head(10)
top10_by_dataset=df.sort_values('vote_average',ascending=False).head(10)
top_movies=top10_by_dataset[['title','vote_average']]
plt.bar(top10['Title'], top10['Vote_average'],color=colors)
plt.title(f"Top 10 {genre.title()} Movies")
plt.xlabel("Movie Title")
plt.ylabel("Rating")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.subplot(1,2,2)
plt.bar(top_movies['title'],top_movies['vote_average'],color=colors)
plt.title(f"Top 10  Movies")
plt.xlabel("Movie Title")
plt.ylabel("Rating")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
