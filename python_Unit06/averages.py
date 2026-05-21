import array_utils
import searches
import plotter

def average_binary_search(size, runs):
    sum_time = 0
    an_array = array_utils.range_array(0, size)
    step = max(1, size // runs)
    positions = list(range(0, size + 1, step))
    
    for i in positions:
        sum_time += searches.binary_search_timer(an_array, i)
    
    return sum_time / len(positions)  # average time per search


def plot_average_binary_searches(min_size, max_size, runs):
    plotter.init("Binary Search", "Size", "Time")
    step = max(1, (max_size - min_size) // runs)
    sizes = range(min_size, max_size + 1, step)
    
    for size in sizes:
        avg_time = average_binary_search(size, runs)
        plotter.add_data_point(avg_time)
        
    plotter.plot()
def main():
    plot_average_binary_searches(100, 10000, 25)
    input("Enter to quit...")
    
    
if __name__ == "__main__":
    main()
    