import random
from datetime import date


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    
    @property
    def get_views(self):
        return self.views


    def play(self):
        self.views += 1


    def __str__(self):
        return f"{self.title} ({self.year})"
    

    def add_view(self, how_much):
        self.views += how_much


class Series(Movie):
    def __init__(self, n_episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_episode = n_episode
        self.season = season


    def __str__(self):
        return f"{self.title} S{str(self.season).zfill(2)}E{str(self.n_episode).zfill(2)}"


def generate_views(lista):
    los = random.choice(lista)
    los.add_view(random.randint(1, 100))


def magic_function(lista):
    for _ in range(10):
        generate_views(lista)


def get_movies(lista):
    only_movies = []
    for video in lista:
        if not isinstance(video, Series):
            only_movies.append(video)
    return sorted(only_movies, key= lambda a: str(a))
    

def get_series(lista):
    only_series = []
    for video in lista:
        if isinstance(video, Series):
            only_series.append(video)
    return sorted(only_series, key= lambda a: str(a))


def search(lista, search_word):
    for video in lista:
        if search_word in video.title:
            print(video)


def ile_odcinkow(lista, title):
    ile = 0
    for video in lista:
        if title in video.title:
            ile += 1
    return ile


def top_titles(lista, topx, content_type):
    if content_type == "all":
        printing_top_titles(lista, topx, "filmy i seiale")
    elif content_type == "movies":
        printing_top_titles(get_movies(lista), topx, "filmy")
    elif content_type == "series":
        printing_top_titles(get_series(lista), topx, "seriale")

def printing_top_titles(lista, topx, text):
        top = sorted(lista, key= lambda video: video.views, reverse=True)
        top = top[0:topx]
        print(f"Najpopularniejsze {text} {normalna_data}")
        place = 1
        for rank_video in top:
            print(f"{place}. {rank_video}")
            place += 1


def add_season(n_episodes, season, title, year, genre, lista):
    for nn in range(n_episodes):
        lista.append(Series(nn + 1, season, title, year, genre))
    return lista


if __name__ == "__main__":
    library = []
    today = date.today()
    normalna_data = f"{str(today.day).zfill(2)}.{str(today.month).zfill(2)}.{today.year}"
    print("Biblioteka filmów")
    library = add_season(2, 1, "Fairy Tail", 2009, "Fantasy", library)
    library = add_season(2, 2, "Fairy Tail", 2010, "Fantasy", library)
    library = add_season(2, 1, "Black Rock Shooter", 2010, "Thriller", library)
    library.append(Movie("Avatar", 2009, "Sci-Fi"))
    library.append(Movie("Avatar 2", 2022, "Sci-Fi"))
    library.append(Movie("Kim", 2022, "Sci-Fi"))
    library.append(Movie("ZZ", 2022, "Sci-Fi"))
    library.append(Movie("BB", 2022, "Sci-Fi"))
    magic_function(library)
    top_titles(library, 1, "series")
