import random
import arrays
import array_utils

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

def print_odds_rect(an_array, index=0):
    if index > len(an_array):
        return None
    if index % 2 != 0:
        print(an_array[index])
        return print_odds_rect(an_array, index+1)
    
    else:
        return print_odds_rect(an_array, index+1)
    
def countdown(n):
    if n <= 0:
        return 0
    else: 
        print(n)
        return n + countdown(n-1)
    

def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n)
        return n * factorial(n-1)
    
    
def main():
    # making_arrays()
    an_array = arrays.Array(10)
    # while_fill(an_array)
    # for_fill(an_array)
    random.seed(1)
    # for _ in range(10):
    #     print(roll_the_die(10))
    an_array = array_utils.random_array(10,0,100)
    
    # print(an_array)
    # print_odds_rect(an_array)
    # print(countdown(5))
    print(factorial(100))
    
if __name__ == "__main__":
    main()