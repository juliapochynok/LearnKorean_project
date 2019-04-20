import ctypes
import fileinput
import random

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._size = 0                                # count actual elements
        self._capacity = 1                         # default array capacity
        self._Array = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._size

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._size:
            raise IndexError( 'invalid index' )
        return self._Array[k]                          # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._size == self._capacity:              # not enough room
            self._resize(2 * self._capacity)       # so double capacity
        self._Array[self._size] = obj
        self._size += 1

    def _resize(self, cap):                          # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(cap)                    # new (bigger) array
        for k in range(self._size):                   # for each existing value
            B[k] = self._Array[k]
        self._Array = B                                # use the bigger array
        self._capacity = cap

    def _make_array(self, capacity1): # nonpublic utitity
        """Return new array with capacity capacity1."""
        vvv = type((capacity1 * ctypes.py_object)( ) )
        return (capacity1 * ctypes.py_object)( )           # see ctypes documentation

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._Array[k] == value:               # found a match!
                for j in range(k, self._size - 1):   # shift others to fill gap
                    self._Array[j] = self._Array[j + 1]
                self._Array[self._n - 1] = None       # help garbage collection
                self._size -= 1                      # we have one less item

                return  # exit immediately
        raise ValueError( "value not found" )     # only reached if no match
    
    def __str__(self):
        '''
        '''
        res = ''
        for i in range(self.__len__()):
            m = str(self._Array[i])
            res += m
        return res

    def index(self, value):
        """
        """
        for k in range(self._size):
            if self._Array[k] == value:           
                return k
        return None


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
            return self.test_yourself( 2)
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

if __name__ == "__main__":
    a = DynamicArray()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    print(a.index(1))