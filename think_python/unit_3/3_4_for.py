# renge puede ser cualquier iterable al parecer
for i in range(2):  # i deve ir si o si, aun que no se utilize en el cuerpo
    print(i)


def print_verse():
    print("spam")


def print_n_verses(n):
    for i in range(n):
        print_verse()
        print("🔥🔥🔥")


print_n_verses(2)
# output:

# spam
# 🔥🔥🔥
# spam
# 🔥🔥🔥
