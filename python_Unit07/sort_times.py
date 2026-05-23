import sorts
import time
import array_utils
import plotter
import merge_sort

SIZES = array_utils.range_array(200, 2300, 300)

def sort_function_timer(an_array, sort_function):
    begin = time.perf_counter()
    sort_function(an_array)
    end = time.perf_counter()       
    return end - begin

def plot_sort_time_using_random_arrays(sort_function):
    plotter.new_series()
    
    for i in range(len(SIZES)):
        rnd_array = array_utils.random_array(SIZES[i])
        delta = sort_function_timer(rnd_array, sort_function)
        plotter.add_data_point(delta)
        
    plotter.plot()
    

def main():
    # an_array1 = array_utils.range_array(2000,0,-1)
    # an_array2 = array_utils.range_array(2000,0,-1)
    # # print("insertion sort (swap):", sort_function_timer(an_array1, sorts.insertion_sort))
    # # print("insertion sort (no swap)", sort_function_timer(an_array2, sorts.insertion_sort_wo_swap))
    # # print("reverse:", insertion_sort_function_timer(an_array3))
    
    # 7.2 Assignment
    plotter.init("Insertion Sort, Insertion Sort w/o Swap, and Merge Sort", "Array Size", "Time")
    plot_sort_time_using_random_arrays(sorts.insertion_sort)
    
    plot_sort_time_using_random_arrays(sorts.insertion_sort_wo_swap)
    plot_sort_time_using_random_arrays(merge_sort.merge_sort)
    input("Enter to quit...")
    
    
if __name__ == "__main__":
    main()
    