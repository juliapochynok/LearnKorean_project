import fileinput
import random
from classes import WordController, User

def main():
    '''
    Main function. Responsible for program's work.
    '''
    file_name = make_userfile()
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
    Asks user to enter his name and makes file named the same way.
    '''
    name = input("Please enter your name and surname without white spaces: ")
    file_name = str(name) + ".txt"
    time = input("Is it your first time using this program: ")
    if time == 'yes' or time == 'YES' or time == 'Yes':
        fl = open(file_name, "w")
        fl.write("0\n==========\n")
        fl.close()
    return file_name


def menu():
    '''
    Prints out menu
    '''
    return """\n1. Learn new word\n 2. Test yourself\n 3.Wordlist\n""" 



if __name__ == "__main__":
    main()