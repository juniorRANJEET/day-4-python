# question based on LIST
states_of_india = ["arunachal pradesh","andhra pradesh","aasam","bihar","chatisgardh","gujrat",
"himachal pradesh","harayana","jharkhand","j&k","karnataka","kerala","ladhakh","manipur","meghalya",
"mizoram","madhaya pradesh","maharastra","nagaland","orissa","punjab","rajsthan","sikkim","tamilnadu",
"telegana","tripura","up","utarakhand","wb","delhi","daman & due","dadar & nagar haveli","pondichery",
"chandigardh","andman & nikobar"]
print(states_of_india[0])
#from last
print(states_of_india[-1])
# to change in the item ine list
states_of_india[2] = "gorkhaland"
print(states_of_india)
# to add single item in the list, it by default when you use:  list.apend("a")
states_of_india.append("POK")
print(states_of_india)
# to add lots of data in the list by default at last use : list.extend(["a","b","c"])
states_of_india.extend(["lahore","kabul","newyork"])
print(states_of_india)
# to add data in the list at a certain location use: list.insert(i,"a")
states_of_india.insert(0,"iraq")
print(states_of_india)
#to remove 1st data from the list
states_of_india.remove("iraq")
print(states_of_india)
# to remove last item in list if index not give: list.pop
states_of_india.pop()
print(states_of_india)
# to remove item from last of list if index define give: list.pop
states_of_india.pop([1])
print(states_of_india)
# to clear every things in the list
states_of_india.clear()
print(states_of_india)