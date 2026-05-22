import sorts
import time
import array_utils

def insertion_sort_function_timer(an_array):
    begin = time.perf_counter()
    sorts.insertion_sort(an_array)
    end = time.perf_counter()
    return end - begin


def main():
    an_array1 = array_utils.range_array(0, 300, 1)
    an_array2 = array_utils.random_array(300)
    an_array3 = array_utils.range_array(300, 0, -1)
    print("sorted:", insertion_sort_function_timer(an_array1))
    print("random:", insertion_sort_function_timer(an_array2))
    print("reverse:", insertion_sort_function_timer(an_array3))
    
    
if __name__ == "__main__":
    main()
    