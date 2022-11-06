wordlist_path = r"c:\Users\sulta\OneDrive\Documents\GitHub\python-projects\projects\random_word_generator\words.txt"
from random import sample

def words(n: int, beginning: str):
    lst = []
    with open(wordlist_path) as file:
        for word in file:
            if word.startswith(beginning):
                lst.append(word.strip())

        if len(lst) < n:
            raise ValueError(f'Could not find {n} words that start with {beginning}. Only found {len(lst)} words.')
    return sample(lst, n)



if __name__ == "__main__":
    word_list = words(int(input("amount of words: ")), input("Beginning of word: "))
    for word in word_list:
        print(word)