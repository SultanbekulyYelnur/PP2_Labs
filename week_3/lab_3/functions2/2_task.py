from movies import movies

def sublist(sequence):
    sub_l = []
    for i in sequence:
        if i["imdb"] > 5.5:
            sub_l.append(i["name"])
    
    return sub_l

print(sublist(movies))