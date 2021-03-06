from yaml import safe_load

with open("./normalize/letters.yml", encoding='utf-8') as f:
    lets = safe_load(f)

string = str(input("Enter string>"))
output=""

for i in string:
    if i in lets:
        output += f"(?:{'|'.join(lets[i])})+"
    else:
        output += i

print(output)