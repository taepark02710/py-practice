import csv
import random

def make_database(filename):
    # card - tuple, database - dictionary
    
    pokemon_data = {}
    
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for pokemon in csv_reader:
            name = pokemon[0]
            number = pokemon[1]
            type = pokemon[2]
            card = (name, number, type)
            
            if number not in pokemon_data:
                pokemon_data[number] = card
    
    return pokemon_data

def make_pack(database):
    
    pack = set()
    
    while len(pack) < 10:
       randint = random.randint(1, 102)
       card = database[str(randint)]
       
       if card not in pack:
           pack.add(card)
           
    return pack

def build_basic_collection(database):
    
    unique_cards = set()
    cnt = 0
    
    while len(unique_cards) != len(database):
        
        cards = make_pack(database)
        for card in cards:
            if card not in unique_cards:
                unique_cards.add(card)
        
        cnt += 1
                
    return cnt
    

def main():
    database = make_database("data/pokemon.csv")
    # pack = make_pack(database)
    # print(pack)
    # print(len(pack))
    # cnt = build_basic_collection(database)
    # print(cnt)
    
    sum = 0
    for _ in range(0, 1000):
        sum += build_basic_collection(database)

    print("The average is", sum / 1000)

if __name__ == "__main__":
    main()