import itertools

string = input ('Digite qual a string que deseja permutar: ')

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))   