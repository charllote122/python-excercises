import random 

names = input("Enter everybody's name separated by a comma::")
names_list=names.split(",")

#length=len(names_list)
#random_choice=random.randint(0,length-1)

person_selected=random.choice(names_list)
print(f"{person_selected} will pay the bill")

