import arrays
import array_utils
import random

def split(an_array):
    if len(an_array) % 2 == 0:
        evens = arrays.Array(len(an_array) // 2)
        odd = arrays.Array(len(an_array) // 2)
    else:
        evens = arrays.Array(len(an_array) // 2 + 1)
        odd = arrays.Array(len(an_array) // 2)
        
    is_even = True
    even_index = 0
    odd_index = 0

    for i in range(len(an_array)):
        if is_even:
            evens[even_index] = an_array[i]
            even_index += 1
        else:
            odd[odd_index] = an_array[i]
            odd_index += 1
        
        is_even = not is_even
    
    return evens, odd

def merge(sorted1, sorted2):
    result = arrays.Array(len(sorted1) + len(sorted2))
    i1 = 0
    i2 = 0
    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] <= sorted2[i2]:
            result[i1 + i2] = sorted1[i1]
            i1 += 1
        else:
            result[i1+i2] = sorted2[i2]
            i2 += 1

    if i1 < len(sorted1):
        for i in range(i1, len(sorted1)):
            result[i2 + i] = sorted1[i]
            
    elif i2 < len(sorted2):
        for i in range(i2, len(sorted2)):
            result[i1 + i] = sorted2[i]
        
    return result

def merge_sort(an_array):
    
    if len(an_array) == 0:
        return an_array
    
    elif len(an_array) == 1:
        return an_array
    
    else:
        even, odd = split(an_array)
        return merge(merge_sort(even), merge_sort(odd))
    
    
def main():
    random.seed(1)
    an_array = array_utils.random_array(10, 0, 100)
    print(an_array)
    # print(split(an_array))
    print(merge_sort(an_array))
    
    
if __name__ == "__main__":
    main()