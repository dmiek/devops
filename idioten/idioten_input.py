
print("Select action: ")
print("1-4 = remove card in column")
print("d = deal cards")
print("n = new game")

r = input()
print(r)

if r == "d":
    print("dealing cards")
elif r == "1" or r == "2" or r == "3" or r == "4":
    print("removing card in column")
elif r == "n":
    print("dealing new game")
else:
    print("input not mapped to action")