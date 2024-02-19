import random

roll=random.randint(1,6)
guess=int(input("guess the number rolled:"))
if guess==roll:
    print("the rolled dice is correct" +str(roll))
else:
    print("the rolled dice is  not correct" +str(roll))



roll=random.choice(["sahithi","bunny","nithin"])
print(roll)

