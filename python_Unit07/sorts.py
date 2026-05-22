import random
import array_utils 

def swap(an_array, a, b):    
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp
    
def shift(an_array, index):
    if index <= 0:
        return None

    if an_array[index-1] > an_array[index]:
        swap(an_array, index, index-1)
        return shift(an_array, index-1)

    else:
        return None
    
    
def insertion_sort(an_array):
    for i in range(len(an_array)):
        shift(an_array, i)
        
    return an_array

def shift_wo_swap(an_array, index):
    target = an_array[index]
    target_index = index
    
    while target_index > 0 and target < an_array[target_index-1]:
        an_array[target_index] = an_array[target_index-1]
        target_index -= 1
        
    an_array[target_index] = target
    

def insertion_sort_wo_swap(an_array):
    for i in range(len(an_array)):
        shift_wo_swap(an_array, i)
        
    return an_array
        

def main():
    random.seed(19)
    an_array = array_utils.random_array(10)
    print(an_array)
    print("Insertion sort:", insertion_sort(an_array))
    print("Insertion sort wo swap", insertion_sort(an_array))
    
    
if __name__ == "__main__":
    main()
    