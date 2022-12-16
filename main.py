
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play="y"
while play=="y":
    yours=[]
    computer=[]
    for i in range(0,2):
        yours.append(random.choice(deck))
    score=sum(yours)
    print(f"Your cards: {yours}, current score: {score}")

    computer.append(random.choice(deck))
    comp_score=sum(computer)
    print(f"Computer's first card:{computer[0]}")
    response=input("Type 'y' to get another card, type 'n' to pass:")

    while response=="y":
        yours.append(random.choice(deck))
        score=sum(yours)
        if score>21:
            if 11 in yours:
                index=yours.index(11)
                yours[index]=11%10
        score=sum(yours)
        print(f"Your cards: {yours}, current score: {score}")
        print(f"Computer's first card:{computer[0]}")
        if score>21:
            break
        response=input("Type 'y' to get another card, type 'n' to pass:")

    if response=="n" or score>21:
        computer.append(random.choice(deck))
        comp_score=sum(computer)
        if comp_score>21:
            if 11 in computer:
                index=computer.index(11)
                computer[index]=11%10
        comp_score=sum(computer)
        while comp_score<17:
            computer.append(random.choice(deck))
            comp_score=sum(computer)
        comp_score = sum(computer)

    if score>comp_score and score<=21 or comp_score>21:
        print(f"Your final hand: {yours}, your final score:{score}")
        print(f"Computer's final hand: {computer}, computer's final score: {comp_score}")
        print("You win!")
    elif comp_score>score or score>21:
        print(f"Your final hand: {yours}, your final score:{score}")
        print(f"Computer's final hand: {computer}, final score: {comp_score}")
        print("You lose!")
    else:
        print(f"Your final hand: {yours}, your final score:{score}")
        print(f"Computer's final hand: {computer}, final score: {comp_score}")
        print("Draw")
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")










