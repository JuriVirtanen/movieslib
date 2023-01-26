class movie:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views
    
class serie:
    def __init__(self, title, year, genre, episodes):
        self.title = title
        self.year = year
        self.genre = genre
        self.episode = episodes

test = serie("Coś", "2000", "Fantasy", [1, 2, 3])
print(test.episode)