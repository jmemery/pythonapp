name = ['Jase', 'Eli', 'Pariece', 'Brendan', 'Amy', 'Shawn', 'Oscar']
favorite_animal = ['dog', 'cat', 'spider', 'giraffe', 'ticks','dolphins', 'llamas']

import itertools

def make_dict(arr1, arr2):
    newdict = {}
    newdict = dict(itertools.izip(name,favorite_animal))
    print (newdict)
make_dict(name, favorite_animal)
