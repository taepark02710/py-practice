import plotter
import plots

def print_lines(filename):
    word = input("Enter the word: ")
    isfound = False
    my_file = open(filename)
    for line in my_file:
        stripped = line.strip().lower()
        if word == stripped:
            isfound = True
    
    if isfound:
        print("Found the word:", word)
    else:
        print("Didn't find the word.")
        
    my_file.close()
    
def longest_word(lang):
    token = lang.split()
    maximum = 0
    word = ""
    for i in range(len(token)):
        if maximum < len(token[i]):
            maximum = len(token[i])
            word = token[i]
    
    return word

def longest_words(filename): 
    my_file = open(filename)
    for line in my_file:
        long_word = longest_word(line)
        print("Longest Word:", long_word)
        

def print_names(filename):
    my_file = open(filename)
    next(my_file)
    for record in my_file:
        records = record.split(",")
        print(records[1],records[0])
    
    my_file.close()
    
    
def average(filename, col):

    with open(filename) as my_file:
        len_file = 0            
        grade = 0
        header = next(my_file).split(",")
        for line in my_file:
            fields = line.split(",")
            grade += int(fields[col])
            len_file += 1
        
        avg = grade / len_file
            
    print(header[col], ":", avg)
    
def plot_grades(filename, col):
    
    
    with open(filename) as my_file:
        header = next(my_file).split(",")
        plotter.init("grades for " + str(header[col]), "Students", "Scores" )

        for line in my_file:
            fields = line.split(",")
            
            field = fields[col]
            plotter.add_data_point(float(field))

    plotter.plot()
            
                
            
def main():
    # print_lines("data/words.txt")
    # print(longest_word("you are the biggest fish"))
    # print(longest_words("data/alice.txt"))
    # print_names("python_Unit05/data/grades_010.csv")
    # average("python_Unit05/data/grades_010.csv", 2)
    plot_grades("python_Unit05/data/grades_010.csv", 10)
    input("Enter to stop...")
if __name__ == "__main__":
    main()
        
    
