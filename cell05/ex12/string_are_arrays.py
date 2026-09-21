import sys

if len(sys.argv) == 2:
    result = ""
    for i in sys.argv[1]:
        if i == "z":
            result = result + "z"

    if result == "":
        print("none")
    else:
        print(result)
else:
    print("none")
    