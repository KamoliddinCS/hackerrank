def print_formatted(number):
    width = len(bin(n)[2:])

    for i in range(1, n+1):
        print(
        str(i).rjust(width),         # Decimal column
        oct(i)[2:].rjust(width),     # Octal column without '0o'
        hex(i)[2:].upper().rjust(width),  # Hexadecimal column without '0x'
        bin(i)[2:].rjust(width)      # Binary column without '0b'
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)