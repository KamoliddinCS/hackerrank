N = int(input())
arr = []


for _ in range(N):
    func, *line = input().split()
    numbers = list(map(int, line))
    if func == "insert":
        arr.insert(numbers[0], numbers[1])
    elif func == "append":
        arr.append(numbers[0])
    elif func == "remove":
        arr.remove(numbers[0])
    elif func == "sort":
        arr.sort()
    elif func == "pop":
        arr.pop()
    elif func == "reverse":
        arr.reverse()
    elif func == "print":
        print(arr)


