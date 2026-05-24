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

def reverse_sequence(sqnce):
    a_list = []
    for i in range(len(sqnce) -1, -1, -1):
        a_list.append(sqnce[i])
        
    return a_list

def slicing():
    a_list = []
    string = "The best way to predict the future is to create it."
    for i in string:
        if i != " ":
          a_list.append(i)
    
    the = a_list[0:3] 
    print(the)
    
    
def dices(a_list):
    if len(a_list) <= 0:
        return None
    else:
        print(a_list[0:1])
        return dices(a_list[1:len(a_list)])

def random_list(size):
    a_list = []
    for _ in range(size):
        element = random.randint(0, 100)
        a_list.append(element)
        
    return a_list

def sorted_test(a_list, backwards=False):
    
    print(a_list)
    sorted_list = sorted(a_list, reverse=backwards)
    return sorted_list

def sort_test(a_list, backwards=False):
    print(a_list)
    a_list.sort(reverse=backwards)
    print(a_list)
    
def sort_cards(hand):
    print(hand)
    hand.sort(key=suit_key)
    print(hand)
    
def suit_key(card):
    if card[1] == "C":
        return 1 + card[0]
    elif card[1] == "D":
        return 100 + card[0]
    elif card[1] == "H":
        return 1000 + card[0]
    else:
        return 10000 + card[0]
      
        
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
    # random.seed(1)
    # an_array = array_utils.random_array(10)
    # print(an_array)
    # b_array = array_insert(an_array, 5, 9999)
    # print(array_pop(b_array, 5))
    # x = ["this", "is", "a", "test"]
    # slicing()
    # dices(x)
    
    # x1 = random_list(18)
    # x2 = random_list(20)
    # print(sorted_test(x1, True))
    # # print(sorted_test(x2))
    # print(sort_test(x1))
    
    hand = [(10, "D"), (10, "C"), (7, "H"), (2, "H"), (6, "S"), (10, "S")]
    sort_cards(hand)
    
    
    
    
if __name__ == "__main__":
    main()
