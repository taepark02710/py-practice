
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
            print("name: " + name + "address: " + address)

        

def main():
    filename = input("Enter the filename: ")
    # is_opened = opener(filename)
    names_and_addresses(filename)

if __name__ == "__main()__":
    main()
        
    
    