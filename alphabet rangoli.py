def print_rangoli(size):
    alph = ['a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    current_letters = []
    final = []
    w = 4 * size - 3
    print(w)

    for i in range(size):
        current_letters.append(alph[size-i-1])
        left_part = current_letters[:-1]
        for u in current_letters:
            final.append(u)
        for j in left_part[::-1]:
            final.append(j)
        print('-'.join(final).center(w, '-'))
        final = []

    for i in range(size-1, 0, -1):
        current_letters = current_letters[:-1]
        left_part = current_letters[:-1]
        for u in current_letters:
            final.append(u)
        for j in left_part[::-1]:
            final.append(j)
        print('-'.join(final).center(w, '-'))
        final = []


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)