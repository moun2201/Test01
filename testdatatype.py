# str="Hello world"
# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str*10)
# print(str + "from BBU BTB")

#number
# a=1_000_000
# print(a)
# print(type(a))
# b=13.04
# print(type(b))
# print(b)

# val1=int("10")
# val2=int("20")
# total=val1+val2
# print(type(total))
# print("Total"+ str(total))
# print(len(str(total)))

# a=True
# print(bool(a))
# a=0.0
# print(bool(a))
# a=1.0
# print(bool(a))
# a=5
# b=10
# print(bool(a==b))
# a=None
# print(bool(a))
# a=()
# print(bool(a))
# a={}
# print(bool(a))
# a={}
# print(bool(a))

# a=int(input("A= "))
# b=int(input("B= "))
# print("result "+str(a) + str(b))

# num=input("Input Number?")
# val1=int(num[0])
# val2=int(num[1])
# total=val1+val2
# print("Result= "+str(total))

# val=5
# print(val>3 and val<20)
# print(val>3 or val<4)
#
# x=10
# y=20
# z=0
# print("x and y", x and y)
# print("x or y", x or y)
# print("x and z", x and z)
# print("z or x", z or x)
# print("y or z", y or z)

# w = int(input("Input Your Weight:"))
# h = float(input("Input Your Height:"))
# BMI = w//h**2
# print("your BMI " +str(BMI))

print("==========welcome To the Tip Calculator")
bill=int(input("What was the total bill ? "))
tip=int(input("How Much tip you like to give "))
p= int (input("How many People To split the bill?"))
Tip_pay=bill*tip/100
total =bill+Tip_pay
each_pay=total/p
print("Each person should pay "+str(each_pay))