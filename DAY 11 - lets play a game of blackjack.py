import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def sum_score(cards):
    if sum(cards)==21 and len(cards):
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score==c_score:
        return 'Draw'
    elif c_score==0:
        return 'lose opponent has blackjack'
    elif u_score==0:
        return 'win with a blackjack'
    elif u_score>21:
        return 'you went over you lose'
    elif c_score>21:
        return 'opponent went over. you win'
    elif u_score>c_score:
        return 'win'
    else:
        return 'you lose'
def play():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game:
        user_score = sum_score(user_cards)
        computer_score = sum_score(computer_cards)
        print(f'your cards:{user_cards},your final score: {user_score}')
        print(f"computer's first card: {computer_cards[0]}")
        if user_score == 0 or user_score > 21 or computer_score == 0:
            game = True
        else:
            again = input('type Y to get another card or type N to pass').lower()
            if again == 'y':
                user_cards.append(deal_card())
            else:
                game = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = sum_score(computer_cards)
    print(f'your final cards:{user_cards},your current score: {user_score}')
    print(f"computer's final cards: {computer_score},your final score :{computer_score}")
    compare(user_score, computer_score)

while input('do you want to paly a game of blackjack Y or N').lower()=='y':
    print('\n' * 100)
    play()
