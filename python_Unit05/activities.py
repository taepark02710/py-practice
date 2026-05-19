
def numbers():
    
    filename = input("Enter the filename: ")
    grand_sum = 0
    
    while filename != "":
        try: 
            with open(filename) as my_file:
                sum = 0
                for nums in my_file:
                    sum += int(nums)
                    
            print(sum)
            grand_sum += sum
            filename = input("Enter the filename: ")
        
        except FileNotFoundError:
            print("File does not exist:", filename)
            filename = input("Enter the filename: ")
        
        except ValueError:
            print("File contains non-numeric data.")
    
    print("Total sum:", grand_sum)
        
def main():
    numbers()
    
if __name__ == "__main__":
    main()