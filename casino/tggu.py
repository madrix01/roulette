def avail_bet(z):
    print("available bet 10,20,50")
    while True:
        x = input("input bet> $")
        z = int(x)
        if (
            z == 10 or z == 50 or z == 20
        ):
            print("You are good to go ==>")
            break
        else:
            print("Please enter proper bet amount")
    return z


def range_no(z):
    print("available range 6 and 10")
    while True :
        x = input("input no. range > ")
        if int(x) == 6:
            z = int(x)
            continue
        else :
            print("enter a valid range")

