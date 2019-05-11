# This data structure is from https://github.com/anrom7/Array\"
# but i also have modified it myself
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

    def _resize(self, c):                          # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                    # new (bigger) array
        for k in range(self._size):                   # for each existing value
            B[k] = self._Array[k]
        self._Array = B                                # use the bigger array
        self._capacity = c

    def _make_array(self, capacity1): # nonpublic utitity
        """Return new array with capacity capacity1."""
        vvv = type((capacity1 * ctypes.py_object)( ) )
        return (capacity1 * ctypes.py_object)( )           # see ctypes documentation

    # def insert(self, k, value):
    #     """Insert value at index k, shifting subsequent values rightward."""
    #     # (for simplicity, we assume 0 <= k <= n in this verion)
    #     if self. n == self._capacity:             # not enough room
    #         self._resize(2 * self._capacity)      # so double capacity
    #     for j in range(self._n, k, -1):           # shift rightmost first
    #         self._A[j] = self._A[j - 1]
    #     self._A[k] = value                        # store newest element
    #     self._n += 1

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



if __name__ == "__main__":
    a = DynamicArray()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    print(a.index(1))