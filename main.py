import random


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


def top_titles(lista, topx, content_type="all"):
    if content_type == "all":
        top = sorted(lista, key=lambda video: video.views, reverse=True)
        repeat = 1
        for rank_video in top:
            print(rank_video)
            if repeat == topx:
                break
            repeat += 1
    elif content_type == "Movies":
        top = sorted(get_movies(lista), key=lambda video: video.views, reverse=True)
        repeat = 1
        for rank_video in top:
            print(rank_video)
            if repeat == topx:
                break
            repeat += 1
    elif content_type == "Series":
        top = sorted(get_series(lista), key=lambda video: video.views, reverse=True)
        repeat = 1
        for rank_video in top:
            print(rank_video)
            if repeat == topx:
                break
            repeat += 1



if __name__=="__main__":
    library = []
    test1 = Series(1, 1, "Love is War", 2019, "Comedy")
    test2 = Series(2, 1, "Love is War", 2019, "Comedy")
    test3 = Series(3, 1, "Love is War", 2019, "Comedy")
    test4 = Series(4, 1, "Love is War", 2019, "Comedy")
    test5 = Series(5, 1, "Love is War", 2019, "Comedy")
    library.append(test1)
    library.append(test2)
    library.append(test3)
    library.append(test4)
    library.append(test5)
    test2.play()
    test2.play()
    test5.play()
    test1.play()
    top_titles(library, 2)