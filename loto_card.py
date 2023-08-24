from random import randrange

def generate_card()->dict:
    '''Generate random Bingo card 
       and return it as dictionary.'''
    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []    
        }
    RANGE_LENGTH = 15
    #The start of the range from where we should choose a number
    start = 1
    #The end of the range from where we should choose a number
    end = RANGE_LENGTH + 1
    #Create Bingo card
    for key in card:
        while len(card[key]) != 5:
            #choose random number 
            number = randrange(start,end)
            #Check if the number does not exist in list, we add it. 
            if number not in card[key]:
                card[key].append(number)
        start = end 
        end  = start + RANGE_LENGTH    

    return card

def show_card(card:dict):
    '''Display Bingo card on screen.
       The function accepts as a parameter Bingo card.'''
    #print letters to the screen
    print(f"{'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}")
    #print numbers to the screen
    for i in range(len(card)):
        for value in card.keys():
            print(f"{card[value][i]:>5}", end="")
        print()


if __name__ == "__main__":
    card = generate_card()
    show_card(card)




