from yaml import safe_load

with open(__file__.replace("__init__.py", "") + "letters.yml", encoding='utf-8') as f:
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
