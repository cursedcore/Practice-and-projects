from sys import argv

# for arg in argv[1:]:
#     print(arg)

if len(argv) != 2:
    print("Missing command-line argument")
    exit()
print(f"Hello, {argv[1]}")