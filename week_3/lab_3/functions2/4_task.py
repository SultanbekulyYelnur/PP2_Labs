from movies import movies

def aver_score():
    res = 0
    for i in movies:
        res += i["imdb"]
    return res / len(movies)
print(aver_score())