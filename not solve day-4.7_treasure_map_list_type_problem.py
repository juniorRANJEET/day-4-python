# treasure map types 3x3 problem with emogi
# emogi want in column 2,and row 3, entered as like 23:
row1 = [" "," "," ",]
row2 = [" "," "," ",]
row3 = [" "," "," ",]
map = [row1,row2,row3]
map = (f"{row1}\n{row2}\n{row3}")
print(map)
position = input("where do you want to put the treasure: ")
horizontal = position[0]
vertical = position[1]
# selected_row = map[vertical-1]
# selected_row[horizontal-1]= '😊'
map[vertical-1][horizontal-1] = 'x'
# column = [vertical-1], row = [horizontal-1] according to math
map = (f"{row1}\n{row2}\n{row3}")
print(map)