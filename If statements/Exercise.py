#How To Use If statements

mark= int (float(input("Please enter mark: ")))

#for isinstance("invalid Mark")
    #print("Invalid  mark")

if mark>=80 and mark<=100 :
    print("Grade A")

elif mark>=70 and mark<=79 :
    print("Grade B")

if mark>=50 and mark<=69:
    print("Grade C")

elif mark>=40 and mark<=49 :
    print("Grade D")

if mark>=0 and mark<=39 :
    print("Grade E")

else:
    print("Outside the range")