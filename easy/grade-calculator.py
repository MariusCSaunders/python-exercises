maths_mark = int(input("What was the maths mark? "))
chems_mark = int(input("What was the chemistry mark? "))
phys_mark = int(input("What was the physics mark? "))

overall_mark = maths_mark + chems_mark + phys_mark
overall_percentage = overall_mark / 3

print("Your overall percentage is " + str(overall_percentage) + "%")

if overall_percentage >= 70:
    print("You got a grade of A")
elif overall_percentage >= 60 and overall_percentage < 69:
    print("You got a grade of B")
elif overall_percentage >= 50 and overall_percentage < 59:
    print("You got a grade of C")
elif overall_percentage >= 40 and overall_percentage < 49:
    print("You got a grade of D")
else:
    print("You failed")