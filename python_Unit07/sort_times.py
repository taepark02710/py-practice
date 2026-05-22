import sorts
import time
import array_utils

def sort_function_timer(an_array, sort_function):
    begin = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()
    return end - begin


def main():
    an_array1 = array_utils.range_array(800,0,-1)
    an_array2 = array_utils.range_array(800,0,-1)
    print("insertion sort (swap):", sort_function_timer(an_array1, sorts.insertion_sort))
    print("insertion sort (no swap)", sort_function_timer(an_array2, sorts.insertion_sort_wo_swap))
    # print("reverse:", insertion_sort_function_timer(an_array3))
    
    
if __name__ == "__main__":
    main()
    