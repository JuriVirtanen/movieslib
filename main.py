import random

class movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.year})"
    
class episode:
    def __init__(self, title, year, genre, n_episode, season):
        if n_episode < 10:
            self.exx = f"0{n_episode}"
        else:
            self.exx = n_episode

        if season < 10:
            self.sxx = f"0{season}"
        else:
            self.sxx = season

        self.title = title
        self.year = year
        self.genre = genre
        self.n_episode = n_episode
        self.season = season
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} S{self.sxx}E{self.exx}"

def generate_views(lista):

    los = random.choice(lista)
    los.play()
    print(los.views)

if __name__=="__main__":
    all = []
    test1 = episode("Love is War", 2019, "Comedy", 1, 1)
    test2 = episode("Love is War", 2019, "Comedy", 2, 1)
    test3 = episode("Love is War", 2019, "Comedy", 3, 1)
    test4 = episode("Love is War", 2019, "Comedy", 4, 1)
    all.append(test1)
    all.append(test2)
    all.append(test3)
    all.append(test4)
    generate_views(all)
    