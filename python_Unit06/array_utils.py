import random
import arrays

def random_array(size, min_value=0, max_value=None):
    if max_value == None:
        max_value = size
        
    an_array = arrays.Array(size)
        
    for i in range(size):
        an_array[i] = random.randint(min_value, max_value)
        
    return an_array

def range_array(start, stop, step=1):
    rng = range(start, stop, step)
    length = len(rng)
    an_array = arrays.Array(length)
    for i in range(length):
        an_array[i] = rng[i]
    
    return an_array



def main():
    random.seed(1)
    # an_array = random_array(10)
    # print(an_array)
    
    an_array = range_array(0, 10,2)
    print(an_array)
    
    an_array2 = range_array(0, 30,4)
    print(an_array2)
    
    an_array3 = range_array(0, 10, 5)
    print(an_array3)
    
if __name__ == "__main__":
    main()