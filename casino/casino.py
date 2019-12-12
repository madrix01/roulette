import random
from junk import bankwin, banklose, proper_bet
import tggu
from tggu import avail_bet, range_no
print("""
 _______________________________
/        MADRIX CASINOS         |
|         play classic          |
|        casino roulette        |
|______________________________ / 
type "p" to continue 
and "q" to quit 
""")

ini_money = 100
while True:
    user_input = input('> ')
    if user_input.lower() == "p":
        print("Let's play")
        while True:
            u_input = input("""
enter your number on which you want to bet
from 1 to 6 > 
            """)
            if int(u_input) > 6:
                print("""
            enter your number on which you want to bet
            from 1 to 6    
            """)
            else:
                break

        x = random.randint(1, 6)
        bet = avail_bet(1)
        if u_input == str(x):
            print("You are lucky today")
            final_money = float(bet) + float(ini_money)
            print(final_money)

        else:
            print("better luck next time")
            final_money = float(ini_money) - float(bet)
            print(final_money)
        print(f"the no. was {x}")
        if final_money <= 0:
            print("""
            Sorry, you have no money left in your account
            Thanks for playing with MADRIX CASINO
            """)
            user_input2 = input("""
            If you want to play again
            Type "a"
            
            """)
            if user_input2.lower() == "a":
                print("Please pay money at the counter")
                final_money = 100
                print("""
                Your account is credited with money
                Enjoy playing with MADRIX CASINO
                """)



        ini_money = final_money

        continue
    elif user_input.lower() == "q":
        break
