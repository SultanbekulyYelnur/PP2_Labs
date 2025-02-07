from movies import movies

def category_list(category):
    res = []
    for i in movies:
        if(i["category"] == category):
            res.append(i["name"])
    return res

print(category_list("Romance"))