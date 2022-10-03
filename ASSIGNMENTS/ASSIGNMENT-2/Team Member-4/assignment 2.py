import random
while( True ):
    a=random.randint(18,99)
    b=random.randint(10,99)
    if (a>35 and b>60):
        print("high TEMP and humidity of :",a,b,"%","alarm is on")
    elif(a<35 and b<60):
        print("Normal TEMP and humidity of:",a,b,"%","alarm is off")
        break
