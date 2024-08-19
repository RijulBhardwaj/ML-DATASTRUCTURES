import pandas as pd
import random

# Define the suits and ranks for a standard 52-card deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a standard 52-card deck
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck to randomize it
random.shuffle(deck)

# Create a DataFrame from the deck
df = pd.DataFrame(deck, columns=['Rank', 'Suit'])

# Define the order for sorting
suit_order = {'Hearts': 1, 'Diamonds': 2, 'Clubs': 3, 'Spades': 4}
rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Add columns for the order of suits and ranks
df['SuitOrder'] = df['Suit'].map(suit_order)
df['RankOrder'] = df['Rank'].map(rank_order)

# Sort the DataFrame by SuitOrder and RankOrder
df_sorted = df.sort_values(by=['SuitOrder', 'RankOrder']).reset_index(drop=True)

# Drop the auxiliary columns used for sorting
df_sorted = df_sorted.drop(columns=['SuitOrder', 'RankOrder'])

print("Sorted Deck:")
print(df_sorted)
