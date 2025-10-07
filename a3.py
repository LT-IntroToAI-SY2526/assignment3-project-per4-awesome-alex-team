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

# asserts
if __name__ == "__main__":
    assert define(["woolsey"]) == ["woolsey: Linsey-woolsey."], "failed define 'woolsey'"
    assert define(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"

    print("all tests passed!")