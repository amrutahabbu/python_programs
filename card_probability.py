'''
(Game: pick a card ) Write a program that simulates picking a card from a deck of
52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
'''


import random
card_rank=['Ace','King','Queen','Jack','2','3','4','5','6','7','8','9','10']
suit =['Heart','Club','diamond','spade']
random_rank = random.choice(card_rank)
random_suit = random.choice(suit)
random_card = random_rank,random_suit
print("The card you picked is " ,random_rank ," of ",random_suit )

