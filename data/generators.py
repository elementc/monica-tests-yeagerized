import os
import random

def get_file_contents(fname) -> list:
    f = open(os.path.join(os.path.dirname(__file__), fname))
    ret = f.readlines()
    return [line.strip().title() for line in ret]

firstnames = get_file_contents("firstnames.txt")

def get_firstname():
    return random.choice(firstnames)

lastnames = get_file_contents("lastnames.txt")

def get_lastname():
    return random.choice(lastnames)

if __name__ == "__main__":
    print(get_firstname(), get_lastname())
