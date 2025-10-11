""" readable = open('lorem.txt')
print(readable.readline().strip())
print(readable.readline()) """

""" with open("lorem.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el contenido del archivo

print(contenido)
 """


def has_e(word):
    """ for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False """
    return 'E' in word or 'e' in word  # in retorna un booleano so ==> True or True return true else false


count = 0
e_word_count = 0

for line in open('lorem.txt'):
    word = line.strip()
    count += 1
    if has_e(word):
        e_word_count += 1


def porcentaje(total, cantidad):
    return (cantidad / total) * 100


print(porcentaje(count, e_word_count))  # 66.94 %
# dos tercios aprox de palabras contienen la letra e
