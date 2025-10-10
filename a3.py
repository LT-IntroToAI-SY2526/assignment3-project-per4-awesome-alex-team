# import dictionary database JSON file
import json

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

# asserts
if __name__ == "__main__":
    assert meaning_by_word(["woolsey"]) == ["woolsey: Linsey-woolsey."], "failed define 'woolsey'"
    assert meaning_by_word(["broadwise"]) == ["broadwise: Breadthwise. [Archaic]"], "failed define 'broadwise'"

    print("all tests passed!")

    pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what does % mean"), meaning_by_word),
    (str.split("what is the meaning of the word _"), meaning_by_word),
    (str.split("what is the definition of _"), meaning_by_word),
    (str.split("can you explain _"), meaning_by_word),
  #  (str.split("what word means _"), word_by_meaning),
   # (str.split("what is the word that means"), word_by_meaning),
]