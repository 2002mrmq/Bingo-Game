from loto_card import generate_card,show_card
from random import randrange

def is_win_col(card:dict)->bool:
    '''The function accepts as a parameter Bingo card.
        Return True if the card has one row with zero, 
        else return False.'''
    #Check The sum of the column
    for key in card:
        if sum(card[key]) == 0:
            return True
    return False


def is_win_row(card:dict)->bool:
    '''The function accepts as a parameter Bingo card.
        Return True if the card has one coulmn with zero,
        else return False.'''
    #Count of the sum of the row
    for index in range(len(card)):
        #amount is the sum of the row
        amount = 0
        for key in card:
            amount += card[key][index]
        #Check the sum of the row
        if amount == 0:
            return True
    return False


def is_win_diag(card:dict)->bool:
    '''The function accepts as a parameter Bingo card.
        Return True if diagonal of the card is zero,
        else return False.'''
    #amount is the sum of the  diagonal
    amount = 0
    #index is the index of the diagonal element
    index = 0
    #Count of the sum of the row
    for key in card:
        amount += card[key][index]
        index += 1
    #Check the sum
    if amount == 0:
        return True
    return False

def play_bingo_with_three_card(card_1: dict, card_2: dict, card_3: dict):
    '''Play Bingo with three cards.
       where one of the cards wins the row, the one wins the coulumn,
       the another wins the diagonal.'''
    while not all([is_win_col(card_1), is_win_diag(card_2), is_win_row(card_3)]):
        #ordinal number 
        num = randrange(1,75)
        if not is_win_col(card_1):
            for key in card_1: 
               if num in card_1[key]:
                 card_1[key][card_1[key].index(num)] = 0
        if not is_win_diag(card_2):
            for key in card_2:
              if num in card_2[key]:
                card_2[key][card_2[key].index(num)] = 0
        if not is_win_row(card_3):
           for key in card_3:
               if num in card_3[key]:
                   card_3[key][card_3[key].index(num)] = 0
    
    show_card(card_1)
    show_card(card_2)
    show_card(card_3)

if __name__ == '__main__':
   card_1 = generate_card()
   card_2 = generate_card()
   card_3 = generate_card()
   play_bingo_with_three_card(card_1,card_2,card_3)