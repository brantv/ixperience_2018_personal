#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:39:15 2018

@author: brant
"""
#Poker
import random
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
spade = '\u2660'
heart = '\u2665'
diamond = '\u2666'
club = '\u2663'
suits = [spade, heart, diamond, club]
hands = []
hands_suit = []
highest_card = []
tie_indicator = 0
tie_array = []
player_storage = 0

print("Enter number of players: ")
num_players = int(input())

for x in range(0, num_players):
    hands.append([])
    hands_suit.append([])
    for y in range(0, 5):
        hands[x].append(random.choice(cards))
        hands_suit[x].append(random.choice(suits))
    
for x in range(0, num_players):
    print("Player " + str(x+1) + "'s hand:")
    print(hands[x][0] + hands_suit[x][0] + " " + hands[x][1] + hands_suit[x][1] + " " + hands[x][2] + hands_suit[x][2] + " " + hands[x][3] + hands_suit[x][3] + " " + hands[x][4] + hands_suit[x][4])
    
for x in range(0, num_players):
    rank_storage = 0
    for y in range(0, 5):
        rank = cards.index(hands[x][y])
        if (rank > rank_storage):
            rank_storage = rank
    highest_card.append(rank_storage)

winning_card = max(highest_card)
for x in range(0,num_players):
    if (highest_card[x] == winning_card):
        tie_indicator += 1
        tie_array.append((x + 1))
    
if (tie_indicator == 1):
    print("The player with the highest card is player " + str(highest_card.index( max(highest_card)) + 1))
elif (tie_indicator > 1):
    print("Tie between players: " + str(tie_array))
    
"""
TODO:
check if card has already been played

"""
