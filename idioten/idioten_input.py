"""
Module for handling game input.
"""

VALID_INPUT = ('d', '1', '2', '3', '4', 'n', 'e')

def kb_input():
    """Keyboard input."""
    print("Select action: \n1-4 = remove card in column \nd = deal cards\nn = new game ")

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

kb_input()
