from words import d
from colorama import Fore
import pandas as pd
def add():
    word = input('Please enter the word :')
    if word not in d:
        meaning = input('Please enter the meaning of the word :')
        f = open('words.py','a')
        f.write('\n')
        f.write(f'd[\'{word}\'] = \'{meaning}\'')
        f.close()
        return Fore.GREEN + 'Successfuly added'

    else:
        return Fore.RED + 'This word already exist in  dictionary.'

def search():
    word = input('Enter the word :')
    if word in d:
        return Fore.BLUE + d[word]
    else:
        return Fore.RED + 'Word not found.'

def print_dict():
    return pd.DataFrame({Fore.GREEN+'WORD':sorted(d),Fore.GREEN+'MEANING'+Fore.WHITE:[d[i] for i in sorted(d)]},index=[i for i in range(1,len(d)+1)])

def inp():
    a = input(r'Please enter what you want to do, add a word or search a word or print dictioonary (a/s/pd) :')
    if a.lower() == 'a':
        return add()
    elif a.lower() == 's':
        return search()
    elif a.lower() == 'pd':
        return print_dict()
    else:
        print(Fore.RED + 'Please enter correctly!')
        return inp()
    
print(inp())