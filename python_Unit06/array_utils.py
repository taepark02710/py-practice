import random
import arrays

def random_array(size, min_value=0, max_value=None):
    if max_value == None:
        max_value = size
        
    an_array = arrays.Array(size)
        
    for i in range(size):
        an_array[i] = random.randint(min_value, max_value)
        
    return an_array


def main():
    random.seed(1)
    an_array = random_array(10)
    print(an_array)
    
if __name__ == "__main__":
    main()