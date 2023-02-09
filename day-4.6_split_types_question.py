# write a program which will select a random name fromt the list of name,which will pay the everyone's foods bill
# don't use choice function
import random
#test_seed = int(input("enter seeds number: "))
# split string method
name_as_CVS = input("enter everybody name: ")
names = name_as_CVS.split(",")
# num_items = len(names)
# # generate random number between 0 to last index
# random_choice = random.randint(0, num_items -1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(person_who_will_pay ,"is going to buy today meal")
