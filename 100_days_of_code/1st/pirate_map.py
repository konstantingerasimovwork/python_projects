row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

charecters = list(position)
charecter_1 = int(charecters[0])
charecter_2 = int(charecters[1])
map[charecter_2 - 1][charecter_1 - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")