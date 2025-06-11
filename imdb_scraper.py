import requests
from bs4 import BeautifulSoup
import json
from imdb import Cinemagoer

def fetch_top_10_movies():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find("script", type="application/ld+json")
    if not script_tag:
        print("[ERROR] JSON verisi bulunamadı!")
        return []

    data = json.loads(script_tag.string)
    items = data.get("itemListElement", [])[:10]
    movies = []

    ia = Cinemagoer()
    for item in items:
        title = item["item"]["name"]
        link = item["item"]["url"]
        movie = ia.search_movie(title)[0]
        movie_data = ia.get_movie(movie.movieID)
        storyline = movie_data.get('plot outline', 'No storyline available.')
        description = movie_data.get('plot', ['No description available.'])[0]

        movies.append({
            "title": title,
            "imdb_link": link,
            "storyline": storyline,
            "description": description
        })

    return movies