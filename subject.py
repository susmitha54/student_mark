subject=[]
marks=[] 
sum=0
x=int(input("Enter no.of subject: "))
for i in range(x):
     subject.append(x)
  
for i in range(x):
    y=int(input("Enter marks of the subject:"))
    marks.append(y) 
    sum=sum+y 
    avg=sum/x 
    if y>35:
        print(input("PASS"))
    else:
        print(input("fail"))     
print("Sum of mark is:",sum) 
print("Average:",avg)
