import fileinput
import random
from classes import WordController, User

def main():
    '''
    '''
    # file_name = make_userfile()
    file_name = 'julia_poch.txt'
    fl = open(file_name, "a")
    user = User(file_name)
    iterat = True
    while iterat == True:
        print(menu())
        section = input("Choose: ")
        if len(section) < 1:
            iterat = False
        user.choose_section(section)


def make_userfile():
    '''
    '''
    name = input("Please enter your name and surname without white spaces: ")
    file_name = str(name) + ".txt"
    time = int(input("Enter which time you're using our program: "))
    if time == 1:
        fl = open(file_name, "w")
        fl.write("0\n==========\n")
        fl.close()
    return file_name


def menu():
    '''
    '''
    return """1. Learn new word\n 2. Test yourself\n 3.Wordlist """ 



if __name__ == "__main__":
    main()