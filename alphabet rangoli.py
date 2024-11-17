import string


def print_rangoli(size):
    alph = string.ascii_lowercase
    width = 4 * size - 3
    pattern = []

    # Generate the top half (including the middle)
    for i in range(size):
        letters = alph[size - i - 1:size]  # Get the required slice
        line = '-'.join(letters[::-1] + letters[1:])  # Create the line
        pattern.append(line.center(width, '-'))

    # Print the full rangoli by mirroring the top half
    print('\n'.join(pattern + pattern[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
