def evens(n):
    sum_even = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum_even += i
            
    return sum_even

def runner(function, number):
    print(function.__name__)
    print(function(number))
    
def main():
    runner(evens, 10)
    runner(evens, 100)
    
    
    
if __name__ == "__main__":
    main()
    
    
    
