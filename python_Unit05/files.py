def print_lines(filename):
    word = input("Enter the word: ")
    isfound = False
    my_file = open(filename)
    for line in my_file:
        stripped = line.strip().lower()
        if word == stripped:
            isfound = True
    
    if isfound:
        print("Found the word:", word)
    else:
        print("Didn't find the word.")
        
    my_file.close()
    
def longest_word(lang):
    token = lang.split()
    maximum = 0
    word = ""
    for i in range(len(token)):
        if maximum < len(token[i]):
            maximum = len(token[i])
            word = token[i]
    
    return word

def longest_words(filename): 
    my_file = open(filename)
    for line in my_file:
        long_word = longest_word(line)
        print("Longest Word:", long_word)
    
def main():
    # print_lines("data/words.txt")
    print(longest_word("you are the biggest fish"))
    print(longest_words("data/alice.txt"))

if __name__ == "__main__":
    main()
        
    
