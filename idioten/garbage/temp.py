from code.idioten_deck import create_deck



# class Decks:
#     """dwdwadaw"""
#
#     def generate_deck():
#         deck = create_deck()
#         return deck

decks = {}

def generate_decks(d):
    """ Fixture for generating the card decks. """
    d["new"] = create_deck()
    d["old"] = create_deck()
    return d


decks = generate_decks(decks)
print(decks)
print(decks["new"])
print(decks["old"])
