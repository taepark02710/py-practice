import random
import arrays

def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1, 0))
    print(arrays.Array(10, ""))
    print(arrays.Array(20, False))

def while_fill(an_array):
    i = 0
    while i < len(an_array):
        an_array[i] = i
        i += 1
     
    print(an_array)
    
def for_fill(an_array):
    for i in range(len(an_array)):
        an_array[i] = i
        
    print(an_array)
    
def roll_the_die(side):
    
    return random.randint(1, side)
    
def main():
    # making_arrays()
    an_array = arrays.Array(10)
    # while_fill(an_array)
    # for_fill(an_array)
    random.seed(1)
    for _ in range(10):
        print(roll_the_die(10))
    
if __name__ == "__main__":
    main()