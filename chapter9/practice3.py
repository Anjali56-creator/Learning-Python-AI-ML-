with open("data.txt","w") as f:
    f.write("Hello, World!")

with open("data.txt","r") as file:
    content = file.read()
    print(content)