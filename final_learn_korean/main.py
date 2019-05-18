import fileinput
import random
from classes import WordController, User

def make_userfile(name, time):
    '''
    Creates user file with his/her name.

    :type name: str
    :param name: user name that will be transformed to file name.
    :type time: str
    :param time: str that is "yes" is it's user's first time 
    in the program.
    '''
    file_name = str(name) + ".txt"
    if time == 'yes' or time == 'YES' or time == 'Yes':
        fl = open(file_name, "w")
        fl.write("0\n==========\n")
        fl.close()
    return file_name