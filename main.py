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
        self.views = self.views + how_much


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
    for ile_razy in range(10):
        generate_views(lista)


def get_movies(lista):
    only_movies = []
    for video in lista:
        if isinstance(video, Movie):
            only_movies.append(video)
    return sorted(only_movies, key=str)
    

def get_series(lista):
    only_series = []
    for video in lista:
        if isinstance(video, Series):
            only_series.append(video)
    return sorted(only_series, key=str)


def search(lista, search_word): # nie jestem pewny czy o coś takiego chodziło
    for video in lista:
        if search_word in str(video):
            print(video)


def ile_odcinkow(lista, title, ile=0):
    for video in lista:
        if title in str(video):
            ile += 1
    return ile


def top_titles(lista, topx, content_type="all"):
    if content_type == "all":
        top = sorted(lista, key=lambda video: video.views, reverse=True)
        repeat = 1
        print(f"Najpopularniejsze filmy i seriale dnia {normalna_data}")
        for rank_video in top:
            print(f"{repeat}. {rank_video}")
            if repeat == topx:
                break
            repeat += 1
    elif content_type == "Movies":
        top = sorted(get_movies(lista), key=lambda video: video.views, reverse=True)
        repeat = 1
        print(f"Najpopularniejsze filmy i seriale dnia {normalna_data}")
        for rank_video in top:
            print(f"{repeat}. {rank_video}")
            if repeat == topx:
                break
            repeat += 1
    elif content_type == "Series":
        top = sorted(get_series(lista), key=lambda video: video.views, reverse=True)
        repeat = 1
        print(f"Najpopularniejsze filmy i seriale dnia {normalna_data}")
        for rank_video in top:
            print(f"{repeat}. {rank_video}")
            if repeat == topx:
                break
            repeat += 1


def add_season(n_episodes, season, title, year, genre, lista):
    for nn in range(n_episodes):
        lista.append(Series(nn + 1, season, title, year, genre))
    return lista


if __name__ == "__main__":
    library = []
    today = date.today()
    normalna_data = f"{str(today.day).zfill(2)}.{str(today.month).zfill(2)}.{today.year}"
    print("Biblioteka filmów")
    library = add_season(12, 1, "Fairy Tail", 2009, "Fantasy", library)
    library = add_season(12, 2, "Fairy Tail", 2010, "Fantasy", library)
    library = add_season(8, 1, "Black Rock Shooter", 2010, "Thriller", library)
    library.append(Movie("Avatar", 2009, "Sci-Fi"))
    library.append(Movie("Avatar 2", 2022, "Sci-Fi"))
    magic_function(library)
    top_titles(library, 3)
    