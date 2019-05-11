from classes import User, WordController
from unittest import TestCase
import unittest
from arrays import DynamicArray

class TestUser(TestCase):

    def setUp(self):
        self.user1 = User("julia_poch.txt")
        self.user2 = User("julia.txt")

    def test_learn_new_word(self):
        self.assertEqual(self.user1.learn_new_word(),\
           "Word: 만나다\n"+\
            "Translation: meet; join\n"+\
            "Definition: For a line", "Результати не відповідають")

    def test_test_yourself(self):
        self.assertEqual(type(self.user1.test_yourself(1)), tuple,  "Не відповідають структури даних")
        self.assertEqual(type(self.user2.test_yourself(1)), tuple,  "Не відповідають структури даних")
        
    def test_see_word_list(self):
        self.assertEqual(self.user1.see_word_list(),\
            "20\n" +\
            "사과,apple,A round-shaped sweet and sour fruit with red skin.\n" +\
            "오다,come,For something to move from another place to here.\n"+\
            "마시다,drink,To make liquid such as water\n"+\
            "먹다,eat; have; consume; take,To put food into one's mouth and take it in one's stomach.\n"+\
            "주다,give,To give an item to someone else so he/she can have or use it.\n"+\
            "가다,go; travel,To move from one place to another place.\n"+\
            "듣다,hear,To sense a sound with ears.\n"+\
            "배우다,learn,To obtain new knowledge.\n"+\
            "만들다,make; create; produce; manufacture,To create something that did not exist\n"+\
            "앉다,sit; be seated,To place one's weight on the bottocks and put his/her body on an object or on the floor with his/her upper body in an upright position.\n"+\
            "자다,sleep,To be in the state of taking a rest for a period of time with one's eyes closed and mental activities suspended.\n"+\
            "씻다,wash,To clean something by removing dirt or grime.\n"+\
            "쓰다,write,To write some letters by drawing strokes on paper with a writing instrument such as a pencil\n"+\
            "울다,cry,To shed tears out of unbearable joy\n"+\
            "웃다,smile,To smile big or make a sound when one is happy or satisfied.\n"+\
            "보다,see; look at; notice,To perceive with eyes the existence or appearance of an object.\n"+\
            "일어나다,stand up; rise; sit up,To sit after lying down or stand after sitting.\n"+\
            "걷다,walk,To lift one's feet\n"+\
            "춤추다,dance,To move one's body to a piece of music or a regular beat.\n"+
            "만나다,meet; join,For a line\n", "Результати не відповідають")



class TestWordController(TestCase):

    def setUp(self):
        self.wordcontrol1 = WordController("julia_poch.txt")
        self.wordcontrol2 = WordController("julia.txt")
        self.arr = DynamicArray()

    def test_read_from_file(self):
        self.assertEqual(type(self.wordcontrol1.read_from_file()), \
            tuple, "Не відповідають структури даних")
        self.assertEqual(type(self.wordcontrol2.read_from_file()), \
            tuple, "Не відповідають структури даних")

    def test_word_string(self):
        self.assertEqual(self.wordcontrol1.word_string(),\
            "20\n" +\
            "사과,apple,A round-shaped sweet and sour fruit with red skin.\n" +\
            "오다,come,For something to move from another place to here.\n"+\
            "마시다,drink,To make liquid such as water\n"+\
            "먹다,eat; have; consume; take,To put food into one's mouth and take it in one's stomach.\n"+\
            "주다,give,To give an item to someone else so he/she can have or use it.\n"+\
            "가다,go; travel,To move from one place to another place.\n"+\
            "듣다,hear,To sense a sound with ears.\n"+\
            "배우다,learn,To obtain new knowledge.\n"+\
            "만들다,make; create; produce; manufacture,To create something that did not exist\n"+\
            "앉다,sit; be seated,To place one's weight on the bottocks and put his/her body on an object or on the floor with his/her upper body in an upright position.\n"+\
            "자다,sleep,To be in the state of taking a rest for a period of time with one's eyes closed and mental activities suspended.\n"+\
            "씻다,wash,To clean something by removing dirt or grime.\n"+\
            "쓰다,write,To write some letters by drawing strokes on paper with a writing instrument such as a pencil\n"+\
            "울다,cry,To shed tears out of unbearable joy\n"+\
            "웃다,smile,To smile big or make a sound when one is happy or satisfied.\n"+\
            "보다,see; look at; notice,To perceive with eyes the existence or appearance of an object.\n"+\
            "일어나다,stand up; rise; sit up,To sit after lying down or stand after sitting.\n"+\
            "걷다,walk,To lift one's feet\n"+\
            "춤추다,dance,To move one's body to a piece of music or a regular beat.\n"+
            "만나다,meet; join,For a line\n", "Результати не відповідають")

    def test_write_to_file(self):
        self.assertEqual(self.wordcontrol2.write_to_file(),\
           "Word: 씻다\n"+\
            "Translation: wash\n"+\
            "Definition: To clean something by removing dirt or grime.", "Результати не відповідають")

if __name__ == "__main__":
    unittest.main()