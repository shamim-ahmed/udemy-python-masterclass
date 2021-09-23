#!/usr/bin/env python3

def print_option_menu(options):
    print("Please choose your option from the list below:\n")

    for i, option in enumerate(options):
        print("{}. {}".format(i, option))

    print()


if __name__ == "__main__":
    options = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
    print_option_menu(options)

    done = False

    while not done:
        choice = int(input())

        if choice == 0:
            done = True
        elif 0 < choice < len(options):
            print("You have entered {}".format(choice))
        else:
            print_option_menu(options)
