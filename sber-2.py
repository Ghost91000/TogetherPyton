# Задание 1

s = 'Abracadabra'
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[:: 2])
print(s[1::2])
print(s[-1:: -1])
print(s[:: 2][-1::-1])
print(len(s))

# Задание 2

input = "a1 2b  3   abc d3e r2D2"
input = input.split(' ')
output = []
for word in input:
    if word != "":
        if word[0].isalpha():
            word = word[0].capitalize() + word[1:]
        output.append(word)
print(" ".join(output))

# Задание 3

input = "1Aa aaaaaaaaaaaaaa"
output = ""

if len(input) < 12:
    output += "Длинна пароля недостаточная. Введите минимум 12 символов. "
else:
    if input != "":
        IsLower = False
        IsUpper = False
        IsNum = False
        IsSpecial = False
        for char in input:
            print(char)
            if char.isdigit():
                IsNum = True
            elif char.islower():
                IsLower = True
            elif char.isupper():
                IsUpper = True
            else:
                IsSpecial = True

    if not IsNum:
        output += "В вашем пароле не хватает цифр. "
    if not IsLower:
        output += "В вашем пароле не хватает строчных букв. "
    if not IsUpper:
        output += "В вашем пароле не хватает прописных букв. "
    if not IsSpecial:
        output += "В вашем пароле не хватает спецсимвола."

    if IsSpecial and IsUpper and IsLower and IsNum:
        output = "Пароль подходит!"
print(output)

