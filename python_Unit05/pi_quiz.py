
PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def py_tester():
    
    count = 0
    
    i = 0
    while i < 100:
        digit = input("Enter the pi decimal(" + str(i+1)+ "): ")
        if int(digit)  == int(PI[i+2]):
            count += 1
        else:
            print("Incorrect! the correct digit is", int(PI[i+2]))
            break
        i += 1
    
    return count

def display_score():
    

def main():
    print(py_tester())
    
    
    
if __name__ == "__main__":
    main()
            
            
    