import textwrap

def wrap(string, max_width):
    new_s = "\n".join(textwrap.wrap(text=string, width=max_width))
    return new_s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)