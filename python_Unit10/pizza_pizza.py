
CHEESE = ["Fresh Mozzarella", "Shredded Cheese", "Cheddar", "None"]
MEAT = ["Pepperoni", "Sausage", "Bacon", "Meatball", "None"]
VEGGIES = ["Mushrooms", "Olives", "Jalapeno", "None"]

class topping:

    __slot__ = ["name", "order_code", "price"]

    def __init__(self, name, order_code, price):
        self.name = name
        self.order_code = order_code
        self.price = price

class pizza:

    __slot__ = ["toppings", "price"]

    def __init__(self):
        self.toppings = {}
        self.price = 5

def print_options(category):

    if category == "Cheese":
        print("Fresh Mozzarella(f):", 3.99, "Shredded Cheese(s):", 1.99, "Cheddar(c):", 0.99, "None(n):", 0)
    
    elif category == "Meats":
        print("Pepperoni(p):", 6.99, "Sausage(s):", 4.50, "Bacon(b):", 4.99, "Meatball(m):", 7.99, "None(n):", 0)

    else:
        print("Mushrooms(m):", 3.99, "Olives(o):", 4.50, "Jalapeno(j):", 8.50, "None(n):", 0)

    


def main():
    pizza1 = pizza()
    print(type(pizza1.toppings))


if __name__ == "__main__":
    main()