def laptop():
    yourfilename=input("Enter the file name  :")
    num=0
    file=open(yourfilename, 'r')
    for line in file:
        words=line.split("=")
    print("number of words:")
    print(num)
    print(words)


laptop()