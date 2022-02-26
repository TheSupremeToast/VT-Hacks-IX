#
# Array-based queue class to store users queueing into office hours 
#
from queue import Empty


class ArrayQueue:

    '''
    Initializes the queue
    capacity = 50 for now
    data = the array we store these mfs in
    first = first person in queue
    n = number of people in queue
    '''
    def __init__(self):
        CAPACITY = 50
        self._data_ = [None]*CAPACITY
        self._front_ = 0
        self._n_ = 0

    '''
    returns queue length
    '''
    def __len__(self):
        return self._n_

    '''
    returns string representation of queue
    '''
    def __str__(self):
        return self._data_

    '''
    returns if queue is empty
    '''
    def is_empty(self):
        return self._n_ == 0
    
    '''
    expands capacity if queue is full
    shits everything in queue to front and then expands
    '''
    def expand_capacity(self, size):
        old_data = self._data_
        k = self._front_
        self._data_ = [None] * size

        for i in range(self._n_):
            self._data_[i] = old_data[k]
            k = (k + 1) % len(old_data)
        self._front_ = 0

    '''
    enqueues a member into the list
    '''
    def enqueue(self, user):
        if self._n_ == len(self._data_):
            self.resize(self._n_ * 2)

        index = (self._front_ + self._n_) % len(self._data_)
        self.data[index] = user
        self._n_ += 1
    
    '''
    dequeues a member from the list
    if the queue is empty itll raise an error
    THIS METHOD NEEDS A REWORK FOR WHEN A PERSON IN THE QUEUE DISCONNECTS
    '''
    def dequeue(self):
        if self.is_empty():
            raise Empty("empty queue lol")

        get_front = self._data_[self._front_]

        self._data_[self._front_]=None
        self._front = (self._front_ + 1) % (len(self._data_))
        self._n -= 1

        if(self._n < len(self._data) // 4):
            self.resize(len(self._data) // 2)
     
        return get_front
