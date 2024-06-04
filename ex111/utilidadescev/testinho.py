import re

inp = "João:saiu!! de%$ˆcasa"
pattern = "[a-zA-ZÀ-ú]+"
output = " ".join(re.findall(pattern, inp))

print(inp)
print(output)