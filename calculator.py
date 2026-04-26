def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    x = int(input("Enter the number(x): "))
    y = int(input("Enter the number(y): "))
    
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    

if __name__ == "__main__":
    main()