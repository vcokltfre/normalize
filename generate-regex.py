from yaml import safe_load

# This loads the yaml file and creates a dict with the lookalike letters
with open("./normalize/letters.yml", encoding='utf-8') as f:
    lets = safe_load(f)

# This initialises the empty strings needed for the following iterations
repeat = string = output = ""

inp = str(input("Enter string>"))
# This removes duplicates letters (ie. floor turns into flor) since the regex will match one or more of the entered
# character
for i in inp:
    if i != repeat:
        string += i
    repeat = i

# This creates the regex
for i in string:
    if i in lets:
        output += f"(?:{i}|{'|'.join(lets[i])})+"
    else:
        output += i

print(output)