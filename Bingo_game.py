import loto_card
from Card_Checker import is_win_col, is_win_diag, is_win_row
from random import randrange

def play_bingo(card:dict)->dict:
    '''The function accepts as a parameter Bingo card.
       Return Bingo card if the number has been read changes to zero․'''
    while not any([is_win_col(card), is_win_diag(card), is_win_row(card)]):
        #ordinal number 
        num = randrange(1,75)
        #check the number in the card
        for key in card:
            if num in card[key]:
                card[key][card[key].index(num)] = 0
                     
    return card

if __name__ == '__main__':
    card = loto_card.generate_card()
    win_card = play_bingo(card)
    loto_card.show_card(win_card)




