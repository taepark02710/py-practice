import csv


def opener(filename):
    try: 
        with open(filename) as my_file:
            return True
        
    except:
        print("File cannot be opened:", filename)
        return False
    
def names_and_addresses(filename):
    with open(filename) as my_file:
        next(my_file)
        for records in my_file:
            fields = records.split(",")
            name = fields[0]
            address = fields[1]
            print("name: " + name + " address: " + address)

    
def names_and_addresses_csv(filename):    
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            print(print("name: " + record[0] + " address: " + record[1]))
  
def average(filename, col):
    sum = 0
    cnt = 0
    
    with open(filename) as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file)
        for record in csv_reader:
            grade = record[col]
            sum += float(grade)
            cnt += 1
            
    avg = sum / cnt
    return avg
    

def main():
    filename = input("Enter the filename: ")
    # is_opened = opener(filename)
    # names_and_addresses(filename)
    # names_and_addresses_csv(filename)
    print(average(filename, 28))
    
    
if __name__ == "__main__":
    main()
        
    
    