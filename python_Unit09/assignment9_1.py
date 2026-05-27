def in_place_reverse(a_list):
    
    for i in range(len(a_list)):
        old = a_list.pop()
        a_list.insert(i, old)     
        
        
    return a_list

def my_slice(a_list, start, stop, step=1):
    
    if stop > len(a_list):
        stop = len(a_list)
        
    return [a_list[i] for i in range(start, stop, step)]
            
def make_multiplication_table():
    
    return [[j * i for i in range(1, 11)] for j in range(1, 11)] 


def main():
    # a_list = [1, 2, 3, 4, 5, 6, 7]
    # print(in_place_reverse(a_list))
    
    # a_list = [0, 10, 20, 30, 40, 50]
    # print(my_slice(a_list, 2, 4))
    # print(my_slice(a_list, 1, 8, 2))
    # print(my_slice(a_list, 5, 1, -1))
    
    for i in make_multiplication_table():
        print(i)
    
    
    
if __name__ == "__main__":
    main()
    