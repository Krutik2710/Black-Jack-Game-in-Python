import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    r_card=random.choice(cards)
    return r_card

def cal_score(cards): 
  if sum(cards) == 21 and len(cards) == 2:
    return 0
 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
      


def compare_score(user_score,computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play():

    print(logo)
    player_card=[]
    computer_card=[]
    flag=False

    for _ in range(2):
        player_card.append(deal_random_card())
        computer_card.append(deal_random_card())

    while not flag:   
        player_score = cal_score(player_card)
        computer_score = cal_score(computer_card)
        print(f"   Your cards: {player_card}, current score: {player_score}")
        print(f"   Computer's first card: {computer_card[0]}")
        if player_score==0 or computer_score==0 or player_score>21:
            flag=True
        else:
            user_should_deal=input("Type 'yes' to take 1 more card else type 'no': ")
            if user_should_deal=="yes":
                player_card.append(deal_random_card())           
            else:
                flag=True
              
    while computer_score != 0 and computer_score < 17:
       computer_card.append(deal_random_card())
       computer_score = cal_score(computer_card)
    
    print(f"   Your cards: {player_card}, final score: {player_score}")
    print(f"   Computer's card: {computer_card}, finalscore: {computer_score}")
    print(compare_score(player_score, computer_score))


    



choice=input("Do you want to play Black Jack then type 'yes' else type 'no': ")
if choice=="yes":
    play()
else:
    print("thankyou !")
  
   
