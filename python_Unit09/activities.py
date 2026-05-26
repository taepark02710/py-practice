import arrays
import time
import random


def unique_array(an_array, value):
    
    for i in range(0, len(an_array)):
        if an_array[i] == None:
            an_array[i] = value
        
def fill_array(length):
    
    an_array = arrays.Array(length)
    begin = time.perf_counter()
    for i in range(length):
        unique_array(an_array, i)
    end = time.perf_counter()
    
    return end - begin

def unique_set(a_set, value):
    
    if value not in a_set:
        a_set.add(value)

def fill_set(length):
    
    set1 = set()
    
    begin = time.perf_counter()
    for i in range(length):
        unique_set(set1, i)
    end = time.perf_counter()
    
    return end - begin
    
def sets():
    
    set1 = {"11", 56, True, "iamset"}
    print(set1)
    set1.add("helloworld")
    set1.add(2458239.358)
    print(set1)
    set2 = set("helloworldhelloworld")
    print(set2)
    
def coupon_collectors(n):
    
    coupons = set()
    cnt = 0
    
    while len(coupons) != n:
        
        coupon = random.randint(1, n)
        
        if coupon not in coupons:
            coupons.add(coupon)
        
        cnt += 1
    
    return cnt

def mixup():
    
    set1 = set("characters")
    
    for s in set1:
        print(s, end=" ")
    
def unique_words(filename):
    
    unique = set()
    
    with open(filename) as my_file:
        for lines in my_file:
            lines_token = lines.split(" ")
            for word in lines_token:
                word = word.lower()
                if word not in unique:
                    unique.add(word)
    
    return unique
    
def superset(a_set, b_set):
    

def main():
    
    # print(fill_array(5000))
    # sets()
    # print(fill_set(5000))
    
    # print(coupon_collectors(500000))
    # mixup()
    unique = unique_words("data/alice.txt")
    print(unique)
    
    
if __name__ == "__main__":
    main()
    
    
    
