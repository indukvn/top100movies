from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
data = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in data]
movies = movie_titles[::-1]
print(movies)

with open("movies.txt", mode="w") as file:
    for title in movies:
        file.write(f"{title}\n")
