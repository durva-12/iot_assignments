sub1= int(input("Enter marks of subject1 : "))
sub2= int(input("Enter marks of subject2 : "))
sub3= int(input("Enter marks of subject30 : "))
sum=sub1+sub2+sub3
avg=sum/3
if (avg>=90) and (avg<=100):
   print("Grade=A")
elif(avg>=80) and (avg<=90):
    print("Grade=B")
elif(avg>=70) and (avg<=80):
    print("Grade=C")
elif(avg>=60) and (avg<=70):
    print("Grade=D")
else:
    print("Grade=F")

