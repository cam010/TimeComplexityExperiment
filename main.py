# Bisect module contains both the binary search algorithm
# aswell as the .insort() method, inserting a value into a
# sorted list.
import bisect

# random.shuffle() to create unordered list
# randome.randint() to choose element to add to list
# random.choice() to choose element to find in list
from random import shuffle, choice, randint

# timeit.default_timer() will be used as a timer
from timeit import default_timer

class Comparison:
    
    def __init__(self, list_length: int):
        self.list_length = list_length
        
        # Create ordered base list
        base_list = [x for x in range(list_length)]
        bisect.insort_left(base_list, randint(0, self.list_length))
        
        # Ordered List
        self.ordered_list = base_list
        
        # Unordered list
        self.unordered_list = base_list
        shuffle(self.unordered_list)
        
        # Element to insert
        self.element_to_insert = randint(0, self.list_length)
        
        # Element to find
        # doesnt matter if ordered or unordered used as they are the same
        self.element_to_find = choice(base_list)
    
    def unordered(self):
        self.insert_unordered()
        self.find_element_unsorted()
    
    def ordered(self):
        self.insert_ordered()
        self.find_ordered()
    
    def insert_unordered(self):
        # list contains integers from 0 - self.list_length - 1
        # therefore self.list_length int can just be appended onto end
        self.unordered_list.append(self.element_to_insert)
        
    def find_element_unsorted(self):
        # Linear search algorithm - index not needed so not returned
        for x in self.unordered_list:
            if x == self.element_to_find:
                return
    
    def insert_ordered(self):
        bisect.insort_left(self.ordered_list, self.element_to_insert)
        
    def find_ordered(self):
        # Binary search algorithm - index not needed so not returned
        bisect.bisect_left(self.ordered_list, self.element_to_find)


def unordered(cls: Comparison, list_length: int, run: int):
    # Simple timer
    start_time = default_timer()
    cls.unordered()
    total_time = default_timer() - start_time
    
    # Write result to file
    with open("results.txt", "a") as f:
        f.write("LIST_LENGTH: {} || RUN: {} || UNORDERED || TIME ELAPSED: {}s\n".format(list_length, run, total_time))
    
    return total_time

def ordered(cls: Comparison, list_length: int, run: int):
    # Simple timer
    start_time = default_timer()
    cls.ordered()
    total_time = default_timer() - start_time
    
    # Write result to file
    with open("results.txt", "a") as f:
        f.write("LIST_LENGTH: {} || RUN: {} || ORDERED || TIME ELAPSED: {}s\n".format(list_length, run, total_time))
    
    return total_time

if __name__ == '__main__':
    # Resets results file
    with open("results.txt", "w") as f:
        f.write("")
        
    list_lengths = [1, 10, 100, 1000, 10_000, 100_000, 
                    1_000_000, 10_000_000, 100_000_000]
    
    for i in range(len(list_lengths)):
        mean_time_unordered = 0
        mean_time_ordered = 0
        
        # 3 Repetitions of each length, allowing for a mean to be calculated
        # to increase the accuracy and reduce anomaly impact
        for j in range(1, 4):
            run = Comparison(list_lengths[i])
            mean_time_unordered += unordered(run, list_lengths[i], j)
            mean_time_ordered += ordered(run, list_lengths[i], j)
        
        # mean calculaltion
        mean_time_unordered /= 3
        mean_time_ordered /= 3
        
        # write summary of run results to file
        with open("results.txt", "a") as f:
            f.write("LIST_LENGTH: {} || MEAN UNORDERED TIME: {} || MEAN ORDERED TIME: {}\n\n\n".format(list_lengths[i], mean_time_unordered, mean_time_ordered))
        


            
                