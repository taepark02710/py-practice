from xmlrpc.client import FastParser
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
    # if a is superset of b
    cnt = 0 
    
    for element_b in b_set:
        if element_b in a_set:
            cnt += 1
            
    if cnt == len(b_set):
        return True
    else:
        return False
    
def subset(a_set, b_set):
    # if a is subset of b
    cnt = 0 
    
    for element_a in a_set:
        if element_a in b_set:
            cnt += 1
            
    if cnt == len(a_set):
        return True
    else:
        return False  
    
def intersection(a_set, b_set):
    
    inter_set = set()
    
    for element_a in a_set:
        if element_a in b_set:
            inter_set.add(element_a)
            
    return inter_set

def union(a_set, b_set):
    
    union_set = b_set
    
    for element_a in a_set:
        if element_a not in union_set:
            union_set.add(element_a)
            
    return union_set

def minus(a_set, b_set):
    
    minus_set = set()
    
    for element_a in a_set:
        if element_a in b_set:
            minus_set.add(element_a)
    
    for minus_ele in minus_set:
        if minus_ele in a_set:
            a_set.remove(minus_ele)
            
def count_words(filename):
    
    maximum = 0
    most_word = 0
    
    freq_word = {}
    with open(filename) as my_file:
        
        for lines in my_file:
            lines = lines.strip()
            words = lines.split(" ")
            for word in words:
                word = word.lower()
                if word not in freq_word:
                    freq_word[word] = 1
                else:
                    freq_word[word] += 1
                    if freq_word[word] > maximum:
                        most_word = word
                        maximum = freq_word[word]
                        
    return freq_word, most_word
        
def find_maximum(dictionary):
    
    maximum = 0
    max_key = ""
    
    for keys in dictionary.keys():
        if maximum < dictionary[keys]:
            max_key = keys
            maximum = dictionary[keys]
            
    return max_key

def hashes():
    
    print(hash("Hello World"))
    print(hash("Hello world"))
    
    

def main():
    
    # print(fill_array(5000))
    # sets()
    # print(fill_set(5000))
    
    # print(coupon_collectors(500000))
    # mixup()
    # unique = unique_words("data/alice.txt")
    # print(unique)
    
    # a_set = {4, 5, 6, 11, 57, 110}
    # b_set = {4, 5, 6, 11, 12, 14, 28, 29, 30, 40}
    
    # # print(superset(a_set, b_set))
    # # print(subset(a_set, b_set))
    
    # # print(intersection(a_set, b_set))
    # # print(union(a_set, b_set))
    # minus(a_set, b_set)
    # print(a_set)
    
    # print(count_words("data/alice.txt"))
    # a_dict = {"5": 5, "10": 10, "1000": 1000, "124" : 124, "500": 500}
    # print(find_maximum(a_dict))
    
    hashes()
    
    
if __name__ == "__main__":
    main()
    
    
    
