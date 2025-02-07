from movies import movies

def cat_av_score(category):
    res = 0
    n = 0
    for i in movies:
        if i["category"] == category:
            res += i["imdb"]
            n +=1
    return res / n
print(cat_av_score("Thriller"))