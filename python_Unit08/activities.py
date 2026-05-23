import random
import arrays
import array_utils

def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for i in a_tuple:
        print(i)
        
def lists():
    x = [True, False, 1, 45, "abcd"]
    for i in x:
        print(i)
        
    x[0] = "45"
    print(x)   
    
def make_list(a_sequence):
    a_list = list()
    for x in a_sequence:
        a_list.append(x)
        print(a_list)
        
    return a_list


        
def scale(a_list, scalar):
    for i in range(len(a_list)):
        a_list[i] = a_list[i] * scalar
    return a_list

def mutater(a_list, a_int):
    print(a_list, a_int)
    a_int = a_int * 5
    a_list[0] = a_list[0] * 5
    print(a_list, a_int)
    
def cat(a_list, b_list):

    return a_list + b_list
    
def extender(a_list, b_list):
    a_list += b_list
    return a_list

def inserter(a_list, value):
    mid = len(a_list) // 2
    a_list.insert(mid, value)
    return a_list

def popper(a_list):
    if len(a_list) <= 0:
        return None
    else:
        print(a_list)
        a_list.pop()
        return popper(a_list)

def array_insert(an_array, index, value):
    new_array = arrays.Array(len(an_array) + 1)
    for i in range(0, index):
        new_array[i] = an_array[i]
        
    new_array[index] = value
        
    for i in range(index, len(an_array)):
        new_array[i+1] = an_array[i]
    
    
    return new_array

def array_pop(an_array, index):
    
    new_array = arrays.Array(len(an_array) - 1)
    value = an_array[index]
    
    for i in range(0, index):
        new_array[i] = an_array[i] 
    for i in range(index+1, len(an_array)):
        new_array[i-1] = an_array[i]
        
    return new_array, value
    
    
        
def main():
    # x = ("a", "b", 35, 4)
    # # tuples(x)
    # # lists()
    # x = [3, 6, 423, 359, 2.453, 234.56]
    # print(scale(x, 99.81))
    
    # a_int = 5
    # a_list = [a_int]
    # mutater(a_list, a_int)
    # mutater(a_list, a_int)
    # mutater(a_list, a_int)
    a_list = ["orange", "purple", "green"]
    b_list = ["369", 369]
    # c_list = cat(a_list, b_list)
    c_list = extender(a_list, b_list)
    # print(c_list)
    # x = []
    # inserter(x, 0)
    # print(x)
    # inserter(x, 1)
    # print(x)
    # inserter(x, 2)
    # print(x)
    # inserter(x, 3)
    # print(x)
    # popper(c_list)
    # print(c_list)
    random.seed(1)
    an_array = array_utils.random_array(10)
    print(an_array)
    b_array = array_insert(an_array, 5, 9999)
    print(array_pop(b_array, 5))
    
    
    
if __name__ == "__main__":
    main()
