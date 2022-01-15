import requests
from bs4 import BeautifulSoup

URL = "https://stacker.com/stories/1587/100-best-movies-all-time"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")

movies_title = [movie.getText() for movie in all_movies]

# for n in range(len(movies_title)-1, -1, -1):
#     print(movies_title[n])

movies = movies_title[::-1]

with open("movies.txt",mode="w") as file:
    for movie in movies:
        file.write(f"{movie}")
