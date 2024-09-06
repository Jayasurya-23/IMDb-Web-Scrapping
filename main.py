import requests,openpyxl
from bs4 import BeautifulSoup
import pandas as pd

# URL of the IMDb page we want to scrape
url = 'https://www.imdb.com/chart/top'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the movie data in the HTML
movies = soup.select('td.titleColumn')
ratings = soup.select('td.imdbRating strong')

# Lists to hold the extracted data
titles = []
years = []
imdb_ratings = []

# Loop through movies and extract the title, year, and rating
for index in range(len(movies)):
    title = movies[index].get_text(strip=True).split('\n')[1].split(' (')[0]  # Movie title
    year = movies[index].span.text.strip('()')  # Release year
    rating = ratings[index].text  # IMDb rating

    titles.append(title)
    years.append(year)
    imdb_ratings.append(rating)

# Create a pandas DataFrame from the data
movies_df = pd.DataFrame({
    'Title': titles,
    'Year': years,
    'Rating': imdb_ratings
})

# Save the DataFrame to an Excel file
movies_df.to_excel('imdb_top_movies.xlsx', index=False)

print("Data successfully scraped and saved to 'imdb_top_movies.xlsx'")
