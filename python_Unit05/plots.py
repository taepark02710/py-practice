import python_Unit05.plotter as plotter

def quit():
    asw = input("Are you sure (y/n): ")
    if asw == "Y" or asw == "y":
        return True
    
    else:
        False

def plot_grades(filename, first_name, last_name):
    is_found = False
    plotter.init(first_name + " " + last_name, "Grade Item", "Score")
    
    with open(filename) as my_file:
        next(my_file)
        for records in my_file:
            fields = records.split(",")
            if fields[0] == last_name and fields[1] == first_name:
                is_found = True
                for index in range(2, 18):
                    try:
                        plotter.add_data_point((float(fields[index])))
                    except ValueError:
                        plotter.add_data_point(0.0)
                        
    plotter.plot()
    return is_found

def student_grades(spt):
    try:
        cmd = spt[0]
        filename = spt[1]
        first = spt[2]
        last = spt[3]
        if plot_grades(filename, first, last):
            print("Plot finished (window may be hidden).")
        else:
            print("Plot failed (no such student).")
            
    except IndexError:
        print("Usage: stu <filename> <first name> <last name>")
    
    except FileNotFoundError:
        print("No such file:", filename)
    

def help():
    print(" stu <filename> <first name> <last name> - plot student grades\n quit - quits\n help - displays this messeage")
    
    
                                
        
def main():
    
    while True:
        try:
            cmd = input(">> ")
            cmd_spt = cmd.split()
            if cmd_spt[0] == "quit":
                if quit():
                    
                    print("Goodbye!")
                    break
            elif cmd_spt[0] == "stu":
                student_grades(cmd_spt)
            
            elif cmd_spt[0] == "help":
                help()
        except IndexError:
            print("Enter a command or 'quit' to quit.")
 
if __name__ == "__main__":
    main()

        
        