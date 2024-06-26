from cs50 import get_float


def main():
    cents = -0.01
    while (cents < 0.0):
        cents = get_float("Change owed: ")
        cents = cents * 100

    quarters = int((cents / 25))
    cents = cents - quarters * 25

    dimes = int((cents / 10))
    cents = cents - dimes * 10

    nickels = int((cents / 5))
    cents = cents - nickels * 5

    pennies = int((cents / 1))
    cents = cents - pennies * 1
    coins = quarters + dimes + nickels + pennies

    print(coins)


main()
