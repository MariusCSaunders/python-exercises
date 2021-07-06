def timestableDisplay(number):
    print("\t\t\t\t Mulitplication Table")

    for j in range(1, number):
        for k in range(1, number):
            print( j * k, end ="\t")
        print("\n")


n1 = int(input("Enter a number: "))
timestableDisplay(n1+1)