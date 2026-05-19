
def numbers():
    
    filename = input("Enter the filename: ")
    grand_sum = 0
    
    while filename != "":
        try: 
            with open(filename) as my_file:
                sum = 0
                for nums in my_file:
                    try:
                        sum += int(nums)
                    except:
                        print("Skipping non-numeric data:", nums)
                    
            print(sum)
            grand_sum += sum
        
        except FileNotFoundError:
            print("File does not exist:", filename)
        
        except ValueError:
            print("File contains non-numeric data.")
        
        filename = input("Enter the filename: ")
    
    print("Total sum:", grand_sum)
    
def division():
    num = input("Enter a numerator: ") 
    den = input("Enter a denominator: ")
    attempts = 0
    
    while (den and num) != "":
        try: 
            print("Result of division =", float(num)/float(den))
            
        
        except ZeroDivisionError as ze:
            print("Can't divide by 0")
            attempts += 1
            if attempts >= 3:
                raise ze
            
        except ValueError as ve: 
            print("Non-numeric value entered.")
            attempts += 1
            if attempts >= 3:
                raise ve
            
        
            
            
        num = input("Enter a numerator: ")
        den = input("Enter a denominator: ")
         
         
def password():
    
    psw = input("Enter the password: ")
    if len(psw) < 10 or len(psw) > 20:
        raise ValueError("Password must be between 10 and 20 characters.")
    
    con = input("Confirm password: ")
    
    if psw != con:
        raise ValueError("Passwords must match!")
    
    return psw
    
         
def main():
    # numbers()
    division()
    # password()
    
if __name__ == "__main__":
    main()