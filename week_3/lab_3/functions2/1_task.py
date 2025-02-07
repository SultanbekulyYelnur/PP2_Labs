from movies import movies
def rating(movie):
    if movie['imdb'] > 5.5:
        return True
    else:
        return False
print(rating(movies[7]))

