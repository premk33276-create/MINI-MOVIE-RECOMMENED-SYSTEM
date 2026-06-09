# Movie Recommendation System

A simple Python-based Movie Recommendation System that recommends movies based on the user's favorite genre using a movie dataset.

##  Features

- Search movies by genre
- Display Top 10 recommended movies
- Show movie ratings
- Show movie runtime
- Provide homepage links (if available)
- Visualize recommendations using bar charts
- Compare:
  - Top 10 movies in selected genre
  - Top 10 highest-rated movies in the entire dataset

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## Project Structure

```
Movie-Recommendation-System/
│
├── movies.csv
├── movie_recommender.py
├── README.md
```

---

## Required Libraries

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

---

## How to Run

1. Clone the repository:

```bash
git clone <your-github-repository-link>
```

2. Navigate to the project folder:

```bash
cd Movie-Recommendation-System
```

3. Run the program:

```bash
python movie_recommender.py
```

4. Enter your favorite genre when prompted:

```text
Enter your Favourite Genre : Action
```

---

## Output Example

```text
Enter your Favourite Genre : Action

Top 10 Action Movies Recommended:

1. The Dark Knight (⭐ 8.5/10, 152 min)
Homepage : https://www.warnerbros.com

2. Inception (⭐ 8.3/10, 148 min)
Homepage : https://www.warnerbros.com

...
```

The program also generates:

- Bar chart of Top 10 movies in the selected genre
- Bar chart of Top 10 highest-rated movies in the dataset

---

##  Visualization

The project creates two graphs:

### 1. Genre-Based Recommendations
Shows the ratings of the top 10 movies from the selected genre.

### 2. Overall Top Rated Movies
Shows the ratings of the top 10 highest-rated movies in the entire dataset.

---

## Dataset Columns Used

The following columns are used from the dataset:

- title
- genres
- vote_average
- runtime
- homepage

---

##  Future Improvements

- Content-based recommendation system
- Collaborative filtering
- Movie posters display
- Streamlit web application
- Search by actor/director
- Genre selection menu
- IMDb integration

---

## ⭐ If you like this project

Give the repository a Star ⭐ on GitHub.
