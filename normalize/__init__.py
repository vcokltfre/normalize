from yaml import safe_load
from pathlib import Path
from requests import get

home = Path.home()
path = Path(home, ".cache")
path.mkdir(exist_ok=True)
file = Path(path, "letters.yml")

if not file.exists():
    data = get("https://raw.githubusercontent.com/vcokltfre/normalize/master/letters.yml")
    with file.open("w", encoding="utf-8") as f:
        f.write(data.text)

with open(file, encoding='utf-8') as f:
    lets = safe_load(f)

letters = {}
every = set()
for k, v in lets.items():
    letters[tuple(v)] = k
    every.update(v)

def normalize(text: str):
    output = ""

    for letter in text:
        if letter in every:
            for k, v in letters.items():
                if letter in k: output += v
        else:
            output += letter

    return output
