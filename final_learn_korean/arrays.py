# This data structure is from https://github.com/anrom7/Array\"
# but i also have modified it myself
import ctypes
import fileinput
import random

class DynamicArray:
    """
    A dynamic array class akin to a simplified Python list.
    """

    def __init__(self):
        """
        Create an empty array.
        """
        self._size = 0                                # count actual elements
        self._capacity = 1                         # default array capacity
        self._Array = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """
        Return number of elements stored in the array.
        """
        return self._size

    def __getitem__(self, k):
        """
        Return element at index k.

        :param k: the index of element.
        :return: the value of the element.
        """
        if not 0 <= k < self._size:
            raise IndexError( 'invalid index' )
        return self._Array[k]                          # retrieve from array

    def append(self, obj):
        """
        Add object to end of the array.

        :param obj: the value of element.
        """
        if self._size == self._capacity:              # not enough room
            self._resize(2 * self._capacity)       # so double capacity
        self._Array[self._size] = obj
        self._size += 1

    def _resize(self, c):                          # nonpublic utitity
        """
        Resize internal array to capacity c.

        :param c: new capacity of array.
        """
        B = self._make_array(c)                    # new (bigger) array
        for k in range(self._size):                   # for each existing value
            B[k] = self._Array[k]
        self._Array = B                                # use the bigger array
        self._capacity = c

    def _make_array(self, capacity1): # nonpublic utitity
        """
        Return new array with capacity capacity1.

        :param capacity1: size of array.
        :return: array  with specified size.
        """
        vvv = type((capacity1 * ctypes.py_object)( ) )
        return (capacity1 * ctypes.py_object)( )           # see ctypes documentation


    def remove(self, value):
        """
        Remove first occurrence of value( or  raise ValueError).

        :param value: the value that needs to be removed.
        """
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._size):
            if self._Array[k] == value:               # found a match!
                for j in range(k, self._size - 1):   # shift others to fill gap
                    self._Array[j] = self._Array[j + 1]
                self._Array[self._size - 1] = None       # help garbage collection
                self._size -= 1                      # we have one less item

                return  # exit immediately
        raise ValueError( "value not found" )     # only reached if no match
    
    def __str__(self):
        '''
        Rerurn string representation of DynamicArray.
        '''
        res = ''
        for i in range(self.__len__()):
            m = str(self._Array[i])
            res += m
        return res

    def index(self, value):
        """
        Returns index of the value if value is in DynamicArray.

        param value: the value which index needs to be found.
        """
        for k in range(self._size):
            if self._Array[k] == value:           
                return k
        return None


