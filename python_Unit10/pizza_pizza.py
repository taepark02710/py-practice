
class topping:

    __slot__ = ["name", "order_code", "price"]

    def __init__(self, name, order_code, price):
        self.name = name
        self.order_code = order_code
        self.price = price

    def get_name(self):

        return self.name
    
    def get_order_code(self):

        return self.order_code
    
    def get_price(self):

        return self.get_price

class pizza:

    __slot__ = ["cheese", "meat", "veggies", "price"]

    def __init__(self):
        self.cheese = ""
        self.meat = []
        self.veggies = []
        self.price = 5

    def add_cheese(self, topping):

        self.cheese = topping

    def add_meat(self, topping):

        self.meat.append(topping)

    def add_veggies(self, topping):

        self.veggies.append(topping)

    def price_all(self):

        self.price += self.cheese.get_price()
        length = 0

        if len(self.meat) > len(self.veggies):
            length = len(self.meat)
        else:
            length = len(self.veggies)

        for i in range(0, length):

            if i < len(self.meat):
                self.price += self.meat[i].get_price()
            if i < len(self.veggies):
                self.price += self.veggies[i].get_price()

        return self.price
    


def print_options(category):

    if category == "Cheese":
        print("Fresh Mozzarella(f):", 3.99, "Shredded Cheese(s):", 1.99, "Cheddar(c):", 0.99, "None(n):", 0)
    
    elif category == "Meats":
        print("Pepperoni(p):", 6.99, "Sausage(s):", 4.50, "Bacon(b):", 4.99, "Meatball(m):", 7.99, "None(n):", 0)

    else:
        print("Mushrooms(m):", 3.99, "Olives(o):", 4.50, "Jalapeno(j):", 8.50, "None(n):", 0)

def main():
    # pizza1 = pizza()
    # print(type(pizza1.toppings))
    print()


if __name__ == "__main__":
    main()