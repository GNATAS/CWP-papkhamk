org_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = set()

for i in org_array:
    if i > 5:
        new_array.add(i + 2)

print(org_array)
print(new_array)