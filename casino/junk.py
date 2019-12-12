def bankwin(bet, initial):
    final_money = float(bet) + float(initial)
    print(final_money)


def banklose(bet, initial):
    final_money = float(initial) - float(bet)
    print(final_money)


def proper_bet(x):
    while True:
        if (
            x == 10 and x == 50 and x == 20
        ):
            print("You are good to go")
            break
        else:
            print("Please enter proper bet amount")
