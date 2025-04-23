vocals = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

user_input = input("Digite uma palavra: ").lower().replace(" ", "")

for i in user_input:
    if i in vocals:
        vocals[i] += 1

print(vocals)