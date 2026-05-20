import time
import arrays
import array_utils


def linear_search(an_array, target):
    for i in range(len(an_array)):
        if an_array[i] == target:
            return i
    
    return None

def linear_search_timer(an_array, target):
    begin = time.perf_counter()
    linear_search(an_array, target)
    end = time.perf_counter()
    
    return end - begin
    
def linear_timer():
    an_array = array_utils.random_array(100, 1, 10000000)
    print(linear_search_timer(an_array, 1))
    print(linear_search_timer(an_array, 5000000))
    print(linear_search_timer(an_array, 10000000))
    
    
def main():
    an_array = array_utils.random_array(10,1,100)
    # print(linear_search(an_array, 1))
    # print(linear_search(an_array, 50))
    # print(linear_search(an_array, 100))
    # print(linear_search(an_array, 101))
    linear_timer()
    
    
    
if __name__ == "__main__":
    main()
    