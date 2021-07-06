isbn_number = input("Enter ISBN:")
digit_13=0
index=0

for char in isbn_number:
    if (char == '-'):
         continue
     
    i=int(char)

    if (index % 2==0):
        digit_13+=i
    else:
        digit_13+=(3*i)
    index+=1

digit_13=10-(digit_13%10)

print("Your ISBN is:" + isbn_number + '-' + str(digit_13))