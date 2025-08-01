# var = open('<filename_ext>','am')
# var.close()

# with open ('<filename_ext>','am') as var:
with open("data.txt", "w") as f:
    # Open file in write mode

    print(type(f))

    f.write("Hello, this is a text file!")  # 

with open("data.txt", "r") as f:
    content = f.readlines()
    print(content)


# read file line by line 
try:
    with open("data.txt", "r") as f:
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print("File not found.")
