dictionary_path = r"c:\Users\sulta\OneDrive\Documents\GitHub\python-projects\projects\dictionary_file\dictionary.txt"
n = -1
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    n = int(input("Function: "))
    if n == 3:
        break
    if n == 1:
        finnish_word = input("The word in Spanish: ")
        english_word = input("The word in English: ")
        with open(dictionary_path, "a") as file:
            file.write(f"{finnish_word} - {english_word} \n")
        print("Dictionary entry added")
    elif n == 2:
        search_term = input("Search term: ")
        with open(dictionary_path) as file:
            for line in file:
                if search_term in line:
                    print(line.strip())
            

print("Bye!")