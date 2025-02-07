def chicken_and_rabbits(numheads = 35, numlegs = 94):
    rabbits = (numlegs - numheads * 2) / 2 
    chickens = numheads - rabbits
    print(f"chickens = {chickens}, rabbits = {rabbits}")
chicken_and_rabbits()