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
    
    
def binary_search(an_array, target, start=None, end=None):
    if start == None and end == None:
        start = 0
        end = len(an_array) - 1
        
    if start > end:
        return None
    
    midpoint = (start + end) // 2
    if an_array[midpoint] == target:
        return midpoint
    
    elif an_array[midpoint] < target:
        return binary_search(an_array, target, midpoint + 1, end)
    
    elif an_array[midpoint] > target:
        return binary_search(an_array, target, start, midpoint - 1)
    
def binary_search_timer(an_array, target):
    begin = time.perf_counter()
    binary_search(an_array, target)
    end = time.perf_counter()

    return end - begin


    
def main():
    an_array = array_utils.range_array(0, 85, 5)
    # print(linear_search(an_array, 1))
    # print(linear_search(an_array, 50))
    # print(linear_search(an_array, 100))
    # print(linear_search(an_array, 101))
    # linear_timer()
    print(an_array)
    print(binary_search(an_array, 30))
    
    
if __name__ == "__main__":
    main()
    