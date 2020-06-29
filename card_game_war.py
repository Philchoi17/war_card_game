import random

# CARD VALUES
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, \
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, \
          'Queen': 12, 'King': 13, 'Ace': 14}
#SUITS DICT
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# RANKS DICT
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', \
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# CARD
# SUIT, RANK, VALUE
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# DECK
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # shuffling deck
        random.shuffle(self.all_cards)

    def deal_one(self):
        # take one card from deck
        return self.all_cards.pop()


#PLAYER
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



# game logic
# GAME SETUP:
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
# While game on:
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_one = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards!, Player One Wins!')
        game_on = False
        break
    
    #START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

#   while at war
    at_war = True
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value > player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print('player Two wins')
                game_one = False
                break
            
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('player One wins')
                game_one = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

