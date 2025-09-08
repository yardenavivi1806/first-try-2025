#---------סעיף א----------
num1=input("enter a number")
num2=input("enter a number")
all_good=True

for d in num1:
    if(num1.count(d)!=num2.count(d)):
        all_good=False

if all_good:
    print("The numbers are exchanged")
else:
    print("The numbers are not exchanged")

#---------סעיף ב-----------
num=input("enter a number to chack")
all_num=[]
new_num=input("enter a number")
while new_num!=-1:
    all_num.append(new_num)
    new_num=int(input("enter a number"))

count=0
good_numbers=[]
for item in all_num:
    all_good=True
    for d in str(item):
        if (str(item).count(d) != num.count(d)):
            all_good = False
    if all_good==True:
        count+=1
        good_numbers.append(item)
print("the number of exchanged numbers is", count, "and this are the numbers: ", good_numbers)