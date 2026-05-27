def make_student(id, name):
    
    return [id, name, 0, 0]

def names():
    
    name = {}
    name["T"] = "Taehun"
    name["P"] = "Park"
    name["K"] = "Kisurk"
    name["P"] = "Park"
    name["M"] = "Min"
    name["P"] = "Park"
    
    print(name)
    
    taehun = name["T"]
    dad = name["K"]
    mom = name["M"]
    print(taehun, dad, mom)
    
def print_dict(dictionary):
    
    key_list = sorted(dictionary.keys())
    
    for key in key_list:
        print("Key: ", key, "Value: ", dictionary[key])
        
def add_student(population, id, name):
    
    student = make_student(id, name)
    if id not in population:
        population[id] = student
        
def get_student(population, id):
    
    if id in population:
        return population[id]
        
        
def main():
    
    # callie = make_student("1234", "Callie")
    # pat = make_student("4567", "Patrick")
    # aidan = make_student("7890", "Aidan")
    # tae = make_student("1489", "Taehun")
    # # names()
    # a_dict = {"Hello": 2, "World": 1, "Art": 0, "Ohio": 2}
    
    # print_dict(a_dict)
    
    population = {}
    add_student(population, "1234", "Callie")
    add_student(population, "4567", "Patrick")
    add_student(population, "7890", "Aidan")
    add_student(population, "1489", "Taehun")
    print(population)
    print(get_student(population, "1234"))
    
    
    

if __name__ == "__main__":
    main()