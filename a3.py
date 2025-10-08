# import dictionary database JSON file
import json

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary_data = json.load(file)

# import other files
from match import match
from typing import List, Tuple, Callable, Any

# main code
def define(matches: List[str]) -> List[str]:
    result = []
    word = matches[0]
    meaning = dictionary_data.get(word)
    if meaning:
        result.append(f"{word}: {meaning}")
    else:
        print("Sorry, that word is not in the dictionary.")
    return result

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("define _"), define),
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

# asserts
if __name__ == "__main__":
    assert define(["woolsey"]) == ["woolsey: Linsey-woolsey."], "failed define 'woolsey'"
    assert define(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"
    assert define(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"

    print("all tests passed!")

while True:
    testword = []
    test = input("Enter a word: ")
    testword.append(test)
    print(define(testword))