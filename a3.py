# import dictionary database JSON file
import json
import random

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary_data = json.load(file)

# import other files
from match import match
from typing import List, Tuple, Callable, Any

# main code
def meaning_by_word(matches: List[str]) -> List[str]:
    result = []
    word = matches[0]
    meaning = dictionary_data.get(word)
    if meaning:
        result.append(f"{word}: {meaning}")
    else:
        print("Sorry, that word is not in the dictionary.")
    return result

def get_random_word() -> str:
    """Return a random word from the dictionary."""
    return random.choice(list(dictionary_data.keys()))

def guess_game():
    """Starts guess game"""
    # Pick a random word and its definition
    word, definition = random.choice(list(dictionary_data.items()))
    
    print("Guess the word based on the following definition:")
    print(definition)
    
    # Get user input
    user_guess = input("\nYour guess: ").strip().lower()
    
    # Check if the guess is correct
    if user_guess == word.lower():
        print("Correct! Well done.")
    else:
        print(f"Wrong. The correct word was '{word}'.")

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("define _"), meaning_by_word),
]

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["Sorry, that word is not in the dictionary"]
    return ["I don't understand"]

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
(str.split("what does % mean"), meaning_by_word),
(str.split("what is the meaning of the word _"), meaning_by_word),
(str.split("what is the definition of _"), meaning_by_word),
(str.split("can you explain _"), meaning_by_word),
#(str.split("what word means _"), word_by_meaning),
#(str.split("what is the word that means"), word_by_meaning),
]
    
#asserts
if __name__ == "__main__":
    assert meaning_by_word(["woolsey"]) == ["woolsey: Linsey-woolsey."], "failed define 'woolsey'"
    assert meaning_by_word(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"
    assert meaning_by_word(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"

    print("all tests passed!")
    
while True:
    word = input("Enter word(/help for other commands): ")
    if "/" in word:
        print("!random - Gives you a random word\n!hangman - Play hangman with the chatbot\n!guess - Guess the word by its meaning")
    elif "!" in word:
        if word.lower() == "!random":
            print(get_random_word())
        if word.lower() == "!guess":
            guess_game()
    else:        
        print(meaning_by_word([word]))