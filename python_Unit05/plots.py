import plotter

def quit(): 
    prompt = input("Are you sure? y or n: ")
    if prompt == 'y': 
        return True 
    elif prompt == 'n': 
        return False
    


def plot_grades(filename,first,last):
    plotter.init(first+' '+last,'GradeItem',"Score")
    plotter.init("grades", "students", "grade")
    file = open(filename)
    next(file)
    i = 2
    try: 
        for line in file: 
            tokens = line.split(',')
            name = str(tokens[0])
            if name == last: 
                for grades in range(2,17):
                    datas = float(tokens[grades])
                    plotter.add_data_point(datas)
        plotter.plot()
        print("Please enter to continue...")
        return True
    except ValueError: 
        plotter.plot_data_points(0.0)
        plotter.plot()
        return False


def student_grades(string):
    result = ''
    split = string.split(' ')
    try: 
        if plot_grades(split[1],split[2],split[3]): 
            result = True
            return True
        else: 
            return False
    except FileNotFoundError:
        print("No such file: ",split[1])
    except IndexError:
            print('Usage: stu <file name> <first name> <last name>')
    except ValueError:
        print("No such student")



def help():
    print("stu <file name> <first name> <last name> - plot student grades item\nquit - quits\nhelp - displays this message")

    
    



def main(): 
    while True:
        token = input(">> ")
        token_split = token.split()
        try:
            if token_split[0] == 'help':
                help()
            if token_split[0] == 'stu': 
                student_grades(token)
                
            if token_split[0] == 'quit':
                if quit() == True:
                    print("GoodBye!")
                    break
        except: 
            print("Enter a command or 'quit' to quit")
            
            

main()