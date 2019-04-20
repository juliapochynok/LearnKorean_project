from arrays import DynamicArray
import fileinput
import random

class WordController:
    '''
    '''
    def __init__(self, fl):
        self._file = fl

    def read_from_file(self):
        '''
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
        '''
        fl1 = open('translations.txt', 'r')
        fl2 = open(self._file, "r")
        word_num = int(fl2.readline())
        for line in fl1:
            line = line.strip().split(",")
            if line[0] == str(word_num + 1):
                info = "Word: "+line[1]+"\nTranslation: "+ line[3]+\
                    "\nDefinition: "+line[4]
                fl2 = open(self._file, "a")
                fl2.write(line[1] + "," + line[3] + "," + line[4] + "\n")
                break
        fl2 = open(self._file, "r")

        for line in fileinput.FileInput(self._file, inplace=1):
            n = str(word_num)
            m = str(word_num + 1)
            line=line.replace(n,m)
            print(line)
        return info

    def word_string(self):
        '''
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
    '''
     
    def __init__(self, fl):
        self._file = fl
        self.word_controller = WordController(fl)

    def choose_section(self, inpt):
        '''
        '''
        if inpt == "1" or inpt == "Learn new word":
            return self.learn_new_word()
        if inpt == '2' or inpt == "Test yourself":
            return self.test_yourself(2)
        if inpt == '3' or inpt == "Wordlist":
            return print(self.see_word_list())
        else:
            return "Invalid input"

    def learn_new_word(self):
        '''
        '''
        info = self.word_controller.write_to_file()
        print(info)
        return info

    def test_yourself(self, number):
        '''
        '''
        learned_words_full, learned_words = self.word_controller.read_from_file()
        check_word = random.choice(learned_words)
        index = learned_words.index(check_word)
        true_trans = learned_words_full[index][1]
        for time in range(number):
            word1 = random.choice(learned_words_full)
            trans1 = word1[1]
            word2 = random.choice(learned_words_full)
            trans2 = word2[1]
            word3 = random.choice(learned_words_full)
            trans3 = word3[1]
            print("Word: {0}\n Choose: ".format(check_word))
            print(" {0}\n {1}\n {2}\n {3}\n".format(true_trans, trans1, trans2, trans3))
            answer = input("Enter your answer: ")
            if check_answer(answer, true_trans):
                print("Correct\n")
            else:
                print("Wrong\n")

    def see_word_list(self):
        '''
        '''
        words = self.word_controller.word_string()
        return words


def check_answer(answer, true_trans):
    '''
    '''
    if answer == true_trans:
        return True
    else:
        return False
