import sys

if len(sys.argv) == 3:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    numbers = list(range(first, second + 1))
    print(numbers)
    
else:
    print("none")