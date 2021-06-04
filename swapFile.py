def swapFileData():
    fone=input("Enter the name of your first file: ")
    ftwo=input("Enter the name of your second file: ")

    with open(fone,'r') as a:
        data_a = a.read()

    with open(ftwo,'r') as b:
        data_b = b.read()

    with open(fone,'w') as a:
        a.write(data_b)

    with open(ftwo,'w') as b:
        b.write(data_a)

swapFileData()

        