with open("journey.txt","r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    print("first line:",line1)
    print("second line:",line2)
    print("third line:",line3)

    #use of readlines()
    with open("journey.txt","r") as f:
        lines = f.readlines()
        print(lines)