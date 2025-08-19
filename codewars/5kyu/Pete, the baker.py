# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    xdict = {}
    for i in recipe.keys():
        x = 0
        if i in available.keys():
            x = available[i] // recipe[i]          
        xdict[i] = x
    return min(xdict.values())
            




recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))