import sys

print(f"Argument : {len(sys.argv)}")
for i in range(len(sys.argv[1:])):    
    print(f"{sys.argv[i]}: {len(sys.argv[i])}")