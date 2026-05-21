import python_Unit05.plotter as plotter
import csv
import re

def plot_grades(filename, first_name, last_name):
    plotter.init(first_name + " " + last_name, "Grade Item", "Score")
    
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            if re.findall(first_name, record[0]):
                for index in range(3, len(record)):
                    plotter.add_data_point(float(record[index]))
                    
    plotter.plot()
    

def get_average(filename, col):
    sum = 0
    cnt = 0
    
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            try:
                grade = float(record[col])
                sum += grade
                cnt += 1
            except: 
                sum += 0
    
    return sum / cnt

def plot_class_average(filename):
    index = 3
    plotter.init("Class Average (" + filename + ")",  "Grade Item", "Average")
    
    try: 
        while True:
            avg = get_average(filename, index)
            plotter.add_data_point(avg)
            index += 1
    except:
        plotter.plot()
            
                    
                
def main():
    # plot_grades("data/full_grades_010.csv", "Sion", "Lobasso")
    
    plot_class_average("data/full_grades_999.csv")
    input("Enter to quit...")
    
if __name__ == "__main__":
    main()