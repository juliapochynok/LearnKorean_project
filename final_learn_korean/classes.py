from arrays import DynamicArray
import fileinput
import random

class WordController:
    '''
    Class representation of WordController
    '''
    def __init__(self, fl):
        '''
        Creates new WordController

        :type fl: str
        :param fl: user txt file
        '''
        self._file = fl

    def read_from_file(self):
        '''
        Reads information from file.
        Returns tuple of two lists: words with translation and definition,
        korean words.
        '''
        fl = open(self._file, "r")
        learned_words_full = DynamicArray()
        learned_words = DynamicArray()
        for line in fl:  
            line = line.strip()
            if '===' not in line and line != '' and line[0] not in '123456789':
                line = line.split(',')
                learned_words_full.append(line)
                learned_words.append(line[0])
        return learned_words_full, learned_words

    def write_to_file(self):
        '''
        Writes information about new word to the file.
        Returns string representation of this information.
        '''
        fl1 = open('translations.txt', 'r')
        fl2 = open(self._file, "r")
        word_num = int(fl2.readline())
        info = None
        for line in fl1:
            line = line.strip().split(",")
            if line[0] == str(word_num + 1):
                info = "Word: "+line[1]+"\nTranslation: "+ line[3]+\
                    "\nDefinition: "+line[4]
                fl2 = open(self._file, "a")
                fl2.write(line[1] + "," + line[3] + "," + line[4] + "\n")
                break
        fl2 = open(self._file, "r")

        if info != None:
            for line in fileinput.FileInput(self._file, inplace=1):
                n = str(word_num)
                m = str(word_num + 1)
                line=line.replace(n,m)
                print(line)
        return info

    def word_string(self):
        '''
        Reads all information from file and 
        returns string representation of it
        '''
        fl = open(self._file, 'r')
        words = ''
        for line in fl:
            line = line.strip()
            if line not in '123456789' and '===' not in line and line != '':
                words += line +'\n'
        return words


class User:
    '''
    Class representation of WordController
    '''   
    def __init__(self, fl = None):
        '''
        Creates new User

        :type fl: str
        :param fl: user txt file
        '''
        self._file = fl
        self.word_controller = WordController(fl)

    def learn_new_word(self):
        '''
        Writes information about one new word to user file.
        Returns string representation of this information.
        '''
        info = self.word_controller.write_to_file()
        print(info)
        return info

    def test_yourself(self, number):
        '''
        Returns tuple of korean word, translation of it and list
        of false translations

        :type number: int
        :param number: number of answer generation
        '''
        learned_words_full, learned_words = self.word_controller.read_from_file()
        if len(learned_words) < 2:
            return False
        else:
            check_word = random.choice(learned_words)
            index = learned_words.index(check_word)
            true_trans = learned_words_full[index][1]
            false_answ = [true_trans]
            for time in range(number):
                word = learned_words_full[index]
                for var in range(3):
                    if len(learned_words_full) > 1:
                        learned_words_full.remove(word)
                    word = random.choice(learned_words_full)
                    trans = word[1]
                    false_answ.append(trans)
            false_answ.sort()
            return (true_trans, false_answ, check_word)

    def see_word_list(self):
        '''
        Reads all information from file and 
        returns string representation of it
        '''
        words = self.word_controller.word_string()
        return words

    def set_file(self, fl):
        '''
        Sets users file

        :type fl: str
        :param fl: user txt file
        '''
        self._file = fl

