print("####################################\n")
h= float(input("enter you height in m : \n"))
w= float(input("enter you weight in kg : \n"))
print("####################################\n")

bmi = w / (h**2)

if bmi<18.5:
    print(int(bmi), "UnderWeight")
elif 18.5<=bmi<=25:
    print(int(bmi),"Normal Weight")
elif 25<=bmi<=30:
    print(int(bmi),"OverWeight")
elif 30<=bmi<=35:
    print(int(bmi),"Obese")
else:
    print(int(bmi)," Clinically Obese")
