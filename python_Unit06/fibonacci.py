import plotter
import time

def fibonacci_naive(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
    
def naive_timer(n):
    plotter.init("Naive Fibonacci", "N", "Time")
    for i in range(n):
        begin = time.perf_counter()
        fibonacci_naive(i)
        end = time.perf_counter()
        plotter.add_data_point(end - begin)
        
    plotter.plot()

def fibonacci_fast(n, fn_minus_1=1, fn_minus_2=0 ):
    if n <= 1:
        return fn_minus_2
    
    else:
        return fibonacci_fast(n-1, fn_minus_1+fn_minus_2, fn_minus_1)

def fast_timer(n):
    plotter.init("Fast Fibonacci", "N", "Time")
    for i in range(n):
        begin = time.perf_counter()
        fibonacci_fast(i)
        end = time.perf_counter()
        plotter.add_data_point(end - begin)
        
    plotter.plot()
    
    
def main():
    print(fibonacci_naive(10))
    # naive_timer(30)
    # input("Enter to continue...")
    print(fibonacci_fast(10))
    fast_timer(75)
    input("Enter to quit...")
    
if __name__ == "__main__":
    main()