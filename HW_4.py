# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.

new_spisok = " "
path = 'file.txt'
data = open(path, 'r')
for line in data:
    new_spisok = line
data.close()

new_spisok1 = new_spisok.split(' ')

result = ""

for value in new_spisok1:
    digit = False
    for char in value:
        if char.isdigit():
            digit = True
    if digit == False:
        result += f'{value} '

print(result)

with open('file.txt', 'w') as data:
    data.write(result)
