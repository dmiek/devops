"""
Module for handling game input.
"""

def kb_input():
    """Keyboard input."""
    print("Select action: ")
    print("1-4 = remove card in column")
    print("d = deal cards")
    print("n = new game")

    inp = input()
    print(inp)

    if inp == "d":
        print("dealing cards")
    elif inp in ('1', '2', '3', '4'):
        print("removing card in column")
    elif inp == "n":
        print("dealing new game")
    else:
        print("input not mapped to action")
