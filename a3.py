# import dictionary database JSON file
import json

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary_data = json.load(file)

# import other files
from match import match
from typing import List, Tuple, Callable, Any

# main code
def define(matches: List[str]) -> List[str]:
    word = 

# asserts
if __name__ == "__main__":
    assert define(["woolsey"]) == ["Linsey-woolsey."], "failed define test"

    print("all tests passed!")