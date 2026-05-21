import plotter
import array_utils
import searches

def linear_plot(size, runs):
    plotter.init("Linear Search", "Length", "Time")
    step = size // runs
    an_array = array_utils.range_array(0, size, step)
    for i in range(0, size+1, step):
        time = searches.linear_search_timer(an_array, i)
        print(i)
        plotter.add_data_point(time)
        
    plotter.plot()
    

def main():
    linear_plot(100000, 20)
    input("Enter to quit...")
    
if __name__ == "__main__":
    main()
    
        
    
    