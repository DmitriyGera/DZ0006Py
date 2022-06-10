alEng='abcdefghijklmnopqrstuvwxyz'
alRu='абвгдеёжзийклмнопзстуфхцчшщъыьэюяабвгдеёжзийклмнопзстуфхцчшщъыьэюя'
text=input('Enter your text: ')
key=4
res=''
for char in text:
    if char.lower() in alEng:
        res += alEng[(alEng.index(char.lower())+key)]
    elif char.lower() in alRu:
        res += alRu[(alEng.index(char.lower())+key)]
    else:
        res += char
print(res)